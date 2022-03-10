"""Event logging"""

import logging
import sys
import warnings
from dataclasses import dataclass
from logging.handlers import RotatingFileHandler
from typing import Optional, Set

# NOTE: `.notify` must always be loaded before this module, `.logging`.
# Failure to do so will result in a circular imports.
from . import notify


def init_log(
    logfile: str,
    level: int,
    debug: bool,
    no_multi: bool,
    verbose: bool = False,
    verbose_log: bool = False,
) -> None:
    """Initialize application event logging"""
    global DEBUG, MULTI, VERBOSE, VERBOSE_LOG

    handler = RotatingFileHandler(
        logfile,
        maxBytes=2 ** 20,  # 1 MiB
        backupCount=1,
    )
    handler.addFilter(filter_)

    VERBOSE, VERBOSE_LOG = verbose or debug, verbose_log
    DEBUG = debug = debug or level == logging.DEBUG
    if debug:
        level = logging.DEBUG
    elif VERBOSE or VERBOSE_LOG:
        level = logging.INFO

    FORMAT = (
        "({process}) ({asctime}) "
        + "{processName}: {threadName}: " * debug
        + "[{levelname}] {name}: "
        + "{funcName}: " * (debug and stacklevel_is_available)
        + "{message}"
    )
    logging.basicConfig(
        handlers=(handler,),
        format=FORMAT,
        datefmt="%d-%m-%Y %H:%M:%S",
        style="{",
        level=level,
    )

    _logger.info("Starting a new session")
    _logger.info(f"Logging level set to {logging.getLevelName(level)}")

    if debug and not stacklevel_is_available:
        warnings.warn(
            "Please upgrade to Python 3.8 or later to get more detailed logs."
        )

    try:
        import multiprocessing.synchronize  # noqa: F401
    except ImportError:
        MULTI = False
    else:
        from .logging_multi import multi_logger

        MULTI = not no_multi

    if MULTI:
        multi_logger.start()


def log(
    msg: str,
    logger: Optional[logging.Logger] = None,
    level: int = logging.INFO,
    *,
    direct: bool = True,
    file: bool = True,
    verbose: bool = False,
    loading: bool = False,
) -> None:
    """Report events to various destinations"""
    if loading:
        msg += "..."

    if verbose:
        if VERBOSE:
            logger.log(level, msg, **_kwargs)
            notify.notify(
                msg, level=getattr(notify, logging.getLevelName(level)), loading=loading
            )
        elif VERBOSE_LOG:
            logger.log(level, msg, **_kwargs)
    else:
        if file:
            logger.log(level, msg, **_kwargs)
        if direct:
            notify.notify(
                msg, level=getattr(notify, logging.getLevelName(level)), loading=loading
            )


def log_exception(msg: str, logger: logging.Logger, *, direct: bool = False) -> None:
    """Report an error with the exception reponsible

    NOTE: Should be called from within an exception handler
    i.e from (also possibly in a nested context) within an except or finally clause.
    """
    if DEBUG:
        logger.exception(f"{msg} due to:", **_kwargs_exc)
    elif VERBOSE or VERBOSE_LOG:
        exc_type, exc, _ = sys.exc_info()
        logger.error(f"{msg} due to: ({exc_type.__name__}) {exc}", **_kwargs)
    else:
        logger.error(msg, **_kwargs)

    if VERBOSE and direct:
        notify.notify(msg, level=notify.ERROR)


# Not annotated because it's not directly used.
def _log_warning(msg, catg, fname, lineno, f=None, line=None):
    """Redirects warnings to the logging system.

    Intended to replace `warnings.showwarning()`.
    """
    _logger.warning(warnings.formatwarning(msg, catg, fname, lineno, line))
    notify.notify(
        "Please view the logs for some warning(s).",
        level=notify.WARNING,
    )


# See "Filters" section in `logging` standard library documentation.
@dataclass
class Filter:
    disallowed: Set[str]

    def filter(self, record: logging.LogRecord) -> bool:
        return record.name.partition(".")[0] not in self.disallowed

    def add(self, name: str) -> None:
        self.disallowed.add(name)

    def remove(self, name: str) -> None:
        self.disallowed.remove(name)


filter_ = Filter({"PIL", "urllib3"})

# Writing to STDERR messes up output, especially with the TUI
warnings.showwarning = _log_warning

# Can't use "term_img", since the logger's level is changed in `.__main__`.
# Otherwise, it would affect children of "term_img".
_logger = logging.getLogger("term-img")

# the _stacklevel_ parameter was added in Python 3.8
stacklevel_is_available = sys.version_info[:3] >= (3, 8, 0)
if stacklevel_is_available:
    # > log > logger.log > _log
    _kwargs = {"stacklevel": 2}
    # > exception-handler > log_exception > logger.exception > _log
    _kwargs_exc = {"stacklevel": 3}
else:
    _kwargs = _kwargs_exc = {}

# Set from within `init_log()`
DEBUG = None
MULTI = None
VERBOSE = None
VERBOSE_LOG = None

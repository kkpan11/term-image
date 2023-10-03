"""
.. The Renderable API
"""

from __future__ import annotations

__all__ = (
    "Renderable",
    "RenderArgs",
    "RenderData",
    "Frame",
    "FrameCount",
    "FrameDuration",
    "Seek",
    "RenderableError",
    "IndefiniteSeekError",
    "RenderError",
    "RenderSizeOutofRangeError",
    "RenderArgsDataError",
    "RenderArgsError",
    "RenderDataError",
    "IncompatibleArgsNamespaceError",
    "IncompatibleRenderArgsError",
    "NoArgsNamespaceError",
    "NoDataNamespaceError",
    "NonAnimatedFrameDurationError",
    "UnassociatedNamespaceError",
    "UninitializedDataFieldError",
    "UnknownArgsFieldError",
    "UnknownDataFieldError",
)

from ._enum import FrameCount, FrameDuration, Seek
from ._exceptions import (
    IndefiniteSeekError,
    NonAnimatedFrameDurationError,
    RenderableError,
    RenderError,
    RenderSizeOutofRangeError,
)
from ._renderable import Renderable
from ._types import (
    Frame,
    IncompatibleArgsNamespaceError,
    IncompatibleRenderArgsError,
    NoArgsNamespaceError,
    NoDataNamespaceError,
    RenderArgs,
    RenderArgsDataError,
    RenderArgsError,
    RenderData,
    RenderDataError,
    UnassociatedNamespaceError,
    UninitializedDataFieldError,
    UnknownArgsFieldError,
    UnknownDataFieldError,
)
<div align="center">
<h1><b>Term-Image</b></h1>
<b>Display Images in the terminal</b>
<br>
<img src="https://raw.githubusercontent.com/AnonymouX47/term-image/main/docs/source/resources/tui.png">

<p align="center">
    <img src="https://static.pepy.tech/badge/term-image">
    <img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103">
    <img src="https://img.shields.io/github/last-commit/AnonymouX47/term-image">
    <a href='https://term-image.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/term-image/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href="https://twitter.com/intent/tweet?text=Display%20and%20browse%20images%20in%20the%20the%20terminal&url=https://github.com/AnonymouX47/term-image&hashtags=developers,images,terminal">
        <img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social">
    </a>
</p>

</div>


## Contents
- [Installation](#installation)
- [Features](#features)
- [Demo](#demo)
- [CLI/TUI Quick Start](#clitui-quick-start)
- [Library Quick Start](#library-quick-start)
- [Usage](#usage)
- [Contribution](#contribution)
- [WIP](#wip)
- [TODO](#todo)
- [Known Issues](#known-issues)
- [FAQs](#faqs)


## Installation

### Requirements
- Operating System: Unix / Linux / MacOS X / Windows (partial support, see the [FAQs](https://term-image.readthedocs.io/en/latest/faqs.html))
- [Python](https://www.python.org/) >= 3.7
- A Terminal emulator with full Unicode support and ANSI 24-bit color support
  - Plans are in place to support a wider variety of terminal emulators, whether not meeting or surpassing these requirements (see [here](https://term-image.readthedocs.io/en/latest/library/index.html#planned-features)).

### Steps
The latest **stable** version can be installed from [PyPI](https://pypi.python.org/pypi/term-image) using `pip`:

```shell
pip install term-image
```

The **development** version can be installed thus:
Clone this repository, then navigate into the project directory in a terminal and run:

```shell
pip install .
```

### Supported Terminal Emulators
See [here](https://term-image.readthedocs.io/en/latest/installation.html#supported-terminal-emulators) for a list of tested terminal emulators.

If you've tested `term-image` on any other terminal emulator that meets all requirements, please mention the name in a new thread under [this discussion](https://github.com/AnonymouX47/term-image/discussions/4).
Also, if you're having an issue with terminal support, you may report or view information about it in the discussion linked above.


## Features

### Library features
- Multiple image format support
  - Basically all formats supported by [`PIL.Image.open()`](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html)
- Multiple image sources (PIL image, local file, URL)
- Multiple render styles
- Support for multiple terminal graphics protocols
- Transparency support (with multiple options)
- Animated image support (including transparent ones)
  - Fully controllable and efficient iteration over frames of animated images
  - Image animation with controllable parameters
- Terminal size awareness
- Variable image size
- Automatic image sizing; best fit within the terminal window or a given size
- Variable image scale
- Horizontal and vertical alignment/padding
- Automatic and manual font-ratio adjustment
- and more... :grin:

### CLI/TUI features
- Basically everything the library supports
- Individual image display
- Browse multiple images
- Browse directories (recursively) [TUI]
- Image grids [TUI]
- Context-based controls [TUI]
- Dynamic controls (context actions are disabled and enabled dynamically) [TUI]
- Customizable controls and configuration options
- Automatic adjustment upon terminal resize [TUI]
- Image deletion [TUI]
- Smooth and fairly performant experience
- Takes advantage of both concurrency and parallelism
- Notification system
- Detailed logging system
- and more... :grin:


## Demo

<details>
<summary>Click to expand</summary>

[TUI Demo Video](https://user-images.githubusercontent.com/61663146/163809903-e8fb254b-a0aa-4d0d-9fc9-dd676c10b735.mp4)

_\*The video was recorded at normal speed and not sped up._

</details>


## CLI/TUI Quick Start

From a local image file
```shell
term-image path/to/image.png
```

From a URL
```shell
term-image https://www.example.com/image.png
```

If the image is animated (GIF, WEBP), the animation is infinitely looped **by default** but can be stopped with `Ctrl-C`.

**By default, if multiple sources or at least one directory is given, the TUI (Text-based/Terminal User Interface) is launched to navigate through the images (and/or directories).**

**NOTE:** `python -m term_image` can be used as an alternative to the `term-image` command **(take note of the _underscore_ VS _hyphen_)**.


## Library Quick Start

### Creating an instance

```python
from term_image.image import from_file

image = from_file("path/to/image.png")
```

You can also use a URL if you don't have the file stored locally
```python
from term_image.image import from_url

image = from_url("https://www.example.com/image.png")
```

The library can also be used with PIL images
```python
from PIL import Image
from term_image.image import AutoImage

img = Image.open("path/to/image.png")
image = AutoImage(img)
```

### Drawing/Displaying an image to/in the terminal

There are two ways to draw an image to the terminal.

#### 1. The `draw()` method
```python
image.draw()
```

#### 2. Using `print()` with a rendered image
```python
print(image)  # without formatting
```
OR
```python
print(f"{image:>200.^100#ffffff}")  # with formatting
```

For animated images, only the first method can animate the output, the second only outputs the current frame.


## Usage

### Library
See the [tutorial](https://term-image.readthedocs.io/en/latest/library/tutorial.html) for a more detailed introduction and the [reference](https://term-image.readthedocs.io/en/latest/library/reference/index.html) for full descriptions and details of the available features.

### CLI (Command-Line Interface)
Run `term-image --help` to see the full usage info and list of options.

### TUI (Text-based/Terminal User Interface)
The controls are **context-based** and displayed at the bottom of the terminal window.
Pressing the `F1` key (in most contexts) brings up a **help** menu describing the available controls (called *actions*) in that context.

The TUI can be configured by modifying the config file `~/.term_image/config.json`. See the [Configuration](https://term-image.readthedocs.io/en/latest/viewer/config.html) section of the docs.

[Here](https://github.com/AnonymouX47/term-image/blob/main/vim-style_config.json) is a config file with Vim-style key-bindings (majorly navigation). *Remember to rename the file to `config.json`.*


## Contribution

If you've found any bug or want to suggest a new feature, please open a new [issue](https://github.com/AnonymouX47/term-image/issues) with proper description, after browsing/searching through the existing issues and making sure you won't create a duplicate.

For code contributions, please read through the [guidelines](https://github.com/AnonymouX47/term-image/blob/main/CONTRIBUTING.md).

Also, check out the [WIP](#wip) and [TODO](#todo) sections below.
If you wish to work on any of the listed tasks, please go through the [issues](https://github.com/AnonymouX47/term-image/issues) tab and join in on an ongoing discussion about the task or create a new issue if one hasn't been created yet, so that the implementation can be discussed.

Hint: You can filter issues by *label* or simply *search* using the task's name or description.

For anything other than the above (such as questions or anything that would fit under the term "discussion"), please open a new [discussion](https://github.com/AnonymouX47/term-image/discussions) instead.

Thanks! :heart:


## WIP
- Support for terminal graphics protocols (See [#23](https://github.com/AnonymouX47/term-image/issues/23))
- Performace Improvements

## TODO

Check [here](https://term-image.readthedocs.io/en/latest/library/index.html#planned-features) for the library and [here](https://term-image.readthedocs.io/en/latest/viewer/index.html#planned-features) for the image viewer.

## Known Issues

Check [here](https://term-image.readthedocs.io/en/latest/library/index.html#known-issues) for the library and [here](https://term-image.readthedocs.io/en/latest/viewer/index.html#known-issues) for the image viewer.

## FAQs
See the [FAQs](https://term-image.readthedocs.io/en/latest/faqs.html) section of the docs.

from pathlib import Path

import pytest

from term_image.image import AutoImage, BaseImage, ImageSource, from_file

from .test_base import BytesPath, python_image, python_img


class TestConvinience:
    def test_auto_image(self):
        with pytest.raises(TypeError, match=r"'image'"):
            AutoImage(python_image)

        # Ensure size arguments get through
        with pytest.raises(ValueError, match=r"both width and height"):
            AutoImage(python_img, width=1, height=1)

        # Ensure scale argument gets through
        with pytest.raises(TypeError, match=r"'scale'"):
            AutoImage(python_img, scale=0.5)

        assert isinstance(AutoImage(python_img), BaseImage)

    def test_from_file(self):
        with pytest.raises(TypeError, match=r"'filepath'"):
            from_file(python_img)

        # Ensure size arguments get through
        with pytest.raises(ValueError, match=r"both width and height"):
            from_file(python_image, width=1, height=1)

        # Ensure scale argument gets through
        with pytest.raises(TypeError, match=r"'scale'"):
            from_file(python_image, scale=1.0)

        for path in (python_image, Path(python_image), BytesPath(python_image)):
            assert isinstance(from_file(path), BaseImage)


def test_image_source():
    assert len(ImageSource) == 3
    assert all(member.name == name for name, member in ImageSource.__members__.items())


def test_style():
    class MyImage(BaseImage):
        pass

    assert MyImage.style is None
    assert str(MyImage) == repr(MyImage)

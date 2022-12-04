import PIL.Image
import PIL.ImageTk


class Image:
    def __init__(self, path, width=0, height=0):
        self._open_image(path)
        self._set_abs_dimensions(width, height)
        self._create_image_tk(self._image)
        self._change_image_tk_dimensions(width, height)

    @property
    def image_tk(self):
        return self._image_tk

    def resize(self, abs_scale_w, abs_scale_h):
        width, height = self._calculate_dimensions(abs_scale_w, abs_scale_h)
        self._change_image_tk_dimensions(width, height)

    def _open_image(self, path):
        self._image = PIL.Image.open(path)

    def _set_abs_dimensions(self, width, height):
        self._abs_width = width if width else self._image.width
        self._abs_height = height if height else self._image.height

    def _create_image_tk(self, image):
        self._image_tk = PIL.ImageTk.PhotoImage(image=image)

    def _change_image_tk_dimensions(self, width, height):
        if width and height:
            image = self._resize_image(width, height)
            self._create_image_tk(image)

    def _resize_image(self, width, height):
        return self._image.resize((width, height))

    def _calculate_dimensions(self, abs_scale_w, abs_scale_h):
        return round(abs_scale_w * self._abs_width), round(abs_scale_h * self._abs_height)

import csv
import tkinter
import tkinter.ttk
from pathlib import Path

from src.composite import Composite
from src.image import Image


class BreweryTab(tkinter.ttk.Frame, Composite):
    def __init__(self, parent, config):
        tkinter.ttk.Frame.__init__(self, parent)
        Composite.__init__(self, config)


class Canvas(tkinter.Canvas, Composite):
    def __init__(self, parent, config):
        tkinter.Canvas.__init__(self, parent)
        Composite.__init__(self, config)

        self.bind('<Configure>', self._resize)

    def position(self):
        super().position()

        self.place(relwidth=1, relheight=1)

    def _initialize(self, config):
        super()._initialize(config)

        self._set_imgs_data_csv_path(config)
        self._set_imgs_coords_csv_path(config)
        self._create_imgs_and_canvas_items()

    def _set_imgs_data_csv_path(self, config):
        self._imgs_data_csv_path = config.get('imgs_data_csv_path')

    def _set_imgs_coords_csv_path(self, config):
        self._imgs_coords_csv_path = config.get('imgs_coords_csv_path')

    def _create_imgs_and_canvas_items(self):
        if self._imgs_data_csv_path and self._imgs_coords_csv_path:
            self._imgs_data = self._read_csv_file(self._imgs_data_csv_path)
            self._create_images()
            self._calculate_abs_dimensions()
            self._imgs_coords = self._read_csv_file(self._imgs_coords_csv_path)
            self._create_canvas_items()

    def _read_csv_file(self, path):
        with open(path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=";")
            return list(reader)

    def _create_images(self):
        self._imgs = {}
        for img in self._imgs_data:
            self._imgs.update({img['name']: Image(Path(__file__).parent / f"./img/{img['name']}.png",
                                                  int(img['width']),
                                                  int(img['height']))})

    def _calculate_abs_dimensions(self):
        self._abs_width, self._abs_height = max(int(img['width']) for img in self._imgs_data), \
                                            max(int(img['height']) for img in self._imgs_data)

    def _create_canvas_items(self):
        self._canvas_items = []
        for img in self._imgs_coords:
            self._canvas_items.append(self.create_image(float(img['x']) * self._abs_width,
                                                        float(img['y']) * self._abs_height,
                                                        anchor=tkinter.CENTER,
                                                        image=self._imgs[img['name']].image_tk))

    def _resize(self, event):
        abs_scale_w, abs_scale_h = self._calculate_abs_scales(event)
        self._resize_images(abs_scale_w, abs_scale_h)
        self._resize_canvas_items(abs_scale_w, abs_scale_h)

    def _calculate_abs_scales(self, event):
        return event.width / self._abs_width, event.height / self._abs_height

    def _resize_images(self, abs_scale_w, abs_scale_h):
        for img in self._imgs.values():
            img.resize(abs_scale_w, abs_scale_h)

    def _resize_canvas_items(self, abs_scale_w, abs_scale_h):
        for canvas_item, img in zip(self._canvas_items, self._imgs_coords):
            self.itemconfig(canvas_item, image=self._imgs[img['name']].image_tk)
            self.coords(canvas_item,
                        round(abs_scale_w * float(img['x']) * self._abs_width),
                        round(abs_scale_h * float(img['y']) * self._abs_height),
                        )

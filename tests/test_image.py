import math
import tkinter.ttk
import unittest
from pathlib import Path

import PIL.ImageTk

from src.image import Image


class TestImage(unittest.TestCase):
    image_path = Path(__file__).parent / "./files/image.bmp"

    def setUp(self):
        super().setUp()

        tkinter.Tk()

        self.expected_image_tk = PIL.ImageTk.PhotoImage(file=self.image_path)

    def test_Should_CreateImageTk_When_GivenImagePath(self):
        image = Image(self.image_path)

        self.assertEqual(self.expected_image_tk.width(), image.image_tk.width())
        self.assertEqual(self.expected_image_tk.height(), image.image_tk.height())

    def test_Should_CreateImageTkWithImageDimensions_When_GivenImagePathAndWidth(self):
        image = Image(path=self.image_path, width=123)

        self.assertEqual(self.expected_image_tk.width(), image.image_tk.width())
        self.assertEqual(self.expected_image_tk.height(), image.image_tk.height())

    def test_Should_CreateImageTkWithImageDimensions_When_GivenImagePathAndHeight(self):
        image = Image(path=self.image_path, height=123)

        self.assertEqual(self.expected_image_tk.width(), image.image_tk.width())
        self.assertEqual(self.expected_image_tk.height(), image.image_tk.height())

    def test_Should_CreateImageTkWithChangedDimensions_When_GivenImagePathAndDimensions(self):
        expected_width, expected_height = 40, 30
        image = Image(path=self.image_path, width=expected_width, height=expected_height)

        self.assertEqual(expected_width, image.image_tk.width())
        self.assertEqual(expected_height, image.image_tk.height())

    def test_Should_ResizeImageTkAndFloorDimensions_When_GivenScalesResultingInDimensionsCloserToLowerEvenNumber(self):
        image = Image(self.image_path)

        abs_scale_w, abs_scale_h = 0.5, 1 / 268
        image.resize(abs_scale_w, abs_scale_h)

        expected_width, expected_height = math.floor(self.expected_image_tk.width() * abs_scale_w), \
                                          math.floor(self.expected_image_tk.height() * abs_scale_h)

        self.assertEqual(expected_width, image.image_tk.width())
        self.assertEqual(expected_height, image.image_tk.height())

    def test_Should_ResizeImageTkAndCeilDimensions_When_GivenScalesResultingInDimensionsCloserToHigherEvenNumber(self):
        image = Image(self.image_path)

        abs_scale_w, abs_scale_h = 1.5, 0.25
        image.resize(abs_scale_w, abs_scale_h)

        expected_width, expected_height = math.ceil(self.expected_image_tk.width() * abs_scale_w), \
                                          math.ceil(self.expected_image_tk.height() * abs_scale_h)

        self.assertEqual(expected_width, image.image_tk.width())
        self.assertEqual(expected_height, image.image_tk.height())

    def test_Should_ResizeImageTk_When_GivenScale(self):
        image = Image(self.image_path)

        expected_width, expected_height = 200, 192
        abs_scale_w, abs_scale_h = expected_width / self.expected_image_tk.width(), \
                                   expected_height / self.expected_image_tk.height()
        image.resize(abs_scale_w, abs_scale_h)

        self.assertEqual(expected_width, image.image_tk.width())
        self.assertEqual(expected_height, image.image_tk.height())

    def test_Should_ResizeImageTkWithDimensions_When_GivenScale(self):
        width, height = 1193, 670
        image = Image(path=self.image_path, width=width, height=height)

        expected_width, expected_height = 200, 192
        abs_scale_w, abs_scale_h = expected_width / self.expected_image_tk.width(), \
                                   expected_height / self.expected_image_tk.height()
        image.resize(abs_scale_w, abs_scale_h)

        self.assertEqual(expected_width, image.image_tk.width())
        self.assertEqual(expected_height, image.image_tk.height())

    def test_Should_ResizeImageTk_When_GivenScalesMultipleTimes(self):
        image = Image(self.image_path)

        abs_scale_w, abs_scale_h = 0.5, 0.25
        image.resize(abs_scale_w, abs_scale_h)
        image.resize(1, 1)

        self.assertEqual(self.expected_image_tk.width(), image.image_tk.width())
        self.assertEqual(self.expected_image_tk.height(), image.image_tk.height())

    def test_Should_ResizeImageTkWithDimensions_When_GivenScalesMultipleTimes(self):
        expected_width, expected_height = 999, 499
        image = Image(path=self.image_path, width=expected_width, height=expected_height)

        abs_scale_w, abs_scale_h = 0.5, 0.25
        image.resize(abs_scale_w, abs_scale_h)
        image.resize(1, 1)

        self.assertEqual(expected_width, image.image_tk.width())
        self.assertEqual(expected_height, image.image_tk.height())


if __name__ == "__main__":
    unittest.main()

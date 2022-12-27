import unittest
from pathlib import Path

from src.application_window import ApplicationWindow


class TestApplicationWindow(unittest.TestCase):
    app = None

    async def _start_app(self):
        self.app.position()
        self.app.mainloop()

    def setUp(self):
        super().setUp()

        self.app = ApplicationWindow({'title': "Hajle Silesia Homebrewing System"})

    def tearDown(self):
        self.app.destroy()

    def test_Should_GetEmptyContent_When_GivenEmptyRawContent(self):
        expected_title = "Hajle Silesia Homebrewing System"
        title = self.app.winfo_toplevel().title()

        self.assertEqual(expected_title, title)

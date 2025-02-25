import csv
import pathlib

from object_factory import HTML


def create_canvas(tab):
    with pathlib.Path(f"config/{tab}.csv").open(encoding="utf-8") as csv_file:
        reader = csv.DictReader(
            [row for row in csv_file if not row.startswith("#")],
            delimiter=";",
        )

        elements = [{key.strip(): value.strip() for key, value in row.items() if value.strip()} for row in reader]

    for element in elements:
        HTML(
            element["tag"],
            element.get("parent"),
            element,
        )

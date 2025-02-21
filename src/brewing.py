import csv

from object_factory import HTML


def create_brewing():
    brewing_tab = HTML(
        "div",
        None,
        {
            "id": "brewing",
            "class": "canvas",
            "hidden": True,
        },
    )

    with open("./config/brewing.csv", encoding="utf-8") as csv_file:
        reader = csv.DictReader(
            [row for row in csv_file if not row.startswith("#")],
            delimiter=";",
        )

        elements = [
            {key.strip(): value.strip() for key, value in row.items() if value.strip()}
            for row in reader
        ]

    for element in elements:
        HTML(
            element["tag"],
            brewing_tab.element,
            element,
        )

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

    with open("./config/brewing_imgs_coords.csv", encoding="utf-8") as csv_file:
        reader = csv.DictReader(
            csv_file,
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

    HTML(
        "script",
        brewing_tab.element,
        {
            "script": """if (flvjs.isSupported()) {
            var videoElement = document.getElementById('mlt_sightglass_video');
            var flvPlayer = flvjs.createPlayer({
                type: 'flv',
                url: 'https://srs-server.default.svc.cluster.local:8080/live/livestream.flv'
            });
            flvPlayer.attachMediaElement(videoElement);
            flvPlayer.load();
            flvPlayer.play();
        }""",
        },
    )

import threading

import uvicorn

from src.api import app, queue, events_handler


class APIThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)

        self.start()

    def run(self):
        uvicorn.run(app, host="0.0.0.0", port=8000, proxy_headers=True)  # nosec

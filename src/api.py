import base64
import json
import os
from queue import Queue

import requests
from fastapi import FastAPI, Request

from src.events_handler import EventsHandler

app = FastAPI()
queue = Queue()
events_handler = EventsHandler(queue)

notifier_host = os.getenv('FILE_CONTENT_PROCESSOR_SERVICE_HOST')
notifier_port = os.getenv('FILE_CONTENT_PROCESSOR_SERVICE_PORT')
notifier_url = f"http://{notifier_host}:{notifier_port}/observers/register"

host = os.getenv('FRONTEND_SERVICE_HOST')
port = os.getenv('FRONTEND_SERVICE_PORT')
url = f"http://{host}:{port}/update"

requests.post(notifier_url, base64.b64encode(json.dumps({'frontend': url}).encode()))


@app.get("/api")
async def api():
    return {"update",
            }


@app.post("/update")
async def update(request: Request):
    request_body_json = base64.b64decode(await request.body()).decode()
    request_body = json.loads(request_body_json)
    events_handler.notify(request_body)

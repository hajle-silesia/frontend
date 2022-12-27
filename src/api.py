import base64
import json
import queue
import threading

import fastapi
import kafka

from src.events_handler import EventsHandler


def load_events():
    consumer = kafka.KafkaConsumer(bootstrap_servers="kafka-cluster-kafka-bootstrap.event-streaming:9092",
                                   value_deserializer=lambda message: json.loads(base64.b64decode(message).decode()),
                                   )
    consumer.subscribe(topics=["file-content-processor-topic"])
    for event in consumer:
        events_handler.notify(event.value)


app = fastapi.FastAPI()
queue = queue.Queue()
events_handler = EventsHandler(queue)

events_thread = threading.Thread(target=load_events)
events_thread.start()


@app.get("/healthz")
async def healthz():
    return {'status': "ok"}

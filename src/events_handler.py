class EventsHandler:
    def __init__(self, queue):
        self._queue = queue

        self._subscribers = []

    def subscribe(self, component):
        self._subscribers.append(component)

    def notify(self, content):
        for subscriber in self._subscribers:
            self._queue.put(content)
            subscriber.event_generate('<<MessageGenerated>>')

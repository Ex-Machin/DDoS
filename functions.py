import threading

class ThreadJob(threading.Thread):
    def __init__(self, callback, event, interval):
        self.callback = callback
        self.event = event
        self.interval = interval
        super(ThreadJob, self).__init__()

    def run(self):
        while not self.event.wait(self.interval):
            self.callback()
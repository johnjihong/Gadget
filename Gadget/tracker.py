"""Task Tracker"""


from time import time
from .log import logger
from .utils import display
from typing import Callable
from threading import Thread
from ipywidgets.widgets import HTML



class Track:
    def __init__(self):
        self.elapsed = 0.0
        self.start_at = None
        self.result = None

    def run(self, *args, **kwargs):
        raise NotImplementedError

    def start(self, *args, **kwargs):
        if self.start_at is not None:
            raise RuntimeError('Already started.')

        self.start_at = time()
        thread = Thread(target=self.run, args=args, kwargs=kwargs)
        thread.start()

    def stop(self):
        if self.start_at is None:
            raise RuntimeError('No started.')

        self.elapsed = time() - self.start_at
        self.start_at = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self.start_at is not None


class Spinner(HTML, Track):
    """Run a task in a separate thread and display spinner during the execution.
    Notebook example:
        from time import sleep
        def long_running_task():
            for i in range(10):
                sleep(1)
        foo = Spinner(long_running_task)
        foo.start()
        foo
    """

    def __init__(self, task: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task = task
        self.value = '<i class="fa fa-spinner fa-spin" style="font-size: 80px; color: red;"></i>'

    def run(self, task: Callable):
        display(self, True)
        try:
            self.result = self.task()
        except Exception as err:
            logger.exception(err)
        finally:
            self.stop()

    def start(self, task: Callable):
        super().start(task)

    def stop(self):
        super().stop()
        display(self, False)
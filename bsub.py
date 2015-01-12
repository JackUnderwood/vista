__author__ = 'John'
from base import UI


class B(UI):
    def __init__(self, override=None):
        super().__init__()
        print("B __init__", override)

        runtime = {
            'myQueue': ("Click", '//*[@id="myqueue"]/span', ""),
            'myQueueGo': ("Click", '//*[@id="myqueueGo"]', "")
        }
        process = UI(override)
        process.update(runtime)
        order = ('myQueue', 'myQueueGo',)
        process.execute(order)

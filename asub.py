__author__ = 'John'
from base import UI


class A(UI):
    def __init__(self, override=None):
        super().__init__()
        print("A __init__", override)
        runtime = {
            'init': ("Click", "path1", ""),
            'login': ("Type", "path2", "Jack Black"),
            'submit': ("Click", "path3", "")
        }
        process = UI(override)
        process.update(runtime)
        order = ('init', 'login', 'submit')
        process.execute(order)
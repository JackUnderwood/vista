__author__ = 'John'
from base import UI


class B(UI):

    def __init__(self, override=None):
        super().__init__()
        print("B __init__", override)

        runtime = {
            'find': ("Click", "path4", ""),
            'search': ("Type", "path5", "Carrot"),
            'drop2': ("Select", "path7", "Middle Select"),
            'submit': ("Click", "path6", "")
        }

        process = UI(override)
        process.update(runtime)
        order = ('find', 'search', 'drop2', 'submit')
        process.execute(order)

__author__ = 'John'
"""
This is an abstract class that will setup the selenium driver and process all commands
from subclasses. This drives the user interface testing framework.
"""


class UI:
    runtime = {}
    override = {}

    def __init__(self, override=None):
        self.override = override
        print("UI __init__", override)

    def update(self, runtime):
        print("UI update()")
        if self.override:
            # override the 'passed in' runtime data
            runtime.update(self.override)
        self.runtime.update(runtime)

    def execute(self, items):
        for item in items:  # 'item' always expects three elements
            t = self.runtime.get(item, ("Unknown", "Unknown", "Unknown"))
            print(t)
            command, path, value = t
            if command == "Click":
                self.click(path)
            elif command == "Type":
                self.type(path, value)
            elif command == "Select":
                self.select(path, value)
            elif command == "Unknown":
                print("This command is unknown - throw an error")
            else:
                print("Throw an error")
            print()

    def click(self, path):
        print("This is a Click command")
        print("PATH is", path)

    def type(self, path, value):
        print("This is a Type command")
        print("PATH and VALUE is", path, value)

    def select(self, path, value):
        print("This is a Select command")
        print("PATH and VALUE is", path, value)

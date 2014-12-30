
__author__ = 'John'


class Strategy:
    runtime = {}

    def __init__(self):
        print("Strategy __init__")

    def update(self, runtime):
        print("Strategy update()")
        self.runtime.update(runtime)
        # ... TESTING...
        # for item in self.runtime:
        #     print(item)

    def execute(self, items):
        for item in items:  # 'item' always expects three elements
            t = self.runtime.get(item, ("Unknown", "Unknown", "Unknown"))
            print(t)
            command, path, value = t
            print("COMMAND:", command)
            if command == "Click":
                print("This is a Click command")
            elif command == "Type":
                print("This is a Type command")
            elif command == "Select":
                print("This is a Select command")
            elif command == "Unknown":
                print("This command is unknown - throw an error")
            else:
                print("Throw an error")


class A:
    runtime = {
        'init': ("Click", "path1", ""),
        'login': ("Type", "path2", "First Name"),
        'submit': ("Click", "path3", "")
    }

    strategy = Strategy()
    strategy.update(runtime)
    order = ('init', 'login', )
    strategy.execute(order)


class B:
    runtime = {
        'find': ("Click", "path4", ""),
        'search': ("Type", "path5", "Carrot"),
        'submit': ("Click", "path6", "")
    }

    strategy = Strategy()
    strategy.update(runtime)
    order = ('find', 'search', 'submit')
    strategy.execute(order)


print("\nHello, world!")

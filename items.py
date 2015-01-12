__author__ = 'John Underwood'


items = {
    "_item": ("click", "{xpath}", ""),
    "_embedded": "some_path_value",
    "access": ("type", "{id path :_embedded}", "Peter Pan"),
    "retrieve": ("select", "{id path}", "list_name2"),
    "_done": ("click", "{xpath}", ""),

    "result": ("content", "xpath", "don't remember")
}

# variable = MyClass(login=[

# ])
# variable.execute()


class StrategyExample:

    def __init__(self, func=None):
        if func:
            self.execute = func

    @staticmethod
    def execute():
        print("Original execution")


def execute_replacement1():
    print("Strategy 1")


def execute_replacement2():
    print("Strategy 2")

if __name__ == "__main__":

    strat0 = StrategyExample()
    strat1 = StrategyExample(execute_replacement1)
    strat2 = StrategyExample(execute_replacement2)

    strat0.execute()
    strat1.execute()
    strat2.execute()
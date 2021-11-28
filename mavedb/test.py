class Parent:
    def __init__(self, *args):
        # How to access *args variable names here?
        # In this example: foo, bar
        pass


class Child(Parent):
    def __init__(self, foo, bar):
        super().__init__(foo, bar)

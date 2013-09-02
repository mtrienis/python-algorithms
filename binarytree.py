class BinaryTree:

    def __init__(self, name):
        self.name = name
        self.visited = False

    def visit(self):
        self.visited = True

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name + ' ' + str(self.visited)
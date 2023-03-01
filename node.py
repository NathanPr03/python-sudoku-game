class Node:

    def __init__(self):
        self.up: Node = self
        self.down: Node = self
        self.left: Node = self
        self.right: Node = self
        self.column_header: Node = self
        self.column_size: int = 0
        self.sudoku_row: int = -1
        self.sudoku_column: int = -1
        self.sudoku_value: int = -1
        self.exact_matrix_row: int = -1
        self.exact_matrix_column: int = -1
        self.node_type = "Undefined" # TODO: Lets make these into separate classes

    def prepend_left(self, node):
        previous = node.left
        self.left = previous
        self.right = node

        node.left = self
        previous.right = self

        return node

    def prepend_down(self):
        previous = self.column_header.up

        self.down = self.column_header
        self.up = previous

        self.column_header.up = self

        previous.down = self

        self.column_header.column_size += 1



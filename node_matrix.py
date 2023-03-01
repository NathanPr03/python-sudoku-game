from __future__ import annotations

from constants import EXACT_COVER_MATRIX_COLUMNS, EXACT_COVER_MATRIX_ROWS
from node import Node


class NodeMatrix:
    root_node: Node = Node()
    column_header_nodes: list[Node] = []

    def __init__(self):
        self.root_node.node_type = "Root"

    def create_sparse_matrix(self, cover_matrix: list[list]):

        for column_index in range(EXACT_COVER_MATRIX_COLUMNS):
            column_header = Node()
            self.root_node = column_header.prepend_left(self.root_node)
            self.column_header_nodes.append(column_header)
            column_header.column_header = column_header
            column_header.node_type = "Column Header"

        for row_index in range(EXACT_COVER_MATRIX_ROWS):
            row_start: Node | None = None
            for column_index in range(EXACT_COVER_MATRIX_COLUMNS):
                if cover_matrix[row_index][column_index] == 1:
                    column_header = self.column_header_nodes[column_index]
                    column_header.exact_matrix_column = column_index

                    node = Node()
                    node.column_header = column_header
                    node.prepend_down()
                    node.exact_matrix_column = column_index
                    node.exact_matrix_row = row_index
                    node.node_type = "Node"
                    if row_start:
                        previous = row_start.left
                        node.right = row_start
                        row_start.left = node
                        node.left = previous
                        previous.right = node
                    else:
                        row_start = node
        return self.root_node

    def solve(self, k, solutions=[]):
        global answers
        print(k)
        if self.root_node.right == self.root_node:
            answers.append(solutions[:])
            return

        column = self.__get_min_column()
        self.__cover(column)

        row_node = column.down
        while row_node != column:
            solutions.append(row_node)

            right_node = row_node.right
            while right_node != row_node:
                self.__cover(right_node)
                right_node = right_node.right

            self.solve(k + 1, solutions)

            solutions.pop()

            column = row_node.column_header
            left_node = row_node.left
            while left_node != row_node:
                if left_node != self.root_node:
                    self.__uncover(left_node)
                left_node = left_node.left
            row_node = row_node.down

        self.__uncover(column)

    def __cover(self, node: Node):
        column_node = node.column_header

        column_node.right.left = column_node.left
        column_node.left.right = column_node.right

        column_traverser: Node = column_node.down
        while column_traverser != column_node:
            row_traverser:Node = column_traverser.right

            while row_traverser != column_traverser:
                row_traverser.up.down = row_traverser.down
                row_traverser.down.up = row_traverser.up
                row_traverser.column_header.column_size -= 1

                row_traverser = row_traverser.right
            column_traverser = column_traverser.down

    def __uncover(self, node: Node):
        column_node = node.column_header

        reverse_column_traverser: Node = column_node.up
        while reverse_column_traverser != column_node:
            reverse_row_traverser = reverse_column_traverser.left

            while reverse_row_traverser != reverse_column_traverser:
                reverse_row_traverser.up.down = reverse_row_traverser
                reverse_row_traverser.down.up = reverse_row_traverser
                reverse_row_traverser.column_header.column_size += 1

                reverse_row_traverser = reverse_row_traverser.left

            reverse_column_traverser = reverse_column_traverser.up

        column_node.right.left = column_node
        column_node.left.right = column_node

    # REMOVE THIS
    def __get_min_column(self):
        node = self.root_node.right
        min_column = node
        while node.right != self.root_node:
            node = node.right
            if node.column_size < min_column.column_size:
                if node.column_size > 0:
                    min_column = node
        return min_column



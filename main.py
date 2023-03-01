import empty_nine_by_nine_cover_matrix
from array_matrix import ArrayMatrix
from node import Node
from node_matrix import NodeMatrix


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    board: list[list] = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 0],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    # board: list[list] = [[0, 0, 0, 0, 0, 0, 0, 5, 0],
    #                      [2, 0, 7, 0, 0, 9, 0, 0, 0],
    #                      [6, 0, 0, 3, 5, 1, 0, 0, 0],
    #                      [5, 0, 0, 0, 0, 0, 0, 1, 0],
    #                      [0, 0, 3, 0, 0, 0, 0, 0, 8],
    #                      [0, 0, 0, 8, 2, 0, 5, 3, 0],
    #                      [0, 0, 0, 0, 7, 0, 8, 0, 4],
    #                      [0, 0, 6, 2, 0, 0, 0, 0, 0],
    #                      [0, 8, 0, 0, 0, 0, 7, 0, 0]]

    cover_matrix: list[list] = empty_nine_by_nine_cover_matrix.nine_by_nine_cover_matrix()

    array_matrix = ArrayMatrix(cover_matrix)
    array_matrix.build_sparse_matrix(board)
    # array_matrix.pretty_print()

    node_matrix = NodeMatrix()
    root: Node = node_matrix.create_sparse_matrix(cover_matrix)
    node_matrix.solve(0)

    hi = 'he'

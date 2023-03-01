from constants import BOARD_SIZE, SQRT_BOARD_SIZE, BOARD_SIZE_SQUARED, EXACT_COVER_MATRIX_ROWS


class ArrayMatrix:
    def __init__(self, cover_matrix: list[list]):
        self.cover_matrix = cover_matrix

    def pretty_print(
            self
    ):
        print("---------------------------------------------------------------------")
        for i in range(len(self.cover_matrix)):
            for j in range(len(self.cover_matrix[1])):
                if j % BOARD_SIZE_SQUARED == 0:
                    print("|", end="")
                print(self.cover_matrix[i][j], end="")

            print("|", end="")
            print()
            print("---------------------------------------------------------------------")

    def build_sparse_matrix(
            self, sudoku_board: list[list]
    ):
        for row_index in range(BOARD_SIZE):
            for column_index in range(BOARD_SIZE):
                val_of_cell: int = sudoku_board[row_index][column_index]

                if val_of_cell == 0:
                    self.__create_rows_for_non_clue(
                        column_index,
                        row_index
                    )
                else:
                    self.__create_rows_for_clue(
                        column_index,
                        row_index,
                        val_of_cell - 1
                    )

    def __create_rows_for_non_clue(
            self,
            column_index: int,
            row_index: int
    ):
        for value in range(BOARD_SIZE):
            self.__fill_in_array_matrix(
                column_index,
                row_index,
                value
            )

    def __create_rows_for_clue(
            self,
            column_index: int,
            row_index: int,
            value: int
    ):
        return self.__fill_in_array_matrix(
            column_index,
            row_index,
            value
        )

    def __fill_in_array_matrix(
            self,
            column_index: int,
            row_index: int,
            value: int
    ):
        matrix_row_index = \
            column_index + \
            (BOARD_SIZE * row_index) + \
            (BOARD_SIZE_SQUARED * value)

        matrix_column_index_row: int = SQRT_BOARD_SIZE * \
                                       BOARD_SIZE * \
                                       value + \
                                       row_index

        matrix_column_index_value: int = BOARD_SIZE_SQUARED + \
                                         SQRT_BOARD_SIZE * \
                                         BOARD_SIZE_SQUARED + \
                                         (column_index + BOARD_SIZE * row_index)

        self.cover_matrix[matrix_row_index][matrix_column_index_row] = 1
        self.cover_matrix[matrix_row_index][matrix_column_index_value] = 1

    def __generate_array_matrix(
            self,
            row_index: int
    ):
        self.__row_constraint(row_index)
        self.__column_constraint(row_index)

    def __row_constraint(self, row_index: int):
        pullback: int = BOARD_SIZE_SQUARED
        column: int = BOARD_SIZE_SQUARED

        for row in range(EXACT_COVER_MATRIX_ROWS):
            if row % BOARD_SIZE_SQUARED == 0 and row > 1:
                pullback += BOARD_SIZE

            if column % BOARD_SIZE == 0:
                column = pullback

            if row == row_index:
                self.cover_matrix[row][column] = 1
            column += 1

    def __column_constraint(self, row_index: int):
        board_size_squared_times_three: int = BOARD_SIZE_SQUARED * 3
        pullback: int = board_size_squared_times_three
        column: int = board_size_squared_times_three

        for row in range(EXACT_COVER_MATRIX_ROWS):
            if row % (BOARD_SIZE_SQUARED * SQRT_BOARD_SIZE) == 0 and row > 1:
                pullback += BOARD_SIZE
            elif row % BOARD_SIZE_SQUARED == 0 and row > 1:
                pullback -= BOARD_SIZE * (SQRT_BOARD_SIZE - 1)
            elif row % (BOARD_SIZE * SQRT_BOARD_SIZE) == 0 and row > 1:
                pullback += BOARD_SIZE

            if column % BOARD_SIZE == 0:
                column = pullback

            if row == row_index:
                self.cover_matrix[row][column] = 1

            column += 1

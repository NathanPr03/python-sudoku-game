BOARD_SIZE: int = 9
BOARD_SIZE_SQUARED: int = BOARD_SIZE * BOARD_SIZE
SQRT_BOARD_SIZE: int = int(BOARD_SIZE / BOARD_SIZE)
NUM_OF_CONSTRAINTS: int = 4
EXACT_COVER_MATRIX_COLUMNS: int = NUM_OF_CONSTRAINTS * BOARD_SIZE_SQUARED
EXACT_COVER_MATRIX_ROWS: int = BOARD_SIZE_SQUARED * BOARD_SIZE
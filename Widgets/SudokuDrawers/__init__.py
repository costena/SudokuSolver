from typing import Optional

from Sudokus.BlackoutSudoku import BlackoutSudoku
from Sudokus.Sudoku import Sudoku
from .BlackoutSudokuDrawer import BlackoutSudokuDrawer
from .SudokuDrawer import SudokuDrawer

SudokuDrawers = {
    Sudoku: SudokuDrawer,
    BlackoutSudoku: BlackoutSudokuDrawer,
}

def getSudokuDrawerType(sudoku_type: type) -> Optional[type]:
    current_type = sudoku_type
    while current_type is not None:
        drawer_type = SudokuDrawers.get(current_type)
        if drawer_type is None:
            current_type = current_type.__base__
            continue
        return drawer_type

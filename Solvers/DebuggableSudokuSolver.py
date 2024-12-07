from typing import Callable, List, Tuple, Optional

from Constraints.Constraint import Constraint
from Solvers.SudokuSolver import SudokuSolver
from Sudokus.Sudoku import Sudoku


class DebuggableSudokuSolver(SudokuSolver):
    def __init__(self, sudoku: Sudoku, step_callback: Callable):
        super(DebuggableSudokuSolver, self).__init__(sudoku)
        self.step_callback: Callable = step_callback
        self.constraint_contexts: List[Optional[Constraint]] = []
        self.eliminating_contexts: List[Tuple[int, int, int]] = []
        self.filling_contexts: List[Tuple[int, int, int]] = []

    def set_step_callback(self, step_callback: Callable):
        self.step_callback = step_callback

    def active(self, constraint: Constraint) -> bool:
        self.constraint_contexts.append(constraint)
        result: bool = super(DebuggableSudokuSolver, self).active(constraint)
        self.constraint_contexts.pop()
        return result

    def resolve(self) -> bool:
        self.constraint_contexts.append(None)
        result: bool = super(DebuggableSudokuSolver, self).resolve()
        self.constraint_contexts.pop()
        return result

    def eliminate(self, x: int, y: int, number: int) -> bool:
        self.eliminating_contexts.append((x, y, number))
        result: bool = super(DebuggableSudokuSolver, self).eliminate(x, y, number)
        self.eliminating_contexts.pop()
        return result

    def fill(self, x: int, y: int, number: int) -> bool:
        self.filling_contexts.append((x, y, number))
        result: bool = super(DebuggableSudokuSolver, self).fill(x, y, number)
        self.filling_contexts.pop()
        return result

    def on_number_filled(self, constraint: Constraint, x: int, y: int, number: int):
        self.constraint_contexts.append(constraint)
        result: bool = super(DebuggableSudokuSolver, self).on_number_filled(constraint, x, y, number)
        self.constraint_contexts.pop()
        return result

    def on_number_eliminated(self, constraint: Constraint, x: int, y: int, number: int):
        self.constraint_contexts.append(constraint)
        result: bool = super(DebuggableSudokuSolver, self).on_number_eliminated(constraint, x, y, number)
        self.constraint_contexts.pop()
        return result

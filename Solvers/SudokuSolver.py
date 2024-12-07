import copy
import pickle
from typing import List, Set, Optional, Callable

from Constraints.Constraint import Constraint
from Sudokus.Sudoku import Sudoku


class SudokuSolver(object):
    def __init__(self, sudoku: Sudoku):
        self.sudoku: Sudoku = sudoku
        self.possible_numbers_table: List[List[Set[int]]] = [
            [
                set(range(1, 10))
                for _ in range(9)
            ]
            for _ in range(9)
        ]
        self.step_callback: Optional[Callable] = None

    def solve(self) -> bool:
        for constraint in self.sudoku.constraints:
            if not self.active(constraint):
                return False
        return self.resolve()

    def active(self, constraint: Constraint) -> bool:
        return constraint.active(self)

    def resolve(self) -> bool:
        entropy2position = {}
        for y in range(9):
            for x in range(9):
                possible_numbers = self.ref_possible_numbers(x, y)
                if len(possible_numbers) == 1:
                    continue
                entropy2position.setdefault(len(possible_numbers), []).append((x, y))
        if len(entropy2position) == 0:
            return True
        for _, positions in sorted(entropy2position.items()):
            for x, y in positions:
                possible_numbers = self.ref_possible_numbers(x, y)
                saved_table = pickle.dumps(self.possible_numbers_table)
                for number in copy.copy(possible_numbers):
                    if self.fill(x, y, number):
                        if self.resolve():
                            return True
                    self.possible_numbers_table = pickle.loads(saved_table)
                return False
        return True

    def ref_possible_numbers(self, x: int, y: int) -> Set[int]:
        return self.possible_numbers_table[y][x]

    def get_number(self, x: int, y: int) -> int:
        possible_numbers = self.ref_possible_numbers(x, y)
        for number in possible_numbers:
            return number

    def eliminate(self, x: int, y: int, number: int) -> bool:
        possible_numbers = self.ref_possible_numbers(x, y)
        if number not in possible_numbers:
            return True
        if len(possible_numbers) == 1:
            return False
        if self.step_callback:
            if not self.step_callback():
                return False
        possible_numbers.remove(number)
        if len(possible_numbers) == 1:
            for constraint in self.sudoku.constraints:
                if not self.on_number_filled(constraint, x, y, self.get_number(x, y)):
                    return False
        for constraint in self.sudoku.constraints:
            if not self.on_number_eliminated(constraint, x, y, number):
                return False
        return True

    def on_number_filled(self, constraint: Constraint, x: int, y: int, number: int):
        return constraint.on_number_filled(x, y, number, self)

    def on_number_eliminated(self, constraint: Constraint, x: int, y: int, number: int):
        return constraint.on_number_eliminated(x, y, number, self)

    def fill(self, x: int, y: int, number: int) -> bool:
        possible_numbers = self.ref_possible_numbers(x, y)
        if number not in possible_numbers:
            return False
        if len(possible_numbers) == 1:
            return True
        for other_number in [other_number for other_number in possible_numbers if other_number != number]:
            if not self.eliminate(x, y, other_number):
                return False
        return True

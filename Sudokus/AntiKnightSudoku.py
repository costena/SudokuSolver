from typing import Iterable, Optional

from Constraints.AntiKnightConstraint import AntiKnightConstraint
from Sudokus.StandardSudoku import StandardSudoku


class AntiKnightSudoku(StandardSudoku):
    def initConstraints(self, known_numbers: Iterable[Iterable[Optional[int]]]):
        super(AntiKnightSudoku, self).initConstraints(known_numbers)
        self.constraints.append(AntiKnightConstraint())

from typing import Iterable, Optional

from Constraints.DiagonalConstraint import DiagonalConstraint
from Sudokus.StandardSudoku import StandardSudoku


class DiagonalSudoku(StandardSudoku):
    def __init__(self, known_numbers: Iterable[Iterable[Optional[int]]]):
        super(DiagonalSudoku, self).__init__(known_numbers)
        self.initDiagonalConstraints()

    def initDiagonalConstraints(self) -> None:
        self.constraints.extend([
            DiagonalConstraint(False),
            DiagonalConstraint(True),
        ])

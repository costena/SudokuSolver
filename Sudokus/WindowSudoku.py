from typing import Iterable, Optional

from Constraints.WindowBlockConstraint import WindowBlockConstraint
from Sudokus.StandardSudoku import StandardSudoku


class WindowSudoku(StandardSudoku):
    def __init__(self, known_numbers: Iterable[Iterable[Optional[int]]]):
        super(WindowSudoku, self).__init__(known_numbers)
        self.initWindowConstraints()

    def initWindowConstraints(self) -> None:
        self.constraints.extend([
            WindowBlockConstraint(1, 1),
            WindowBlockConstraint(5, 1),
            WindowBlockConstraint(1, 5),
            WindowBlockConstraint(5, 5),
        ])

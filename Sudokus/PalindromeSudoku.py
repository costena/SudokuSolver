from typing import Iterable, Optional, Tuple, List

from Constraints.ContinuousConstraint import ContinuousConstraint
from Constraints.DiscontinuousConstraint import DiscontinuousConstraint
from Constraints.PalindromeConstraint import PalindromeConstraint
from Constraints.Shapes.Rectangle import Rectangle
from Constraints.Shapes.Shape import Shape
from Constraints.Shapes.SinglePosition import SinglePosition
from Constraints.Shapes.UnionShape import UnionShape
from Sudokus.StandardSudoku import StandardSudoku
from Types import PointType, DirectionType


class PalindromeSudoku(StandardSudoku):
    def __init__(self, known_numbers: Iterable[Iterable[Optional[int]]], lines: Iterable[Iterable[PointType]]):
        super(PalindromeSudoku, self).__init__(known_numbers)
        self.initPalindromeConstraints(lines)

    def initPalindromeConstraints(self, lines: Iterable[Iterable[PointType]]):
        for line in lines:
            single_positions: List[Shape] = []
            for x, y in line:
                single_position = SinglePosition(x, y)
                single_positions.append(single_position)
            shape = UnionShape(single_positions)
            constraint = PalindromeConstraint(shape)
            self.constraints.append(constraint)

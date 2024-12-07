from typing import Iterable, Optional, Tuple, List

from Constraints.ContinuousConstraint import ContinuousConstraint
from Constraints.DiscontinuousConstraint import DiscontinuousConstraint
from Constraints.Shapes.Rectangle import Rectangle
from Sudokus.StandardSudoku import StandardSudoku
from Types import PointType, DirectionType


class ContinuousSudoku(StandardSudoku):
    def __init__(self, known_numbers: Iterable[Iterable[Optional[int]]], bezels: Iterable[Tuple[PointType, DirectionType]]):
        super(ContinuousSudoku, self).__init__(known_numbers)
        self.initContinuousConstraints(bezels)

    def initContinuousConstraints(self, bezels: Iterable[Tuple[PointType, DirectionType]]):
        shapes = []
        for position, direction in bezels:
            shape = Rectangle(position[0], position[1], direction[0] + 1, direction[1] + 1)
            constraint = ContinuousConstraint(shape)
            self.constraints.append(constraint)
            shapes.append(shape)
        constraint = DiscontinuousConstraint(Rectangle(0, 0, 9, 9), shapes)
        self.constraints.append(constraint)

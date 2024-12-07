from typing import Iterable, Optional, List

from Constraints.ColumnConstraint import ColumnConstraint
from Constraints.Constraint import Constraint
from Constraints.MutexConstraint import MutexConstraint
from Constraints.NumberConstraint import NumberConstraint
from Constraints.RowConstraint import RowConstraint
from Constraints.Shapes.SinglePosition import SinglePosition
from Constraints.Shapes.UnionShape import UnionShape
from Sudokus.Sudoku import Sudoku
from Types import PointType


class ZigzagSudoku(Sudoku):
    def __init__(self, known_numbers: Iterable[Iterable[Optional[int]]], blocks: Iterable[Iterable[PointType]]):
        super(ZigzagSudoku, self).__init__()
        self.initZigzagConstraints(known_numbers, blocks)

    def initZigzagConstraints(self, known_numbers: Iterable[Iterable[Optional[int]]], blocks: Iterable[Iterable[PointType]]):
        for y, row in enumerate(known_numbers):
            for x, number in enumerate(row):
                if number is not None:
                    constraint = NumberConstraint(x, y, number)
                    self.constraints.append(constraint)
        self.constraints.extend(self.createRowConstraints())
        self.constraints.extend(self.createColumnConstraints())
        self.constraints.extend(self.createBlockConstraints(blocks))

    def createRowConstraints(self):
        return [RowConstraint(y) for y in range(9)]

    def createColumnConstraints(self):
        return [ColumnConstraint(x) for x in range(9)]

    def createBlockConstraints(self, blocks: Iterable[Iterable[PointType]]) -> List[Constraint]:
        constraints = []
        for block in blocks:
            positions = []
            for x, y in block:
                position = SinglePosition(x, y)
                positions.append(position)
            shape = UnionShape(positions)
            constraint = MutexConstraint(shape)
            constraints.append(constraint)
        return constraints

from typing import Iterable, Optional, List, Dict

from Constraints.ColumnConstraint import ColumnConstraint
from Constraints.Constraint import Constraint
from Constraints.FullMutexConstraint import FullMutexConstraint
from Constraints.MutexConstraint import MutexConstraint
from Constraints.NumberConstraint import NumberConstraint
from Constraints.RowConstraint import RowConstraint
from Constraints.Shapes.Shape import Shape
from Constraints.Shapes.SinglePosition import SinglePosition
from Constraints.Shapes.UnionShape import UnionShape
from Sudokus.Sudoku import Sudoku
from Types import PointType


class BlackoutSudoku(Sudoku):
    def __init__(self, known_numbers: Iterable[Iterable[Optional[int]]]):
        super(BlackoutSudoku, self).__init__()
        self.blackout_positions: List[PointType] = []
        self.initBlackoutConstraints(known_numbers)

    def initBlackoutConstraints(self, known_numbers: Iterable[Iterable[Optional[int]]]):
        for y, row in enumerate(known_numbers):
            for x, number in enumerate(row):
                match number:
                    case None:
                        continue
                    case 0:
                        self.blackout_positions.append((x, y))
                    case _:
                        constraint = NumberConstraint(x, y, number)
                        self.constraints.append(constraint)
        self.constraints.extend(self.createRowConstraints(known_numbers))
        self.constraints.extend(self.createColumnConstraints(known_numbers))
        self.constraints.extend(self.createBlockConstraints(known_numbers))

    def createRowConstraints(self, known_numbers: Iterable[Iterable[Optional[int]]]) -> List[Constraint]:
        constraints = []
        for y, row in enumerate(known_numbers):
            shapes = []
            for x, number in enumerate(row):
                if number != 0:
                    shape = SinglePosition(x, y)
                    shapes.append(shape)
            shape = UnionShape(shapes)
            constraint = MutexConstraint(shape)
            constraints.append(constraint)
        return constraints

    def createColumnConstraints(self, known_numbers: Iterable[Iterable[Optional[int]]]) -> List[Constraint]:
        constraints = []
        shapes: Dict[int, List[Shape]] = {}
        for y, row in enumerate(known_numbers):
            for x, number in enumerate(row):
                if number != 0:
                    shape = SinglePosition(x, y)
                    shapes.setdefault(x, []).append(shape)
        for shapes_of_row in shapes.values():
            shape = UnionShape(shapes_of_row)
            constraint = MutexConstraint(shape)
            constraints.append(constraint)
        return constraints

    def createBlockConstraints(self, known_numbers: Iterable[Iterable[Optional[int]]]) -> List[Constraint]:
        constraints = []
        shapes: Dict[PointType, List[Shape]] = {}
        for y, row in enumerate(known_numbers):
            for x, number in enumerate(row):
                if number != 0:
                    shape = SinglePosition(x, y)
                    shapes.setdefault((x // 3, y // 3), []).append(shape)
        for shapes_of_block in shapes.values():
            shape = UnionShape(shapes_of_block)
            constraint = MutexConstraint(shape)
            constraints.append(constraint)
        return constraints
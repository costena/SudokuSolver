from typing import Iterable, Optional, Tuple, List

from Constraints.KillerCageConstraint import KillerCageConstraint
from Constraints.Shapes.SinglePosition import SinglePosition
from Constraints.Shapes.UnionShape import UnionShape
from Sudokus.StandardSudoku import StandardSudoku
from Types import PointType


class KillerSudoku(StandardSudoku):
	def __init__(self, known_numbers: Iterable[Iterable[Optional[int]]], killer_cages: Iterable[Tuple[int, Iterable[PointType]]]):
		super(KillerSudoku, self).__init__(known_numbers)
		self.initKillerCageConstraints(killer_cages)

	def initKillerCageConstraints(self, killer_cages: Iterable[Tuple[int, Iterable[PointType]]]):
		for summation, positions in killer_cages:
			single_positions: List[SinglePosition] = []
			for x, y in positions:
				single_position = SinglePosition(x, y)
				single_positions.append(single_position)
			shape = UnionShape(single_positions)
			constraint = KillerCageConstraint(shape, summation)
			self.constraints.append(constraint)

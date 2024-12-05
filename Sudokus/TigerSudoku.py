from typing import Iterable, Optional

from Constraints.MinimumDifferConstraint import MinimumDifferConstraint
from Constraints.SummationConstraint import SummationConstraint
from Sudokus.StandardSudoku import StandardSudoku


class TigerSudoku(StandardSudoku):
	def initConstraints(self, conundrum: Iterable[Iterable[Optional[int]]]):
		super(TigerSudoku, self).initConstraints(conundrum)
		self.constraints.extend([
			MinimumDifferConstraint(0, 8, 1, 7, 5),
			MinimumDifferConstraint(1, 2, 2, 2, 5),
			MinimumDifferConstraint(1, 2, 1, 3, 5),
			MinimumDifferConstraint(1, 3, 1, 4, 5),
			MinimumDifferConstraint(1, 4, 1, 5, 5),
			MinimumDifferConstraint(1, 5, 1, 6, 5),
			MinimumDifferConstraint(1, 6, 1, 7, 5),
			MinimumDifferConstraint(2, 2, 3, 2, 5),
			MinimumDifferConstraint(2, 4, 3, 4, 5),
			MinimumDifferConstraint(2, 8, 3, 7, 5),
			MinimumDifferConstraint(3, 2, 4, 2, 5),
			MinimumDifferConstraint(3, 4, 4, 4, 5),
			MinimumDifferConstraint(3, 6, 4, 6, 5),
			MinimumDifferConstraint(3, 6, 3, 7, 5),
			MinimumDifferConstraint(4, 0, 4, 1, 5),
			MinimumDifferConstraint(4, 1, 5, 1, 5),
			MinimumDifferConstraint(4, 1, 4, 2, 5),
			MinimumDifferConstraint(4, 2, 5, 2, 5),
			MinimumDifferConstraint(4, 3, 4, 4, 5),
			MinimumDifferConstraint(4, 4, 5, 4, 5),
			MinimumDifferConstraint(4, 4, 4, 5, 5),
			MinimumDifferConstraint(4, 5, 5, 5, 5),
			MinimumDifferConstraint(4, 6, 5, 6, 5),
			MinimumDifferConstraint(5, 2, 6, 2, 5),
			MinimumDifferConstraint(5, 4, 6, 4, 5),
			MinimumDifferConstraint(5, 5, 6, 5, 5),
			MinimumDifferConstraint(5, 6, 5, 7, 5),
			MinimumDifferConstraint(5, 7, 5, 8, 5),
			MinimumDifferConstraint(5, 8, 6, 8, 5),
			MinimumDifferConstraint(6, 2, 7, 2, 5),
			MinimumDifferConstraint(6, 5, 7, 5, 5),
			MinimumDifferConstraint(6, 8, 7, 7, 5),
			MinimumDifferConstraint(7, 2, 7, 3, 5),
			MinimumDifferConstraint(7, 4, 7, 5, 5),
		])
		self.constraints.extend([
			SummationConstraint(2, 1, 1, 1, 1),
			SummationConstraint(2, 3, 1, 1, 2),
			SummationConstraint(0, 5, 3, 1, 20),
			SummationConstraint(3, 5, 5, 1, 22),
		])

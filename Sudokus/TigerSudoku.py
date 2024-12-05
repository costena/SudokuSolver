from typing import Iterable, Optional

from Constraints.MinimumDifferConstraint import MinimumDifferConstraint
from Sudokus.StandardSudoku import StandardSudoku


class TigerSudoku(StandardSudoku):
	def initConstraints(self, conundrum: Iterable[Iterable[Optional[int]]]):
		super(TigerSudoku, self).__init__(conundrum)
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
		])

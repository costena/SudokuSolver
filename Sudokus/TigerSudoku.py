from typing import Iterable, Optional

from Constraints.GermanWhispersLineConstraint import GermanWhispersLineConstraint
from Constraints.KillerCageConstraint import KillerCageConstraint
from Sudokus.StandardSudoku import StandardSudoku


class TigerSudoku(StandardSudoku):
	def initConstraints(self, conundrum: Iterable[Iterable[Optional[int]]]):
		super(TigerSudoku, self).initConstraints(conundrum)
		self.constraints.extend([
			GermanWhispersLineConstraint(0, 8, 1, 7, 5),
			GermanWhispersLineConstraint(1, 2, 2, 2, 5),
			GermanWhispersLineConstraint(1, 2, 1, 3, 5),
			GermanWhispersLineConstraint(1, 3, 1, 4, 5),
			GermanWhispersLineConstraint(1, 4, 1, 5, 5),
			GermanWhispersLineConstraint(1, 5, 1, 6, 5),
			GermanWhispersLineConstraint(1, 6, 1, 7, 5),
			GermanWhispersLineConstraint(2, 2, 3, 2, 5),
			GermanWhispersLineConstraint(2, 4, 3, 4, 5),
			GermanWhispersLineConstraint(2, 8, 3, 7, 5),
			GermanWhispersLineConstraint(3, 2, 4, 2, 5),
			GermanWhispersLineConstraint(3, 4, 4, 4, 5),
			GermanWhispersLineConstraint(3, 6, 4, 6, 5),
			GermanWhispersLineConstraint(3, 6, 3, 7, 5),
			GermanWhispersLineConstraint(4, 0, 4, 1, 5),
			GermanWhispersLineConstraint(4, 1, 5, 1, 5),
			GermanWhispersLineConstraint(4, 1, 4, 2, 5),
			GermanWhispersLineConstraint(4, 2, 5, 2, 5),
			GermanWhispersLineConstraint(4, 3, 4, 4, 5),
			GermanWhispersLineConstraint(4, 4, 5, 4, 5),
			GermanWhispersLineConstraint(4, 4, 4, 5, 5),
			GermanWhispersLineConstraint(4, 5, 5, 5, 5),
			GermanWhispersLineConstraint(4, 6, 5, 6, 5),
			GermanWhispersLineConstraint(5, 2, 6, 2, 5),
			GermanWhispersLineConstraint(5, 4, 6, 4, 5),
			GermanWhispersLineConstraint(5, 5, 6, 5, 5),
			GermanWhispersLineConstraint(5, 6, 5, 7, 5),
			GermanWhispersLineConstraint(5, 7, 5, 8, 5),
			GermanWhispersLineConstraint(5, 8, 6, 8, 5),
			GermanWhispersLineConstraint(6, 2, 7, 2, 5),
			GermanWhispersLineConstraint(6, 5, 7, 5, 5),
			GermanWhispersLineConstraint(6, 8, 7, 7, 5),
			GermanWhispersLineConstraint(7, 2, 7, 3, 5),
			GermanWhispersLineConstraint(7, 4, 7, 5, 5),
		])
		self.constraints.extend([
			KillerCageConstraint(2, 1, 1, 1, 1),
			KillerCageConstraint(2, 3, 1, 1, 2),
			KillerCageConstraint(0, 5, 3, 1, 20),
			KillerCageConstraint(3, 5, 5, 1, 22),
		])

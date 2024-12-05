from typing import Iterable, Optional

from Constraints.GermanWhispersLineConstraint import GermanWhispersLineConstraint
from Constraints.KillerCageConstraint import KillerCageConstraint
from Constraints.Shapes.SinglePosition import SinglePosition
from Constraints.Shapes.UnionShape import UnionShape
from Sudokus.StandardSudoku import StandardSudoku


class KillerSudoku(StandardSudoku):
	def initConstraints(self, conundrum: Iterable[Iterable[Optional[int]]]):
		super(KillerSudoku, self).initConstraints(conundrum)
		# self.constraints.extend([
		# 	KillerCageConstraint(0, 0, 3, 1, 21),
		# 	KillerCageConstraint(3, 0, 1, 1, 9),
		# 	KillerCageConstraint(UnionShape([
		# 		SinglePosition(4, 0),
		# 		SinglePosition(3, 1),
		# 		SinglePosition(4, 1),
		# 	]), 7),
		# 	KillerCageConstraint(5, 0, 1, 2, 12),
		# 	KillerCageConstraint(UnionShape([
		# 		SinglePosition(6, 0),
		# 		SinglePosition(6, 1),
		# 		SinglePosition(7, 1),
		# 		SinglePosition(8, 1),
		# 		SinglePosition(7, 2),
		# 	]), 31),
		# 	KillerCageConstraint(7, 0, 2, 1, 6),
		# 	KillerCageConstraint(0, 1, 1, 2, 6),
		# 	KillerCageConstraint(1, 1, 1, 2, 11),
		# 	KillerCageConstraint(UnionShape([
		# 		SinglePosition(2, 1),
		# 		SinglePosition(2, 2),
		# 		SinglePosition(3, 2),
		# 	]), 13),
		# 	KillerCageConstraint(4, 2, 1, 2, 14),
		# 	KillerCageConstraint(5, 2, 2, 1, 4),
		# 	KillerCageConstraint(8, 2, 1, 2, 16),
		# 	KillerCageConstraint(0, 3, 1, 1, 3),
		# 	KillerCageConstraint(1, 3, 2, 1, 13),
		# 	KillerCageConstraint(3, 3, 1, 2, 12),
		# 	KillerCageConstraint(5, 3, 2, 1, 6),
		# 	KillerCageConstraint(UnionShape([
		# 		SinglePosition(7, 3),
		# 		SinglePosition(7, 4),
		# 		SinglePosition(8, 4),
		# 		SinglePosition(8, 5),
		# 	]), 13),
		# 	KillerCageConstraint(UnionShape([
		# 		SinglePosition(0, 4),
		# 		SinglePosition(1, 4),
		# 		SinglePosition(2, 4),
		# 		SinglePosition(0, 5),
		# 		SinglePosition(1, 5),
		# 		SinglePosition(1, 6),
		# 	]), 23),
		# 	KillerCageConstraint(4, 4, 1, 1, 9),
		# 	KillerCageConstraint(UnionShape([
		# 		SinglePosition(5, 4),
		# 		SinglePosition(6, 4),
		# 		SinglePosition(5, 5),
		# 	]), 17),
		# 	KillerCageConstraint(2, 5, 1, 2, 14),
		# 	KillerCageConstraint(3, 5, 2, 1, 4),
		# 	KillerCageConstraint(UnionShape([
		# 		SinglePosition(6, 5),
		# 		SinglePosition(5, 6),
		# 		SinglePosition(6, 6),
		# 	]), 16),
		# 	KillerCageConstraint(7, 5, 1, 2, 10),
		# 	KillerCageConstraint(0, 6, 1, 1, 4),
		# 	KillerCageConstraint(UnionShape([
		# 		SinglePosition(3, 6),
		# 		SinglePosition(4, 6),
		# 		SinglePosition(4, 7),
		# 		SinglePosition(5, 7),
		# 	]), 28),
		# 	KillerCageConstraint(8, 6, 1, 1, 6),
		# 	KillerCageConstraint(0, 7, 1, 2, 11),
		# 	KillerCageConstraint(1, 7, 1, 2, 15),
		# 	KillerCageConstraint(2, 7, 2, 2, 12),
		# 	KillerCageConstraint(UnionShape([
		# 		SinglePosition(6, 7),
		# 		SinglePosition(7, 7),
		# 		SinglePosition(8, 7),
		# 		SinglePosition(7, 8),
		# 		SinglePosition(8, 8),
		# 	]), 24),
		# 	KillerCageConstraint(4, 8, 2, 1, 11),
		# 	KillerCageConstraint(6, 8, 1, 1, 4),
		# ])
		self.constraints.extend([
			KillerCageConstraint(0, 0, 2, 1, 8),
			KillerCageConstraint(2, 0, 3, 1, 9),
			KillerCageConstraint(5, 0, 3, 1, 19),
			KillerCageConstraint(8, 0, 1, 3, 17),
			KillerCageConstraint(UnionShape([
				SinglePosition(0, 1),
				SinglePosition(0, 2),
				SinglePosition(1, 2),
			]), 16),
			KillerCageConstraint(1, 1, 2, 1, 13),
			KillerCageConstraint(3, 1, 2, 1, 9),
			KillerCageConstraint(5, 1, 1, 2, 7),
			KillerCageConstraint(6, 1, 2, 1, 12),
			KillerCageConstraint(UnionShape([
				SinglePosition(2, 2),
				SinglePosition(3, 2),
				SinglePosition(3, 3),
			]), 16),
			KillerCageConstraint(4, 2, 1, 2, 14),
			KillerCageConstraint(6, 2, 2, 1, 4),
			KillerCageConstraint(UnionShape([
				SinglePosition(0, 3),
				SinglePosition(1, 3),
				SinglePosition(0, 4),
			]), 16),
			KillerCageConstraint(UnionShape([
				SinglePosition(2, 3),
				SinglePosition(2, 4),
				SinglePosition(3, 4),
			]), 14),
			KillerCageConstraint(5, 3, 2, 1, 9),
			KillerCageConstraint(7, 3, 2, 1, 10),
			KillerCageConstraint(UnionShape([
				SinglePosition(1, 4),
				SinglePosition(0, 5),
				SinglePosition(1, 5),
				SinglePosition(2, 5),
			]), 22),
			KillerCageConstraint(4, 4, 3, 1, 18),
			KillerCageConstraint(7, 4, 1, 2, 8),
			KillerCageConstraint(8, 4, 1, 3, 17),
			KillerCageConstraint(UnionShape([
				SinglePosition(3, 5),
				SinglePosition(4, 5),
				SinglePosition(3, 6),
				SinglePosition(3, 7),
			]), 21),
			KillerCageConstraint(5, 5, 1, 1, 2),
			KillerCageConstraint(UnionShape([
				SinglePosition(6, 5),
				SinglePosition(6, 6),
				SinglePosition(7, 6),
			]), 6),
			KillerCageConstraint(0, 6, 1, 3, 13),
			KillerCageConstraint(UnionShape([
				SinglePosition(1, 6),
				SinglePosition(2, 6),
				SinglePosition(1, 7),
				SinglePosition(2, 7),
				SinglePosition(1, 8),
			]), 29),
			KillerCageConstraint(4, 6, 1, 2, 13),
			KillerCageConstraint(5, 6, 1, 1, 5),
			KillerCageConstraint(5, 7, 2, 1, 14),
			KillerCageConstraint(7, 7, 2, 1, 11),
			KillerCageConstraint(2, 8, 2, 1, 5),
			KillerCageConstraint(4, 8, 3, 1, 18),
			KillerCageConstraint(7, 8, 2, 1, 10),
		])

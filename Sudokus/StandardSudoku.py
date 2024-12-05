from typing import Iterable, Optional

from Constraints.BlockConstraint import BlockConstraint
from Constraints.ColumnConstraint import ColumnConstraint
from Constraints.NumberConstraint import NumberConstraint
from Constraints.RowConstraint import RowConstraint
from Sudokus.Sudoku import Sudoku


class StandardSudoku(Sudoku):
	def __init__(self, conundrum: Iterable[Iterable[Optional[int]]]):
		super(StandardSudoku, self).__init__()
		self.initConstraints(conundrum)
	
	def initConstraints(self, conundrum: Iterable[Iterable[Optional[int]]]):
		self.constraints.extend(self.createRowConstraints())
		self.constraints.extend(self.createColumnConstraints())
		self.constraints.extend(self.createBlockConstraints())
		for y, row in enumerate(conundrum):
			for x, number in enumerate(row):
				if number is not None:
					constraint = NumberConstraint(x, y, number)
					self.constraints.append(constraint)

	def createRowConstraints(self):
		return [RowConstraint(y) for y in range(9)]

	def createColumnConstraints(self):
		return [ColumnConstraint(x) for x in range(9)]

	def createBlockConstraints(self):
		return [BlockConstraint(x, y) for x in range(0, 9, 3) for y in range(0, 9, 3)]

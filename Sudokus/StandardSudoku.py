from typing import Iterable, Optional

from Constraints.BlockConstraint import BlockConstraintFull
from Constraints.ColumnConstraint import ColumnConstraintFull
from Constraints.NumberConstraint import NumberConstraint
from Constraints.RowConstraint import RowConstraintFull
from Sudokus.Sudoku import Sudoku


class StandardSudoku(Sudoku):
	def __init__(self, known_numbers: Iterable[Iterable[Optional[int]]]):
		super(StandardSudoku, self).__init__()
		self.initStandardConstraints(known_numbers)
	
	def initStandardConstraints(self, known_numbers: Iterable[Iterable[Optional[int]]]):
		for y, row in enumerate(known_numbers):
			for x, number in enumerate(row):
				if number is not None:
					constraint = NumberConstraint(x, y, number)
					self.constraints.append(constraint)
		self.constraints.extend(self.createRowConstraints())
		self.constraints.extend(self.createColumnConstraints())
		self.constraints.extend(self.createBlockConstraints())

	def createRowConstraints(self):
		return [RowConstraintFull(y) for y in range(9)]

	def createColumnConstraints(self):
		return [ColumnConstraintFull(x) for x in range(9)]

	def createBlockConstraints(self):
		return [BlockConstraintFull(x, y) for x in range(0, 9, 3) for y in range(0, 9, 3)]

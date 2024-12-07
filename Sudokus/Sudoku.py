from typing import List

from Constraints.Constraint import Constraint


class Sudoku(object):
	def __init__(self):
		self.constraints: List[Constraint] = []

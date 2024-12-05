import itertools

from Constraints.Constraint import Constraint
from Constraints.Shapes.Rectangle import Rectangle
from Constraints.Shapes.Shape import Shape
from Constraints.Shapes.SinglePosition import SinglePosition


class SummationConstraint(Constraint):
	def __init__(self, x: int, y: int, w: int, h: int, summation: int):
		super(SummationConstraint, self).__init__(Rectangle(x, y, w, h))
		self.summation: int = summation
	
	def __repr__(self):
		return f"<SummationConstraint(shape={self.shape}, summation={self.summation})>"
	
	def active(self, sudoku: 'Sudoku') -> bool:
		assert isinstance(self.shape, Rectangle)
		if self.shape.w == self.shape.h == 1:
			sudoku.context_constraint = self
			return sudoku.fill(self.shape.x, self.shape.y, self.summation)
		cell_count: int = self.shape.w * self.shape.h
		min_number: int = max(1, self.summation - (cell_count - 1) * 9)
		max_number: int = min(9, self.summation - (cell_count - 1))
		for number in itertools.chain(range(1, min_number), range(max_number + 1, 10)):
			# print(f"eliminate: {self}, {self.shape.x}, {self.shape.y}, {number}")
			sudoku.context_constraint = self
			if not sudoku.eliminate(self.shape.x, self.shape.y, number):
				return False
		return True
	
	def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		return self.check(x, y, number, sudoku)

	def on_number_eliminated(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		return self.check(x, y, number, sudoku)

	def check(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		if not self.shape.contains_position(x, y):
			return True
		min_summation = 0
		max_summation = 0
		for position_x, position_y in self.shape.iter_positions():
			possible_numbers = sudoku.ref_possible_numbers(position_x, position_y)
			min_summation += min(possible_numbers)
			max_summation += max(possible_numbers)
		if min_summation > self.summation or max_summation < self.summation:
			return False
		for position_x, position_y in self.shape.iter_positions():
			possible_numbers = sudoku.ref_possible_numbers(position_x, position_y)
			remained_min_summation = min_summation - min(possible_numbers)
			remained_max_summation = max_summation - max(possible_numbers)
			max_number = min(9, self.summation - remained_min_summation)
			min_number = max(1, self.summation - remained_max_summation)
			for number in itertools.chain(range(1, min_number), range(max_number + 1, 10)):
				# print(f"eliminate: {self}, {position_x}, {position_y}, {number}")
				sudoku.context_constraint = self
				if not sudoku.eliminate(position_x, position_y, number):
					return False
		return True

from typing import Union
import itertools

from Constraints.Constraint import Constraint
from Constraints.Shapes.Rectangle import Rectangle
from Constraints.Shapes.Shape import Shape


class KillerCageConstraint(Constraint):
	def __init__(self, x_or_shape: Union[int, Shape], y_or_summation: int, w: int=0, h: int=0, summation: int=0):
		if isinstance(x_or_shape, int):
			x = x_or_shape
			y = y_or_summation
			super(KillerCageConstraint, self).__init__(Rectangle(x, y, w, h))
		elif isinstance(x_or_shape, Shape):
			shape = x_or_shape
			summation = y_or_summation
			super(KillerCageConstraint, self).__init__(shape)
		self.summation: int = summation
	
	def __repr__(self):
		return f"<KillerCageConstraint(shape={self.shape}, summation={self.summation})>"
	
	def active(self, sudoku: 'Sudoku') -> bool:
		positions = list(self.shape.iter_positions())
		cell_count: int = len(positions)
		if cell_count == 1:
			position = positions[0]
			return sudoku.fill(position[0], position[1], self.summation)
		for x, y in self.shape.iter_positions():
			return self.check(x, y, sudoku)
		return True
	
	def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		return self.check(x, y, sudoku)

	def on_number_eliminated(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		return self.check(x, y, sudoku)

	def check(self, x: int, y: int, sudoku: 'Sudoku') -> bool:
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
				if not sudoku.eliminate(position_x, position_y, number):
					return False
		return True

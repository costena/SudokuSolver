import copy

from Constraints.Constraint import Constraint
from Constraints.Shapes.SinglePosition import SinglePosition
from Constraints.Shapes.UnionShape import UnionShape


class GermanWhispersLineConstraint(Constraint):
	def __init__(self, x1: int, y1: int, x2: int, y2: int, minimum_differ: int):
		super(GermanWhispersLineConstraint, self).__init__(UnionShape([SinglePosition(x1, y1), SinglePosition(x2, y2)]))
		self.minimum_differ: int = minimum_differ

	def __repr__(self):
		return f"<MinimumDifferConstraint(shape={self.shape}, minimum_differ={self.minimum_differ}"

	def active(self, sudoku: 'Sudoku') -> bool:
		if self.minimum_differ == 5:
			for position_x, position_y in self.shape.iter_positions():
				if not sudoku.eliminate(position_x, position_y, 5):
					return False
		return True
	
	def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		if not self.shape.contains_position(x, y):
			return True
		for peer_x, peer_y in self.iter_peers(x, y):
			possible_numbers = sudoku.ref_possible_numbers(peer_x, peer_y)
			for n in copy.copy(possible_numbers):
				if abs(n - number) < self.minimum_differ:
					if not sudoku.eliminate(peer_x, peer_y, n):
						return False
		return True

	def on_number_eliminated(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		if not self.shape.contains_position(x, y):
			return True
		possible_numbers = sudoku.ref_possible_numbers(x, y)
		for peer_x, peer_y in self.iter_peers(x, y):
			peer_possible_numbers = sudoku.ref_possible_numbers(peer_x, peer_y)
			for peer_number in copy.copy(peer_possible_numbers):
				if all(abs(peer_number - possible_number) < self.minimum_differ for possible_number in possible_numbers):
					if not sudoku.eliminate(peer_x, peer_y, peer_number):
						return False
		return True

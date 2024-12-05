from typing import Iterable, Tuple

from Constraints.Shapes.Shape import Shape


class Constraint(object):
	def __init__(self, shape: Shape):
		self.shape: Shape = shape
	
	def __repr__(self):
		return f"<Constraint()>"
	
	def active(self, sudoku: 'Sudoku') -> bool:
		return True
	
	def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		return True
	
	def iter_peers(self, x: int, y: int) -> Iterable[Tuple[int, int]]:
		if not self.shape.contains_position(x, y):
			return ()
		for peer_x, peer_y in self.shape.iter_positions():
			if peer_x == x and peer_y == y:
				continue
			yield peer_x, peer_y

from typing import Iterable, Tuple


class Constraint(object):
	def __repr__(self):
		return f"<Constraint()>"
	
	def active(self, sudoku: 'Sudoku') -> bool:
		return True
	
	def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		return True
	
	def iter_peers(self, x: int, y: int) -> Iterable[Tuple[int, int]]:
		return ()

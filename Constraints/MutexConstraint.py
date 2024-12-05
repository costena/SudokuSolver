from Constraints.Constraint import Constraint


class MutexConstraint(Constraint):
	def __repr__(self):
		return f"<MutexConstraint(shape={self.shape})>"
	
	def active(self, sudoku: 'Sudoku') -> bool:
		return True
	
	def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		for other_x, other_y in self.iter_peers(x, y):
			if not sudoku.eliminate(other_x, other_y, number):
				return False
		return True

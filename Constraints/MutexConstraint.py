from Constraints.Constraint import Constraint


class MutexConstraint(Constraint):
	def __repr__(self):
		return f"<MutexConstraint(shape={self.shape})>"
	
	def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		if not self.shape.contains_position(x, y):
			return True
		for peer_x, peer_y in self.iter_peers(x, y):
			# print(f"eliminate: {self}, {peer_x}, {peer_y}, {number}")
			sudoku.context_constraint = self
			if not sudoku.eliminate(peer_x, peer_y, number):
				return False
		return True

	def on_number_eliminated(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		count: int = 0
		target_x: int = -1
		target_y: int = -1
		for peer_x, peer_y in self.iter_peers(x, y):
			peer_possible_numbers = sudoku.ref_possible_numbers(peer_x, peer_y)
			if number in peer_possible_numbers:
				count += 1
				target_x = peer_x
				target_y = peer_y
			if count > 1:
				break
		else:
			if count == 1:
				sudoku.context_constraint = self
				if not sudoku.fill(target_x, target_y, number):
					return False
		return True

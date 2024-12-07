from Constraints.MutexConstraint import MutexConstraint


class FullMutexConstraint(MutexConstraint):
	def __repr__(self):
		return f"<FullMutexConstraint(shape={self.shape})>"

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
				if not sudoku.fill(target_x, target_y, number):
					return False
		return True

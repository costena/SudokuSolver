from typing import Iterable, Tuple

from Constraints.MutexConstraint import MutexConstraint


class ColumnConstraint(MutexConstraint):
	def __init__(self, x: int):
		super(ColumnConstraint, self).__init__()
		self.x: int = x
	
	def __repr__(self):
		return f"<ColumnConstraint(x={self.x})>"

	def iter_peers(self, x: int, y: int) -> Iterable[Tuple[int, int]]:
		if x != self.x:
			return ()
		for peer_y in range(9):
			if peer_y == y:
				continue
			yield x, peer_y

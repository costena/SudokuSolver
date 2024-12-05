from typing import Iterable, Tuple

from Constraints.Constraint import Constraint
from Constraints.MutexConstraint import MutexConstraint


class RowConstraint(MutexConstraint):
	def __init__(self, y: int):
		super(RowConstraint, self).__init__()
		self.y: int = y
	
	def __repr__(self):
		return f"<RowConstraint(y={self.y})>"

	def iter_peers(self, x: int, y: int) -> Iterable[Tuple[int, int]]:
		if y != self.y:
			return ()
		for peer_x in range(9):
			if peer_x == x:
				continue
			yield peer_x, y

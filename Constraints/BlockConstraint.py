from typing import Iterable, Tuple

from Constraints.MutexConstraint import MutexConstraint


class BlockConstraint(MutexConstraint):
	def __init__(self, x: int, y: int):
		super(BlockConstraint, self).__init__()
		self.x: int = x
		self.y: int = y

	def __repr__(self):
		return f"<BlockConstraint(x={self.x}, y={self.y})>"

	def iter_peers(self, x: int, y: int) -> Iterable[Tuple[int, int]]:
		if not (self.x <= x < self.x + 3 and self.y <= y < self.y + 3):
			return ()
		for peer_y in range(self.y, self.y + 3):
			for peer_x in range(self.x, self.x + 3):
				if peer_x == x and peer_y == y:
					continue
				yield peer_x, peer_y

from typing import Iterable, Tuple

from Constraints.MutexConstraint import MutexConstraint
from Constraints.Shapes.Rectangle import Rectangle


class AntiKnightConstraint(MutexConstraint):
    def __init__(self):
        super(AntiKnightConstraint, self).__init__(Rectangle(0, 0, 9, 9))

    def __repr__(self):
        return f"<AntiKnightConstraint()>"

    def iter_peers(self, x: int, y: int) -> Iterable[Tuple[int, int]]:
        for offset_x, offset_y in [
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
        ]:
            peer_x, peer_y = x + offset_x, y + offset_y
            if self.shape.contains_position(peer_x, peer_y):
                yield peer_x, peer_y

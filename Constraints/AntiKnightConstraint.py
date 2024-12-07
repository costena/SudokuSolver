from typing import Iterable, Tuple

from Constraints.Constraint import Constraint
from Constraints.Shapes.Rectangle import Rectangle


class AntiKnightConstraint(Constraint):
    def __init__(self):
        super(AntiKnightConstraint, self).__init__(Rectangle(0, 0, 9, 9))

    def __repr__(self):
        return f"<AntiKnightConstraint()>"

    def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
        for peer_x, peer_y in self.iter_peers(x, y):
            if not sudoku.eliminate(peer_x, peer_y, number):
                return False
        return True

    def iter_peers(self, x: int, y: int) -> Iterable[Tuple[int, int]]:
        assert isinstance(self.shape, Rectangle)
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

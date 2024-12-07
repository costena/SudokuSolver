from typing import Iterable, List, Tuple, Dict, Set

from Constraints.MutexConstraint import MutexConstraint
from Constraints.Shapes.Shape import Shape
from Types import PointType


class DiscontinuousConstraint(MutexConstraint):
    def __init__(self, shape: Shape, ignore_shapes: Iterable[Shape]):
        super(DiscontinuousConstraint, self).__init__(shape)
        self.ignore_shape_map: Dict[PointType, Set[Shape]] = {}
        for shape in ignore_shapes:
            for position in shape.iter_positions():
                self.ignore_shape_map.setdefault(position, set()).add(shape)

    def __repr__(self):
        return f"<DiscontinuousConstraint(shape={self.shape})>"

    def on_number_eliminated(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
        if not self.shape.contains_position(x, y):
            return True
        possible_numbers = sudoku.ref_possible_numbers(x, y)
        not_allowed_numbers = set(range(max(possible_numbers) - 1, min(possible_numbers) + 2))
        allowed_numbers = set(range(9))
        allowed_numbers.difference_update(not_allowed_numbers)
        lost_numbers = set(range(9))
        lost_numbers.difference_update(range(number - 1, number + 2))
        lost_numbers.difference_update(allowed_numbers)
        if len(lost_numbers) == 0:
            return True
        for peer_x, peer_y in self.iter_peers(x, y):
            if (peer_x, peer_y) in self.ignore_shape_map.get((x, y), set()):
                continue
            for lost_number in lost_numbers:
                if not sudoku.eliminate(peer_x, peer_y, lost_number):
                    return False
        return True

    def iter_peers(self, x: int, y: int) -> Iterable[Tuple[int, int]]:
        for offset_x, offset_y in [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]:
            peer_x, peer_y = x + offset_x, y + offset_y
            ignore_shapes = self.ignore_shape_map.get((x, y), set())
            if self.shape.contains_position(peer_x, peer_y):
                for ignore_shape in ignore_shapes:
                    if ignore_shape.contains_position(peer_x, peer_y):
                        break
                else:
                    yield peer_x, peer_y

from Constraints.Constraint import Constraint


class PalindromeConstraint(Constraint):
    def __repr__(self):
        return f"<PalindromeConstraint(shape={self.shape})>"

    def on_number_eliminated(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
        if not self.shape.contains_position(x, y):
            return True
        positions = list(self.shape.iter_positions())
        for (other_x, other_y), (mirror_x, mirror_y) in zip(positions, reversed(positions)):
            if mirror_x == x and mirror_y == y:
                continue
            if other_x == x and other_y == y:
                if not sudoku.eliminate(mirror_x, mirror_y, number):
                    return False
                return True
        return True

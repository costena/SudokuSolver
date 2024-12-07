from Constraints.Constraint import Constraint


class MutexConstraint(Constraint):
    def __repr__(self):
        return f"<MutexConstraint(shape={self.shape})>"

    def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
        if not self.shape.contains_position(x, y):
            return True
        for peer_x, peer_y in self.iter_peers(x, y):
            if not sudoku.eliminate(peer_x, peer_y, number):
                return False
        return True

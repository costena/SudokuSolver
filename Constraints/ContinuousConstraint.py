from Constraints.MutexConstraint import MutexConstraint


class ContinuousConstraint(MutexConstraint):
    def __repr__(self):
        return f"<ContinuousConstraint(shape={self.shape})>"

    def on_number_eliminated(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
        if not self.shape.contains_position(x, y):
            return True
        possible_numbers = sudoku.ref_possible_numbers(x, y)
        allowed_numbers = set(
            [number - 1 for number in possible_numbers] +
            [number + 1 for number in possible_numbers]
        )
        lost_numbers = {number - 1, number + 1}
        lost_numbers.difference_update(allowed_numbers)
        lost_numbers.intersection_update(range(9))
        if len(lost_numbers) == 0:
            return True
        for peer_x, peer_y in self.iter_peers(x, y):
            for lost_number in lost_numbers:
                if not sudoku.eliminate(peer_x, peer_y, lost_number):
                    return False
        return True

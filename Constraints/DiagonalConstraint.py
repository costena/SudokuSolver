from Constraints.FullMutexConstraint import FullMutexConstraint
from Constraints.Shapes.SinglePosition import SinglePosition
from Constraints.Shapes.UnionShape import UnionShape


class DiagonalConstraint(FullMutexConstraint):
    def __init__(self, is_bottom_left_to_top_right: bool):
        if is_bottom_left_to_top_right:
            shape = UnionShape([
                SinglePosition(x, 8 - x)
                for x in range(9)
            ])
        else:
            shape = UnionShape([
                SinglePosition(x, x)
                for x in range(9)
            ])
        super(DiagonalConstraint, self).__init__(shape)
        self.is_bottom_left_to_top_right: bool = is_bottom_left_to_top_right

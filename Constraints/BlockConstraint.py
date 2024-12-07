from Constraints.FullMutexConstraint import FullMutexConstraint
from Constraints.Shapes.Rectangle import Rectangle


class BlockConstraintFull(FullMutexConstraint):
	def __init__(self, x: int, y: int):
		super(BlockConstraintFull, self).__init__(Rectangle(x, y, 3, 3))

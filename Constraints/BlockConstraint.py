from Constraints.MutexConstraint import MutexConstraint
from Constraints.Shapes.Rectangle import Rectangle
from Constraints.Shapes.Shape import Shape


class BlockConstraint(MutexConstraint):
	def __init__(self, x: int, y: int):
		super(BlockConstraint, self).__init__(Rectangle(x, y, 3, 3))

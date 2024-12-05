from Constraints.MutexConstraint import MutexConstraint
from Constraints.Shapes.Rectangle import Rectangle
from Constraints.Shapes.Shape import Shape


class ColumnConstraint(MutexConstraint):
	def __init__(self, x: int):
		super(ColumnConstraint, self).__init__(Rectangle(x, 0, 1, 9))

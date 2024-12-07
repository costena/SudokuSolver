from Constraints.FullMutexConstraint import FullMutexConstraint
from Constraints.Shapes.Rectangle import Rectangle


class ColumnConstraintFull(FullMutexConstraint):
	def __init__(self, x: int):
		super(ColumnConstraintFull, self).__init__(Rectangle(x, 0, 1, 9))

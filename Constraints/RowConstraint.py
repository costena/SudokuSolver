from Constraints.FullMutexConstraint import FullMutexConstraint
from Constraints.Shapes.Rectangle import Rectangle


class RowConstraint(FullMutexConstraint):
	def __init__(self, y: int):
		super(RowConstraint, self).__init__(Rectangle(0, y, 9, 1))

from Constraints.Constraint import Constraint
from Constraints.Shapes.SinglePosition import SinglePosition
from Constraints.Shapes.UnionShape import UnionShape


class MinimumDifferConstraint(Constraint):
	def __init__(self, x1: int, y1: int, x2: int, y2: int, disparity: int):
		super(MinimumDifferConstraint, self).__init__(UnionShape([SinglePosition(x1, y1), SinglePosition(x2, y2)]))
		self.disparity = disparity

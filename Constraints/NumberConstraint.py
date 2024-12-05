from Constraints.Constraint import Constraint
from Constraints.Shapes.SinglePosition import SinglePosition


class NumberConstraint(Constraint):
	def __init__(self, x: int, y: int, number: int):
		super(NumberConstraint, self).__init__(SinglePosition(x, y))
		self.number: int = number
	
	def __repr__(self):
		return f"<NumberConstraint(shape={self.shape}, number={self.number})>"

	def active(self, sudoku: 'Sudoku'):
		assert isinstance(self.shape, SinglePosition)
		sudoku.context_constraint = self
		return sudoku.fill(self.shape.x, self.shape.y, self.number)

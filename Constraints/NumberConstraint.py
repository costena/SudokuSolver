from Constraints.Constraint import Constraint


class NumberConstraint(Constraint):
	def __init__(self, x: int, y: int, number: int):
		super(NumberConstraint, self).__init__()
		self.x: int = x
		self.y: int = y
		self.number: int = number
	
	def __repr__(self):
		return f"<NumberConstraint(x={self.x}, y={self.y}, number={self.number})>"
	
	def active(self, sudoku: 'Sudoku'):
		return sudoku.fill(self.x, self.y, self.number)

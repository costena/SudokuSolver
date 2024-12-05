from Constraints.Constraint import Constraint
from Constraints.Shapes.Rectangle import Rectangle
from Constraints.Shapes.Shape import Shape
from Constraints.Shapes.SinglePosition import SinglePosition


class SummationConstraint(Constraint):
	def __init__(self, x: int, y: int, w: int, h: int, summation: int):
		super(SummationConstraint, self).__init__(Rectangle(x, y, w, h))
		self.summation: int = summation
	
	def active(self, sudoku: 'Sudoku') -> bool:
		assert isinstance(self.shape, Rectangle)
		if self.shape.w == self.shape.h == 1:
			return sudoku.fill(self.shape.x, self.shape.y, self.summation)
		return True
	
	def on_number_filled(self, x: int, y: int, number: int, sudoku: 'Sudoku') -> bool:
		if not self.shape.contains_position(x, y):
			return True

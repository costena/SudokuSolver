from Constraints.Shapes.Shape import Shape


class SinglePosition(Shape):
	def __init__(self, x: int, y: int):
		super(SinglePosition, self).__init__()
		self.x: int = x
		self.y: int = y
	
	def __repr__(self):
		return f"<SingleCell(x={self.x}, y={self.y})>"

	def iter_positions(self):
		yield self.x, self.y
	
	def contains_position(self, x: int, y: int) -> bool:
		return x == self.x and y == self.y

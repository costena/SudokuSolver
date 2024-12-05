from Constraints.Shapes.Shape import Shape


class Rectangle(Shape):
	def __init__(self, x: int, y: int, w: int, h: int):
		super(Rectangle, self).__init__()
		self.x: int = x
		self.y: int = y
		self.w: int = w
		self.h: int = h
	
	def __repr__(self):
		return f"<Rectangle(x={self.x}, y={self.y}, w={self.w}, h={self.h})>"
	
	def iter_positions(self):
		for y in range(self.y, self.y + self.h):
			for x in range(self.x, self.x + self.w):
				yield x, y
	
	def contains_position(self, x: int, y: int) -> bool:
		return self.x <= x < self.x + self.w and self.y <= y < self.y + self.h

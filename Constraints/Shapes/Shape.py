class Shape(object):
	def __repr__(self):
		return f"<Shape()>"
	
	def iter_positions(self):
		raise NotImplementedError
	
	def contains_position(self, x: int, y: int) -> bool:
		raise NotImplementedError

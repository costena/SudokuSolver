from typing import Iterable, List, Set, Tuple

from Constraints.Shapes.Shape import Shape


class UnionShape(Shape):
	def __init__(self, shapes: Iterable[Shape]):
		super(UnionShape, self).__init__()
		self.shapes: List[Shape] = list(shapes)
	
	def __repr__(self):
		return f"<UnionShape(shapes=[{', '.join([f'{shape}' for shape in self.shapes])}])>"
	
	def iter_positions(self):
		detected: Set[Tuple[int, int]] = set()
		for shape in self.shapes:
			for x, y in shape.iter_positions():
				if (x, y) not in detected:
					yield x, y
				detected.add((x, y))

	def contains_position(self, x: int, y: int) -> bool:
		return any(shape.contains_position(x, y) for shape in self.shapes)

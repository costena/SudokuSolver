from typing import Iterable, List

from Constraints.Constraint import Constraint
from Constraints.Shapes.SinglePosition import SinglePosition


class PossibleNumbersConstraint(Constraint):
	def __init__(self, x: int, y: int, possible_numbers: Iterable[int]):
		super(PossibleNumbersConstraint, self).__init__(SinglePosition(x, y))
		self.possible_numbers: List[int] = list(possible_numbers)

	def __repr__(self):
		assert isinstance(self.shape, SinglePosition)
		return f"<PossibleNumbersConstraint(x={self.shape.x}, y={self.shape.y}, possible_numbers={self.possible_numbers})>"

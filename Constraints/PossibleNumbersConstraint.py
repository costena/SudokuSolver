from typing import Iterable, List

from Constraints.Constraint import Constraint


class PossibleNumbersConstraint(Constraint):
	def __init__(self, x: int, y: int, possible_numbers: Iterable[int]):
		super(PossibleNumbersConstraint, self).__init__()
		self.x: int = x
		self.y: int = y
		self.possible_numbers: List[int] = list(possible_numbers)

	def __repr__(self):
		return f"<PossibleNumbersConstraint(x={self.x}, y={self.y}, possible_numbers={self.possible_numbers})>"

import copy
from typing import List, Set, Tuple

from Constraints.Constraint import Constraint


class Sudoku(object):
	def __init__(self):
		self.constraints: List[Constraint] = []
		self.possible_numbers_table: List[List[Set[int]]] = [
			[
				set(range(1, 10))
				for _ in range(9)
			]
			for _ in range(9)
		]

	def solve(self) -> bool:
		for constraint in self.constraints:
			if not constraint.active(self):
				return False
		return self.resolve(0, 0)
	
	def resolve(self, start_x: int, start_y: int) -> bool:
		for y in range(start_y, 9):
			for x in range(start_x, 9):
				possible_numbers: Set[int] = self.ref_possible_number(x, y)
				if len(possible_numbers) == 1:
					continue
				saved_table: List[List[Set[int]]] = copy.deepcopy(self.possible_numbers_table)
				for number in copy.copy(possible_numbers):
					if not self.fill(x, y, number):
						continue
					if self.resolve(x, y):
						break
					self.possible_numbers_table = saved_table
				break
		return True

	def ref_possible_number(self, x: int, y: int) -> Set[int]:
		return self.possible_numbers_table[y][x]
	
	def get_number(self, x: int, y: int) -> int:
		possible_numbers = self.ref_possible_number(x, y)
		for number in possible_numbers:
			return number
	
	def eliminate(self, x: int, y: int, number: int) -> bool:
		possible_numbers = self.ref_possible_number(x, y)
		if number not in possible_numbers:
			return True
		possible_numbers.remove(number)
		if len(possible_numbers) == 1:
			for constraint in self.constraints:
				if not constraint.on_number_filled(x, y, self.get_number(x, y), self):
					return False
		
		for constraint in self.constraints:
			count: int = 0
			target_x: int = -1
			target_y: int = -1
			for peer_x, peer_y in constraint.iter_peers(x, y):
				peer_possible_numbers = self.ref_possible_number(peer_x, peer_y)
				if number in peer_possible_numbers:
					count += 1
					target_x = peer_x
					target_y = peer_y
				if count > 1:
					break
			else:
				if count == 1:
					if not self.fill(target_x, target_y, number):
						return False
		return True
	
	def fill(self, x: int, y: int, number: int) -> bool:
		possible_numbers = self.ref_possible_number(x, y)
		if number not in possible_numbers:
			return False
		if len(possible_numbers) == 1:
			return True
		for other_number in [other_number for other_number in possible_numbers if other_number != number]:
			if not self.eliminate(x, y, other_number):
				return False
		return True

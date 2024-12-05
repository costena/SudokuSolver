import copy
import pickle
from typing import List, Set, Tuple, Optional, Callable

import yaml

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
		self.step_callback: Optional[Callable] = None
		self.answer = [
			'863594721',
			'941627358',
			'527183946',
			'182365497',
			'734918265',
			'695472813',
			'416839572',
			'379251684',
			'258746139',
		]
		self.answer = [
			[int(a) for a in b]
			for b in self.answer
		]
		self.context_constraint = None
		self.context_position_number = None

	def solve(self) -> bool:
		for constraint in self.constraints:
			if not constraint.active(self):
				return False
		return self.resolve(0, 0)

	def resolve(self, start_x: int, start_y: int) -> bool:
		jesus = {}
		for y in range(9):
			for x in range(9):
				possible_numbers = self.ref_possible_numbers(x, y)
				if len(possible_numbers) == 1:
					continue
				jesus.setdefault(len(possible_numbers), []).append((x, y))
		if len(jesus) == 0:
			return True
		for _, positions in sorted(jesus.items()):
			for x, y in positions:
				possible_numbers = self.ref_possible_numbers(x, y)
				saved_table = pickle.dumps(self.possible_numbers_table)
				for number in copy.copy(possible_numbers):
					self.context_constraint = None
					if self.fill(x, y, number):
						if self.resolve(x, y):
							return True
					self.possible_numbers_table = pickle.loads(saved_table)
				return False
		return True

	def ref_possible_numbers(self, x: int, y: int) -> Set[int]:
		return self.possible_numbers_table[y][x]
	
	def get_number(self, x: int, y: int) -> int:
		possible_numbers = self.ref_possible_numbers(x, y)
		for number in possible_numbers:
			return number
	
	def eliminate(self, x: int, y: int, number: int) -> bool:
		if number == self.answer[y][x]:
			pass
		possible_numbers = self.ref_possible_numbers(x, y)
		if number not in possible_numbers:
			return True
		if len(possible_numbers) == 1:
			return False
		possible_numbers.remove(number)
		self.context_position_number = (x, y, number)
		if self.step_callback:
			self.step_callback()
		if len(possible_numbers) == 1:
			for constraint in self.constraints:
				if not constraint.on_number_filled(x, y, self.get_number(x, y), self):
					return False
		
		for constraint in self.constraints:
			if not constraint.on_number_eliminated(x, y, number, self):
				return False
		return True
	
	def fill(self, x: int, y: int, number: int) -> bool:
		possible_numbers = self.ref_possible_numbers(x, y)
		if number not in possible_numbers:
			return False
		if len(possible_numbers) == 1:
			return True
		for other_number in [other_number for other_number in possible_numbers if other_number != number]:
			# print(f"eliminate: {self}, {x}, {y}, {other_number}")
			if not self.eliminate(x, y, other_number):
				return False
		return True

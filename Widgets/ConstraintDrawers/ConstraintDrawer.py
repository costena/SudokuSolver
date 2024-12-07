from typing import Optional, Set, Dict, Tuple, List

from PyQt5.QtCore import QRect, QLine
from PyQt5.QtGui import QPainter

from Constraints.Constraint import Constraint


class ConstraintDrawer(object):
	def __init__(self, constraint: Constraint):
		self.constraint: Constraint = constraint

	def paint(self, painter: QPainter, rect: QRect):
		pass

	def special_paint(self, painter: QPainter, rect: QRect):
		pass

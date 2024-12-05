from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter

from Constraints.Constraint import Constraint


class ConstraintDrawer(object):
	def __init__(self, constraint: Constraint):
		self.constraint: Constraint = constraint
	
	def paint(self, painter: QPainter, rect: QRect):
		pass
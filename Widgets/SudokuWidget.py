from typing import Optional, Dict

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QResizeEvent, QPaintEvent
from PyQt5.QtWidgets import QWidget

from Constraints.Constraint import Constraint
from Sudokus.Sudoku import Sudoku
from Widgets.ConstraintDrawers import getConstraintDrawerType
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


class SudokuWidget(QWidget):
	def __init__(self, parent=None):
		super(SudokuWidget, self).__init__(parent)
		self.sudoku: Optional[Sudoku] = None
		self.constraint_drawers: Dict[Constraint, ConstraintDrawer] = {}
		self.canvas_rect: QRect = QRect()
	
	def setSudoku(self, sudoku: Optional[Sudoku]) -> None:
		self.sudoku = sudoku
		self.initConstraintDrawers()
	
	def initConstraintDrawers(self):
		for constraint in self.sudoku.constraints:
			constraint_type: type = type(constraint)
			constraint_drawer_type: type = getConstraintDrawerType(constraint_type)
			if constraint_drawer_type is not None:
				constraint_drawer: Optional[ConstraintDrawer] = constraint_drawer_type(constraint)
				self.constraint_drawers[constraint] = constraint_drawer

	def paintEvent(self, event: QPaintEvent):
		painter = QPainter(self)
		for constraint in self.sudoku.constraints:
			constraint_drawer: ConstraintDrawer = self.constraint_drawers.get(constraint)
			if constraint_drawer is None:
				continue
			constraint_drawer.paint(painter, self.canvas_rect)
	
	def resizeEvent(self, event: QResizeEvent):
		size = event.size()
		w = h = min(size.width(), size.height()) * 9 // 11
		x = (size.width() - w) // 2
		y = (size.height() - h) // 2
		self.canvas_rect = QRect(x, y, w, h)
		return super(SudokuWidget, self).resizeEvent(event)
		

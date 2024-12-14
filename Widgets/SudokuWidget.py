from typing import Optional, Dict

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QResizeEvent, QPaintEvent
from PyQt5.QtWidgets import QWidget

from Constraints.Constraint import Constraint
from Sudokus.Sudoku import Sudoku
from Widgets.ConstraintDrawers import getConstraintDrawerType
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer
from Widgets.SudokuDrawers import getSudokuDrawerType, SudokuDrawer


class SudokuWidget(QWidget):
	def __init__(self, parent=None):
		super(SudokuWidget, self).__init__(parent)
		self.sudoku: Optional[Sudoku] = None
		self.sudoku_drawer: Optional[SudokuDrawer] = None
		self.canvas_rect: QRect = QRect()
	
	def setSudoku(self, sudoku: Optional[Sudoku]) -> None:
		self.sudoku = sudoku
		self.initSudokuDrawer()
	
	def initSudokuDrawer(self):
		sudoku_type = type(self.sudoku)
		sudoku_drawer_type = getSudokuDrawerType(sudoku_type)
		assert sudoku_drawer_type is not None
		self.sudoku_drawer = sudoku_drawer_type(self.sudoku)

	def paintEvent(self, event: QPaintEvent):
		painter = QPainter(self)
		self.sudoku_drawer.paint(painter, self.canvas_rect)
	
	def resizeEvent(self, event: QResizeEvent):
		size = event.size()
		w = h = min(size.width(), size.height()) * 9 // 11
		x = (size.width() - w) // 2
		y = (size.height() - h) // 2
		self.canvas_rect = QRect(x, y, w, h)
		return super(SudokuWidget, self).resizeEvent(event)
		

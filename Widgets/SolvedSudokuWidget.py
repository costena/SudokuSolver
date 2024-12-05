from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QFont

from Widgets.SudokuWidget import SudokuWidget


class SolvedSudokuWidget(SudokuWidget):
	def paintEvent(self, event: QPaintEvent):
		painter = QPainter(self)
		rect = self.canvas_rect
		for j in range(9):
			for i in range(9):
				x = rect.x() + rect.width() * i // 9
				y = rect.y() + rect.height() * j // 9
				w = rect.width() // 9
				h = rect.height() // 9
				fw = rect.width() * 2 // 3 // 9
				fh = rect.height() * 3 // 4 // 9
				fx = x + (w - fw) * 3 // 4
				fy = y + (h - fh) * 2 // 3
				fs = fh
				f = QFont("", fs)
				painter.save()
				painter.setFont(f)
				painter.setPen(Qt.GlobalColor.red)
				painter.drawText(fx, fy + fh, f"{self.sudoku.get_number(i, j)}")
				painter.restore()
		super(SolvedSudokuWidget, self).paintEvent(event)

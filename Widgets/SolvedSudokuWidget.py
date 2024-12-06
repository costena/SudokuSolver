from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QFont, QPen

from Widgets.SudokuWidget import SudokuWidget


class SolvedSudokuWidget(SudokuWidget):
	def paintEvent(self, event: QPaintEvent):
		super(SolvedSudokuWidget, self).paintEvent(event)
		painter = QPainter(self)
		rect = self.canvas_rect
		for j in range(9):
			for i in range(9):
				possible_numbers = self.sudoku.ref_possible_numbers(i, j)
				if len(possible_numbers) == 1:
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
				else:
					x = rect.x() + rect.width() * i // 9
					y = rect.y() + rect.height() * j // 9
					w = rect.width() // 9
					h = rect.height() // 9
					fw = rect.width() * 2 // 3 // 9
					fh = rect.height() * 3 // 4 // 9
					fx = x + (w - fw) * 2 // 3
					fy = y + (h - fh) * 3 // 4
					fs = fh // 5
					f = QFont("", fs)
					painter.save()
					painter.setFont(f)
					for k in range(9):
						number = k + 1
						if number in possible_numbers:
							painter.drawText(fx + fw * (k % 3) // 3, fy + fh * (k // 3 + 1) // 3, f"{number}")
					painter.restore()

		if self.sudoku.context_position_number:
			i, j, number = self.sudoku.context_position_number
			x = rect.x() + rect.width() * i // 9
			y = rect.y() + rect.height() * j // 9
			w = rect.width() // 9
			h = rect.height() // 9
			fw = rect.width() * 2 // 3 // 9
			fh = rect.height() * 3 // 4 // 9
			fx = x + (w - fw) * 2 // 3
			fy = y + (h - fh) * 3 // 4
			fs = fh // 5
			f = QFont("", fs)
			painter.save()
			painter.setFont(f)
			painter.setPen(QPen(Qt.GlobalColor.blue))
			k = number - 1
			painter.drawText(fx + fw * (k % 3) // 3, fy + fh * (k // 3 + 1) // 3, f"{number}")
			painter.restore()

		constraint = self.sudoku.context_constraint
		if constraint is None:
			return
		constraint_drawer = self.constraint_drawers.get(constraint)
		if constraint_drawer is not None:
			constraint_drawer.special_paint(painter, self.canvas_rect)

from typing import Optional

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QFont, QPen

from Solvers.DebuggableSudokuSolver import DebuggableSudokuSolver
from Solvers.SudokuSolver import SudokuSolver
from Widgets.SudokuWidget import SudokuWidget


class SolvedSudokuWidget(SudokuWidget):
	def __init__(self, parent=None):
		super(SolvedSudokuWidget, self).__init__(parent)
		self.sudoku_solver: Optional[SudokuSolver] = None

	def setSudokuSolver(self, sudoku_solver: Optional[SudokuSolver]):
		self.sudoku_solver = sudoku_solver

	def paintEvent(self, event: QPaintEvent):
		super(SolvedSudokuWidget, self).paintEvent(event)
		if not isinstance(self.sudoku_solver, DebuggableSudokuSolver):
			return

		painter = QPainter(self)
		if len(self.sudoku_solver.constraint_contexts) > 0:
			constraint = self.sudoku_solver.constraint_contexts[-1]
			self.sudoku_drawer.special_paint(painter, self.canvas_rect, constraint)

		rect = self.canvas_rect
		for j in range(9):
			for i in range(9):
				possible_numbers = self.sudoku_solver.ref_possible_numbers(i, j)
				if len(possible_numbers) == 1:
					x = rect.x() + rect.width() * i // 9
					y = rect.y() + rect.height() * j // 9
					w = rect.width() // 9
					h = rect.height() // 9
					fw = rect.width() * 2 // 3 // 9
					fh = rect.height() * 3 // 4 // 9
					fx = x + (w - fw) * 3 // 4
					fy = y + (h - fh) // 2
					fs = fh * 2 //3
					f = QFont("", fs)
					painter.save()
					painter.setFont(f)
					painter.setPen(Qt.GlobalColor.red)
					painter.drawText(fx, fy + fh, f"{self.sudoku_solver.get_number(i, j)}")
					painter.restore()
				else:
					x = rect.x() + rect.width() * i // 9
					y = rect.y() + rect.height() * j // 9
					w = rect.width() // 9
					h = rect.height() // 9
					fw = rect.width() * 2 // 3 // 9
					fh = rect.height() * 3 // 4 // 9
					fx = x + (w - fw) * 2 // 3
					fy = y + (h - fh) // 2
					fs = fh // 5
					f = QFont("", fs)
					painter.save()
					painter.setFont(f)
					for k in range(9):
						number = k + 1
						if number in possible_numbers:
							painter.drawText(fx + fw * (k % 3) // 3, fy + fh * (k // 3 + 1) // 3, f"{number}")
					painter.restore()

		if len(self.sudoku_solver.eliminating_contexts) > 0:
			i, j, number = self.sudoku_solver.eliminating_contexts[-1]
			x = rect.x() + rect.width() * i // 9
			y = rect.y() + rect.height() * j // 9
			w = rect.width() // 9
			h = rect.height() // 9
			fw = rect.width() * 2 // 3 // 9
			fh = rect.height() * 3 // 4 // 9
			fx = x + (w - fw) * 2 // 3
			fy = y + (h - fh) // 2
			fs = fh // 5
			f = QFont("", fs)
			f.setBold(True)
			painter.save()
			painter.setFont(f)
			painter.setPen(QPen(Qt.GlobalColor.blue))
			k = number - 1
			painter.drawText(fx + fw * (k % 3) // 3, fy + fh * (k // 3 + 1) // 3, f"{number}")
			painter.restore()

		if len(self.sudoku_solver.filling_contexts) > 0:
			i, j, number = self.sudoku_solver.filling_contexts[-1]
			x = rect.x() + rect.width() * i // 9
			y = rect.y() + rect.height() * j // 9
			w = rect.width() // 9
			h = rect.height() // 9
			fw = rect.width() * 2 // 3 // 9
			fh = rect.height() * 3 // 4 // 9
			fx = x + (w - fw) * 2 // 3
			fy = y + (h - fh) // 2
			fs = fh // 5
			f = QFont("", fs)
			f.setBold(True)
			painter.save()
			painter.setFont(f)
			painter.setPen(QPen(Qt.GlobalColor.red))
			k = number - 1
			painter.drawText(fx + fw * (k % 3) // 3, fy + fh * (k // 3 + 1) // 3, f"{number}")
			painter.restore()

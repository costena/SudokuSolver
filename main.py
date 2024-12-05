import sys
from queue import Queue
from threading import Thread

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton

from Sudokus.KillerSudoku import KillerSudoku
from Sudokus.Sudoku import Sudoku
from Sudokus.StandardSudoku import StandardSudoku
from Sudokus.TigerSudoku import TigerSudoku
from Widgets.SolvedSudokuWidget import SolvedSudokuWidget
from Widgets.SudokuWidget import SudokuWidget


in_queue = Queue()

need_update = False


def wait_for_next():
	global need_update
	need_update = True
	# return True
	return in_queue.get()


def main():
	sudoku = createSudoku()
	# print(sudoku.solve())

	sudoku.step_callback = wait_for_next

	thread = Thread(target=sudoku.solve)
	thread.start()
	
	app = QApplication(sys.argv)
	window = QWidget()
	layout = QHBoxLayout(window)
	raw_sudoku_widget = SudokuWidget()
	raw_sudoku_widget.setSudoku(sudoku)
	layout.addWidget(raw_sudoku_widget)
	solved_sudoku_widget = SolvedSudokuWidget()
	solved_sudoku_widget.setSudoku(sudoku)
	layout.addWidget(solved_sudoku_widget)
	button = QPushButton()
	button.setFixedWidth(64)
	button.clicked.connect(lambda: [in_queue.put(True) for _ in range(100)])
	layout.addWidget(button)
	window.setLayout(layout)
	window.resize(1000, 1000)
	window.show()
	timer = QTimer()
	timer.timeout.connect(lambda: need_update and solved_sudoku_widget.update())
	timer.start(0)
	app.exec()

	thread.join()


def createSudoku() -> Sudoku:
	# raw_conundrum = [
	# 	"5..2...4.",
	# 	"...6.3...",
	# 	".3...9..7",
	# 	"..3..7...",
	# 	"..7..8...",
	# 	"6......2.",
	# 	".8......3",
	# 	"...4..6..",
	# 	"...1..5..",
	# ]
	# return StandardSudoku([
	# 	[
	# 		int(raw_number) if raw_number != '.' else None
	# 		for raw_number in raw_row
	# 	]
	# 	for raw_row in raw_conundrum
	# ])

	# return TigerSudoku([])

	return KillerSudoku([
		# [
		# 	int(raw_number) if raw_number != '.' else None
		# 	for raw_number in raw_row
		# ]
		# for raw_row in [
		# 	"86......2",
		# 	"..3.2..68",
		# 	"..4....9.",
		# 	"....64...",
		# 	".125....4",
		# 	"749..2..5",
		# 	".3.8.19..",
		# 	"..6....51",
		# 	"98.2....3",
		# ]
	])


if __name__ == '__main__':
	main()
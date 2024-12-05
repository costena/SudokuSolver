import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget

from Sudokus.StandardSudoku import StandardSudoku
from Sudokus.Sudoku import Sudoku
from Widgets.SolvedSudokuWidget import SolvedSudokuWidget
from Widgets.SudokuWidget import SudokuWidget


def main():
	sudoku = createSudoku()
	# assert sudoku.solve()
	
	app = QApplication(sys.argv)
	window = QWidget()
	layout = QHBoxLayout(window)
	raw_sudoku_widget = SudokuWidget()
	raw_sudoku_widget.setSudoku(sudoku)
	layout.addWidget(raw_sudoku_widget)
	# solved_sudoku_widget = SolvedSudokuWidget()
	# solved_sudoku_widget.setSudoku(sudoku)
	# layout.addWidget(solved_sudoku_widget)
	window.setLayout(layout)
	window.show()
	app.exec()


def createSudoku() -> Sudoku:
	raw_conundrum = [
		"5..2...4.",
		"...6.3...",
		".3...9..7",
		"..3..7...",
		"..7..8...",
		"6......2.",
		".8......3",
		"...4..6..",
		"...1..5..",
	]
	return StandardSudoku([
		[
			int(raw_number) if raw_number != '.' else None
			for raw_number in raw_row
		]
		for raw_row in raw_conundrum
	])


if __name__ == '__main__':
	main()
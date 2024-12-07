import sys
from queue import Queue
from threading import Thread

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton, QVBoxLayout, QCheckBox

from Presets import ZigzagPresets, DiagonalPresets, WindowPresets
from Solvers.DebuggableSudokuSolver import DebuggableSudokuSolver
from Solvers.SudokuSolver import SudokuSolver
from Sudokus.Sudoku import Sudoku
from Widgets.SolvedSudokuWidget import SolvedSudokuWidget
from Widgets.SudokuWidget import SudokuWidget


in_queue = Queue()

need_update = False
debug = True


def wait_for_next():
	global need_update
	need_update = True
	if debug:
		return in_queue.get()
	return True


def disable_debug():
	global debug
	debug = False
	in_queue.put(True)
	

def enable_debug():
	global debug
	debug = True


def main():
	sudoku = createSudoku()
	sudoku_solver = createSudokuSolver(sudoku)
	# print(sudoku.solve())

	thread = Thread(target=sudoku_solver.solve)
	thread.start()
	
	app = QApplication(sys.argv)
	window = QWidget()
	layout = QHBoxLayout(window)
	raw_sudoku_widget = SudokuWidget()
	raw_sudoku_widget.setSudoku(sudoku)
	layout.addWidget(raw_sudoku_widget)
	solved_sudoku_widget = SolvedSudokuWidget()
	solved_sudoku_widget.setSudoku(sudoku)
	solved_sudoku_widget.setSudokuSolver(sudoku_solver)
	layout.addWidget(solved_sudoku_widget)
	h_layout = QVBoxLayout()
	run_button = QPushButton("Run")
	run_button.setFixedWidth(64)
	run_button.clicked.connect(disable_debug)
	h_layout.addWidget(run_button)
	pause_button = QPushButton("Pause")
	pause_button.setFixedWidth(64)
	pause_button.clicked.connect(enable_debug)
	h_layout.addWidget(pause_button)
	step_button = QPushButton("Step")
	step_button.setFixedWidth(64)
	step_button.clicked.connect(lambda: in_queue.put(True))
	h_layout.addWidget(step_button)
	step10_button = QPushButton("Step10")
	step10_button.setFixedWidth(64)
	step10_button.clicked.connect(lambda: [in_queue.put(True) for _ in range(10)])
	h_layout.addWidget(step10_button)
	timer_check = QCheckBox("Timer")
	timer_check.setFixedWidth(64)
	step_timer = QTimer()
	step_timer.timeout.connect(lambda: in_queue.put(True))
	timer_check.stateChanged.connect(lambda: step_timer.start(10) if timer_check.isChecked() else step_timer.stop())
	h_layout.addWidget(timer_check)
	layout.addLayout(h_layout)
	window.setLayout(layout)
	window.resize(1000, 1000)
	window.show()
	timer = QTimer()
	timer.timeout.connect(lambda: need_update and solved_sudoku_widget.update())
	timer.start(1)
	app.exec()
	
	in_queue.put(False)

	thread.join()


def createSudoku() -> Sudoku:
	return WindowPresets.get_sudoku(0)


def createSudokuSolver(sudoku: Sudoku) -> SudokuSolver:
	return DebuggableSudokuSolver(sudoku, wait_for_next)



if __name__ == '__main__':
	main()
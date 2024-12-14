from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QBrush

from Sudokus.BlackoutSudoku import BlackoutSudoku
from Widgets.SudokuDrawers.SudokuDrawer import SudokuDrawer


class BlackoutSudokuDrawer(SudokuDrawer):
    def paint(self, painter: QPainter, rect: QRect):
        super(BlackoutSudokuDrawer, self).paint(painter, rect)
        assert isinstance(self.sudoku, BlackoutSudoku)
        brush = QBrush(Qt.GlobalColor.black)
        painter.save()
        painter.setBrush(brush)
        for logic_x, logic_y in self.sudoku.blackout_positions:
            x = rect.left() + rect.width() * logic_x // 9
            y = rect.top() + rect.height() * logic_y // 9
            w = rect.width() * (logic_x + 1) // 9 - rect.width() * logic_x // 9
            h = rect.height() * (logic_y + 1) // 9 - rect.height() * logic_y // 9
            painter.drawRect(x, y, w, h)
        painter.restore()


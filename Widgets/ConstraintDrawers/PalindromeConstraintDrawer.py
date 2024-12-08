from PyQt5.QtCore import QRect, Qt, QLine
from PyQt5.QtGui import QPainter, QPen

from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


class PalindromeConstraintDrawer(ConstraintDrawer):
    def paint(self, painter: QPainter, rect: QRect):
        pen = QPen(Qt.GlobalColor.lightGray, max(6, rect.width() // 64))
        return self.paint_internal(painter, rect, pen)

    def special_paint(self, painter: QPainter, rect: QRect):
        pen = QPen(Qt.GlobalColor.blue, max(6, rect.width() // 64))
        return self.paint_internal(painter, rect, pen)

    def paint_internal(self, painter: QPainter, rect: QRect, pen: QPen):
        last_x = None
        last_y = None
        lines = []
        for logic_x, logic_y in self.constraint.shape.iter_positions():
            x = rect.x() + rect.width() * logic_x // 9 + rect.width() // 2 // 9
            y = rect.y() + rect.height() * logic_y // 9 + rect.height() // 2 // 9
            if last_x is None:
                last_x = x
                last_y = y
                continue
            line = QLine(last_x, last_y, x, y)
            lines.append(line)
            last_x = x
            last_y = y
        painter.save()
        painter.setPen(pen)
        painter.drawLines(lines)
        painter.restore()

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

from Constraints.Shapes.Rectangle import Rectangle
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


class ContinuousConstraintDrawer(ConstraintDrawer):
    def paint(self, painter: QPainter, rect: QRect):
        pen = QPen(Qt.GlobalColor.black, max(6, rect.width() // 64))
        return self.paint_internal(painter, rect, pen)

    def special_paint(self, painter: QPainter, rect: QRect):
        pen = QPen(Qt.GlobalColor.blue, max(6, rect.width() // 64))
        return self.paint_internal(painter, rect, pen)

    def paint_internal(self, painter: QPainter, rect: QRect, pen: QPen):
        shape = self.constraint.shape
        assert isinstance(shape, Rectangle)
        x = rect.x() + rect.width() * (shape.x + shape.w - 1) // 9
        y = rect.y() + rect.height() * (shape.y + shape.h - 1) // 9
        if shape.w == 2:
            x1 = x
            y1 = y + rect.height() // 45
            x2 = x
            y2 = y + rect.height() // 9 - rect.height() // 45
        elif shape.h == 2:
            x1 = x + rect.width() // 45
            y1 = y
            x2 = x + rect.width() // 9 - rect.height() // 45
            y2 = y
        else:
            raise Exception
        painter.save()
        painter.setPen(pen)
        painter.drawLine(x1, y1, x2, y2)
        painter.restore()

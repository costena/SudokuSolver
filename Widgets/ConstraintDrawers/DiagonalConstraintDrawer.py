from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

from Constraints.DiagonalConstraint import DiagonalConstraint
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


class DiagonalConstraintDrawer(ConstraintDrawer):
    def paint(self, painter: QPainter, rect: QRect):
        pen = QPen(Qt.GlobalColor.lightGray, max(3, rect.width() // 128))
        return self.paint_internal(painter, rect, pen)

    def special_paint(self, painter: QPainter, rect: QRect):
        pen = QPen(Qt.GlobalColor.blue, max(6, rect.width() // 64))
        return self.paint_internal(painter, rect, pen)

    def paint_internal(self, painter: QPainter, rect: QRect, pen: QPen):
        assert isinstance(self.constraint, DiagonalConstraint)
        painter.save()
        painter.setPen(pen)
        if self.constraint.is_bottom_left_to_top_right:
            painter.drawLine(rect.bottomLeft(), rect.topRight())
        else:
            painter.drawLine(rect.topLeft(), rect.bottomRight())
        painter.restore()

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

from Widgets.ConstraintDrawers.RectangleConstraintDrawer import RectangleConstraintDrawer


class WindowBlockConstraintDrawer(RectangleConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.darkBlue, max(3, rect.width() // 128))
		brush = QBrush(QColor(0, 0, 255, 50))
		return self.paint_internal(painter, rect, pen, brush)

	def special_paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.blue, max(6, rect.width() // 64))
		brush = QBrush(QColor(0, 0, 255, 50))
		return self.paint_internal(painter, rect, pen, brush)

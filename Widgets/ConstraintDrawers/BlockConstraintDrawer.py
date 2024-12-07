from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

from Widgets.ConstraintDrawers.RectangleConstraintDrawer import RectangleConstraintDrawer


class BlockConstraintDrawer(RectangleConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.black, max(3, rect.width() // 128))
		return self.paint_internal(painter, rect, pen)

	def special_paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.blue, max(6, rect.width() // 64))
		return self.paint_internal(painter, rect, pen)

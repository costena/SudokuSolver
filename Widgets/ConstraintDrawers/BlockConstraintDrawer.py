from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

from Widgets.ConstraintDrawers.RectangleConstraintDrawer import RectangleConstraintDrawer


class BlockConstraintDrawer(RectangleConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.black, 3)
		return self.paint_internal(painter, rect, pen)

	def special_paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.blue, 11)
		return self.paint_internal(painter, rect, pen)

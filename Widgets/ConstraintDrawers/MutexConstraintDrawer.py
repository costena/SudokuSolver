from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

from Widgets.ConstraintDrawers.ShapeConstraintDrawer import ShapeConstraintDrawer


class MutexConstraintDrawer(ShapeConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.black, max(3, rect.width() // 128))
		return self.paint_internal(painter, rect, pen)

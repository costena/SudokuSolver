from typing import Optional

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen, QBrush

from Constraints.Shapes.Rectangle import Rectangle
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


class RectangleConstraintDrawer(ConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.black, 1)
		return self.paint_internal(painter, rect, pen)

	def special_paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.blue, max(6, rect.width() // 64))
		return self.paint_internal(painter, rect, pen)

	def paint_internal(self, painter: QPainter, rect: QRect, pen: QPen, brush: Optional[QBrush]=None):
		assert isinstance(self.constraint.shape, Rectangle)
		x = rect.x() + rect.width() * self.constraint.shape.x // 9
		y = rect.y() + rect.height() * self.constraint.shape.y // 9
		w = rect.width() * (self.constraint.shape.x + self.constraint.shape.w) // 9 - x + rect.x()
		h = rect.height() * (self.constraint.shape.y + self.constraint.shape.h) // 9 - y + rect.y()
		painter.save()
		painter.setPen(pen)
		if brush is not None:
			painter.setBrush(brush)
		painter.drawRect(x, y, w, h)
		painter.restore()

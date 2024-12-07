from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

from Constraints.GermanWhispersLineConstraint import GermanWhispersLineConstraint
from Constraints.Shapes.UnionShape import UnionShape
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


class GermanWhispersLineConstraintDrawer(ConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.green, 5)
		return self.paint_internal(painter, rect, pen)

	def special_paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.blue, 5)
		return self.paint_internal(painter, rect, pen)

	def paint_internal(self, painter: QPainter, rect: QRect, pen: QPen):
		assert isinstance(self.constraint, GermanWhispersLineConstraint)
		assert isinstance(self.constraint.shape, UnionShape)
		x1 = rect.x() + rect.width() * self.constraint.shape.shapes[0].x // 9 + rect.width() // 2 // 9
		y1 = rect.y() + rect.height() * self.constraint.shape.shapes[0].y // 9 + rect.height() // 2 // 9
		x2 = rect.x() + rect.width() * self.constraint.shape.shapes[1].x // 9 + rect.width() // 2 // 9
		y2 = rect.y() + rect.height() * self.constraint.shape.shapes[1].y // 9 + rect.height() // 2 // 9
		painter.save()
		painter.setPen(pen)
		painter.drawLine(x1, y1, x2, y2)
		painter.restore()

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QFont, QPen

from Constraints.NumberConstraint import NumberConstraint
from Constraints.Shapes.SinglePosition import SinglePosition
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


class NumberConstraintDrawer(ConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.black)
		return self.paint_internal(painter, rect, pen, False)

	def special_paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.blue)
		return self.paint_internal(painter, rect, pen, True)

	def paint_internal(self, painter: QPainter, rect: QRect, pen: QPen, bold: bool):
		assert isinstance(self.constraint, NumberConstraint)
		assert isinstance(self.constraint.shape, SinglePosition)
		x = rect.x() + rect.width() * self.constraint.shape.x // 9
		y = rect.y() + rect.height() * self.constraint.shape.y // 9
		w = rect.width() // 9
		h = rect.height() // 9
		fw = rect.width() * 2 // 3 // 9
		fh = rect.height() * 3 // 4 // 9
		fx = x + (w - fw) * 3 // 4
		fy = y + (h - fh) // 2
		fs = fh * 2 // 3
		f = QFont("", fs)
		f.setBold(bold)
		painter.save()
		painter.setPen(pen)
		painter.setFont(f)
		painter.drawText(fx, fy + fh, f"{self.constraint.number}")
		painter.restore()

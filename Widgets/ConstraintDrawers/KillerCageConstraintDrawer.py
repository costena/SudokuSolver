from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen, QFont

from Constraints.KillerCageConstraint import KillerCageConstraint
from Constraints.Shapes.Rectangle import Rectangle
from Widgets.ConstraintDrawers import register_constraint_drawer
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


@register_constraint_drawer(KillerCageConstraint)
class KillerCageConstraintDrawer(ConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		assert isinstance(self.constraint, KillerCageConstraint)
		if not isinstance(self.constraint.shape, Rectangle):
			return
		x = rect.x() + rect.width() * self.constraint.shape.x // 9 + rect.width() // 90
		y = rect.y() + rect.height() * self.constraint.shape.y // 9 + rect.height() // 90
		w = rect.width() * self.constraint.shape.w // 9 - rect.width() // 45
		h = rect.height() * self.constraint.shape.h // 9 - rect.height() // 45
		fh = rect.height() // 45
		fs = fh * 2 // 3
		f = QFont("", fs)
		painter.save()
		painter.setFont(f)
		pen = QPen(Qt.GlobalColor.black, 1)
		pen.setStyle(Qt.PenStyle.DashLine)
		painter.setPen(pen)
		painter.setBrush(Qt.BrushStyle.NoBrush)
		painter.drawRect(x, y, w, h)
		painter.drawText(x - fh // 3, y + fh * 2 // 3, f"{self.constraint.summation}")
		painter.restore()

	def special_paint(self, painter: QPainter, rect: QRect):
		assert isinstance(self.constraint, KillerCageConstraint)
		if not isinstance(self.constraint.shape, Rectangle):
			return
		x = rect.x() + rect.width() * self.constraint.shape.x // 9 + rect.width() // 90
		y = rect.y() + rect.height() * self.constraint.shape.y // 9 + rect.height() // 90
		w = rect.width() * self.constraint.shape.w // 9 - rect.width() // 45
		h = rect.height() * self.constraint.shape.h // 9 - rect.height() // 45
		fh = rect.height() // 45
		fs = fh * 2 // 3
		f = QFont("", fs)
		painter.save()
		painter.setFont(f)
		pen = QPen(Qt.GlobalColor.blue, 1)
		pen.setStyle(Qt.PenStyle.DashLine)
		painter.setPen(pen)
		painter.setBrush(Qt.BrushStyle.NoBrush)
		painter.drawRect(x, y, w, h)
		painter.drawText(x - fh // 3, y + fh * 2 // 3, f"{self.constraint.summation}")
		painter.restore()

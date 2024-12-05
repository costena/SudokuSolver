from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

from Constraints.RowConstraint import RowConstraint
from Widgets.ConstraintDrawers import register_constraint_drawer
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


@register_constraint_drawer(RowConstraint)
class RowConstraintDrawer(ConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		assert isinstance(self.constraint, RowConstraint)
		x = rect.x()
		y = rect.y() + rect.height() * self.constraint.y // 9
		w = rect.width()
		h = rect.height() * (self.constraint.y + 1) // 9 - y + rect.y()
		painter.save()
		painter.setPen(QPen(Qt.GlobalColor.black, 1))
		painter.setBrush(Qt.BrushStyle.NoBrush)
		painter.drawRect(x, y, w, h)
		painter.restore()

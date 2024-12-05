from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

from Constraints.ColumnConstraint import ColumnConstraint
from Widgets.ConstraintDrawers import register_constraint_drawer
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


@register_constraint_drawer(ColumnConstraint)
class ColumnConstraintDrawer(ConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		assert isinstance(self.constraint, ColumnConstraint)
		x = rect.x() + rect.width() * self.constraint.x // 9
		y = rect.y()
		w = rect.width() * (self.constraint.x + 1) // 9 - x + rect.x()
		h = rect.height()
		painter.save()
		painter.setPen(QPen(Qt.GlobalColor.black, 1))
		painter.setBrush(Qt.BrushStyle.NoBrush)
		painter.drawRect(x, y, w, h)
		painter.restore()

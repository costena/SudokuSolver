from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QFont

from Constraints.NumberConstraint import NumberConstraint
from Widgets.ConstraintDrawers import register_constraint_drawer
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


@register_constraint_drawer(NumberConstraint)
class NumberConstraintDrawer(ConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		assert isinstance(self.constraint, NumberConstraint)
		x = rect.x() + rect.width() * self.constraint.x // 9
		y = rect.y() + rect.height() * self.constraint.y // 9
		w = rect.width() // 9
		h = rect.height() // 9
		fw = rect.width() * 2 // 3 // 9
		fh = rect.height() * 3 // 4 // 9
		fx = x + (w - fw) * 3 // 4
		fy = y + (h - fh) * 2 // 3
		fs = fh
		f = QFont("", fs)
		painter.save()
		painter.setFont(f)
		painter.drawText(fx, fy + fh, f"{self.constraint.number}")
		painter.restore()

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QFont

from Constraints.PossibleNumbersConstraint import PossibleNumbersConstraint
from Constraints.Shapes.SinglePosition import SinglePosition
from Widgets.ConstraintDrawers import register_constraint_drawer
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


@register_constraint_drawer(PossibleNumbersConstraint)
class PossibleNumbersConstraintDrawer(ConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		assert isinstance(self.constraint, PossibleNumbersConstraint)
		assert isinstance(self.constraint.shape, SinglePosition)
		x = rect.x() + rect.width() * self.constraint.shape.x // 9
		y = rect.y() + rect.height() * self.constraint.shape.y // 9
		w = rect.width() // 9
		h = rect.height() // 9
		fw = rect.width() * 2 // 3 // 9
		fh = rect.height() * 3 // 4 // 9
		fx = x + (w - fw) * 2 // 3
		fy = y + (h - fh) * 3 // 4
		fs = fh // 3
		f = QFont("", fs)
		painter.save()
		painter.setFont(f)
		for i in range(9):
			number = i + 1
			if number in self.constraint.possible_numbers:
				painter.drawText(fx + fw * (i % 3) // 3, fy + fh * (i // 3 + 1) // 3, f"{number}")
		painter.restore()

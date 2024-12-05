from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

from Constraints.BlockConstraint import BlockConstraint
from Constraints.Shapes.Rectangle import Rectangle
from Widgets.ConstraintDrawers import register_constraint_drawer
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


@register_constraint_drawer(BlockConstraint)
class BlockConstraintDrawer(ConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		assert isinstance(self.constraint, BlockConstraint)
		assert isinstance(self.constraint.shape, Rectangle)
		x = rect.x() + rect.width() * self.constraint.shape.x // 9
		y = rect.y() + rect.height() * self.constraint.shape.y // 9
		w = rect.width() * (self.constraint.shape.x + 3) // 9 - x + rect.x()
		h = rect.height() * (self.constraint.shape.y + 3) // 9 - y + rect.y()
		painter.save()
		painter.setPen(QPen(Qt.GlobalColor.black, 3))
		painter.setBrush(Qt.BrushStyle.NoBrush)
		painter.drawRect(x, y, w, h)
		painter.restore()

	def special_paint(self, painter: QPainter, rect: QRect):
		assert isinstance(self.constraint, BlockConstraint)
		assert isinstance(self.constraint.shape, Rectangle)
		x = rect.x() + rect.width() * self.constraint.shape.x // 9
		y = rect.y() + rect.height() * self.constraint.shape.y // 9
		w = rect.width() * (self.constraint.shape.x + 3) // 9 - x + rect.x()
		h = rect.height() * (self.constraint.shape.y + 3) // 9 - y + rect.y()
		painter.save()
		painter.setPen(QPen(Qt.GlobalColor.blue, 3))
		painter.setBrush(Qt.BrushStyle.NoBrush)
		painter.drawRect(x, y, w, h)
		painter.restore()

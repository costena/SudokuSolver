from PyQt5.QtCore import QRect, Qt, QLine
from PyQt5.QtGui import QPainter, QPen, QFont, QFontMetrics

from Constraints.KillerCageConstraint import KillerCageConstraint
from Widgets.ConstraintDrawers.ShapeConstraintDrawer import ShapeConstraintDrawer
from Widgets.ConstraintDrawers.Utils import sign


class KillerCageConstraintDrawer(ShapeConstraintDrawer):
	def paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.black, 1)
		pen.setStyle(Qt.PenStyle.DashLine)
		return self.paint_internal(painter, rect, pen, False)

	def special_paint(self, painter: QPainter, rect: QRect):
		pen = QPen(Qt.GlobalColor.blue, max(6, rect.width() // 64))
		pen.setStyle(Qt.PenStyle.DashLine)
		return self.paint_internal(painter, rect, pen, True)

	def paint_internal(self, painter: QPainter, rect: QRect, pen: QPen, bold: bool=False):
		polygons = []
		for logic_points in self.shapes:
			points = []
			for i, point in enumerate(logic_points):
				last_point = logic_points[(i - 1) % len(logic_points)]
				next_point = logic_points[(i + 1) % len(logic_points)]
				x = rect.x() + rect.width() * point[0] // 9
				y = rect.y() + rect.height() * point[1] // 9

				out_direction = (
					sign(next_point[0] - point[0]),
					sign(next_point[1] - point[1]),
				)
				in_direction = (
					sign(point[0] - last_point[0]),
					sign(point[1] - last_point[1]),
				)
				offset_logic_x, offset_logic_y = {
					((0, 1), (-1, 0)): (-1, -1),
					((-1, 0), (0, 1)): (-1, -1),

					((1, 0), (0, 1)): (-1, 1),
					((0, 1), (1, 0)): (-1, 1),

					((-1, 0), (0, -1)): (1, -1),
					((0, -1), (-1, 0)): (1, -1),

					((1, 0), (0, -1)): (1, 1),
					((0, -1), (1, 0)): (1, 1),
				}[(in_direction, out_direction)]
				offset_x = offset_logic_x * rect.width() // 90
				offset_y = offset_logic_y * rect.height() // 90
				x += offset_x
				y += offset_y
				points.append((x, y))
			polygons.append(points)

		assert isinstance(self.constraint, KillerCageConstraint)
		x = 0
		y = 0
		for logic_x, logic_y in self.constraint.shape.iter_positions():
			x = rect.x() + rect.width() * logic_x // 9
			y = rect.y() + rect.height() * logic_y // 9
			break
		fh = rect.height() // 45
		fs = fh * 2 // 3
		f = QFont("", fs)
		f.setBold(bold)
		fm = QFontMetrics(f)
		text = f"{self.constraint.summation}"
		fw = fm.width(text)
		painter.save()
		painter.setFont(f)
		painter.setPen(pen)
		painter.setBrush(Qt.BrushStyle.NoBrush)
		lines = []
		for points in polygons:
			last_point = None
			for point in points:
				if last_point is None:
					last_point = (point[0] + fw, point[1])
					continue
				line = QLine(last_point[0], last_point[1], point[0], point[1])
				lines.append(line)
				last_point = point
			point = (points[0][0], points[0][1] + fh)
			line = QLine(last_point[0], last_point[1], point[0], point[1])
			lines.append(line)
		painter.drawLines(lines)
		painter.drawText(x + fh // 5, y + fh * 6 // 5, text)
		painter.restore()

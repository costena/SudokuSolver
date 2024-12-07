from typing import Tuple, List, Dict, Set, Optional

from PyQt5.QtCore import QLine, QPoint, QRect, Qt
from PyQt5.QtGui import QPolygon, QPainter, QPen

from Constraints.Constraint import Constraint
from Types import PointType, LineType
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer

EdgeType = List[PointType]


class ShapeConstraintDrawer(ConstraintDrawer):
    def __init__(self, constraint: Constraint):
        super(ShapeConstraintDrawer, self).__init__(constraint)
        self.shapes: List[EdgeType] = self.create_edges()

    def paint(self, painter: QPainter, rect: QRect):
        pen = QPen(Qt.GlobalColor.black, 1)
        return self.paint_internal(painter, rect, pen)

    def special_paint(self, painter: QPainter, rect: QRect):
        pen = QPen(Qt.GlobalColor.blue, max(6, rect.width() // 64))
        return self.paint_internal(painter, rect, pen)

    def paint_internal(self, painter: QPainter, rect: QRect, pen: QPen):
        polygons = []
        for logic_points in self.shapes:
            points = []
            for i, point in enumerate(logic_points):
                x = rect.x() + rect.width() * point[0] // 9
                y = rect.y() + rect.height() * point[1] // 9
                points.append((x, y))
            polygons.append(points)

        painter.save()
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        lines = []
        for points in polygons:
            last_point = None
            for point in points:
                if last_point is None:
                    last_point = point
                    continue
                line = QLine(last_point[0], last_point[1], point[0], point[1])
                lines.append(line)
                last_point = point
            point = points[0]
            line = QLine(last_point[0], last_point[1], point[0], point[1])
            lines.append(line)
        painter.drawLines(lines)
        painter.restore()

    def create_edges(self) -> List[EdgeType]:
        lines: Dict[PointType, Set[PointType]] = {}

        def add_line(from_position: PointType, to_position: PointType):
            positions: Optional[Set[PointType]] = lines.get(to_position)
            if positions is not None and from_position in positions:
                positions.remove(from_position)
                if len(positions) == 0:
                    lines.pop(to_position)
                return
            lines.setdefault(from_position, set()).add(to_position)

        def is_parallel(line_a: LineType, line_b: LineType) -> bool:
            return all([
                (line_a[1][1] - line_a[0][1] != 0) == (line_b[1][1] - line_b[0][1] != 0),
                (line_a[1][0] - line_a[0][0] != 0) == (line_b[1][0] - line_b[0][0] != 0),
            ])

        for x, y in self.constraint.shape.iter_positions():
            add_line((x, y), (x + 1, y))
            add_line((x + 1, y), (x + 1, y + 1))
            add_line((x + 1, y + 1), (x, y + 1))
            add_line((x, y + 1), (x, y))

        edges: List[EdgeType] = []
        while len(lines) > 0:
            from_position = None
            for position in lines.keys():
                from_position = position
                break
            ordered_lines: List[LineType] = []
            while from_position in lines:
                to_positions = lines.pop(from_position)
                to_position = None
                for position in to_positions:
                    to_position = position
                    break
                ordered_lines.append((from_position, to_position))
                from_position = to_position
            edge: List[PointType] = []
            current_line: Optional[LineType] = None
            for line in ordered_lines:
                if current_line is None:
                    current_line = line
                    continue
                if is_parallel(line, current_line):
                    current_line = current_line[0], line[1]
                else:
                    edge.append(current_line[0])
                    current_line = line
            edge.append(current_line[0])
            first_line, last_line = (edge[0], edge[1]), (edge[-1], edge[0])
            if is_parallel(first_line, last_line):
                edge[0] = edge[-1]
                edge.pop()
            edges.append(edge)
        return edges

from typing import Dict, Optional

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter

from Constraints.Constraint import Constraint
from Sudokus.Sudoku import Sudoku
from Widgets.ConstraintDrawers import getConstraintDrawerType
from Widgets.ConstraintDrawers.ConstraintDrawer import ConstraintDrawer


class SudokuDrawer:
    def __init__(self, sudoku: Sudoku):
        self.sudoku = sudoku
        self.constraint_drawers: Dict[Constraint, ConstraintDrawer] = {}
        self.initConstraintDrawers()

    def initConstraintDrawers(self):
        for constraint in self.sudoku.constraints:
            constraint_type = type(constraint)
            constraint_drawer_type = getConstraintDrawerType(constraint_type)
            if constraint_drawer_type is not None:
                constraint_drawer: Optional[ConstraintDrawer] = constraint_drawer_type(constraint)
                self.constraint_drawers[constraint] = constraint_drawer

    def paint(self, painter: QPainter, rect: QRect):
        for constraint in self.sudoku.constraints:
            constraint_drawer: ConstraintDrawer = self.constraint_drawers.get(constraint)
            if constraint_drawer is None:
                continue
            constraint_drawer.paint(painter, rect)

    def special_paint(self, painter: QPainter, rect: QRect, constraint: Constraint):
        constraint_drawer = self.constraint_drawers.get(constraint)
        if constraint_drawer is not None:
            constraint_drawer.special_paint(painter, rect)

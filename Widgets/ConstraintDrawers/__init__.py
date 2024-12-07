from typing import Optional, Callable

from Constraints.BlockConstraint import BlockConstraint
from Constraints.ColumnConstraint import ColumnConstraint
from Constraints.DiagonalConstraint import DiagonalConstraint
from Constraints.GermanWhispersLineConstraint import GermanWhispersLineConstraint
from Constraints.KillerCageConstraint import KillerCageConstraint
from Constraints.MutexConstraint import MutexConstraint
from Constraints.NumberConstraint import NumberConstraint
from Constraints.PossibleNumbersConstraint import PossibleNumbersConstraint
from Constraints.RowConstraint import RowConstraint
from Constraints.WindowBlockConstraint import WindowBlockConstraint
from .DiagonalConstraintDrawer import DiagonalConstraintDrawer
from .RectangleConstraintDrawer import RectangleConstraintDrawer
from .BlockConstraintDrawer import BlockConstraintDrawer
from .PossibleNumbersConstraintDrawer import PossibleNumbersConstraintDrawer
from .NumberConstraintDrawer import NumberConstraintDrawer
from .KillerCageConstraintDrawer import KillerCageConstraintDrawer
from .GermanWhispersLineConstraintDrawer import GermanWhispersLineConstraintDrawer
from .MutexConstraintDrawer import MutexConstraintDrawer
from .WindowBlockConstraintDrawer import WindowBlockConstraintDrawer

ConstraintDrawers = {
	ColumnConstraint: RectangleConstraintDrawer,
	RowConstraint: RectangleConstraintDrawer,
	BlockConstraint: BlockConstraintDrawer,
	PossibleNumbersConstraint: PossibleNumbersConstraintDrawer,
	NumberConstraint: NumberConstraintDrawer,
	KillerCageConstraint: KillerCageConstraintDrawer,
	GermanWhispersLineConstraint: GermanWhispersLineConstraintDrawer,
	MutexConstraint: MutexConstraintDrawer,
	DiagonalConstraint: DiagonalConstraintDrawer,
	WindowBlockConstraint: WindowBlockConstraintDrawer,
}


def getConstraintDrawerType(constraint_type: type) -> Optional[type]:
	return ConstraintDrawers.get(constraint_type)

from typing import Optional, Callable, Dict

from Constraints.BlockConstraint import BlockConstraint
from Constraints.ColumnConstraint import ColumnConstraint
from Constraints.ContinuousConstraint import ContinuousConstraint
from Constraints.DiagonalConstraint import DiagonalConstraint
from Constraints.GermanWhispersLineConstraint import GermanWhispersLineConstraint
from Constraints.KillerCageConstraint import KillerCageConstraint
from Constraints.FullMutexConstraint import FullMutexConstraint
from Constraints.MutexConstraint import MutexConstraint
from Constraints.NumberConstraint import NumberConstraint
from Constraints.PalindromeConstraint import PalindromeConstraint
from Constraints.PossibleNumbersConstraint import PossibleNumbersConstraint
from Constraints.RowConstraint import RowConstraint
from Constraints.WindowBlockConstraint import WindowBlockConstraint
from .ContinuousConstraintDrawer import ContinuousConstraintDrawer
from .DiagonalConstraintDrawer import DiagonalConstraintDrawer
from .PalindromeConstraintDrawer import PalindromeConstraintDrawer
from .RectangleConstraintDrawer import RectangleConstraintDrawer
from .BlockConstraintDrawer import BlockConstraintDrawer
from .PossibleNumbersConstraintDrawer import PossibleNumbersConstraintDrawer
from .NumberConstraintDrawer import NumberConstraintDrawer
from .KillerCageConstraintDrawer import KillerCageConstraintDrawer
from .GermanWhispersLineConstraintDrawer import GermanWhispersLineConstraintDrawer
from .MutexConstraintDrawer import MutexConstraintDrawer
from .ShapeConstraintDrawer import ShapeConstraintDrawer
from .WindowBlockConstraintDrawer import WindowBlockConstraintDrawer


ConstraintDrawers = {
	MutexConstraint: ShapeConstraintDrawer,
	ColumnConstraint: RectangleConstraintDrawer,
	RowConstraint: RectangleConstraintDrawer,
	BlockConstraint: BlockConstraintDrawer,
	PossibleNumbersConstraint: PossibleNumbersConstraintDrawer,
	NumberConstraint: NumberConstraintDrawer,
	KillerCageConstraint: KillerCageConstraintDrawer,
	GermanWhispersLineConstraint: GermanWhispersLineConstraintDrawer,
	FullMutexConstraint: MutexConstraintDrawer,
	DiagonalConstraint: DiagonalConstraintDrawer,
	WindowBlockConstraint: WindowBlockConstraintDrawer,
	ContinuousConstraint: ContinuousConstraintDrawer,
	PalindromeConstraint: PalindromeConstraintDrawer,
}


def getConstraintDrawerType(constraint_type: type) -> Optional[type]:
	current_type = constraint_type
	while current_type is not None:
		drawer_type = ConstraintDrawers.get(current_type)
		if drawer_type is None:
			current_type = current_type.__base__
			continue
		return drawer_type

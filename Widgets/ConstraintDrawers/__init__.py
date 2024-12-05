from typing import Optional, Callable

ConstraintDrawers = {}


def register_constraint_drawer(constraint_type: type) -> Callable:
	def wrapper(constraint_drawer_type: type) -> type:
		ConstraintDrawers[constraint_type] = constraint_drawer_type
		return constraint_drawer_type
	
	return wrapper


def getConstraintDrawerType(constraint_type: type) -> Optional[type]:
	return ConstraintDrawers.get(constraint_type)


from . import RowConstraintDrawer
from . import ColumnConstraintDrawer
from . import BlockConstraintDrawer
from . import PossibleNumbersConstraintDrawer
from . import NumberConstraintDrawer
from . import KillerCageConstraintDrawer
from . import GermanWhispersLineConstraintDrawer

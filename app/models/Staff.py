"""Staff Model."""
from masoniteorm.models import Model


class Staff(Model):
    """Staff Model."""

    __fillable__ = ["name", "staff_number"]


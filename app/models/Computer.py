"""Computer Model."""
from masoniteorm.models import Model


class Computer(Model):
    """Computer Model."""

    __fillable__ = ["name", "number"]

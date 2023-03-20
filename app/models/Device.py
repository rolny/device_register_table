"""Device Model."""
from masoniteorm.models import Model


class Device(Model):
    """Device Model."""

    __fillable__ = ["name", "devices_number"]

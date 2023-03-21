"""Borrow Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

class Borrow(Model):
    """Borrow Model."""

    __fillable__ = [
                    "borrow_staff_number",
                    "confirm_user_id",
                    "devices_number",
                    "borrow_time",
                    "return_time",
                    ]

    @belongs_to("devices_number", "devices_number")
    def device(self):
        from app.models.Device import Device
        return Device

    @belongs_to("borrow_staff_number", "staff_number")
    def bs(self):
        from app.models.Staff import Staff
        return Staff

    @belongs_to("confirm_user_id", "id")
    def user(self):
        from app.models.User import User
        return User



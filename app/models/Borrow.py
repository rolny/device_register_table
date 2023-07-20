"""Borrow Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

class Borrowdevice(Model):
    """Borrowdevice Model."""
    __fillable__ = [
                    "borrow_staff_number",
                    "confirm_user_id",
                    "devices_number",
                    "borrow_time",
                    "return_time",
                    ]

    @belongs_to("devices_number", "number")
    def device(self):
        from app.models.Device import Device
        return Device

    @belongs_to("borrow_staff_number", "number")
    def bs(self):
        from app.models.Staff import Staff
        return Staff

    @belongs_to("confirm_user_id", "id")
    def user(self):
        from app.models.User import User
        return User


class Borrowcomputer(Model):
    """Borrowcomputer Model."""
    __fillable__ = [
                    "borrow_staff_number",
                    "confirm_user_id",
                    "computers_number",
                    "borrow_time",
                    "return_time",
                    ]

    @belongs_to("computers_number", "number")
    def computer(self):
        from app.models.Computer import Computer
        return Computer

    @belongs_to("borrow_staff_number", "number")
    def bs(self):
        from app.models.Staff import Staff
        return Staff

    @belongs_to("confirm_user_id", "id")
    def user(self):
        from app.models.User import User
        return User


class Borrowbook(Model):
    """Borrowbook Model."""
    __fillable__ = [
                    "borrow_staff_number",
                    "confirm_user_id",
                    "books_number",
                    "borrow_time",
                    "return_time",
                    ]

    @belongs_to("books_number", "number")
    def book(self):
        from app.models.Book import Book
        return Book

    @belongs_to("borrow_staff_number", "number")
    def bs(self):
        from app.models.Staff import Staff
        return Staff

    @belongs_to("confirm_user_id", "id")
    def user(self):
        from app.models.User import User
        return User
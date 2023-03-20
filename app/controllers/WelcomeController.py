"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masoniteorm.query import QueryBuilder
from app.models.Staff import Staff
from app.models.Device import Device
from app.models.Borrow import Borrow


import datetime

class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View, request: Request):
        staff_all = Staff.get()
        devices = Device.get()
        Borrow_table = Borrow.get()
        nowtime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
        print(nowtime)
        return view.render("welcome", {"staff_all": staff_all, "devices": devices, "nowtime": nowtime, "Borrow_table": Borrow_table})

    def add(self, request: Request, response: Response):
        d_n = request.input("device")
        devices = Device.get()
        devices.where("name", d_n).first()["devices_number"]
        b_s_name = request.input("borrow")
        b_t = request.input("borrow_time")
        staff = Staff.get()
        b_sn = staff.where("name", b_s_name).first()["staff_number"]
        print(f"b_sn{b_sn}")
        Borrow.create(
                {
                    "devices_number": d_n,
                    "borrow_staff_number": b_sn,
                    "borrow_time": b_t,
                }
            )
        return response.redirect('/')

    def confirm_update(self, request: Request, response: Response):
        c_s_name = request.input("confirm")
        r_t = request.input("return_time")
        bt_id = request.input("btid")
        staff = Staff.get()
        c_sn = staff.where("name", c_s_name).first()["staff_number"]
        Borrow.where("id", bt_id).update({"return_time": r_t, "confirm_staff_number": c_sn})
        return response.redirect('/')
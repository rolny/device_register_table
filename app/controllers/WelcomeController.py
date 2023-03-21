"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masoniteorm.query import QueryBuilder
from masonite.authentication import Auth
from app.models.Staff import Staff
from app.models.Device import Device
from app.models.Borrow import Borrow
from app.models.User import User


import datetime

class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View, request: Request, auth: Auth):
        staff_all = Staff.get()
        user_all = User.get()
        devices = Device.get()
        Borrow_table = Borrow.get()
        nowtime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
        user = auth.user()
        return view.render("welcome", {
            "staff_all": staff_all,
            "user_all": user_all,
            "devices": devices,
            "nowtime": nowtime,
            "Borrow_table": Borrow_table,
            "user_inuse": user,
            })

    def add(self, request: Request, response: Response):
        d_n = request.input("device")
        devices = Device.get()
        devices.where("name", d_n).first()["devices_number"]
        b_s_name = request.input("borrow")
        b_t = request.input("borrow_time")
        staff = Staff.get()
        b_sn = staff.where("name", b_s_name).first()["staff_number"]
        Borrow.create(
                {
                    "devices_number": d_n,
                    "borrow_staff_number": b_sn,
                    "borrow_time": b_t,
                }
            )
        return response.redirect('/')

    def confirm_update(self, request: Request, response: Response, auth: Auth):
        c_user_id = request.input("confirm")
        r_t = request.input("return_time")
        bt_id = request.input("btid")
        user = auth.user()
        if not user:
            return response.redirect(name="login")
        elif user:            
            if user.id != c_user_id:
                Borrow.where("id", bt_id).update({"return_time": r_t, "confirm_user_id": c_user_id})
                return response.redirect('/')
            else:
                return response.redirect(name="login").with_errors("錯誤的確認者")
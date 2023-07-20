"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masoniteorm.query import QueryBuilder
from masonite.authentication import Auth
from app.models.Staff import Staff
from app.models.Device import Device
from app.models.Borrow import Borrowdevice, Borrowbook, Borrowcomputer
from app.models.User import User

import pandas as pd
import datetime

class WelcomeController(Controller):
    """WelcomeController Controller Class."""
    def toindex(self, response: Response):
        return response.redirect('/index/devices')
    def show(self, view: View, request: Request, auth: Auth):
        qry = QueryBuilder()
        staff_all = Staff.get()
        nowtime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
        user = auth.user()
        return view.render("welcome", {
            "staff_all": staff_all,
            "query": qry,
            "nowtime": nowtime,
            "user_inuse": user,
            "item": request.param("item"),
            "computers": Borrowcomputer,
            "devices": Borrowdevice,
            "books": Borrowbook,
            })

    def add(self, request: Request, response: Response):
        item = request.param("item")
        d_n = request.input("device")
        b_s_name = request.input("borrow")
        b_t = request.input("borrow_time")
        staff = Staff.get()
        b_sn = staff.where("name", b_s_name).first()["number"]
        if item == "devices":
            Borrowdevice.create(
                    {
                        "devices_number": d_n,
                        "borrow_staff_number": b_sn,
                        "borrow_time": b_t,
                    }
                )
        elif item == "books":
            Borrowbook.create(
                    {
                        "books_number": d_n,
                        "borrow_staff_number": b_sn,
                        "borrow_time": b_t,
                    }
                )
        elif item == "computers":
            Borrowcomputer.create(
                    {
                        "computers_number": d_n,
                        "borrow_staff_number": b_sn,
                        "borrow_time": b_t,
                    }
                )
        return response.redirect(f'/index/{item}')

    def confirm_update(self, request: Request, response: Response, auth: Auth):
        c_user_id = request.input("confirm")
        item = request.param("item")
        r_t = request.input("return_time")
        bt_id = request.input("btid")
        user = auth.user()
        item = request.param("item")
        if not user:
            return response.redirect(name="login")
        elif user:            
            if user.id != c_user_id:
                if item == "devices":
                    Borrowdevice.where("id", bt_id).update({"return_time": r_t, "confirm_user_id": c_user_id})
                elif item == "books":
                    Borrowbook.where("id", bt_id).update({"return_time": r_t, "confirm_user_id": c_user_id})
                elif item == "computers":
                    Borrowcomputer.where("id", bt_id).update({"return_time": r_t, "confirm_user_id": c_user_id})
                return response.redirect(f'/index/{item}')
            else:
                return response.redirect(name="login").with_errors("錯誤的確認者")
            

    def output(self, request: Request, response: Response):        
        item = request.param("item")
        qry = QueryBuilder()
        pd.DataFrame(qry.table(f"borrow{item}").get()).to_csv("out.csv", index=False)
        response.download(f"borrow{item}", f"out.csv", force=True)
        return response
    

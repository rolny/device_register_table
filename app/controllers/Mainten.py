"""A MaintenController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masoniteorm.query import QueryBuilder
from masonite.authentication import Auth
from app.models.Staff import Staff
from app.models.Device import Device
from app.models.Book import Book
from app.models.Computer import Computer
from app.models.User import User
from app.models.Borrow import Borrowdevice, Borrowbook, Borrowcomputer
import pandas as pd

class MaintenController(Controller):
    """MaintenController Controller Class."""
    def show(self, view: View, request: Request, auth: Auth):
        qry = QueryBuilder()
        staff_all = Staff.get()
        computer = Computer.get()
        book = Book.get()
        device = Device.get()
        user = auth.user()
        return view.render("maintenance",
                           {"device": device,
                            "computer": computer,
                            "book": book,
                            "staff": staff_all,
                            })
    

    def add(self, request: Request, response: Response, auth: Auth):
        item = request.input("whitch")
        dnam = request.input("dnam")
        dnum = request.input("dnum")
        user = auth.user()
        qry = QueryBuilder()
        print(dnum, dnam, item)
        if not user:
            return response.redirect(name="login")
        elif user:
            try:
                qry.table(item).create({"name": dnam, "number": dnum})
                return response.redirect(name=f"maintenance")
            except:
                return response.redirect(name=f"maintenance").with_errors([f"{item}編號重複"])

            
    def delete(self, request: Request, response: Response, auth: Auth):
        item = request.param("item")
        dnum = request.input("dnum")
        qry = QueryBuilder()
        user = auth.user()
        if not user:
            return response.redirect(name="login")
        elif user:
            qry.table(f"{item}").where("number", dnum).delete()
            return response.redirect(f'/maintenance')
        

    def output(self, request: Request, response: Response):        
        item = request.param("item")
        qry = QueryBuilder()
        pd.DataFrame(qry.table(f"{item}").get()).to_csv("out.csv", index=False)
        response.download(f"{item}", f"out.csv", force=True)
        return response
    

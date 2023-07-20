from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
            Route.get("/", "WelcomeController@toindex"),
            Route.get("/index", "WelcomeController@toindex"),
            Route.get("/index/?item", "WelcomeController@show").name("index"),            
            Route.post("/add/?item", "WelcomeController@add").name("add"),
            Route.post("/C_U/?item", "WelcomeController@confirm_update").name("C_U"),
            Route.post("/output/?item", "WelcomeController@output").name("output"),
            Route.get("/maintenance", "MaintenController@show").name("maintenance"),
            Route.post("/mainten/add", "MaintenController@add").name("mainten.add"),
            Route.post("/mainten/output/?item", "MaintenController@output").name("mainten.output"),
            Route.post("/mainten/delete/?item", "MaintenController@delete").name("mainten.delete"),
]           

ROUTES += Auth.routes()

#無新增帳號、修改密碼
#ROUTES += Auth.routes_live()

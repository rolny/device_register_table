from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
            Route.get("/", "WelcomeController@show"),
            Route.post("/ADD", "WelcomeController@add"),
            Route.post("/C_U", "WelcomeController@confirm_update"),
]           

ROUTES += Auth.routes()

#無新增帳號、修改密碼
#ROUTES += Auth.routes_live()

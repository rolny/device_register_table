from masonite.routes import Route

ROUTES = [
            Route.get("/", "WelcomeController@show"),
            Route.post("/ADD", "WelcomeController@add"),
            Route.post("/C_U", "WelcomeController@confirm_update"),
]



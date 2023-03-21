from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
            Route.get("/", "WelcomeController@show"),
            Route.post("/ADD", "WelcomeController@add"),
            Route.post("/C_U", "WelcomeController@confirm_update"),
            Route.get("/login", "auth.LoginController@show").name("login"),
            Route.post("/login", "auth.LoginController@store").name("login.store"),
            Route.get("/logout", "auth.LoginController@logout").name("logout"),
            Route.get("/register", "auth.RegisterController@show").name("register"),
            Route.post("/register", "auth.RegisterController@store").name("register.store"),            
]

# ROUTES += Auth.routes()


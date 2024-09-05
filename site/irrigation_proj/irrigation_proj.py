import reflex as rx

from rxconfig import config
from .pages import home

app = rx.App(
    theme = rx.theme(
        appearance = "light",
        accent_color = "cyan",
        background = True
    )
)
app.add_page(home.home(), route = "/")

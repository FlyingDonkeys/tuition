from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_question", views.new_question, name="new_question"),
    path("home", views.home, name="home"),

    # Some APIs without associated views
    path("logout", views.logout_view, name="logout")
]
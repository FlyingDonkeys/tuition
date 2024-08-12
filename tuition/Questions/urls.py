from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_question", views.new_question, name="new_question"),
    path("new_answer/<int:question_id>", views.new_answer, name="new_answer"),
    path("home", views.home, name="home"),
    path("question/<int:question_id>", views.question, name="question"),

    # Some APIs without associated views
    path("logout", views.logout_view, name="logout")
]
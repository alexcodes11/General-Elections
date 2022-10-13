from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quotes/<int:quotes_id>", views.quotes, name="quotes")
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quotes/<int:quotes_id>", views.quotes, name="quotes"),
    path("state/<str:state_name>", views.state, name="state"),
    path("protransit/<str:state_name>", views.protransit, name="protransit")
]
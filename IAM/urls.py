from django.urls import path

from . import views

app_name = "iam"
urlpatterns = [
    path("register/", view=views.RegistrationView.as_view(), name="RegistrationView"),
    path("login/", view=views.Login.as_view(), name="LoginView"),
    path("users/", view= views.UserListView.as_view(), name="UserListView"),
]
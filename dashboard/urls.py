from django.urls import path

from . import views

app_name = "dashboard"
urlpatterns = [
    path("", view=views.PDFView.as_view(), name="PDFview"),
]
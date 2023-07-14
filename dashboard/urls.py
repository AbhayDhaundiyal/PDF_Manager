from django.urls import path

from . import views

app_name = "dashboard"
urlpatterns = [
    path("", view=views.PDFView.as_view(), name="PDFview"),
    path("file/<int:file_id>/", view=views.OpenPDFView.as_view(), name="OpenPDF"),
    path("file/<int:file_id>/<int:comment_id>/", view=views.CommentsView.as_view(), name="Comments"),
]
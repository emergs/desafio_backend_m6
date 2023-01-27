from django.urls import path
from .views import upload_file

urlpatterns = [
    path("file_parser/", upload_file, name="file_parser")
]

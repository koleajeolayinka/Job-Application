from django.urls import path
from uploadapp import views


urlpatterns = [
    path("image", views.upload_image, name="upload-image"),
    path("file", views.upload_file, name="upload-file")

]

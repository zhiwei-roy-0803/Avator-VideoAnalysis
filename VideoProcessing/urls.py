from django.urls import path
from .views import *

urlpatterns = [
    path("<str:username>/", index, name="home"),
    path("<str:username>/upload", upload, name="upload"),
    path("<str:username>/<str:filename>/show_original", show_original, name="original"),
    path("<str:username>/<str:filename>/show_processed", show_processed, name="result"),
    path("<str:username>/<str:filename>/start_processing", run, name="start"),
    path("<str:username>/<str:filename>/delete", destroy, name="delete")
]

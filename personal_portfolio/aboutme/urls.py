from django.urls import path
from . import views

urlpatterns = [
    path("", views.aboutme_index, name="aboutme_index"),
    path("<int:pk>/", views.aboutme_detail, name="aboutme_detail"),
]

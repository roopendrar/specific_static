from django.urls import path
from app4 import views
my_app="app4"

urlpatterns = [
    path('profile/',views.profile,name="profile"),
]

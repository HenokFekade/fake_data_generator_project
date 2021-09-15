from django.urls import path
from fake_data.views import post

urlpatterns = [
    path('fake-data', post),
]

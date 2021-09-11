from django.urls import path
from fake_data.views import GetFakeData, post

urlpatterns = [
    path('fake-data', post),
    # path('fake-data', GetFakeData.as_view())
]

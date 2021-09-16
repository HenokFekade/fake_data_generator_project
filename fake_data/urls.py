from django.urls import path
from fake_data.views import post_without_saving, post_with_auto_save

urlpatterns = [
    path('fake-data', post_without_saving),
    path('fake-data-auto-save', post_with_auto_save),
]

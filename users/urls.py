from django.urls import path

from users.views import register_user, login, logout


urlpatterns = [
    path('registor', register_user),
    path('login', login),
    path('logout', logout),
]

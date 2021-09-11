from django.apps import AppConfig


class CustomizeUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

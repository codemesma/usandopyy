from django.apps import AppConfig


class User_enConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_en'

    def ready(self):
        import users_en.signals  # noqa

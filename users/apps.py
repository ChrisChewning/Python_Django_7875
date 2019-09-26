from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #import the signals to the UsersConfig class.
    def ready(self):
        import users.signals
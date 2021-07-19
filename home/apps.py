from django.apps import AppConfig
from django.contrib.auth import get_user_model


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'


def ready():
    User = get_user_model()
    if User.objects.exists():
        return
    User.objects.create_superuser(username='admin', password='admin@123', email='admin@admin.com')

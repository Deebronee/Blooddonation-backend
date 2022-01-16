from django.apps import AppConfig
# configering the app

class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rest_api'

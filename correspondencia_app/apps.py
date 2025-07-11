from django.apps import AppConfig

class CorrespondenciaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'correspondencia_app'

    def ready(self):
        import correspondencia_app.signals

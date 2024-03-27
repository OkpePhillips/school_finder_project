from django.apps import AppConfig


class SchFinderApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sch_finder_api'

    def ready(self):
        import sch_finder_api.signals
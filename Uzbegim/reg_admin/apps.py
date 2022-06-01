from django.apps import AppConfig


class RegAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reg_admin'
    verbose_name = "Ресепшен"
    def ready(self):
        import reg_admin.signals
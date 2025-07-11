from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from correspondencia_app.models import EntradaCorrespondencia, SalidaCorrespondencia, Gestor


class Command(BaseCommand):
    help = 'Crear roles de usuario y asignar permisos'

    def handle(self, *args, **kwargs):
        # Crear grupo para administradores
        admin_group, _ = Group.objects.get_or_create(name='Administrador')
        admin_permissions = Permission.objects.all()
        admin_group.permissions.set(admin_permissions)

        # Crear grupo para editores (pueden ver, agregar y modificar, pero no eliminar)
        editor_group, _ = Group.objects.get_or_create(name='Editor')

        # Obtener permisos de modelos específicos
        models = [EntradaCorrespondencia, SalidaCorrespondencia, Gestor]
        editor_permissions = []
        for model in models:
            content_type = ContentType.objects.get_for_model(model)
            perms = Permission.objects.filter(content_type=content_type).exclude(codename__startswith='delete')
            editor_permissions.extend(perms)

        editor_group.permissions.set(editor_permissions)

        # Crear grupo para solo lectura
        viewer_group, _ = Group.objects.get_or_create(name='Visualizador')
        viewer_permissions = []
        for model in models:
            content_type = ContentType.objects.get_for_model(model)
            perms = Permission.objects.filter(content_type=content_type, codename__startswith='view')
            viewer_permissions.extend(perms)

        viewer_group.permissions.set(viewer_permissions)

        self.stdout.write(self.style.SUCCESS('✅ Roles creados y permisos asignados correctamente.'))

from django.db import models

class DocumentManager(models.Model):
    nombre    = models.CharField(max_length=100, blank=False)
    email     = models.EmailField(blank=False)
    telefono  = models.CharField(max_length=20, blank=False)
    archivo   = models.FileField(upload_to='gestores/', blank=True, null=True)

    class Meta:
        verbose_name        = "Gestor de Documentos"
        verbose_name_plural = "Gestores de Documentos"

    def __str__(self):
        return self.nombre

from django.db import models

class EntradaCorrespondencia(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_recepcion = models.DateField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_destino = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='archivos_entrada/', null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"

class SalidaCorrespondencia(models.Model):
    numero_documento = models.CharField(max_length=100)
    fecha_envio = models.DateField()
    remitente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    asunto = models.TextField()
    departamento_origen = models.CharField(max_length=255)  # Este campo debe existir
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='salidas/', null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.numero_documento

class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

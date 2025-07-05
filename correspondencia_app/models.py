from django.db import models
from django.contrib.auth.models import User

class Entrada(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_recepcion = models.DateField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_destino = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='entradas/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.numero_documento


class Salida(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_envio = models.DateField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_origen = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='salidas/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.numero_documento


class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, default="Sin cargo")
    correo = models.EmailField(default="sin@correo.com")
    telefono = models.CharField(max_length=20, default="0000-0000")

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100, default="Sin departamento")

    def __str__(self):
        return self.user.username

# correspondencia_app/models.py
from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    def __str__(self):
        return self.nombre

class CorrespondenciaEntrada(models.Model):
    numero_documento = models.CharField(max_length=50)
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    fecha_recepcion = models.DateField()
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='adjuntos/', blank=True)
    observaciones = models.TextField(blank=True)
    departamento_destino = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    gestor = models.ForeignKey(Gestor, on_delete=models.SET_NULL, null=True, blank=True)

class CorrespondenciaSalida(models.Model):
    numero_documento = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=100)
    fecha_envio = models.DateField()
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='adjuntos/', blank=True)
    observaciones = models.TextField(blank=True)
    departamento_origen = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    gestor = models.ForeignKey(Gestor, on_delete=models.SET_NULL, null=True, blank=True)

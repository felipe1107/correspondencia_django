from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class CorrespondenciaEntrada(models.Model):
    numero_documento = models.CharField(max_length=100)
    fecha_recepcion = models.DateField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.CharField(max_length=200)
    departamento_destino = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='archivos/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.asunto

class CorrespondenciaSalida(models.Model):
    numero_documento = models.CharField(max_length=100)
    fecha_envio = models.DateField()
    destinatario = models.CharField(max_length=100)
    asunto = models.CharField(max_length=200)
    departamento_destino = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='archivos/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.asunto

from django.db import models

class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class CorrespondenciaEntrada(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_recepcion = models.DateField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_destino = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='archivos_entrada/', blank=True, null=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"

class CorrespondenciaSalida(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_envio = models.DateField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_origen = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='archivos_salida/', blank=True, null=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"

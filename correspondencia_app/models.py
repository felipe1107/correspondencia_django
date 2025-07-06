from django.db import models

# Modelo: Gestor
class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

# Modelo: CorrespondenciaEntrada
class CorrespondenciaEntrada(models.Model):
    numero_documento = models.CharField(max_length=100)
    fecha_recepcion = models.DateField()
    remitente = models.CharField(max_length=200)
    destinatario = models.CharField(max_length=200)
    asunto = models.TextField()
    departamento_destino = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='entradas/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"

# Modelo: CorrespondenciaSalida
class CorrespondenciaSalida(models.Model):
    numero_documento = models.CharField(max_length=100)
    fecha_envio = models.DateField()
    remitente = models.CharField(max_length=200)
    destinatario = models.CharField(max_length=200)
    asunto = models.TextField()
    departamento_origen = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='salidas/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"

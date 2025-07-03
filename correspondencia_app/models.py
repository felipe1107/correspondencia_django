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
    numero_documento = models.CharField(max_length=50)
    fecha_recepcion = models.DateField()
    remitente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    asunto = models.TextField()
    departamento_destino = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='entradas/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"


class CorrespondenciaSalida(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_envio = models.DateField()
    remitente = models.CharField(max_length=255, blank=True, null=True)  # ← Temporalmente opcional
    destinatario = models.CharField(max_length=255)
    asunto = models.TextField()
    departamento_origen = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='salidas/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.destinatario}"

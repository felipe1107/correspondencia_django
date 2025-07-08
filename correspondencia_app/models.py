from django.db import models

# Modelo de Entradas de Correspondencia
class EntradaCorrespondencia(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_recepcion = models.DateField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_destino = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
    ])
    archivo_adjunto = models.FileField(upload_to='entradas_adjuntos/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"


# Modelo de Salidas de Correspondencia
class SalidaCorrespondencia(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_envio = models.DateField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    medio_envio = models.CharField(max_length=50, choices=[
        ('correo', 'Correo'),
        ('mensajero', 'Mensajero'),
        ('otro', 'Otro'),
    ])
    archivo_adjunto = models.FileField(upload_to='salidas_adjuntos/', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"


# Modelo de Gestores
class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

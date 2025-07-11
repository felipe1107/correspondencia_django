from django.db import models
from django.utils import timezone

# Función para generar número de documento automático
def generar_numero_documento(modelo):
    ultimo = modelo.objects.order_by('-id').first()
    if not ultimo:
        return 'DOC-0001'
    ultimo_numero = int(ultimo.numero_documento.split('-')[-1])
    return f'DOC-{ultimo_numero + 1:04d}'

class EntradaCorrespondencia(models.Model):
    numero_documento = models.CharField(max_length=20, unique=True, editable=False)
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_destino = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='archivos_entrada/', blank=True, null=True)
    observaciones = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.numero_documento:
            self.numero_documento = generar_numero_documento(EntradaCorrespondencia)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero_documento

class SalidaCorrespondencia(models.Model):
    numero_documento = models.CharField(max_length=20, unique=True, editable=False)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_origen = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='archivos_salida/', blank=True, null=True)
    observaciones = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.numero_documento:
            self.numero_documento = generar_numero_documento(SalidaCorrespondencia)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero_documento

class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    departamento = models.CharField(max_length=100)  # Nuevo campo
    cargo = models.CharField(max_length=100)         # Nuevo campo
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre



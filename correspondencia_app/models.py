from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
class Gestor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class CorrespondenciaEntrada(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_recepcion = models.DateField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_destino = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='archivos_entrada/', null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"

class CorrespondenciaSalida(models.Model):
    numero_documento = models.CharField(max_length=50)
    fecha_envio = models.DateField()
    destinatario = models.CharField(max_length=100)
    remitente = models.CharField(max_length=100)
    asunto = models.TextField()
    departamento_origen = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    archivo_adjunto = models.FileField(upload_to='archivos_salida/', null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"

class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

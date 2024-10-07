from django.db import models

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    licencia = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='conductores/', null=True, blank=True)  # Nuevo campo

    def __str__(self):
        return self.nombre

class Infraccion(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class Papeleta(models.Model):
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    infraccion = models.ForeignKey(Infraccion, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f'Papeleta {self.id} - {self.conductor.nombre}'

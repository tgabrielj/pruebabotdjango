from django.db import models

# Create your models here.

class Students(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.student_name
    
class Escaneador(models.Model):
    en_ejecucion = models.BooleanField(default=False)
    estrategia = models.CharField(max_length=100)

    def get_estrategia(self):
        return self.estrategia
    
    def active(self):
        return self.filter(en_ejecucion=True)
    
    def __str__(self):
        return self.estrategia
    
class Operacion(models.Model):
    id_escaneador = models.IntegerField()
    nombre_estrategia = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    precio_entrada = models.CharField(max_length=100)
    movimiento = models.CharField(max_length=100)

    def __str__(self):
        return self.fecha + ' - ' + self.precio_entrada + ' - by ' + self.nombre_estrategia

    def get_estrategia(self):
        return self.estrategia
    

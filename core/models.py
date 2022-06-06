from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria

class Persona(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, verbose_name='Apellido')
    coreo = models.CharField(max_length=40,  verbose_name='Correo')
    telefono = models.CharField(max_length=15, verbose_name='Numero')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')

    def __str__(self):
        return self.nombre
    

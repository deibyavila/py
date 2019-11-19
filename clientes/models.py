from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tercero(models.Model):
    
    #user =  models.OneToOneField(User, on_delete=models.CASCADE)
    nit = models.BigIntegerField(null=False)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email =  models.CharField(max_length=100, null=False)
    fecha_nacimiento = models.DateField(blank=True , null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(null=False)
    sexo = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino'),('N/A', 'No Aplica')))
    #tipo_documento =  models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='static/tercero', blank=True)

    def __str__(self):
        return '%s %s %s %s' % (self.nit ,'-', self.primer_nombre, self.primer_apellido)
        
class Tipo_Documento(models.Model):
     descripcion = models.CharField(max_length=100)

class TiposTercero(models.Model):
    codigo = models.CharField(max_length=2, null=False)
    descripcion = models.CharField(max_length=100, null=False)

class PerfilesContables(models.Model):
    descripcion = models.CharField(max_length=100, null=False)
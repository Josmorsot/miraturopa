from django.db import models
from django.contrib.auth.models import User
import md5


class Usuario(User):
    nombre= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=100)
    fechaNacimiento=models.DateTimeField()
    sexo=models.CharField(max_length=1,choices=(('H','Hombre'),('M','Mujer'),))
    random=md5.new(str(nombre)).hexdigest()
    profile=models.FileField(upload_to='profile/'+random)
    
    def __unicode__(self):
        return self.email
    
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre
    
class Color(models.Model):
    tono=models.CharField(max_length=50)
    def __unicode__(self):
        return self.tono

class Talla(models.Model):
    valor=models.CharField(max_length=5)
    def __unicode__(self):
        return self.valor
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion= models.CharField(max_length=150)
    precio=models.DecimalField(max_digits=6,decimal_places=2)
    imagen=models.FileField(upload_to='items')
    meGusta=models.ManyToManyField(Usuario,related_name='like',blank=True,null=True,)
    click=models.ManyToManyField(Usuario,related_name='click',blank=True,null=True,)
    categoria=models.ForeignKey(Categoria)
    color=models.ManyToManyField(Color)
    talla=models.ManyToManyField(Talla)
    sexo=models.CharField(max_length=1,choices=(('H','Hombre'),('M','Mujer'),))
    url=models.CharField(max_length=300)
    tienda=models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre
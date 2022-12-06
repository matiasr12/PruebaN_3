from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.CharField(max_length=40)
    curso_asignado=(models.CharField(max_length=20))
    fechaInicio=models.DateField(max_length=40)
    fechatermino=models.DateField(max_length=10)
    saldo=models.CharField(max_length=40)
    rut=models.CharField(max_length=40)

    def __str__(self):
        return  self.nombre
    
class Apoderado(models.Model):
    nombre=models.CharField(max_length=40)
    rut=models.CharField(max_length=20)
    edad=models.CharField(max_length=40)
    telefono=models.CharField(max_length=15)
    SegundoApoderado=models.CharField(max_length=40)
    telefono2=models.CharField(max_length=15)
    def __str__(self):
        return  self.nombre
     

   

class Alumnos(models.Model):
    nombre=models.CharField(max_length=40)
    rut=models.CharField(max_length=20)
    edad=models.CharField(max_length=40)
    curso=models.CharField(max_length=40)
    telefono=models.CharField(max_length=15)
    correo=models.EmailField(max_length=40)
    profesor=models.ForeignKey(Profesor,on_delete=models.CASCADE)
    apoderado=models.ForeignKey(Apoderado,on_delete=models.CASCADE)



    
    
from django.db import models
import datetime
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField('Nombre', max_length=255)
    fecha_inicio = models.DateField('Fecha de inicio')
    fecha_fin = models.DateField('Fecha de fin', null=True, blank=True)
    created_at = models.DateTimeField('Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Vacuna'
        verbose_name_plural = 'Vacunas'
    
    def __str__(self):
        return self.nombre

class Cupo(models.Model):
    cantidad = models.IntegerField('Cantidad')
    created_at = models.DateTimeField('Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Cupo'
        verbose_name_plural = 'Cupos'
    
    def __str__(self):
        return str(self.cantidad)

class Hora(models.Model):
    hora = models.TimeField('Hora')
    cupos = models.ForeignKey(Cupo, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Hora'
        verbose_name_plural = 'Horas'
    
    def __str__(self):
        return str(self.hora)

class Dia(models.Model):
    dia = models.DateField('Día')
    horas = models.ManyToManyField(Hora)
    created_at = models.DateTimeField('Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name = 'Dia'
        verbose_name_plural = 'Dias'
    
    def __str__(self):
        return str(self.dia)

class Centro(models.Model):
    nombre = models.CharField('Centro', max_length=180)
    direccion = models.CharField('Dirección', max_length=200)
    dias = models.ManyToManyField(Dia)
    vacunas = models.ManyToManyField(Vacuna,)
    created_at = models.DateTimeField('Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Centro'
        verbose_name_plural = 'Centros'

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    centros = models.ForeignKey(Centro, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return str(self.user)

class Paciente(models.Model):
    nombre = models.CharField('nombres', max_length=100,  validators=[RegexValidator(r'\w', 'Formato incorreccto')])
    apellido_paterno = models.CharField('apellido paterno', max_length=100, validators=[RegexValidator(r'[a-z]', 'Formato incorreccto')] )
    apellido_materno = models.CharField('apellido materno', max_length=100,  validators=[RegexValidator(r'[a-z]', 'Formato incorreccto')])
    rut = models.CharField('Rut',max_length=8, validators=[RegexValidator(r'^[0-9]{7}', 'Formato incorrecto')] )
    dv = models.CharField('Dv', max_length=1, validators=[RegexValidator(r'[0-9kK]{1}', 'Formato incorrecto debe ser digito o K')])
    fecha_nac = models.DateField('fecha nacimiento')
    email = models.EmailField('email', max_length=250)
    celular = models.CharField('Celular',max_length=9, validators=[RegexValidator(r'[0-9]{9}', 'Formato debe ser: 9xxxxxxxx')])
    direccion = models.CharField('Dirección', max_length=255)
    created_at = models.DateTimeField('Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.nombre

class Inoculacion(models.Model):
    fecha = models.DateField('Fecha inoculación')
    pacientes = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    centros = models.ForeignKey(Centro, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Inoculacion'
        verbose_name_plural = 'Inoculaciones'

    def __str__(self):
        return str(self.fecha)

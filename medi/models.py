from django.db import models

# Create your models here.

class Medicamento(models.Model):
    medicamento = models.TextField(null=False,blank=False,unique=True)
    marca = models.TextField(null=False,blank=False)
    sustancia = models.TextField(null=False,blank=False)
    forma = models.TextField(null=False,blank=False)
    composicion = models.TextField(null=False,blank=False)
    indicaciones = models.TextField(null=False,blank=False)
    propiedades = models.TextField(null=False,blank=False)
    contraindicaciones = models.TextField(null=False,blank=False)
    restricciones = models.TextField(null=False,blank=False)
    reacciones = models.TextField(null=False,blank=False)
    interacciones = models.TextField(null=False,blank=False)
    hallazgos = models.TextField(null=False,blank=False)
    precauciones = models.TextField(null=False,blank=False)
    dosis = models.TextField(null=False,blank=False)
    manifestaciones = models.TextField(null=False,blank=False)
    presentacion = models.TextField(null=False,blank=False)
    
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['created_at']

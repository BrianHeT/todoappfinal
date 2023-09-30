from django.db import models

class Todo(models.Model) :
    titulo=models.CharField(max_length=120)
    descripcion=models.CharField(max_length=500)
    completado=models.BooleanField(default=False)
    actualizar=models.DateTimeField(auto_now=True)
    crear=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo


from django.db import models


class Client(models.Model):
    nombre_completo = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    nickname = models.CharField(max_length=300)
    company_short = models.CharField(max_length=300)
    adresse = models.CharField(max_length=300)
    email = models.EmailField()
    telephone = models.CharField(max_length=30)
    comment = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.nombre_completo


class Proyecto(models.Model):
    nombre = models.CharField(max_length=300)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    fecha_creacion = models.DateField()
    fecha_ejecucion = models.DateField()

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre_completo = models.CharField(max_length=300)
    nickname = models.CharField(max_length=300)
    adresse = models.CharField(max_length=300)
    email = models.EmailField()
    telephone = models.CharField(max_length=30)
    comment = models.CharField(max_length=500)
    sedcard = models.BooleanField(default=False)
    tipo = models.CharField(max_length=3, choices=(('mod', 'Modelo'), ('fot', 'Fotografo'), ('mak', 'Make Up'), ('sty', 'Styling'), ('rhh', 'Recursos Humanos'), ('otr', 'Styling')), default='mod')

    def __str__(self):
        return self.nombre_completo


class Afectacion(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateField()
    inicio = models.TimeField()
    termino = models.TimeField()

    def __str__(self):
        return self.persona.nombre_completo + ' - ' + self.proyecto.nombre

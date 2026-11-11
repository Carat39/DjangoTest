from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Band(models.Model):

    def __str__(self): #Pour l'interface admin et les affichages par défaut
        return f'{self.name}'

    class Genre(models.TextChoices): #Pour choisir dans une liste pour le champ genre
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices,default='HH', max_length=5)
    biography = models.fields.CharField(max_length=1000,default='')
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2027)],
    default=2000
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):

    class Type(models.TextChoices):
        RECORD = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISCELLANEOUS = 'M'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000, default= '')
    sold =models.fields.BooleanField(default = True)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(-2000000),MaxValueValidator(2026)],
        default=2012
    )
    type = models.fields.CharField(choices=Type.choices,default='R')
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL) #One to many




#python .\manage.py makemigrations
#python .\manage.py migrate
#python .\manage.py shell
# On peut créer des objet dans la bdd ici
#band = Band.objects.create(name='Foo Fighters')
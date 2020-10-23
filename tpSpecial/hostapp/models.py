from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings


# No se si poner reservation o booking,


class Property(models.Model):
    # settings.AUTH_USER_MODEL --> referencia al modelo User base de Django
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # verbose_name --> es el nombre con el que va a aparecer en el admin
    city = models.CharField(max_length=50, verbose_name="Ciudad")
    # https://docs.djangoproject.com/en/1.10/ref/validators/
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    description = models.CharField(max_length=500, verbose_name="Descripcion de la Ficha")
    title = models.CharField(max_length=20, verbose_name="Titulo de la Ficha")
    max_persons = models.PositiveIntegerField(verbose_name="Maximo personas", default=1)
    bedrooms = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Dormitorios", default=1)
    beds = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Camas", default=1)
    bathrooms = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Baños", default=1)
    image = models.ImageField(null=True)
    # periodoFechasAlquiler(array)
    # servicios(array)
    # esto se llama choice, el primer dato sale en la bd, el segundo es con el que se trabaja (rezemos)
    CATEGORY_CHOICES = (
        ('HAB PRIV', 'Habitación Privada'),
        ('CA ENT', 'Casa Entera')
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

# https://gist.github.com/bradmontgomery/1c52b799c4ad274e0cbdd012a8b18f10 Discutir si esto es usable.


class Service(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True)


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    # periodoFechasAlquiler(array)

# TODO Falta agregar el array de fechas y de servicios, decidir tamaño de imagenes

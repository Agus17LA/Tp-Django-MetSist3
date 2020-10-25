from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField


class Property(models.Model):
    # settings.AUTH_USER_MODEL --> referencia al modelo User base de Django
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # verbose_name --> es el nombre con el que va a aparecer en el admin
    city = models.CharField(max_length=50, verbose_name="Ciudad")
    # https://docs.djangoproject.com/en/1.10/ref/validators/
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)], verbose_name="Precio por dia", help_text="Numeros enteros en lo posible")
    title = models.CharField(max_length=20, verbose_name="Titulo de la Ficha")
    description = models.CharField(max_length=500, verbose_name="Descripcion de la Ficha")
    max_persons = models.PositiveIntegerField(verbose_name="Maximo personas", default=1)
    bedrooms = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Dormitorios", default=1)
    beds = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Camas", default=1)
    bathrooms = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Baños", default=1)
    image = models.ImageField(null=True)
    # esto se llama choice, el primer dato se guarda en la bd, el segundo es el q se muestra en el admin al addear
    SERVICE_CHOICES = (
        ('Se admiten mascotas', 'Admiten mascotas'),
        ('Lugar de estacionamiento privado', 'Estacionamiento privado'),
        ('Internet', 'Internet'),
        ('Apto para familias y niños', 'Familias y niños')
    )
    # https://pypi.org/project/django-multiselectfield/
    services = MultiSelectField(choices=SERVICE_CHOICES, min_choices=1, default="No tiene servicios")
    CATEGORY_CHOICES = (
        ('HAB PRIV', 'Habitación Privada'),
        ('CA ENT', 'Casa Entera')
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)


class Reservation(models.Model):
    user = models.CharField(max_length=30, verbose_name="Usuario que reservó")
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])


class ReservationDate(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True)
    date = models.DateField(default="1998-7-27", null=True)
# TODO decidir el tamaño de las imagenes y ver q se tome el id del logeado en ADMIN para agregar propiedades
# TODO tmb falta ver como manejar exactamente las fechas


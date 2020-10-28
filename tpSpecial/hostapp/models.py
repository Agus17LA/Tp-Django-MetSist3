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
<<<<<<< Updated upstream
    # periodoFechasAlquiler(array)
    # servicios(array)
    # esto se llama choice, el primer dato sale en la bd, el segundo es con el que se trabaja (rezemos)
=======
    # esto se llama choice, el primer dato se guarda en la bd, el segundo es el q se muestra en el admin al addear
    SERVICE_CHOICES = (
        ('Se admiten mascotas', 'Admiten mascotas'),
        ('Lugar de estacionamiento privado', 'Estacionamiento privado'),
        ('Lugar de estacionamiento gratuito techado', 'Estacionamiento gratuito techado'),
        ('Lugar de estacionamiento gratuito a la calle', 'Estacionamiento gratuito a la calle'),
        ('Internet', 'Internet'),
        ('Apto para familias y niños', 'Familias y niños'),
        ('Televisor', 'Televisor'),
        ('Elementos basicos para la playa', 'Elementos de playa'),
        ('Lavarropas', 'Lavarropas'),
        ('Servicios básicos de higiene', 'Servicios básicos de higiene'),
        ('Agua caliente', 'Agua caliente'),
        ('Aire acondicionado', 'Aire acondicionado'),
        ('Calefacción', 'Calefacción'),
        ('Elementos de cocina basicos', 'Cocina basica'),
        ('Microondas', 'Microondas'),
        ('Desayuno incluido', 'Desayuno incluido'),
        ('Patio trasero', 'Patio trasero'),
        ('Patio delantero', 'Patio delantero'),
        ('Balcón', 'Balcón'),
        ('Parrilla', 'Parrilla'),
        ('Frente a la playa', 'Frente a la playa'),
        ('A pocas cuadras de la playa', 'Cercano a la playa'),
        ('Botiquin', 'Botiquin'),
        ('Alarma', 'Alarma'),
        ('Detector de humo', 'Detector de humo'),
        ('Detector de monoxido de carbono', 'Detector monoxido de carbono'),
        ('Barrio privado', 'Barrio privado')
    )
    # https://pypi.org/project/django-multiselectfield/
    services = MultiSelectField(choices=SERVICE_CHOICES, min_choices=1, default="No tiene servicios")
>>>>>>> Stashed changes
    CATEGORY_CHOICES = (
        ('Bungaló', 'Bungaló'),
        ('Cabaña', 'Cabaña'),
        ('Casa Comunal', 'Casa Comunal'),
        ('Casa de Huéspedes', 'Casa de Huéspedes'),
        ('Casa Entera', 'Casa Entera'),
        ('Chalé', 'Chalé'),
        ('Departamento', 'Departamento'),
        ('Duplex', 'Duplex'),
        ('Loft', 'Loft'),
        ('Mansión', 'Mansión'),
        ('Villa Residencial', 'Villa Residencial'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

# https://gist.github.com/bradmontgomery/1c52b799c4ad274e0cbdd012a8b18f10 Discutir si esto es usable.


class Service(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True)


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
<<<<<<< Updated upstream
    final_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    # periodoFechasAlquiler(array)
=======
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True)
    date = models.DateField(default="1998-7-27", null=True)
    code = models.CharField(null=True, max_length=50, verbose_name="El codigo de la reserva")
# TODO decidir el tamaño de las imagenes y ver q se tome el id del logeado en ADMIN para agregar propiedades
# TODO tmb falta ver como manejar exactamente las fechas
>>>>>>> Stashed changes

# TODO Falta agregar el array de fechas y de servicios, decidir tamaño de imagenes

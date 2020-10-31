from django.shortcuts import render
# Create your views here.
from .models import *
from django.http import HttpResponse
import datetime


def index(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, "index.hmtl", context)


def homescreen(request):
    properties = Property.objects.all()
    cities = City.objects.all()
    
    return render(request, template_name="index.html", context={'properties' : properties, 'cities' : cities})

# lista basica y generica para ver todas las properties
def list_properties(request):
    properties = Property.objects.all()
    # ver bien como traer los services de una property (creo que esto esta mal)
    services = Property.objects.get.services
    return render(request, template_name="list_properties.html",
                  context={'properties': properties, 'services': services})


# pagina de la propiedad con todos los datos en display (se llega apretando el botón de 'Leer más'
# en la card de la propiedad en la homescreen)
def property_page(request):
    if request.GET["id_property"]:
        id_property = request.GET["id_property"]
        property_aux = Property.objects.get(id=id_property)
        return render(request, template_name="property_page.html", context={'property_aux': property_aux})


def success(request):
    return render(request, template_name="success.html")

def error(request):
    return render(request, template_name="error.html")

def reservation(request):
    if request.POST:
        # filtra por el id de propiedad que recibe por post, solo agarra los que no tiene id de reservacion, y ordena por fecha ascendente
        reservations_date_list = ReservationDate.objects.filter(property__id=request.POST["property_id"]).filter(
            reservation__id=None).order_by('date')
        # transformacion que nos ayuda mas adelante
        reservations_date_list = list(reservations_date_list)
        aux = []

        # copia a reser_date_list y la pasa a string para evitar problemas con datetime
        for x in reservations_date_list:
            aux.append(str(x))

        # separa en una lista al rango de fechas
        daterange_array = request.POST['daterange'].split(' - ')
        # transforma al formato de la base de datos
        initial_date = datetime.datetime.strptime(daterange_array[0], '%m/%d/%Y').strftime('%Y:%m:%d')
        final_date = datetime.datetime.strptime(daterange_array[1], '%m/%d/%Y').strftime('%Y:%m:%d')

        try:
            initial_index = aux.index(initial_date)
            final_index = aux.index(final_date)
            # si esta condicion no se cumple es porque hay "huecos" entre medio del rango de fechas
            if 1 + final_index - initial_index == request.POST['quantity-days']:
                return render(request, template_name="success.html")
                # meter codigo del save en la base de datos
            return render(request, template_name="error.html")
        except:
            return render(request, template_name="error.html")

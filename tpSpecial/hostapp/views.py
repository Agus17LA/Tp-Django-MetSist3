from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse


def index(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, "index.hmtl", context)


def homescreen(request):
    properties = Property.objects.all()
    list_categories = list(Property.CATEGORY_CHOICES)
    print(list_categories)
    return render(request, template_name="index.html", context={'properties' : properties, 'categories' : list_categories})

#lista basica y generica para ver todas las properties
def list_properties(request):
    properties = Property.objects.all()
    #ver bien como traer los services de una property (creo que esto esta mal)
    services = Property.objects.get.services
    return render(request, template_name="list_properties.html", context={'properties' : properties, 'services' : services})

#pagina de la propiedad con todos los datos en display (se llega apretando el botón de 'Leer más' 
# en la card de la propiedad en la homescreen)
def property_page(request):
    if request.GET["id_property"]:
        id_property = request.GET["id_property"]
        property_aux = Property.objects.get(id=id_property)
        return render(request, template_name="property_page.html", context={'property_aux': property_aux})


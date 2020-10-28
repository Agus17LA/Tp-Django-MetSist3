from django.shortcuts import render
from .models import *


def index(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, "index.hmtl", context)


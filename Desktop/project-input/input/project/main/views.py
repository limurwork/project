from django.shortcuts import render
from main.forms import Detalis,Marta

from . import models


def index(request):
    eror = ''

    if request.method == 'GET':
        forma = Marta(request.POST)
        if forma.is_valid():
            forma.save()
        else:
            eror = ''
    forma = Marta()
    datat = {
        'forma': forma,
        'erora': eror
    }


    if request.method == 'POST':
        form = Detalis(request.POST)
        if form.is_valid():
            form.save()

        else:
            eror = ''
    form = Detalis()
    data = {
        'form': form,
        'eror': eror
    }


    return render(request, "index.html", data)

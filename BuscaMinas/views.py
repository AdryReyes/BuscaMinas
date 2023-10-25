from django.shortcuts import render
from .forms import CreaTableroForm 

# Create your views here.

def indexed(request):
    return render(request, template_name='BuscaMinas/index.html', context={})

def crea_tablero(request):
    #si se ha enviado el formulario

    #tablero_form = CreaTableroForm()
    if request.method == 'GET':
        tablero_form = CreaTableroForm(request.GET)
        #Ejecutamos la validacion
        if tablero_form.is_valid():
            #Los datos se cogen del diccionario cleaned_data
            columnas = tablero_form.cleaned_data['columnas']
            filas = tablero_form.cleaned_data['filas']
            #Si se pide la pagina por primera vez
            return render(request, template_name='BuscaMinas/crea_tablero.html', context={'filas':filas, 'columas':columnas, 'rango_filas':range(filas), 'rango_columnas':range(columnas)})
        tablero_form = CreaTableroForm()
        return render(request, template_name='BuscaMinas/crea_tablero.html', context={'form':tablero_form})
    



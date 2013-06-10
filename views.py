# importamos librerias
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response

# genero la vista para el index
def index(request):
	cadena = "Hola, mi primera app."
	return HttpResponse(cadena)
# genero la vista post y tomo la variable id para saber el numero de post. EJ: post/2
def post(request, id):
	return HttpResponse("Este es el post %s" % id)

def hora_actual_OLD(request):
	ahora = datetime.now() # almaceno en ahora la hora hora_actual
	t = get_template('template1.html') # almaceno en t el nombre del template
	c = Context({'hora': ahora}) # genero el contexto mostrando la variable ahora
	html = t.render(c) # genero el render del template almacenado mostranto el contexto
	return HttpResponse(html)

def hora_actual(request):
	# shortcuts del def anterior hora_actual_OLD
	# defino el Template() y el Context()
	ahora = datetime.now()
	lugar = "Cordoba"
	return render_to_response('template1.html', {'hora': ahora,'lugar': lugar}) 
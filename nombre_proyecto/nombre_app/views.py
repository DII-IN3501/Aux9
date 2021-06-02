from nombre_app.models import Usuario
from django.shortcuts import render
from nombre_app.forms import Formulario, IniciarSesion

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'nombre_app/index.html')

def formulario(request):
    form = Formulario()
    return render(request, 'nombre_app/formulario.html', {'form': form})

def resultados(request):
    fname = request.POST['fname']
    lname = request.POST['lname']

    needs = []
    if 'need1' in request.POST: # OJO con los checkboxes
        needs.append("sueño")
    if 'need2' in request.POST:  # OJO con los checkboxes
        needs.append("hambre")
    if 'need3' in request.POST:  # OJO con los checkboxes
        needs.append("tristeza")

    nota = request.POST['nota']

    username = request.POST['username']
    password = request.POST ['password']
    user = User.objects.create_user(username=username, password=password)
    
    usuario = Usuario(user=user, fname=fname, lname=lname)
    usuario.save()
    
    #diccionario con las respuestas
    context = {}
    context['fname'] = fname
    context['lname'] = lname
    context['needs'] = needs
    context['nota'] = nota
    context['username'] = username

    return render(request, 'nombre_app/resultados.html', context)


def loginView(request):
    form = IniciarSesion()
    return render(request, 'nombre_app/login.html', {'form' : form})

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    usuario = authenticate(username=username, password=password)
    login(request, usuario)
    return render(request, 'nombre_app/index.html')    

def logoutView(request):
    logout(request)
    return render(request, 'nombre_app/index.html')


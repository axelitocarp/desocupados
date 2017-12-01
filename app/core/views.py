from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app.core.forms import RegistroDesocupado, RegistroEmpresa, ModificarEmpresa, ModificarDesocupado
from app.core.forms import RegistroDesocupado, RegistroEmpresa, JobForm
from django.contrib.auth.models import User
from app.core.models import *

@login_required
def home(request):
    user = request.user
    user.refresh_from_db()
    return render(request, 'home.html', {'user': user})

@login_required
def perfil(request):
    user = request.user
    user.refresh_from_db()
    return render(request, 'perfil.html', {'user': user})

def registro_desocupado(request):
    # Cuando algo llega a esta vista (llamada desde una URL) puede venir por dos
    # vias distintas. Como una petición GET (Se ingresó en la barra de direccion
    # del navegador la URL o se siguió un link a esa URL) o como POST (Se envió
    # un formulario a esa dirección). Por tanto tengo que procesar ambas
    # alternativas.
    if request.method == "GET":
        # Como es GET solo debo mostrar la página. Llamo a otra función que se
        # encargará de eso.
        return get_registro_desocupado_form(request)
    elif request.method == 'POST':
        # Como es POST debo procesar el formulario. Llamo a otra función que se
        # encargará de eso.
        return handle_registro_desocupado_form(request)

def get_registro_desocupado_form(request):
    form = RegistroDesocupado()
    return render(request, 'signup.html', {'form': form})

def handle_registro_desocupado_form(request):
    form = RegistroDesocupado(request.POST)
    # Cuando se crea un formulario a partir del request, ya se obtienen a traves
    # de este elemento los datos que el usuario ingresó. Como el formulario de
    # Django ya está vinculado a la entidad, entonces hacer form.save() ya crea
    # un elemento en la base de datos.
    if form.is_valid():
        # Primero hay que verificar si el formulario es válido, o sea, si los
        # datos ingresados son correctos. Sino se debe mostrar un error.
        form.save()
        # Si se registró correctamente, se lo envía a la pantalla de login
        return redirect('login')
    else:
        # Quedarse en la misma página y mostrar errores
        return render(request, 'signup.html', {'form': form})

def registro_empresa(request):
    if request.method == "GET":
        return get_registro_empresa_form(request)
    elif request.method == 'POST':
        return handle_registro_empresa_form(request)

def get_registro_empresa_form(request):
    form = RegistroEmpresa()
    return render(request, 'signup.html', {'form': form})

def handle_registro_empresa_form(request):
    form = RegistroEmpresa(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'signup.html', {'form': form})


def eliminar(request, user_id):
	User.objects.get(id=user_id).delete()
	return render(request, 'test.html', {'id': user_id})

@login_required
def editar(request):
    user = User.objects.get(id=request.user.id)
    if user.is_desocupado():
        form = ModificarDesocupado
        data = user.desocupado
    elif user.is_empresa():
        form = ModificarEmpresa
        data = user.empresa

    if request.method == "GET":
        return get_editar_form(request, form, data)
    elif request.method == 'POST':
        return handle_editar_form(request, form,data)

def get_editar_form(request,formName, data):
    form = formName(instance=data)
    return render(request, 'signup.html', {'form':form})

def handle_editar_form(request,formName, data):
    form = formName(request.POST, instance=data)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'signup.html', {'form':form})

# Estas son las que ya estaban, las comento porque con el cambio alguna cosa
# podría tener que cambiarse o adaptarse. Notece ademas el uso de login_required
# en el views en lugar de urls, los decorators de hecho son esas cosas que
# comienzan con @ y van arriba de la función

@login_required
def registro_trabajo(request):
    if request.method == "GET":
        return get_registro_trabajo_form(request)
    elif request.method == 'POST':
        return handle_registro_trabajo_form(request)

def get_registro_trabajo_form(request):
    form = JobForm()
    return render(request, 'jobs.html', {'form': form})

def handle_registro_trabajo_form(request):
    form = JobForm(request.POST)
    if form.is_valid():
        job = form.save(commit=False)
        job.empresa = request.user.empresa
        job.save()
        return redirect('home')
    else:
        return render(request, 'jobs.html', {'form': form})

def listar_trabajos(request):
    lista = Trabajo.objects.filter(empresa = request.user.empresa)
    return render(request, 'mis_trabajos_list.html', {'lista_trabajos': lista})

def listar_todos_trabajos(request):
    lista = Trabajo.objects.all()
    return render(request, 'mis_trabajos_list.html', {'lista_trabajos': lista})

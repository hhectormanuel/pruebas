from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import UsuarioForm
from .models import Usuario

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        form = UsuarioForm()
        usuarios = Usuario.objects.all()
        context = {
            'form' : form,
            'usuarios':usuarios,
        }
        return render(request, 'base.html', context)

    def post(self, request, *args, **kwargs):
        form = UsuarioForm()
        if request.method == "POST":
            form = UsuarioForm(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data.get('nombre')
                apellido = form.cleaned_data.get('apellido')
                edad = form.cleaned_data.get('edad')
                user = Usuario.objects.create(
                    nombre = nombre, apellido = apellido, edad = edad
                )
                user.save()
                return redirect('home:home')
        

        usuarios = Usuario.objects.all()
        context = {
            'form' : form,
            'usuarios':usuarios,
        }
        return render(request, 'base.html', context)

class UpdateUsuario(UpdateView):
    model = Usuario
    fields= ('__all__')
    template_name= 'update.html'
    object= 'usuario'
    success_url = '/'

class DeleteUsuario(DeleteView):
    model = Usuario
    template_name= 'delete.html'
    success_url = '/'

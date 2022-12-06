from django.shortcuts import render
from templatesApp.models import Profesor
from templatesApp.models import Alumnos
from templatesApp.models import Apoderado
from templatesApp.forms import FormAlumnos
from templatesApp.forms import FormProfesor
from templatesApp.forms import FormApoderado
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request,'index.html')


def Listado(request):
    profesor=Profesor.objects.all()
    data ={'profesor':profesor}
    return render(request,'profesores.html',data)


def Listado2(request):
    alumnos=Alumnos.objects.all()
    data={'alumnos':alumnos}
    return render(request,'alumnos.html',data)

def Listado3(request):
    apoderado=Apoderado.objects.all()
    data={'apoderado':apoderado}
    return render(request,'apoderado.html',data)

def agregarAlumno(request):
    form =FormAlumnos()
    if request.method =='POST':
        form = FormAlumnos(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'agregarProyecto.html',data)

def agregarProfesor(request):
    form = FormProfesor()
    if request.method =='POST':
        form = FormProfesor(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    Data={'form':form}
    return render(request,'agregarProfesor.html',Data)

def agregarApoderado(request):
    form = FormApoderado()
    if request.method =='POST':
        form = FormApoderado(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    Data={'form':form}
    return render(request,'agregarApoderado.html',Data)

def elinarProyecto(request,rut):
    alumnos=Alumnos.objects.get(rut=rut)
    alumnos.delete()
    return redirect('/alumnos')

def elinarApoderado(request,rut):
    apoderado=Apoderado.objects.get(rut=rut)
    apoderado.delete()
    return redirect('/apoderado')

def elinarProfesor(request,rut):
    profesor=Profesor.objects.get(rut=rut)
    profesor.delete()
    return redirect('/profesores')

def actualizarProyecto(request,rut):
     alumnos=Alumnos.objects.get(rut=rut)
     form=FormAlumnos(instance=alumnos)
     if request.method =='POST':
         form = FormAlumnos(request.POST,instance=alumnos)
         if form.is_valid():
             form.save()
         return index(request)
     data={'form':form}
     return render(request,'agregarProyecto.html',data)



def actualizarProfesor(request,rut):
     profesor=Profesor.objects.get(rut=rut)
     form=FormProfesor(instance=profesor)
     if request.method =='POST':
         form = FormProfesor(request.POST,instance=profesor)
         if form.is_valid():
             form.save()
         return index(request)
     data={'form':form}
     return render(request,'agregarProfesor.html',data)



def actualizarApoderado(request,rut):
     apoderado=Apoderado.objects.get(rut=rut)
     form=FormApoderado(instance=apoderado)
     if request.method =='POST':
         form = FormApoderado(request.POST,instance=apoderado)
         if form.is_valid():
             form.save()
         return index(request)
     data={'form':form}
     return render(request,'agregarApoderado.html',data)




"""templatesDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from templatesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('profesores/',views.Listado),
    path('alumnos/',views.Listado2),
    path('apoderado/',views.Listado3),
    path('agregarProyecto/',views.agregarAlumno),
    path('agregarProfesor/',views.agregarProfesor),
    path('agregarApoderado/',views.agregarApoderado),
    path('elinarProyecto/<rut>',views.elinarProyecto),
    path('elinarApoderado/<rut>',views.elinarApoderado),
    path('elinarProfesores/<rut>',views.elinarProfesor),
    path('actualizarProyecto/<rut>',views.actualizarProyecto),
    path('actualizarProfesor/<rut>',views.actualizarProfesor),
     path('actualizarApoderado/<rut>',views.actualizarApoderado),


    
]
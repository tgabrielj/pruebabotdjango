"""botrading URL Configuration

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
from escaneador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('escanear/', views.escanear, name='escanear'),
    path('escaneadores/', views.escaneadores, name='escaneadores'),
    path('escaneadores/activar/<int:escaneador_id>/', views.escaneador_activar, name = 'escaneador_activar' ),
    path('escaneadores/ver_operaciones/<int:escaneador_id>/', views.ver_operaciones, name = 'ver_operaciones' ),
    path('escaneadores/desactivar/<int:escaneador_id>/', views.escaneador_desactivar, name = 'escaneador_desactivar' ),
]

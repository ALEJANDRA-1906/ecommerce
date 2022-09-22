"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from venta.views import inicio,articulo,cliente,crearCliente,venta,planCuenta,tipocuenta,crearTipodecuentas,cuentas, niveles , crearNiveles, crearCuenta, activos_fijos,listadeactivosf, crearActivo_fijo,departamentos , añadir_Departa , tipCategoria , añadir_Categoria

from django.conf.urls.static import static
from ecommerce import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('articulo/', articulo, name='articulo'),
    path('cliente/', cliente, name='cliente'),
    path('crearcliente/', crearCliente, name='crearcliente'),
    path('venta/', venta, name='venta'),
    path('planCuenta/', planCuenta, name='planCuenta'),
    path('cuentas/', cuentas, name='cuentas'),
    path('crearcuenta/', crearCuenta, name='crearcuenta'),
    path('niveles/', niveles, name='niveles'),
    path('crearnivel/', crearNiveles, name='crearnivel'),
    path('tipocuenta/', tipocuenta, name='tipocuenta'),
    path('creartipodecuenta/', crearTipodecuentas, name='creartipodecuenta'),
    path('activos_fijos/', activos_fijos, name='activos_fijos'),
    path('listadeactivosf/', listadeactivosf,name='listadeactivosf'),
    path('crearac_fijos/', crearActivo_fijo, name='crearac_fijos'),
    path('departamentos/', departamentos, name='departamentos'),
    path('añadir_departa/', añadir_Departa, name='añadir_departa'),
    path('tipcategoria/', tipCategoria,name='tipcategoria'),
    path('añadir_categoria/', añadir_Categoria, name='añadir_categoria'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

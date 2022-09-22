from django.shortcuts import HttpResponse
from django.shortcuts import render

html_base = """
 <h1>Shopping Car</h1>
 <ul>
   <li><a href="/">Inicio</a></li>
   <li><a href="/articulo/">Articulos</a></li>
   <li><a href="/cliente/">Clientes</a></li>
   <li><a href="/venta/">Ventas</a></li>
   <li><a href="/consulta/">Consultas</a></li>
   <li><a href="/planCuenta/">Plan de Cuentas</a></li>
   <li><a href="/activos_fijos/">Activos Fijos</a></li>
 </li>
"""


def inicio(request):
    data = {
        'titulo': "Inicio"
    }
    return render(request, 'base.html', data)


def articulo(request):
    return HttpResponse(html_base +
                        """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")


def cliente(request):
    data = {
        'titulo': 'GESTION DE CLIENTESssss',
        'crear_url': '/crearcliente',
        'listar_url': '/cliente',
    }
    return render(request, "ventas/clientes/listCliente.html", data)


def crearCliente(request):
    data = {
        'titulo': 'MANTENIMIENTO DE CLIENTES',
        'crear_url': '/crearcliente',
        'action': 'add',
        'listar_url': '/cliente',
    }
    return render(request, "ventas/clientes/formCliente.html", data)


def venta(request):
    data = {
        'titulo': "Inicio"
    }
    return render(request, "ventas/ventas.html", data)


def planCuenta(request):
    data = {
        'titulo': "Inicio"
    }
    return render(request, "planCuentas/planCuentas.html", data)


def tipocuenta(request):
    data = {
        'titulo': "CUENTAS CONTABLES ",
        'crearT_url': '/creartipodecuenta',
        'listarT_url': '/tipocuenta',

    }
    return render(request, "planCuentas/tipodeCuenta/tipoCuenta.html", data)


def crearTipodecuentas(request):
    data = {
        'titulo': 'CLASIFICACION DE CUENTAS CONTABLES',
        'crearT_url': '/creartipodecuenta',
        'action': 'add',
        'listarT_url': '/tipocuenta',
    }
    return render(request, "planCuentas/tipodeCuenta/nuevaTipocuenta.html", data)


def niveles(request):
    data = {
        'titulo': "NIVELES DE PLAN DE CUENTAS",
        'crearN_url': '/crearnivel',
        'listarN_url': '/niveles',
    }
    return render(request, "planCuentas/Nivel/nivel.html", data)


def crearNiveles(request):
    data = {
        'titulo': 'ADMINISTACION DE NIVELES',
        'crearN_url': '/crearnivel',
        'action': 'add',
        'listarN_url': '/niveles',
    }
    return render(request, "planCuentas/Nivel/nuevoNivel.html", data)


def cuentas(request):
    data = {
        'titulo': 'GESTION DE CUENTAS',
        'crearP_url': '/crearcuenta',
        'listarP_url': '/cuentas',
    }
    return render(request, "planCuentas/Cuentas/cuentasP.html", data)


def crearCuenta(request):
    data = {
        'titulo': 'ADMINISTRACION DE CUENTAS CONTABLES',
        'crearP_url': '/crearcuenta',
        'action': 'add',
        'listarP_url': '/cuentas',
    }
    return render(request, "planCuentas/Cuentas/nuevaCuenta.html", data)


def activos_fijos(request):
    data = {
        'titulo': "Inicio"
    }
    return render(request, "activos fijos/Activos_fijos.html", data)


def listadeactivosf(request):
    data = {
        'titulo': "ACTIVOS FIJOS",
        'crearA_url': '/crearac_fijos',
        'listarA_url': '/listadeactivosf',

    }
    return render(request, "activos fijos/Ac_fijos/activos_F.html", data)


def crearActivo_fijo(request):
    data = {
        'titulo': 'ADMINISTRACION DE ACTIVOS FIJOS',
        'crearA_url': '/crearac_fijos',
        'action': 'add',
        'listarA_url': '/listadeactivosf',
    }
    return render(request, "activos fijos/Ac_fijos/nuevo_Activofijo.html", data)

def departamentos(request):
    data = {
        'titulo': "DEPARTAMENTO",
        'crearD_url': '/añadir_departa',
        'listarD_url': '/departamentos',

    }
    return render(request, "activos fijos/departamento/lis_depart.html", data)

def añadir_Departa(request):
    data = {
        'titulo': "DEPARTAMENTO",
        'crearD_url': '/añadir_departa',
        'action': 'add',
        'listarD_url': '/departamentos',

    }
    return render(request, "activos fijos/departamento/añadir_dep.html", data)

def tipCategoria(request):
    data = {
        'titulo': "CATEGORIAS",
        'crearC_url': '/añadir_categoria',
        'listarC_url': '/tipcategoria',

    }
    return render(request, "activos fijos/Categorias/categorias.html", data)

def añadir_Categoria(request):
    data = {
        'titulo': "CATEGORIA",
        'crearC_url': '/añadir_categoria',
        'action': 'add',
        'listarC_url': '/tipcategoria',

    }
    return render(request, "activos fijos/Categorias/añadir_Cat.html", data)





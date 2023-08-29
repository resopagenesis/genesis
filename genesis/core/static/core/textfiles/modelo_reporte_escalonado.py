def Reporte@modeloView(request):

    # Variables del proyecto para el reporte
    primeralinea = @primeralinea
    maxlineas = @maxlineas

    numeroLineas = 0
    salto = 0
    pagina = 1
    
    # Lista de transferencia
    datos_detalle = []

    # Variables de reporte
    datos_reporte = []
    datos_reporte.append(numeroLineas)
    datos_reporte.append(salto)
    datos_reporte.append(pagina)
    datos_reporte.append(maxlineas)

    # Control de titulos por modelos
@controltitulos

@totales

@recorrido

    plan = Reporte("@modelo.pdf",@size,'@orientacion',datos_detalle)
    plan.detalle()
    plan.grabar()
    return HttpResponseRedirect('/@aplicacion/listar_@modelo')

 

import os
import re
from re import A
import shutil
from .models import ErroresCreacion
from personalizacion.models import Personaliza
from proyectos.models import Seccion as secp, Fila as filap, Columna as colp
from modelos.models import Seccion as secm, Fila as filam, Columna as colm
from principal.models import Seccion as secpr, Fila as filapr, Columna as colpr
from propiedades.models import Propiedad
from modelos.models import Modelo, ZonaReporte, ReporteAdHocObjeto
from proyectos.models import Proyecto, DespliegaArbol
from aplicaciones.models import Aplicacion
import json, pickle

def CrearSeccionPrincipal(proyecto):
    seccion = secpr()
    seccion.nombre = 'S1'
    seccion.proyecto = proyecto
    seccion.borde = True
    seccion.altura = '1000px'
    seccion.save()

    fila = filapr()
    fila.nombre = 'S1F1'
    fila.seccion = seccion
    fila.altura = '150px'
    fila.color1 = 'white'
    fila.color2 = 'white'
    fila.borde = False
    fila.save()

    columna = colpr()
    columna.nombre = 'C1F1S1'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 2
    columna.save()

    columna = colpr()
    columna.nombre = 'C2F1S1'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 8
    columna.justificacionhorizontaltexto = 'center'
    columna.justificacionverticaltexto = 'center'
    columna.fonttexto = 'Lugrasimo,18,700'
    columna.textocolumna = 'Nombre de la aplicacion'
    columna.save()

    columna = colpr()
    columna.nombre = 'C3F1S1'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 2
    columna.save()

    fila = filapr()
    fila.nombre = 'S1F2'
    fila.seccion = seccion
    fila.altura = '700px'
    fila.color1 = 'white'
    fila.color2 = 'white'
    fila.borde = False
    fila.save()

    columna = colpr()
    columna.nombre = 'C1F2S1'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 1
    columna.save()

    columna = colpr()
    columna.nombre = 'C2F2S1'
    columna.fila = fila
    columna.color1 = '#f1f1f1'
    columna.color2 = '#f1f1f1'
    seccion.degradado = 'right' 
    columna.borde = False
    columna.ingresosistema = True
    columna.secciones = 6
    columna.margeninterno = '0px,0px,0px,20px'
    columna.dimensionesimagen = '80%,40%'
    columna.imagen = 'main/sistemas_uf1pv4C.jpeg'
    columna.save()

    columna = colpr()
    columna.nombre = 'C3F2S1'
    columna.fila = fila
    columna.textocolumna = 'Ingresar al sistema'
    columna.color1 = '#f1f1f1'
    columna.color2 = '#f1f1f1'
    seccion.degradado = 'right' 
    columna.borde = False
    columna.ingresosistema = True
    columna.fonttexto = 'Roboto,14,500'
    columna.secciones = 4
    columna.save()

    columna = colpr()
    columna.nombre = 'C4F2S1'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 1
    columna.save()

    seccion = secpr()
    seccion.nombre = 'S2'
    seccion.proyecto = proyecto
    seccion.borde = True
    seccion.altura = '1000px'
    seccion.save()

    fila = filapr()
    fila.nombre = 'S2F1'
    fila.seccion = seccion
    fila.altura = '20px'
    fila.color1 = 'white'
    fila.color2 = 'white'
    fila.borde = False
    fila.save()

    fila = filapr()
    fila.nombre = 'S2F2'
    fila.seccion = seccion
    fila.altura = '300px'
    fila.color1 = 'white'
    fila.color2 = 'white'
    fila.borde = False
    fila.save()

    columna = colpr()
    columna.nombre = 'C1F2S2'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 4
    columna.borde = True
    columna.margeninterno = '0px,0px,0px,20px'
    columna.save()

    columna = colpr()
    columna.nombre = 'C2F2S2'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 3
    columna.borde = True
    columna.margeninterno = '0px,0px,0px,20px'
    columna.save()

    columna = colpr()
    columna.nombre = 'C3F2S2'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 4
    columna.borde = True
    columna.margeninterno = '0px,0px,0px,20px'
    columna.save()

    fila = filapr()
    fila.nombre = 'S2F3'
    fila.seccion = seccion
    fila.altura = '20px'
    fila.color1 = 'white'
    fila.color2 = 'white'
    fila.borde = False
    fila.save()

    fila = filapr()
    fila.nombre = 'S2F4'
    fila.seccion = seccion
    fila.altura = '300px'
    fila.color1 = 'white'
    fila.color2 = 'white'
    fila.borde = False
    fila.save()

    columna = colpr()
    columna.nombre = 'C1F4S2'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 4
    columna.borde = True
    columna.margeninterno = '0px,0px,0px,20px'
    columna.save()

    columna = colpr()
    columna.nombre = 'C2F4S2'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 3
    columna.borde = True
    columna.margeninterno = '0px,0px,0px,20px'
    columna.save()

    columna = colpr()
    columna.nombre = 'C3F4S2'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 4
    columna.borde = True
    columna.margeninterno = '0px,0px,0px,20px'
    columna.save()

    fila = filapr()
    fila.nombre = 'S2F5'
    fila.seccion = seccion
    fila.altura = '20px'
    fila.color1 = 'white'
    fila.color2 = 'white'
    fila.borde = False
    fila.save()

    fila = filapr()
    fila.nombre = 'S2F6'
    fila.seccion = seccion
    fila.altura = '300px'
    fila.color1 = 'white'
    fila.color2 = 'white'
    fila.borde = False
    fila.save()

    columna = colpr()
    columna.nombre = 'C1F6S2'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 4
    columna.borde = True
    columna.margeninterno = '0px,0px,0px,20px'
    columna.save()

    columna = colpr()
    columna.nombre = 'C2F6S2'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 3
    columna.borde = True
    columna.margeninterno = '0px,0px,0px,20px'
    columna.save()

    columna = colpr()
    columna.nombre = 'C3F6S2'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 4
    columna.borde = True
    columna.margeninterno = '0px,0px,0px,20px'
    columna.save()

def CrearSeccionProyecto(modelo,proyecto):

    if modelo == None:
        seccion = secp()
        seccion.proyecto = proyecto
    else:
        seccion = secm()
        seccion.modelo = modelo
    seccion.nombre = 'S1'
    seccion.borde = False
    seccion.altura = '1000px'
    seccion.save()

    # fila logo titulo

    if modelo == None:
        fila = filap()
    else:
        fila = filam()
    fila.nombre = 'logo_titulo'
    fila.seccion = seccion
    fila.altura = '120px'
    fila.color1 = '#005187'
    fila.color2 = '#005187'
    fila.borde = False
    fila.save()

    # columna logo

    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'logo'
    columna.fila = fila
    columna.borde = False
    columna.color1 = '#005187'
    columna.color2 = '#005187'
    columna.justificacionhorizontaltexto = 'center'
    columna.justificacionverticaltexto = 'center'
    columna.secciones = 4
    columna.funcion = 'l'
    columna.save()

    # columna titulo

    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'titulo'
    columna.fila = fila
    columna.borde = False
    columna.color1 = '#005187'
    columna.color2 = '#005187'
    columna.secciones = 8
    columna.justificacionhorizontaltexto = 'center'
    columna.justificacionverticaltexto = 'center'
    columna.fonttexto = 'Lugrasimo,22,700'
    columna.textocolumna = 'Nombre de la aplicacion'
    columna.colortexto = '#faf9f8'
    columna.funcion = 't'
    columna.save()

    # fila separacion 1
    
    if modelo == None:
        fila = filap()
    else:
        fila = filam()
    fila.nombre = 'fs1'
    fila.seccion = seccion
    fila.altura = '5px'
    fila.borde = False
    fila.save()

    # fila busqueda menu

    if modelo == None:
        fila = filap()
    else:
        fila = filam()
    fila.nombre = 'busqueda_menu'
    fila.seccion = seccion
    fila.altura = '60px'
    fila.color1 = '#faad25'
    fila.color2 = '#faad25'
    fila.borde = False
    fila.save()

    # columna busqueda

    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'busqueda'
    columna.fila = fila
    columna.borde = False
    columna.color1 = '#4cdafa'
    columna.color2 = '#4cdafa'
    columna.secciones = 4
    columna.funcion = 'b'
    columna.save()

    # columna menu

    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'menu'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 8
    columna.funcion = 'm'
    columna.color1 = '#d0fdd7'
    columna.color2 = '#d0fdd7'
    columna.save()

    # fila separacion 2
    
    if modelo == None:
        fila = filap()
    else:
        fila = filam()
    fila.nombre = 'fs2'
    fila.seccion = seccion
    fila.altura = '5px'
    fila.borde = False
    fila.save()

    # fila tres secciones

    if modelo == None:
        fila = filap()
    else:
        fila = filam()
    fila.nombre = 'tres_secciones'
    fila.seccion = seccion
    fila.altura = 'auto'
    fila.borde = False
    fila.save()

    # columna izquierda

    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'izquierda'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 1
    columna.color1 = 'transparent'
    columna.color2 = 'transparent'
    columna.save()

    # centro

    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'centro'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 10
    if modelo != None:
        columna.funcion = 'd'
    columna.save()

    # derecha

    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'derecha'
    columna.fila = fila
    columna.borde = False
    columna.secciones = 1
    columna.color1 = 'transparent'
    columna.color2 = 'transparent'
    columna.save()

def CreaListaSeccion(lista, Sec, Fil, Col, proyecto,modelo):
    # Crea la lista
    ns=0
    nf=0
    nc=0
    iw=''
    ih=''
    url=''
    jh=''
    jv=''
    texto = ''
    ctexto = ''
    stri = ''
    if modelo == None:
        ls = Sec.objects.filter(proyecto=proyecto)
    else:
        ls = Sec.objects.filter(modelo=modelo)
    for seccion in ls:
        lista.append([seccion,'s',0,ns])
        ns+=1
        for fila in Fil.objects.filter(seccion=seccion):
            lista.append([fila,'f',50,nf])
            nf=+1
            for columna in Col.objects.filter(fila=fila):
                fn = columna.fonttexto.split(',')[0]
                fs = columna.fonttexto.split(',')[1]
                fb = columna.fonttexto.split(',')[2]
                try:
                    ms = columna.margeninterno.split(',')[0]
                    md = columna.margeninterno.split(',')[1]
                    mb = columna.margeninterno.split(',')[2]
                    mi = columna.margeninterno.split(',')[3]
                except:
                    ms = '0px'
                    md = '0px'
                    mb = '0px'
                    mi = '0px'
                # logo
                if columna.funcion == 'l':
                    if proyecto.avatar:
                        url = proyecto.avatar.url
                        iw = str(proyecto.avatarwidth) + 'px'
                        ih = str(proyecto.avatarheight) + 'px'
                        if proyecto.justificacionhorizontallogo == 'c':
                            jh= 'center'
                        if proyecto.justificacionhorizontallogo == 'i':
                            jh='start'
                        if proyecto.justificacionhorizontallogo == 'd':
                            jh='end'
                        if proyecto.justificacionverticallogo == 'c':
                            jv='center'
                        if proyecto.justificacionverticallogo == 's':
                            jv='start'
                        if proyecto.justificacionverticallogo == 'i':
                            jv='end'
                    elif columna.imagen:
                        url = columna.imagen.url
                        iw = columna.dimensionesimagen.split(',')[0]
                        ih = columna.dimensionesimagen.split(',')[1]
                        jh=columna.justificacionhorizontaltexto
                        jv=columna.justificacionverticaltexto
                    else:
                        url=''
                        texto = columna.textocolumna
                        ctexto = columna.colortexto
                        jh=columna.justificacionhorizontaltexto
                        jv=columna.justificacionverticaltexto
                # titulo
                if columna.funcion == 't':
                    texto = ''
                    if proyecto.imagentitulo or proyecto.titulo != '':
                        if proyecto.justificacionhorizontaltitulo == 'c':
                            jh= 'center'
                        if proyecto.justificacionhorizontaltitulo == 'i':
                            jh='start'
                        if proyecto.justificacionhorizontaltitulo == 'd':
                            jh='end'
                        if proyecto.justificacionverticaltitulo == 'c':
                            jv='center'
                        if proyecto.justificacionverticaltitulo == 's':
                            jv='start'
                        if proyecto.justificacionverticaltitulo == 'i':
                            jv='end'
                    if proyecto.imagentitulo:
                        url = proyecto.imagentitulo.url
                    elif proyecto.titulo:
                        url=''
                        texto = proyecto.titulo
                        ctexto = proyecto.colortitulo
                        fn = proyecto.fonttitulo.split(',')[0]
                        fs = proyecto.fonttitulo.split(',')[1]
                        fb = proyecto.fonttitulo.split(',')[2]
                    elif columna.imagen:
                        url = columna.imagen.url
                        jh=columna.justificacionhorizontaltexto
                        jv=columna.justificacionverticaltexto
                    else:
                        url=''
                        texto = columna.textocolumna
                        ctexto = columna.colortexto
                        jh=columna.justificacionhorizontaltexto
                        jv=columna.justificacionverticaltexto
                if columna.funcion == 'b':
                    texto = ''
                    url=''
                    jh='center'
                    jv='center'
                if columna.funcion == 'o':
                    texto = ''
                    if columna.imagen:
                        url = columna.imagen.url
                        iw = columna.dimensionesimagen.split(',')[0]
                        ih = columna.dimensionesimagen.split(',')[1]
                        jh=columna.justificacionhorizontaltexto
                        jv=columna.justificacionverticaltexto
                    else:
                        url=''
                        texto = columna.textocolumna
                        ctexto = columna.colortexto
                        jh=columna.justificacionhorizontaltexto
                        jv=columna.justificacionverticaltexto

                lista.append([columna,'c',100,nc,fn,fs,fb,iw,ih,ms,md,mb,mi,proyecto,url,jh,jv,texto,ctexto,stri])

def CopiaImagenes(destino,upload,url,origen,nombreProyecto,etapa,usuario,borraPrevio):

    if borraPrevio:
        try:
            os.remove(destino)
        except:
            pass

    try:
        img = url.split('/')
        imagen = ''
        for i in img:
            imagen = i
        origen = origen + imagen
        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
    except Exception as e:
        errores = ErroresCreacion()
        errores.etapa = etapa
        errores.paso = "No se escribio en el archivo: " + destino
        errores.proyecto = nombreProyecto
        errores.usuario = usuario
        errores.descripcion = e
        errores.severo = True
        errores.save()

def CambiaOrdenGeneracion(proyecto):
    strTexto = []
    try:
        lista = Modelo.objects.filter(padre='nada',proyecto=proyecto).order_by('ordengeneracion')
        orden = 1
        lis = [orden]
        
        for li in lista:
            li.ordengeneracion = lis[0]
            if orden == lista.count():
                li.ultimoregistro = 'u'
            else:
                li.ultimoregistro = 'p'
            li.identa = 1
            li.save()
            lis[0] += 1
            strTexto.append('1' + ',' + li.nombre)
            ListaRecursiva(1,strTexto,li.nombre,proyecto,li.ordengeneracion+1,lis)
            orden+=1
    except Exception as e:
        print('error en la sub ',str(e))
    return strTexto

def ListaRecursiva(index,strTexto,nombre,proyecto,i,lis):
    for li in Modelo.objects.filter(padre=nombre,proyecto=proyecto):
        li.ordengeneracion = i
        li.identa = index+1
        li.save()
        i+=1
        lis[0] = i
        strTexto.append(str(index+1) + ',' + li.nombre)
        ListaRecursiva(index+1,strTexto,li.nombre,proyecto,i,lis)

# Dashboard

def RecursivoModelosHijo(modelo,lista):
    for mod in Modelo.objects.filter(padre=modelo.nombre):
        lista.append(mod)
        RecursivoModelosHijo(mod,lista)

def RecursivoTextosListas(modelo,lista,lista1,lista2):

    lista.append('strTexto_' + modelo.nombre + ' = []')
    
    if modelo.padre == 'nada':
        lista2.append('strTexto_' + modelo.nombre)
    if modelo.padre != 'nada' and Modelo.objects.get(nombre=modelo.padre,proyecto=modelo.proyecto).padre == 'nada':
        lista.append('lista_' + modelo.nombre + ' = []')
        lista1.append('lista_' + modelo.nombre + '.append(strTexto_' + modelo.nombre + ')')
        lista2.append('lista_' + modelo.nombre)
        
    for modelo_hijo in Modelo.objects.filter(padre = modelo.nombre, proyecto=modelo.proyecto):
        RecursivoTextosListas(modelo_hijo,lista,lista1,lista2)

    return lista,lista1,lista2

# def RecursivoListasRetorno(modelo,lista):

#     if modelo.padre =='nada':
#         lista.append('lista_' + modelo.nombre)

#     if modelo.padre != 'nada' and Modelo.objects.get(nombre=modelo.padre,proyecto=modelo.proyecto).padre == 'nada':
#         lista.append('lista_' + modelo.nombre)

#     for modelo_hijo in Modelo.objects.filter(padre = modelo.nombre, proyecto=modelo.proyecto):
#         RecursivoListasRetorno(modelo_hijo,lista)

#     return lista    

import copy
def RecursivoListasRetorno(modelo,lista,listaTexto):
    strLista = modelo.nombre
    strListaTexto = modelo.nombre
    mod = copy.copy(modelo)
    while mod.padre != 'nada':
        strLista = Modelo.objects.get(nombre=mod.padre,proyecto=mod.proyecto).nombre + '_' + strLista
        mod = Modelo.objects.get(nombre=mod.padre,proyecto=mod.proyecto)
    strListaTexto = 'strTexto_' + strLista
    strLista = 'lista_' + strLista
    lista.append(strLista)
    listaTexto.append(strListaTexto)
    for modelo_hijo in Modelo.objects.filter(padre = modelo.nombre, proyecto=modelo.proyecto):
        RecursivoListasRetorno(modelo_hijo,lista,listaTexto)
    return lista,listaTexto

def SinTags(texto):
    txt = ''
    flgProcesa = True
    text = texto.split('</p>')
    for palabra  in text:
        for caracter in palabra:
            if caracter == '<' or caracter == '&':
                flgProcesa = False
                continue
            if caracter == '>' or caracter ==';':
                flgProcesa = True
                continue
            if flgProcesa:
                txt += caracter
    return txt

def SinQuotes(texto):
    txt = texto.replace('&quot;','"')
    txt = texto.replace('&#39;','"')
    return txt

def VerificarSoloLetras(texto):
    caracteres = 'abcdefghijklmnopqrstuvwxyz_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    error = ''
    for i in texto:
        if i not in caracteres:
            error = ' caracteres no permitidos '
            break
    return error

def NoNumeroInicio(texto):
    patron = '[a-zA-Z]'
    error = ''
    if texto != '':
        if re.search(patron,str(texto)[0:1]) == None:
            error = ' debe comenzar con una letra '
    return error

def TextoValido(texto):
    error = ''
    if len(texto) > 0:
        if texto[0] == "'" and texto[len(texto)-1] != "'":
            error = ' no se cierra correctamente '
        if texto[0] == '"' and texto[len(texto)-1] != '"':
            error = ' no se cierra correctamente '
    return error

def TieneDash(modelo):
    tiene_dash = False
    for propiedad in Propiedad.objects.filter(modelo=modelo):
        if propiedad.dashboard:
            tiene_dash=True
            break
    return tiene_dash

# Actualizar el archivo js
def CrearArchivoJs(modelo,aplicacion):
    strfjs =  '// Funcion que se ejecuta cuando se acciona el boton' + '\n'
    strfjs +=  '// de busqueda en el html del modelo @modelo' + '\n'
    strfjs +=  '// #@[p_js_busqueda_@modelo_01] //' + '\n'
    strfjs += '$(function(){' + '\n'
    strfjs +=  '// #@[p_js_busqueda_@modelo_02] //' + '\n'
    strfjs += '\tvar enlace = $(' + "'" + '#link_busqueda_@modelo' + "'" + ');' + '\n'
    strfjs +=  '// #@[p_js_busqueda_@modelo_03] //' + '\n'
    strfjs += '\tenlace.on(' + "'" + 'click' + "'" + ',function(){' + '\n'
    strfjs +=  '// #@[p_js_busqueda_@modelo_04] //' + '\n'
    strfjs += '\tvar texto = $(' + "'" + '#textob@modelo' + "'" + ');' + '\n'
    strfjs +=  '// #@[p_js_busqueda_@modelo_05] //' + '\n'
    strfjs += '\tenlace.attr(' + "'" + 'href' + "'" + ',' + "'" + 'http://127.0.0.1:8001/@aplicacion/listar_@modelo?duplica=0&criterio=' + "'" + ' + ' + 'texto.val());' + '\n'
    strfjs +=  '// #@[p_js_busqueda_@modelo_06] //' + '\n'
    strfjs += '});' + '\n'
    strfjs +=  '// #@[p_js_busqueda_@modelo_07] //' + '\n'
    strfjs += '}())' + '\n'
    strfjs +=  '// #@[p_js_busqueda_@modelo_08] //' + '\n'

    strfjs = strfjs.replace('@modelo', modelo.nombre)
    strfjs = strfjs.replace('@aplicacion', aplicacion.nombre)

    return strfjs

from os import strerror
from modelos.models import Modelo

def PropiedadesModelo(proyecto, modelo,propiedad):
    strp = ''
    if propiedad.tipo == 'u':
        strp = '\t' + propiedad.nombre + ' =  models.ForeignKey(User,on_delete=models.CASCADE)' + '\n'
        modelo.crearlogin = True
        modelo.save()
        proyecto.conseguridad = True
        proyecto.save()
    if propiedad.tipo == 's':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = ',default=' + "''"
            else:
                pi = ',default=' + "'" + propiedad.valorinicial + "'"
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' = ' + 'models.CharField(max_length=' + str(propiedad.largostring) + pi + ')' + '\n'
    if propiedad.tipo == 'x':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default =' + "''"
            else:
                pi = 'default=' + "'" + propiedad.valorinicial + "'"
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' = ' + 'models.TextField(' + pi + ')' + '\n'
    if propiedad.tipo == 'm':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + '0'
            else:
                pi = 'default=' + propiedad.valorinicial
        else:
            pi = ''
        strp += '\t' + propiedad.nombre + ' =  models.SmallIntegerField(' + pi  + ')' + '\n'
    if propiedad.tipo == 'i':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + '0'
            else:
                pi = 'default=' + propiedad.valorinicial
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' =  models.IntegerField(' + pi + ')' + '\n'
    if propiedad.tipo == 'l':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + '0'
            else:
                pi = 'default=' + propiedad.valorinicial
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' =  models.BigIntegerField(' + pi + ')' + '\n'
    if propiedad.tipo == 'd':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + '0,'
            else:
                pi = 'default=' + propiedad.valorinicial + ','
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' =  models.DecimalField(' + pi + 'decimal_places=2,max_digits=10)' + '\n'
    if propiedad.tipo == 'f':
        strp = '\t' + propiedad.nombre + ' =  models.ForeignKey(' +  propiedad.foranea + ', on_delete=models.CASCADE,' + ' related_name=' + "'" + '%(class)s_@related' + "'" + ')' + '\n'
        strp = strp.replace('@related', propiedad.nombre)
        # llenar la variable de modelos foraneos
        try:
            modelo_foraneo = Modelo.objects.get(nombre=propiedad.foranea , proyecto=proyecto)
            if modelo_foraneo.aplicacion != modelo.aplicacion:
                if strmf.find('from ' + modelo_foraneo.aplicacion.nombre + '.models import ' +  propiedad.foranea) == -1:
                    strmf += 'from ' + modelo_foraneo.aplicacion.nombre + '.models import ' +  propiedad.foranea + '\n'  
        except:
            pass
    if propiedad.tipo == 't':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + 'timezone.now'
            else:
                pi = 'default=' + "'" + propiedad.valorinicial + "'"
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' =  models.DateTimeField(' + pi + ')' + '\n'
    if propiedad.tipo == 'e': #TimeField
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + "'00:00'"
            else:
                pi = 'default=' + "'" + propiedad.valorinicial + "'"
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' = ' + 'models.TimeField(' + pi + ')' + '\n'
    if propiedad.tipo == 'n': #DateField
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + 'timezone.now'
            else:
                pi = 'default=' + "'" + propiedad.valorinicial + "'"
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' = ' + 'models.DateField(' + pi + ')' + '\n'
    if propiedad.tipo == 'b':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + 'False'
            else:
                pi = 'default=' + propiedad.valorinicial
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' =  models.BooleanField(' + pi + ')' + '\n'
    if propiedad.tipo == 'r':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + "''"
            else:
                pi = 'default=' + "'" + propiedad.valorinicial + "'"
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' = ' + 'models.CharField(max_length=' + str(propiedad.largostring) + ',' + pi + ')' + '\n'
    if propiedad.tipo == 'a':
        if propiedad.mandatoria == False:
            if propiedad.valorinicial == '':
                pi = 'default=' + "''"
            else:
                pi = 'default=' + "'" + propiedad.valorinicial + "'"
        else:
            pi = ''
        strp = '\t' + propiedad.nombre + ' = ' + 'models.CharField(max_length=' + str(propiedad.largostring) + ',' + pi + ')' + '\n'
    if propiedad.tipo == 'h':
        strp = '\t' + propiedad.nombre + ' = ' + 'RichTextField()' + '\n'
    if propiedad.tipo == 'p':
        strp = '\t' + propiedad.nombre + ' = models.ImageField(upload_to=' + "'" + modelo.nombre + "'" + ',blank=True,null=True)' + '\n'

    return strp

def IdentificacionModelo(modelo, strp):
    strmodelo = 'class @nombremodelo(models.Model):' + '\n\n'
    strmodelo += '#@[p_propiedades_@nombremodelo_01]' + '\n\n'
    strmodelo += '@propiedades' + '\n'
    strmodelo += '#@[p_propiedades_@nombremodelo_02]' + '\n'
    strmodelo += '\n'
    strmodelo += '\tdef __str__(self):' + '\n'
    strmodelo += '#@[p_self_@nombremodelo_01]' + '\n'
    strmodelo += '\t\treturn @paraself' + '\n' 
    strmodelo += '#@[p_self_@nombremodelo_02]' + '\n'

    strmodelo = strmodelo.replace('@nombremodelo', modelo.nombre)

    strmodelo = strmodelo.replace('@propiedades', strp)
    if modelo.nombreself != '':
        strmodelo = strmodelo.replace('@paraself', modelo.nombreself)
    else:
        strself = False
        for prop in Propiedad.objects.filter(modelo=modelo):
            if prop.paraidentificar:
                strmodelo = strmodelo.replace('@paraself', 'self.' + prop.nombre)
                strself = True
                break
        if not strself:
            for prop in Propiedad.objects.filter(modelo=modelo):
                strmodelo = strmodelo.replace('@paraself', 'self.' + prop.nombre)
                break
    return strmodelo

def VistaEditarModeloHijo(proyecto,aplicacion,modelo):
    strv = '# Este modelo es dependiente de ' + modelo.padre + '\n'
    strv += '# Vista que es utilizada para la edicion del' + '\n'
    strv += '# modelo @modelo cuyos registros y se encuentran' + '\n'
    strv += '# grabados en la Base de Datos' + '\n'
    strv += '#@[p_editar_' + modelo.nombre + '_01]' + '\n'
    strv += 'class Editar@modeloView(UpdateView):' + '\n'
    strv += '#@[p_editar_' + modelo.nombre + '_02]' + '\n'
    strv += '\t# El modelo que se edita' + '\n'
    strv += '\tmodel = @modelo' + '\n'
    strv += '#@[p_editar_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t# El formulario para la edicion' +'\n'
    strv += '\tform_class = @modeloForm' + '\n'
    # strv += '\ttemplate_name_suffix = ' + "'" + '_update_form' + "'"  + '\n'
    strv += '#@[p_editar_' + modelo.nombre + '_04]' + '\n' 
    strv += '\t# El HTML que se despliega ante el usuario' + '\n' 
    strv += '\ttemplate_name = ' + "'" + '@aplicacion/@modelo_update_form.html' + "'"  + '\n'
    strv += '\n'                
    strv += '#@[p_editar_' + modelo.nombre + '_05]' + '\n' 
    strv += '\t# El procedimiento de salida de la edicion' + '\n'
    strv += '\tdef get_success_url(self):' + '\n'
    strv += '#@[p_editar_success_' + modelo.nombre + '_01]' + '\n' 

    # success de la edicion del modelo hijo o nieto
    modelo_padre = Modelo.objects.get(nombre=modelo.padre , proyecto=proyecto)
    if modelo_padre.padre != 'nada': # modelo nieto
        modelo_abuelo = Modelo.objects.get(nombre=modelo_padre.padre , proyecto=proyecto)
        strv += '\t\t# El modelo @modelo es dependiente' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_02]' + '\n' 
        strv += '\t\t# Despues de editar el modelo se vuelve al HTML de edicion' + '\n' 
        strv += '\t\t# con el mensaje de actualizacion correcta del registro' + '\n'
        strv += '\t\ttry:' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_03]' + '\n' 
        strv += '\t\t\tif self.request.GET["padre"] != "":' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_04]' + '\n' 
        strv += '\t\t\t\treturn reverse_lazy(' + "'" + ModeloRaizHtml(modelo_padre,modelo_padre.proyecto)[1] + ':editar_' + ModeloRaizHtml(modelo_padre,modelo_padre.proyecto)[0] + "'" + ', args=[self.request.GET[' + "'" +'raiz' + "'" + ']]) + ' + "'" + '?correcto' + "'" + ' + ' + "'" + '&padre=' + "'" + ' + str(self.request.GET[' + "'" + 'padre' + "'" + '])' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_05]' + '\n' 
        strv += '\t\texcept:' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_06]' + '\n' 
        strv += '\t\t\t\treturn reverse_lazy(' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ', args=[self.request.GET[' + "'" +'@modelopadre_id' + "'" + ']]) + ' + "'" + '?correcto' + "'" + ' + ' + "'" + '&@modeloabuelo_id=' + "'" + ' + str(self.request.GET[' + "'" + '@modeloabuelo_id' + "'" + '])' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_07]' + '\n' 
        strv = strv.replace('@modeloabuelo', modelo_abuelo.nombre)
        strv += '#@[p_editar_success_' + modelo.nombre + '_08]' + '\n' 
    else: # modelo hijo
        strv += '\t\t# El modelo @modelo es independiente' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_02]' + '\n' 
        strv += '\t\t# Despues de editar el modelo se vuelve al HTML de edicion' + '\n' 
        strv += '\t\t# con el mensaje de actualizacion correcta del registro' + '\n'
        strv += '\t\ttry:' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_03]' + '\n' 
        strv += '\t\t\tif self.request.GET["padre"] != "padre":' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_04]' + '\n' 
        strv += '\t\t\t\treturn reverse_lazy(' + "'" + ModeloRaizHtml(modelo_padre,modelo_padre.proyecto)[1] + ':editar_' + ModeloRaizHtml(modelo_padre,modelo_padre.proyecto)[0] + "'" + ', args=[self.request.GET[' + "'" +'raiz' + "'" + ']]) + ' + "'" + '?correcto' + "'" + ' + ' + "'" + '&padre=' + "'" + ' + str(self.request.GET[' + "'" + 'padre' + "'" + '])' + '\n'
        strv += '\t\texcept:' + '\n'
        strv += '#@[p_editar_success_' + modelo.nombre + '_05]' + '\n' 
        strv += '\t\t\t\treturn reverse_lazy(' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ', args=[self.request.GET[' + "'" + '@modelopadre_id' + "'" + ']]) + ' + "'" + '?correcto' + "'"  + '\n'

    strv += '\n'                
    strv += '\t# Se preparan los context para enviarlos al HTML de edicion' + '\n'
    strv += '\tdef get_context_data(self,**kwargs):' + '\n'
    strv += '\t\tcontext = super(Editar@modeloView, self).get_context_data(**kwargs)' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\t# Se recupera el registro de @modelo que se edita' + '\n'
    strv += '\t\tmodelo_current = (self.object)' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t\t# Se envian al HTML el id del modelo y su campo que lo identifica' + '\n' 
    strv += '\t\t# Este campo fue el que se definio como identificador de borrado del modelo' + '\n'
    strv += '\t\tcontext[' + "'" + '@modelo_id' + "'" + '] = modelo_current.id' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_03]' + '\n' 
    # strv += '\t\tcontext[' + "'" + 'nombre' + "'" + '] = @modelo.@paraborrar' + '\n'
    strv += '\t\tcontext[' + "'" + 'nombre' + "'" + '] = @paraborrar' + '\n'
    strv += '@listahijos' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_04]' + '\n' 
    strv += '@idsuperior' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_05]' + '\n' 
    strv += '@numerohijos' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_06]' + '\n' 
    strv += ModeloRaiz(modelo,proyecto) + '\n'

    strv += '\t\ttry:' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_07]' + '\n' 
    strv += '\t\t\tcontext["esquema"] = self.request.GET["esquema"]' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_08]' + '\n' 
    strv += '\t\texcept:' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_09]' + '\n' 
    strv += '\t\t\tcontext["esquema"] = ' + '"' + 'sin_treeview' + '"' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_10]' + '\n' 

    if modelo.proyecto.conroles:
        for pr in Propiedad.objects.filter(modelo=modelo):
            strv += '\t\t# Controla si el usuario puede editar el valor a la propiedad: ' + pr.nombre + ' del modelo' + '\n'
            strv += '#@[p_puede_editar_' + modelo.nombre + '_' + pr.nombre + '_01]' + '\n' 
            strv += "\t\tcontext['puede_ver_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedever')" + '\n'
            strv += '#@[p_puede_editar_' + modelo.nombre + '_' + pr.nombre + '_02]' + '\n' 
            strv += "\t\tcontext['puede_editar_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeeditar')" + '\n'
            strv += "\t\tcontext['puede_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeeditar')" + '\n'
            strv += '#@[p_puede_editar_' + modelo.nombre + '_' + pr.nombre + '_03]' + '\n' 

    strv += '\t\treturn context' + '\n'

    strv = strv.replace('@numerohijos', NumeroHijos(proyecto,modelo))
    strv = strv.replace('@listahijos', ListaHijos(proyecto,modelo))
    strv = strv.replace('@idsuperior', IdSuperior(proyecto,modelo))
    # aplicacion padre
    strv = strv.replace('@aplicacionpadre', Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre)
    # modelo
    strv = strv.replace('@modelopadre', modelo_padre.nombre)
    strv = strv.replace('@modelo', modelo.nombre)
    # aplicacion
    strv = strv.replace('@aplicacion', aplicacion.nombre)

    strv = strv.replace('@paraborrar', ParaBorrar(modelo))

    strv += '\n'
    return strv

def ModeloRaiz(modelo, proyecto):
    sinPadre = False
    lista = []
    lista.append('\t\tmodelo_x_' + modelo.nombre + ' = modelo_current')
    while not sinPadre:
        try:
            mod = Modelo.objects.get(nombre=modelo.padre,proyecto=proyecto)
            lista.append('#@[p_modelo_raiz_' + mod.nombre + '_01]') 
            lista.append('\t\tmodelo_x_' + mod.nombre + ' = ' + mod.nombre + '.objects.get(id=modelo_x_' + modelo.nombre + '.' + mod.nombre + '.id)')
            lista.append('#@[p_modelo_raiz_' + mod.nombre + '_02]')
            lista.append('\t\tcontext["' + mod.nombre + '"] = modelo_x_' +  mod.nombre)
            modelo = mod
        except:
            sinPadre = True
    strTexto = ''
    for tx in lista:
        strTexto += tx + '\n'
    return strTexto

def ModeloRaizHtml(modelo, proyecto):
    sinPadre = False
    lista = []
    while not sinPadre:
        try:
            mod = Modelo.objects.get(nombre=modelo.padre,proyecto=proyecto)
            modelo = mod
        except:
            sinPadre = True
            lista.append(modelo.nombre)
            lista.append(modelo.aplicacion.nombre)
    return lista

def NumeroHijos(proyecto,modelo):
    # define si existe un numero de registros para los hijos
    strnh = ''
    for hijo in Modelo.objects.filter(padre=modelo.nombre , proyecto=proyecto):
        strnh += '# Se envia al HTML el numero de modelos dependientes de @modelo' + '\n' 
        strnh += '\t\tcontext[' + "'" + 'numero' + hijo.nombre + "'" + '] = ' + hijo.nombre + '.objects.filter(@modelo=modelo_current).count()' + '\n'
    return strnh

def ListaHijos(proyecto,modelo):
    # lista hijos
    strlh = ''
    for model in Modelo.objects.filter(padre=modelo.nombre , proyecto=proyecto):
        strlh += '\t\t# Se envia al HTML la lista de los modelos dependientes de @modelo' + '\n'
        strlh += '\t\t' + model.nombre + '_' + model.nombre + ' = ' + model.nombre + '.objects.filter(' + modelo.nombre + ' = modelo_current' + ')' + '\n'
        strlh += '#@[p_editar_context_lista_hijos' + modelo.nombre + '_01]' + '\n' 
        strlh += '\t\t' + 'context[' + "'" + 'lista' + model.nombre + "'" + '] =  ' + model.nombre  + '_' + model.nombre + '\n'
        strlh += '#@[p_editar_context_lista_hijos' + modelo.nombre + '_02]' + '\n' 

        if proyecto.conroles:
            strlh += '\t\t# Controla si el usuario puede listar registros del modelo: ' + model.nombre +  '\n'
            strlh += "\t\tif not roles.PuedeModelo('" + model.nombre + "',self.request.user.username,'puedelistar'):" + '\n'
            strlh += '#@[p_roles_' + modelo.nombre + '_01]' + '\n' 
            strlh += '\t\t\t' + 'context[' + "'" + 'lista' + model.nombre + "'" + '] = None' + '\n'
            for pr in Propiedad.objects.filter(modelo=model):
                strlh += '\t\t# Controla si el usuario puede ver el valor a la propiedad: ' + pr.nombre + ' del modelo' + '\n'
                strlh += '#@[p_roles_' + modelo.nombre + '_' + pr.nombre + '_01]' + '\n' 
                strlh += "\t\tcontext['puede_ver_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedever')" + '\n'
            strlh += '\t\t# Controla si el usuario puede insertar registros al modelo: ' + model.nombre +  '\n'
            strlh += '#@[p_roles_' + modelo.nombre + '_02]' + '\n' 
            strlh += "\t\tcontext['puede_insertar_" + model.nombre + "'] = roles.PuedeModelo('" + model.nombre + "',self.request.user.username,'puedeinsertar')" + '\n'
            strlh += '#@[p_roles_' + modelo.nombre + '_03]' + '\n' 
            strlh += '\t\t# Controla si el usuario puede editar registros al modelo' + '\n'
            strlh += "\t\tcontext['puede_editar_" + model.nombre + "'] = roles.PuedeModelo('" + model.nombre + "',self.request.user.username,'puedeeditar')" + '\n'
            strlh += '#@[p_roles_' + modelo.nombre + '_04]' + '\n' 
            strlh += '\t\t# Controla si el usuario puede borrar registros al modelo' + '\n'
            strlh += '#@[p_roles_' + modelo.nombre + '_05]' + '\n' 
            strlh += "\t\tcontext['puede_borrar_" + model.nombre + "'] = roles.PuedeModelo('" + model.nombre + "',self.request.user.username,'puedeborrar')" + '\n'

    return strlh




def IdSuperior(proyecto,modelo):
    # define los id superiores
    stris = ''
    modelo_padre = Modelo.objects.get(nombre=modelo.padre , proyecto=proyecto)
    if modelo_padre.padre != 'nada':  # modelo nieto
        modelo_abuelo = Modelo.objects.get(nombre=modelo_padre.padre , proyecto=proyecto)
        stris += '#@[p_editar_context_padre' + modelo.nombre + '_01]' + '\n' 
        stris += '\t\tcontext[' + "'" + '@modelopadre_id' + "'" + '] = modelo_current.@modelopadre.id' + '\n'
        stris += '\t\t# Se recupera el modelo abuelo y se envia su id' + '\n'
        stris += '\t\t@modelopadre_@modelopadre = @modelopadre.objects.get(id=modelo_current.@modelopadre.id)' + '\n'
        stris += '#@[p_editar_context_padre' + modelo.nombre + '_02]' + '\n' 
        stris += '\t\tcontext[' + "'" + '@modeloabuelo_id' + "'" + '] = @modelopadre_@modelopadre.@modeloabuelo.id' + '\n'
        stris = stris.replace('@modeloabuelo', modelo_abuelo.nombre)
        stris += '#@[p_editar_context_padre' + modelo.nombre + '_03]' + '\n' 
    else: # modelo hijo
        stris += '#@[p_editar_context_padre' + modelo.nombre + '_01]' + '\n' 
        stris += '\t\t# Se recupera el modelo padre y se envia su id' + '\n'
        stris += '\t\tcontext[' + "'" + '@modelopadre_id' + "'" + '] = modelo_current.@modelopadre.id' + '\n'
        stris += '#@[p_editar_context_padre' + modelo.nombre + '_02]' + '\n' 
    stris = stris.replace('@modelopadre', modelo_padre.nombre)
    return stris

from aplicaciones.models import Aplicacion

def VistaCrearModeloHijo(proyecto, aplicacion, modelo, strim):
    modelo_padre = Modelo.objects.get(nombre=modelo.padre , proyecto=proyecto)
    strv = '# Este modelo es dependiente de ' + modelo.padre + '\n'
    strv += '# Esta vista es utilizada para el registro de nuevos' + '\n'
    strv += '# registros del modelo @modelo' + '\n'
    strv += '#@[p_crear_' + modelo.nombre + '_01]' + '\n' 
    strv += 'class Crear@modeloView(CreateView):' + '\n'
    strv += '#@[p_crear_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t# Se define el modelo cuyo registro de inserta' + '\n'
    strv += '\tmodel = @modelo' + '\n'
    strv += '#@[p_crear_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t# El formulario para el nuevo registro' + '\n'
    strv += '\tform_class = @modeloForm' + '\n'
    strv += '#@[p_crear_' + modelo.nombre + '_04]' + '\n' 
    strv += '\t# El HTML para el nuevo registro' + '\n'
    strv += '\ttemplate_name = ' + "'" + '@aplicacion/@modelo_form.html' + "'"  + '\n'
    strv += '#@[p_crear_' + modelo.nombre + '_05]' + '\n' 
    strv += '\n'                
    strv += '\t# El procedimiento de salida de la insercion' + '\n'
    strv += '\tdef get_success_url(self):' + '\n'
    strv += '#@[p_crear_success_' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\t# Despues de la insercion del registro, el control' + '\n'
    strv += '\t\t# retorna al HTML de edicion del modelo padre' + '\n'
    if modelo_padre.padre != 'nada': # modelo nieto
        modelo_abuelo = Modelo.objects.get(nombre=modelo_padre.padre , proyecto=proyecto)
        strv += '#@[p_crear_success_' + modelo.nombre + '_02]' + '\n' 
        strv += '\t\treturn reverse_lazy(' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ', args=[self.request.GET[' + "'" +'@modelopadre_id' + "'" + ']]) + ' + "'" + '?correcto' + "'" + ' + ' + "'" + '&@modeloabuelo_id=' + "'" + ' + str(self.request.GET[' + "'" + '@modeloabuelo_id' + "'" + '])' + '\n'
        strv = strv.replace('@modeloabuelo', modelo_abuelo.nombre)
    else:
        strv += '#@[p_crear_success_' + modelo.nombre + '_02]' + '\n' 
        strv += '\t\treturn reverse_lazy(' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ', args=[self.request.GET[' + "'" + '@modelopadre_id' + "'" + ']]) + ' + "'" + '?correcto' + "'" + '\n'
    strv += '\n'                
    strv += '\t# Procedimiento para el clik de insercion' + '\n'
    strv += '#@[p_crear_post_' + modelo.nombre + '_01]' + '\n' 
    strv += '\tdef post(self,request,*args,**kwargs):' + '\n'
    strv += '#@[p_crear_post_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t\t# Se recupera el formulario con los controles ya llenos' + '\n'
    strv += '\t\tform = self.form_class(request.POST)' + '\n'
    strv += '\t\t# Se recupera el registro del modelo padre ' + '\n'
    strv += '\t\t@modelopadre_post = @modelopadre.objects.get(id = request.GET[' + "'" + '@modelopadre_id' + "'" + '])' + '\n'
    strv += '#@[p_crear_post_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t\tif form.is_valid():' + '\n'
    strv += '\t\t# El formulario es valido, no existen incongruencias' + '\n'
    strv += '#@[p_crear_post_' + modelo.nombre + '_04]' + '\n' 
    strv += '\t\t# Se graba el registro en la base de datos pero ' + '\n'
    strv += '\t\t# la grabacion se mantiene pendiente, sin commit ' + '\n'
    strv += '\t\t\t@modelo= form.save(commit=False)' + '\n'
    strv += '#@[p_crear_post_' + modelo.nombre + '_05]' + '\n' 
    strv += '\t\t\t# Se asigna a @modelo la dependencia con el modelo padre' + '\n'
    strv += '\t\t\t@modelo.@modelopadre = @modelopadre_post' + '\n'
    strv += '#@[p_crear_post_' + modelo.nombre + '_06]' + '\n' 

    # Ver si existe una propiedad de tipo usuario
    prop = ModeloConPropiedadUsuario(modelo)
    if prop != None:
        if proyecto.conseguridad:
            strv += '\t\t\tuser = request.user' + '\n'
            strv += '#@[p_crear_post_' + modelo.nombre + '_07]' + '\n' 
            strv += '\t\t\t# Se graba en @modelo a propietario del proyecto ' + '\n'
            strv += '\t\t\t# ya que el modelo se tienen seguridad ' + '\n'
            strv += '\t\t\t@modelo.' + prop.nombre + ' = user' + '\n'
            strv += '#@[p_crear_post_' + modelo.nombre + '_08]' + '\n' 

    strv += '\t\t\t# Se graba el registro definitivamente en la base de datos ' + '\n'
    strv += '\t\t\t@modelo.save()' + '\n'
    strv += '#@[p_crear_post_' + modelo.nombre + '_09]' + '\n' 
    strv += '\t\t\t# Se leva el control al procedimiento de salida por grabacion exitosa' + '\n'
    strv += '\t\t\treturn HttpResponseRedirect(self.get_success_url())' + '\n'
    strv += '#@[p_crear_post_' + modelo.nombre + '_10]' + '\n' 
    strv += '\t\telse:' + '\n'
    strv += '#@[p_crear_post_' + modelo.nombre + '_11]' + '\n' 
    strv += '\t\t\t# Se leva el control al HTML de insercion grabacion no exitosa' + '\n'
    strv += '\t\t\treturn render(request,' + "'" + modelo.aplicacion.nombre + '/' + modelo.nombre + '_form.html' + "'" + ', {' + "'" + 'form' + "'" + ':form,' + "'" + modelo_padre.nombre + '_id' + "'" + ':' + modelo_padre.nombre + '_post.id})'
    strv += '\n'    

    # codigo para get_context en Crear
    strv += '@getcontext'
    strgc = ''
    # modelo_padre = Modelo.objects.get(nombre=modelo.padre , proyecto=proyecto)
    if modelo_padre.padre != 'nada':  # modelo nieto
        modelo_abuelo = Modelo.objects.get(nombre=modelo_padre.padre , proyecto=proyecto)
        strgc = '\t# Se preparan los context para enviarlos al HTML de insercion' + '\n'
        strgc += '\tdef get_context_data(self,**kwargs):' + '\n'
        strgc += '#@[p_crear_context_' + modelo.nombre + '_01]' + '\n' 
        strgc += '\t\tcontext = super(Crear@modeloView, self).get_context_data(**kwargs)' + '\n'
        strgc += '\t\t# Se recupera el objeto padre y se envia su id' + '\n'
        strgc += '#@[p_crear_context_' + modelo.nombre + '_02]' + '\n' 
        strgc += '\t\tobj = @modelopadre.objects.get(id=self.request.GET[' + "'" + '@modelopadre_id' + "'" + '])' + '\n'
        strgc += '\t\tcontext[' + "'" + '@modelopadre_id' + "'" + '] = obj.id' + '\n'
        strgc += '#@[p_crear_context_' + modelo.nombre + '_03]' + '\n' 
        strgc += '\t\t# Se recupera el modelo abuelo y se envia su id' + '\n'
        strgc += '\t\t@modeloabuelo_@modeloabuelo = @modeloabuelo.objects.get(id=obj.@modeloabuelo.id)' + '\n'
        strgc += '#@[p_crear_context_' + modelo.nombre + '_04]' + '\n' 
        strgc += '\t\tcontext[' + "'" + '@modeloabuelo_id' + "'" + '] = @modeloabuelo_@modeloabuelo.id' + '\n'
        strgc += '#@[p_crear_context_' + modelo.nombre + '_05]' + '\n' 

        if modelo.proyecto.conroles:
            strgc += '\t\t# Controla si el usuario puede listar los registros del modelo' + '\n'
            strgc += "\t\tif not roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedelistar'):" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_01' + ']' + '\n'
            strgc += "\t\t\tcontext['lista'] = None" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_02' + ']' + '\n'
            strgc += '\t\t# Controla si el usuario puede insertar registros al modelo' + '\n'
            strgc += "\t\tcontext['puede_insertar'] = roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedeinsertar')" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_03' + ']' + '\n'
            strgc += '\t\t# Controla si el usuario puede editar registros al modelo' + '\n'
            strgc += "\t\tcontext['puede_editar'] = roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedeeditar')" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_04' + ']' + '\n'
            strgc += '\t\t# Controla si el usuario puede borrar registros al modelo' + '\n'
            strgc += "\t\tcontext['puede_borrar'] = roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedeborrar')" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_05' + ']' + '\n'

        if modelo.proyecto.conroles:
            for pr in Propiedad.objects.filter(modelo=modelo):
                strgc += '\t\t# Controla si el usuario puede editar el valor a la propiedad: ' + pr.nombre + ' del modelo' + '\n'
                strgc += '#@[p_puede_asignar_' + modelo.nombre + '_' + pr.nombre + '_01]' + '\n' 
                strgc += "\t\tcontext['puede_ver_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedever')" + '\n'
                strgc += '#@[p_puede_asignar_' + modelo.nombre + '_' + pr.nombre + '_02]' + '\n' 
                strgc += "\t\tcontext['puede_asignar_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeasignarvalor')" + '\n'
                strgc += "\t\tcontext['puede_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeasignarvalor')" + '\n'
                strgc += '#@[p_puede_asignar_' + modelo.nombre + '_' + pr.nombre + '_03]' + '\n' 

        strgc += '\t\treturn context' + '\n'
        strgc = strgc.replace('@modeloabuelo', modelo_abuelo.nombre)
        if strim.find('from ' +  Aplicacion.objects.get(id=modelo_abuelo.aplicacion.id).nombre + '.models import ' + modelo_abuelo.nombre) == -1:                            
            strim += 'from ' +  Aplicacion.objects.get(id=modelo_abuelo.aplicacion.id).nombre + '.models import ' + modelo_abuelo.nombre + '\n'  
    else:
        strgc += '\tdef get_context_data(self,**kwargs):' + '\n'
        strgc += '\t\tcontext = super(Crear@modeloView, self).get_context_data(**kwargs)' + '\n'
        strgc += '#@[p_crear_context_' + modelo.nombre + '_01]' + '\n' 
        strgc += '\t\t# Se recupera el objeto padre y se envia su id' + '\n'
        strgc += '\t\tcontext[' + "'" + '@modelopadre_id' + "'" + '] = self.request.GET[' + "'" + '@modelopadre_id' + "'" + ']' + '\n'
        strgc += '#@[p_crear_context_' + modelo.nombre + '_02]' + '\n' 

        if modelo.proyecto.conroles:
            strgc += '\t\t# Controla si el usuario puede listar los registros del modelo' + '\n'
            strgc += "\t\tif not roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedelistar'):" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_01' + ']' + '\n'
            strgc += "\t\t\tcontext['lista'] = None" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_02' + ']' + '\n'
            strgc += '\t\t# Controla si el usuario puede insertar registros al modelo' + '\n'
            strgc += "\t\tcontext['puede_insertar'] = roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedeinsertar')" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_03' + ']' + '\n'
            strgc += '\t\t# Controla si el usuario puede editar registros al modelo' + '\n'
            strgc += "\t\tcontext['puede_editar'] = roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedeeditar')" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_04' + ']' + '\n'
            strgc += '\t\t# Controla si el usuario puede borrar registros al modelo' + '\n'
            strgc += "\t\tcontext['puede_borrar'] = roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedeborrar')" + '\n'
            strgc += '#@[p_lista_roles_' + modelo.nombre + '_05' + ']' + '\n'

        if modelo.proyecto.conroles:
            for pr in Propiedad.objects.filter(modelo=modelo):
                strgc += '\t\t# Controla si el usuario puede editar el valor a la propiedad: ' + pr.nombre + ' del modelo' + '\n'
                strgc += '#@[p_puede_asignar_' + modelo.nombre + '_' + pr.nombre + '_01]' + '\n' 
                strgc += "\t\tcontext['puede_ver_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedever')" + '\n'
                strgc += '#@[p_puede_asignar_' + modelo.nombre + '_' + pr.nombre + '_02]' + '\n' 
                strgc += "\t\tcontext['puede_asignar_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeasignarvalor')" + '\n'
                strgc += "\t\tcontext['puede_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeasignarvalor')" + '\n'
                strgc += '#@[p_puede_asignar_' + modelo.nombre + '_' + pr.nombre + '_03]' + '\n' 

        strgc += '\t\treturn context' + '\n'
    strgc = strgc.replace('@modelopadre', modelo_padre.nombre)

    strv = strv.replace('@getcontext', strgc)

    if strim.find('from ' +  Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre + '.models import ' + modelo_padre.nombre) == -1:
        strim += 'from ' +  Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre + '.models import ' + modelo_padre.nombre + '\n'  

    # aplicacion padre
    strv = strv.replace('@aplicacionpadre', Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre)
    # modelo
    strv = strv.replace('@modelopadre', modelo_padre.nombre)
    strv = strv.replace('@modelo', modelo.nombre)
    # aplicacion
    strv = strv.replace('@aplicacion', aplicacion.nombre)

    strv = strv.replace('@paraborrar', ParaBorrar(modelo))

    strv += '\n'            
    return strv, strim
                        
# Borrar modelo hijo

def VistaBorrarModeloHijo(proyecto,aplicacion,modelo):
    strv = '# Este modelo es dependiente de ' + modelo.padre + '\n'
    strv += '# Esta vista es utilizada para el borrado de' + '\n'
    strv += '# registros del modelo @modelo' + '\n'
    strv += '#@[p_borrar_' + modelo.nombre + '_01]' + '\n' 
    strv += 'class Borrar@modeloView(DeleteView):' + '\n'
    strv += '#@[p_borrar_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t# Se define el modelo a borrar' + '\n'
    strv += '\tmodel = @modelo' + '\n'
    strv += '#@[p_borrar_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t# El template HTML para desplegar la opcion de borrado' + '\n'
    strv += '\ttemplate_name = ' + "'" + '@aplicacion/@modelo_confirm_delete.html' + "'"  + '\n'
    strv += '#@[p_borrar_' + modelo.nombre + '_04]' + '\n' 
    strv += '\n'                
    strv += '\t# El procedimiento de salida del borrado' + '\n'
    strv += '\tdef get_success_url(self):' + '\n'
    strv += '#@[p_borrar_success_' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\t# El control vuelve a la edicion del modelo padre' + '\n'
    strv += '\t\treturn reverse_lazy(' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ', args=[self.request.GET[' + "'" + '@modelopadre_id' + "'" + ']]) + ' + "'" + '?correcto' + "'" + '\n'
    strv += '#@[p_borrar_success_' + modelo.nombre + '_02]' + '\n' 
    strv += '\n'                
    strv += '\t# Se preparan los contextos para el HTML de borrado' + '\n'
    strv += '\tdef get_context_data(self,**kwargs):' + '\n'
    strv += '\t\tcontext = super(Borrar@modeloView, self).get_context_data(**kwargs)' + '\n'
    strv += '#@[p_borrar_context_' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\t# Se recupera el modelo y se envia el nombre definido para el borrado' + '\n'
    strv += '\t\tmodelo_current = @modelo.objects.get(id=self.object.id)' + '\n'
    strv += '#@[p_borrar_context_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t\tcontext[' + "'" + 'nombreborrar' + "'" + '] = @paraborrar' + '\n'
    strv += '#@[p_borrar_context_' + modelo.nombre + '_03]' + '\n' 
    strv += '@idsuperior' + '\n'
    strv += '#@[p_borrar_context_' + modelo.nombre + '_04]' + '\n' 
    strv += '\t\treturn context' + '\n'

    strv = strv.replace('@idsuperior', IdSuperior(proyecto,modelo))

    # modelo padre
    modelo_padre = Modelo.objects.get(nombre=modelo.padre , proyecto=proyecto)
    strv = strv.replace('@modelopadre', modelo_padre.nombre)
    strv = strv.replace('@modelo', modelo.nombre)
    strv = strv.replace('@paraself', modelo.nombre + '.' + modelo.nombreself)

    # aplicacion
    strv = strv.replace('@aplicacionpadre', Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre)
    strv = strv.replace('@aplicacion', aplicacion.nombre)

    strv = strv.replace('@paraborrar', ParaBorrar(modelo))

    return strv

def ModeloConPropiedadUsuario(modelo):
    for prop in Propiedad.objects.filter(modelo=modelo):
        if prop.tipo == 'u':
            return prop
    return None    

def ParaBorrar(modelo):
    if modelo.nombreborrar != '':
        # separa los componentes
        strpb = modelo.nombreborrar.split("+ '-' + ")
        strpbt = ''
        for strc in strpb:
            if strpbt == '':
                strpbt = 'str(modelo_current.' + strc + ')'
            else:
                strpbt += '+ ' + "'" + "-" + "'" + ' + ' + 'str(modelo_current.' + strc + ')'
        # strv = strv.replace('@paraborrar', modelo_current.nombreborrar)
    else:
        paraborrar = False
        for prop in Propiedad.objects.filter(modelo=modelo):
            if prop.paraborrar:
                strpbt = 'modelo_current.' + prop.nombre
                paraborrar = True
                break
        if not paraborrar:
            for prop in Propiedad.objects.filter(modelo=modelo):
                strpbt = 'modelo_current.' + prop.nombre
                # modelo.nombreborrar = prop.nombre
                # modelo.save()
                break
    return strpbt    

def VistaListarRaiz(aplicacion, modelo, proyecto):
    strv = '# Este modelo es independiente por lo que' + '\n'
    strv += '# se elabora una lista de sus registros' + '\n'

    strv += '#@[p_listar_' + modelo.nombre + '_01]' + '\n' 
    strv += 'class Listar@modeloView(ListView):' + '\n'
    strv += '#@[p_listar_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t# Definir el modelo a utilizar' + '\n'
    strv += '\tmodel = @modelo' + '\n'
    strv += '#@[p_listar_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t# Especificar el template HTML' + '\n'
    strv += '\ttemplate_name = ' + "'" + '@aplicacion/@modelo_list.html' + "'"  + '\n'
    strv += '#@[p_listar_' + modelo.nombre + '_04]' + '\n' 
    strv += '\n'                
    strv += '\t# Prepara los context para el HTML' + '\n'
    strv += '\tdef get_context_data(self,**kwargs):' + '\n'
    strv += '#@[p_listar_context_' + modelo.nombre + '_01' + ']' + '\n'
    strv += '\t\tcontext = super(Listar@modeloView, self).get_context_data(**kwargs)' + '\n'

    if modelo.buscadorlista:
        strv += '\t\ttry:' + '\n'
        strv += '\t\t# La lista tiene un buscador para seleccionar los registros' + '\n'
        strv += '\t\t# a traves del parametro GET criterio' + '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_01' + ']' + '\n'
        strv += '\t\t\tcontext[' + "'" + 'criterio' + "'" + '] = self.request.GET[' + "'" + 'criterio' + "'" + ']' + '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_02' + ']' + '\n'
        strv += '\t\t\t# Si criterio es * se buscan todos los registros' + '\n'
        strv += '\t\t\tif context[' + "'" + 'criterio' + "'" + '] ==' + "'" + '*' + "'" + ':' + '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_03' + ']' + '\n'
        strv += '\t\t\t\tcontext[' + "'" + 'lista' + "'" + '] = @modelo.objects.all()' + '\n'
        strv += '\t\t\t# Si criterio es blaco no se buscan registros' + '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_04' + ']' + '\n'
        strv += '\t\t\telif context[' + "'" + 'criterio' + "'" + '] ==' + "'" + "'" + ':' + '\n'
        strv += '\t\t\t\tcontext[' + "'" + 'lista' + "'" +'] = None' + '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_05' + ']' + '\n'
        strv += '\t\t\telse:' + '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_06' + ']' + '\n'

        # ver que propiedades se buscan
        pb = ''
        for pr in Propiedad.objects.filter(modelo=modelo):
            if pr.participabusquedalista:
                tx = ''
                if pr.tipo == 's' or pr.tipo == 'd' or pr.tipo == 'e' or pr.tipo == 'h' or pr.tipo == 'i' or pr.tipo == 'l' or pr.tipo == 'm' or pr.tipo == 'n' or pr.tipo == 't' or pr.tipo == 'x':
                    tx = modelo.nombre + '.objects.filter(' + pr.nombre + '__icontains = context[' + "'" + 'criterio' + "'" + '])' 
                    if pb == '':
                        pb = tx
                    else:
                        pb += '|' + tx
                tx= ''
                if pr.tipo == 'f':
                    strv += '\t\t\t\tids = []' + '\n'
                    mf = Modelo.objects.get(nombre=pr.foranea,proyecto=proyecto)
                    strv += '\t\t\t\tfor os in ' + pr.foranea + '.objects.filter(' + mf.nombreborrar + '__contains = context[' + "'" + 'criterio' + "'" + ']):' + '\n'
                    strv += '\t\t\t\t\tids.append(os.id)' + '\n'
                    tx = modelo.nombre + '.objects.filter(' + pr.nombre + '__in = ids)'
                    if pb == '':
                        pb = tx
                    else:
                        pb += '|' + tx
                tx = ''
                if pr.tipo == 'r':
                    lb = ''
                    sb = ''
                    for rb in pr.textobotones.split(';'):
                        if lb == '':
                            lb = '"' + rb.split(',')[1] + '"'
                            sb = '"' + rb.split(',')[0] + '"'
                        else:
                            lb += ',' + '"' + rb.split(',')[1] + '"'
                            sb += ',' + '"' + rb.split(',')[0] + '"'
                    strv += '\t\t\t\tlb = [' + lb + ']' + '\n'
                    strv += '\t\t\t\tsb = [' + sb + ']' + '\n'
                    strv += '\t\t\t\tcb = []' + '\n'
                    strv += '\t\t\t\tfor os in range(0,len(lb)):' + '\n'
                    strv += "\t\t\t\t\tif context['criterio'] in lb[os]:" + '\n'
                    strv += '\t\t\t\t\t\tcb.append(sb[os])' + '\n'
                    tx = modelo.nombre + '.objects.filter(' + pr.nombre + '__in = cb)'
                    if pb == '':
                        pb = tx
                    else:
                        pb += '|' + tx

                    tx += '\n'
        strv += '\t\t\t\t# Se busca el criterio en todas las propiedades marcadas para ese fin' + '\n'
        if pb != '':
            strv += '\t\t\t\tcontext[' + "'" + 'lista' + "'" + '] = ' + pb + '\n'
        else:
            strv += '\t\t\t\tcontext[' + "'" + 'criterio' + "'" + '] = ' + "'" + "'" + '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_07' + ']' + '\n'
        strv += '\t\texcept:' '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_08' + ']' + '\n'
        strv += '\t\t\t# En caso de error no se buscan registros' + '\n'
        strv += '\t\t\tcontext[' + "'" + 'criterio' + "'" + '] = ' + "'" + "'" + '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_09' + ']' + '\n'
    else:
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_01' + ']' + '\n'
        strv += '\t\tcontext[' + "'" + 'lista' + "'" + '] = @modelo.objects.all()' + '\n'
        strv += '#@[p_buscador_lista_' + modelo.nombre + '_02' + ']' + '\n'


    strv += '#@[p_listar_context_' + modelo.nombre + '_02' + ']' + '\n'
    strv += '\t\tcontext[' + "'" + 'unico' + "'" + '] = ' + "'" + '0' + "'" + '\n'
    
    # Registro unico
    if modelo.registrounico:
        strv += '\t\tif context[' + "'" + 'lista' + "'" + '].count()>0:' + '\n'
        strv += '#@[p_registro_unico_' + modelo.nombre + '_01' + ']' + '\n'
        strv += '\t\t\tcontext[' + "'" + 'unico' + "'" + '] = ' + "'" + '1' + "'" + '\n'

    # Propiedades que totalizan
    for pr in Propiedad.objects.filter(modelo=modelo):
        if pr.totaliza:
            strv += "\t\ttry:\n"
            strv += '#@[p_totaliza_' + modelo.nombre + '_' + pr.nombre + '_01' + ']' + '\n'
            strv += '\t\t\ttotal=0\n'
            strv += '#@[p_totaliza_' + modelo.nombre + '_' + pr.nombre + '_02' + ']' + '\n'
            strv += '\t\t\tfor reg in context["lista"]:\n'
            strv += '#@[p_totaliza_' + modelo.nombre + '_' + pr.nombre + '_03' + ']' + '\n'
            strv += '\t\t\t\ttotal += reg.' + pr.nombre + '\n'
            strv += '#@[p_totaliza_' + modelo.nombre + '_' + pr.nombre + '_04' + ']' + '\n'
            strv += '\t\t\tcontext["total_@totaliza_propiedad"] = total\n'
            strv += '#@[p_totaliza_' + modelo.nombre + '_' + pr.nombre + '_05' + ']' + '\n'
            strv += "\t\texcept:\n"
            strv += '#@[p_totaliza_' + modelo.nombre + '_' + pr.nombre + '_06' + ']' + '\n'
            strv += "\t\t\tpass\n"
            strv = strv.replace('@totaliza_propiedad',pr.nombre)

        if proyecto.conroles:
            strv += '\t\t# Controla si el usuario puede ver la propiedad: ' + pr.nombre + ' del modelo' + '\n'
            strv += '#@[p_puede_ver_' + modelo.nombre + '_' + pr.nombre + '_01' + ']' + '\n'
            strv += "\t\tcontext['puede_ver_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedever'" + ")" + '\n'

    # Ver si se controlan los roles

    if proyecto.conroles:
        strv += '\t\t# Controla si el usuario puede listar los registros del modelo' + '\n'
        strv += "\t\tif not roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedelistar'):" + '\n'
        strv += '#@[p_lista_roles_' + modelo.nombre + '_01' + ']' + '\n'
        strv += "\t\t\tcontext['lista'] = None" + '\n'
        strv += '#@[p_lista_roles_' + modelo.nombre + '_02' + ']' + '\n'
        strv += '\t\t# Controla si el usuario puede insertar registros al modelo' + '\n'
        strv += "\t\tcontext['puede_insertar'] = roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedeinsertar')" + '\n'
        strv += '#@[p_lista_roles_' + modelo.nombre + '_03' + ']' + '\n'
        strv += '\t\t# Controla si el usuario puede editar registros al modelo' + '\n'
        strv += "\t\tcontext['puede_editar'] = roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedeeditar')" + '\n'
        strv += '#@[p_lista_roles_' + modelo.nombre + '_04' + ']' + '\n'
        strv += '\t\t# Controla si el usuario puede borrar registros al modelo' + '\n'
        strv += "\t\tcontext['puede_borrar'] = roles.PuedeModelo('" + modelo.nombre + "',self.request.user.username,'puedeborrar')" + '\n'
        strv += '#@[p_lista_roles_' + modelo.nombre + '_05' + ']' + '\n'

    strv += '\t\treturn context' + '\n'

    strv = strv.replace('@aplicacionreal',aplicacion.nombre)
    strv = strv.replace('@aplicacion', aplicacion.nombre)
    strv = strv.replace('@modelo', modelo.nombre)

    strv += '\n'         
    return strv

def VistaEditarRaiz(proyecto,aplicacion, modelo):
    strv = '# Este modelo es independiente y esta vista' + '\n'
    strv += '# es la utilizada para la edicion de un registro' + '\n'
    strv += '# ya grabado en la Base de Datos' + '\n'
    if modelo.treeview:
        strv += '# Importar el arbol para despliegue TreeView' + '\n\n'
        strv += 'from core.views import Arbol' + modelo.nombre  + '\n\n'
    strv += '#@[p_editar_' + modelo.nombre + '_01]' + '\n' 
    strv += 'class Editar@modeloView(UpdateView):' + '\n'
    strv += '#@[p_editar_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t# Define el modelo' + '\n'
    strv += '\tmodel = @modelo' + '\n'
    strv += '#@[p_editar_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t# Define el formulario' + '\n'
    strv += '\tform_class = @modeloForm' + '\n'
    strv += '#@[p_editar_' + modelo.nombre + '_04]' + '\n' 
    strv += '\t# Define el HTML de edicion' + '\n'
    strv += '\ttemplate_name = ' + "'" + '@aplicacion/@modelo_update_form.html' + "'"  + '\n'
    strv += '#@[p_editar_' + modelo.nombre + '_05]' + '\n' 
    strv += '\n'                
    strv += '\t# Procedimiento de salida despues de actualizacion exitosa' + '\n'
    strv += '\tdef get_success_url(self):' + '\n'
    strv += '#@[p_editar_success_' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\t# Retorna al HTML de edicion con la comunicacion de correcta actualizacion' + '\n'
    strv += '\t\treturn reverse_lazy(' + "'" + '@aplicacion:editar_@modelo' + "'" + ', args=[self.object.id]) + ' + "'" + '?correcto' + "'"  + '\n'
    strv += '\n'                
    strv += '\t# Prepara los context para el HTML de edicion' + '\n'
    strv += '\tdef get_context_data(self,**kwargs):' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t\tcontext = super(Editar@modeloView, self).get_context_data(**kwargs)' + '\n'
    strv += '\t\t# Recupera el modelo a ser editado y envia su id' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t\t@modelo = (self.object)' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_04]' + '\n' 
    strv += '\t\tcontext["' + modelo.nombre + '"] = ' + modelo.nombre + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_05]' + '\n' 
    strv += '\t\tmodelo_current = (self.object)' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_06]' + '\n' 
    strv += '\t\tcontext[' + "'" + '@modelo_id' + "'" + '] = modelo_current.id' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_07]' + '\n' 
    strv += '@listahijos' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_08]' + '\n' 
    strv += '\t\t# Envia el context con la identificacion que se dio al borrado' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_09]' + '\n' 
    strv += '\t\tcontext[' + "'" + 'nombre' + "'" + '] = @paraborrar' + '\n'
    strv += '#@[p_editar_context_' + modelo.nombre + '_10]' + '\n' 

    # define si existe un numero de registros para los hijos
    for hijo in Modelo.objects.filter(padre=modelo.nombre, proyecto=proyecto ):
        strv += '\t\t# Envia el context con el numero de modelos dependientes' + '\n'
        strv += '\t\tcontext[' + "'" + 'numero' + hijo.nombre + "'" + '] = ' + hijo.nombre + '.objects.filter(@modelo=@modelo).count()' + '\n'

    strv += '#@[p_editar_context_' + modelo.nombre + '_11]' + '\n' 

    if modelo.treeview:

        strv += '\t\t# Envia al template de edicion el listado de TreeView de acuerdo al esquema' + '\n'
        strv += '\t\ttry:' + '\n'
        strv += '#@[p_editar_treeview_' + modelo.nombre + '_01]' + '\n' 
        strv += '\t\t\tnudo = self.request.GET["padre"]' + '\n'
        strv += '#@[p_editar_treeview_' + modelo.nombre + '_02]' + '\n' 
        strv += '\t\t\tcontext["listar"] = Arbol' + modelo.nombre + '(nudo,0)' + '\n'
        strv += '#@[p_editar_treeview_' + modelo.nombre + '_03]' + '\n' 
        strv += '\t\texcept:' + '\n'
        strv += '#@[p_editar_treeview_' + modelo.nombre + '_04]' + '\n' 
        strv += '\t\t\tcontext["listar"] = Arbol' + modelo.nombre + '("",0)' + '\n'
        strv += '#@[p_editar_treeview_' + modelo.nombre + '_05]' + '\n' 

    if modelo.proyecto.conroles:
        for pr in Propiedad.objects.filter(modelo=modelo):
            strv += '\t\t# Controla si el usuario puede editar el valor a la propiedad: ' + pr.nombre + ' del modelo' + '\n'
            strv += "\t\tcontext['puede_ver_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedever')" + '\n'
            strv += '#@[p_editar_conroles_' + modelo.nombre + '_01]' + '\n' 
            strv += "\t\tcontext['puede_editar_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeeditar')" + '\n'
            strv += "\t\tcontext['puede_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeeditar')" + '\n'
            strv += '#@[p_editar_conroles_' + modelo.nombre + '_02]' + '\n' 

    strv += '\t\treturn context' + '\n'

    strv = strv.replace('@aplicacionreal',aplicacion.nombre)
    strv = strv.replace('@aplicacion', aplicacion.nombre)
    strv = strv.replace('@modelo', modelo.nombre)

    strv += '\n'         
    return strv

def VistaCrearRaiz(proyecto, aplicacion,modelo):
    strv = '# Este modelo es independiente y esta vista' + '\n'
    strv += '# es la utilizada para la insercion de un nuevo registro' + '\n'
    strv += '# en la Base de Datos' + '\n'
    strv += '#@[p_crear_' + modelo.nombre + '_01]' + '\n' 
    strv += 'class Crear@modeloView(CreateView):' + '\n'
    strv += '#@[p_crear_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t# Define el modelo cuyo registro se inserta' + '\n'
    strv += '\tmodel = @modelo' + '\n'
    strv += '\t# Define el formulario de controles' + '\n'
    strv += '\tform_class = @modeloForm' + '\n'
    strv += '#@[p_crear_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t# Define el HTML de insercion' + '\n'
    strv += '\ttemplate_name = ' + "'" + '@aplicacion/@modelo_form.html' + "'"  + '\n'
    strv += '#@[p_crear_' + modelo.nombre + '_04]' + '\n' 
    # strv += '\tsuccess_url = reverse_lazy(' + "'" + '@aplicacion:listar_@modelo' + "'" + ')' + '\n'
    strv += '\n'                
    strv += '\t# Procedimiento de retorno por insercion exitosa' + '\n'
    strv += '\tdef get_success_url(self):' + '\n'
    strv += '#@[p_crear_success_' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\t# Retorna al HTML de la lista de registros del modelo' + '\n'
    strv += '\t\treturn reverse_lazy(' + "'" + '@aplicacion:listar_@modelo' + "'" + ') + ' + "'" + '?correcto' + "'"  + '\n'
    strv += '\t# Prepara los context de insercion' + '\n'
    strv += '\tdef get_context_data(self,**kwargs):' + '\n'
    strv += '#@[p_crear_context' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\tcontext = super(Crear@modeloView, self).get_context_data(**kwargs)' + '\n'
    strv += '#@[p_crear_context' + modelo.nombre + '_02]' + '\n' 

    if modelo.proyecto.conroles:
        for pr in Propiedad.objects.filter(modelo=modelo):
            strv += '\t\t# Controla si el usuario puede asignar el valor a la propiedad: ' + pr.nombre + ' del modelo' + '\n'
            strv += "\t\tcontext['puede_ver_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedever')" + '\n'
            strv += '#@[p_crear_context' + modelo.nombre + '_03]' + '\n' 
            strv += "\t\tcontext['puede_asignar_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeasignarvalor')" + '\n'
            strv += "\t\tcontext['puede_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedeasignarvalor')" + '\n'
            strv += '#@[p_crear_context' + modelo.nombre + '_04]' + '\n' 
    strv += '\t\treturn context' + '\n'

    # El modelo tiene una propiedad tipo usuario
    strp = ''
    prop = ModeloConPropiedadUsuario(modelo)
    if prop != None:
        if proyecto.conseguridad:
            strp = '\t# El modelo fue definido con la opcion de seguridad' + '\n'
            strp += '\tdef post(self,request,*args,**kwargs):' + '\n'
            strp += '#@[p_crear_post_' + modelo.nombre + '_01]' + '\n' 
            strp += '\t\t# Recupera el formulario con el nuevo registro del modelo' + '\n'
            strp += '\t\tform = self.form_class(request.POST,request.FILES)' + '\n'
            strp += '#@[p_crear_post_' + modelo.nombre + '_02]' + '\n' 
            strp += '\t\t# Recupera el usuario' + '\n'
            strp += '\t\tuser = request.user' + '\n'
            strp += '#@[p_crear_post_' + modelo.nombre + '_03]' + '\n' 
            strp += '\t\tif form.is_valid():' + '\n'
            strp += '#@[p_crear_post_' + modelo.nombre + '_04]' + '\n' 
            strp += '\t\t\t# Prepara al modelo para grabacion pero sin commit' + '\n'
            strp += '\t\t\t@modelo = form.save(commit=False)' + '\n'
            strp += '#@[p_crear_post_' + modelo.nombre + '_05]' + '\n' 
            strp += '\t\t\t# Asigna al registro el campo de usuario' + '\n'
            strp += '\t\t\t@modelo.@propiedad = user' + '\n'
            strp += '#@[p_crear_post_' + modelo.nombre + '_06]' + '\n' 
            strp += '\t\t\t# Graba el registro definitivamente en la base de datos' + '\n'
            strp += '\t\t\t@modelo.save()' + '\n'
            strp += '#@[p_crear_post_' + modelo.nombre + '_07]' + '\n' 
            strp += '\t\t\t# Envia el control al procedimiento de inserecion exitosa' + '\n'
            strp += '\t\t\treturn HttpResponseRedirect(self.get_success_url())' + '\n'
            strp += '#@[p_crear_post_' + modelo.nombre + '_08]' + '\n' 
            strp += '\t\t# Envia el control nuevamente al HTML de insercion' + '\n'
            strp += '\t\treturn render(request, ' + "'" + '@aplicacion/@modelo_form.html' + "'" + ', {' + "'" + 'form' + "'" + ': form})' + '\n'
            strp += '#@[p_crear_post_' + modelo.nombre + '_09]' + '\n' 

            strp = strp.replace('@modelo',modelo.nombre)
            strp = strp.replace('@aplicacion',aplicacion.nombre)
            strp = strp.replace('@propiedad',prop.nombre)
    strv += strp

    strv = strv.replace('@aplicacionreal',aplicacion.nombre)
    strv = strv.replace('@aplicacion', aplicacion.nombre)
    strv = strv.replace('@modelo', modelo.nombre)

    strv += '\n'        
    return strv

def VistaBorrarRaiz(proyecto,aplicacion,modelo):
    strv = '# Este modelo es independiente y esta vista' + '\n'
    strv += '# es la utilizada para el borrado de un registro' + '\n'
    strv += '# ya grabado en la Base de Datos' + '\n'
    strv += '#@[p_borrar_' + modelo.nombre + '_01]' + '\n' 
    strv += 'class Borrar@modeloView(DeleteView):' + '\n'
    strv += '#@[p_borrar_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t# Define le modelo a borrar' + '\n'
    strv += '\tmodel = @modelo' + '\n'
    strv += '#@[p_borrar_' + modelo.nombre + '_03]' + '\n' 
    # strv += '\tsuccess_url = reverse_lazy(' + "'" + '@aplicacion:listar_@modelo' + "'" + ')' + '\n'
    strv += '\t# Define el HTML de borrado' + '\n'
    strv += '\ttemplate_name = ' + "'" + '@aplicacion/@modelo_confirm_delete.html' + "'"  + '\n'
    strv += '#@[p_borrar_' + modelo.nombre + '_04]' + '\n' 
    strv += '\n'                
    strv += '\t# Procedimiento de retorno por borrado exitoso' + '\n'
    strv += '\tdef get_success_url(self):' + '\n'
    strv += '#@[p_borrar_success_' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\t# Retorna al HTML de lista de registros del modelo' + '\n'
    strv += '\t\treturn reverse_lazy(' + "'" + '@aplicacion:listar_@modelo' + "'" + ') + ' + "'" + '?correcto' + "'"  + '\n'
    strv += '\t# Prepara los context de borrado' + '\n'
    strv += '\tdef get_context_data(self,**kwargs):' + '\n'
    strv += '#@[p_borrar_context_' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\tcontext = super(Borrar@modeloView, self).get_context_data(**kwargs)' + '\n'
    strv += '\t\t# Recupera el modelo a borrar y envia su id' + '\n'
    strv += '#@[p_borrar_context_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t\tmodelo_current = @modelo.objects.get(id=self.object.id)' + '\n'
    strv += '#@[p_borrar_context_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t\tcontext[' + "'" + 'nombreborrar' + "'" + '] = @paraborrar' + '\n'
    strv += '#@[p_borrar_context_' + modelo.nombre + '_04]' + '\n' 

    if modelo.proyecto.conroles:
        strv += '\t\t# Controla si el usuario puede borrar registros al modelo' + '\n'
        strv += "\t\tcontext['puede_borrar'] = roles.PuedeBorrar('" + modelo.nombre + "',self.request.user.username)" + '\n'

    strv += '#@[p_borrar_context_' + modelo.nombre + '_05]' + '\n' 


    strv += '\t\treturn context' + '\n\n'
    strv = strv.replace('@aplicacionreal',aplicacion.nombre)
    strv = strv.replace('@aplicacion', aplicacion.nombre)
    strv = strv.replace('@modelo', modelo.nombre)    
    return strv

def VistaModeloSinBase(aplicacion,modelo):
    strv = '#@[p_@modelo_sinbase_01]' + '\n'
    strv += '# Define la unica vista para el modelo que no se graba en la Base de Datos' + '\n'
    strv += 'class @modeloView(FormView):' + '\n'
    strv += '#@[p_@modelo_view_01]' + '\n'
    strv += '\t# Define el HTML que despliega los controles' + '\n'
    strv += '\ttemplate_name = ' + "'" + '@aplicacion/@modelo_sinbase.html' + "'" + '\n'
    strv += '\t# Define el formulario de los controles' + '\n'
    strv += '\tform_class = @modeloForm' + '\n'
    strv += '#@[p_@modelo_view_02]' + '\n'
    strv += '\t# Procedimiento de retorno' + '\n'
    strv += '\tdef get_success_url(self):' + '\n'
    strv += '#@[p_@modelo_success_01]' + '\n'
    strv += '\t\t# Retorna al encabezado el proyecto' + '\n'
    strv += '\t\treturn reverse_lazy(' + "'" + 'core:home' + "'" + ')' + '\n'
    strv += '#@[p_@modelo_success_02]' + '\n'

    strv = strv.replace('@modelo', modelo.nombre)
    strv = strv.replace('@aplicacion',aplicacion.nombre)

    return strv

def PropiedadDash(prop, modelo):
    strv = ''
    if prop.tipo == 'b':
        strv = 'reg_@modelo.' + prop.nombre + ' ? 1 : 0'
    if prop.tipo =='d' or prop.tipo == 'i' or prop.tipo =='l' or prop.tipo =='m':
        strv =  'reg_@modelo.' + prop.nombre  
    if prop.tipo =='n' or prop.tipo == 't' or prop.tipo =='e':
        strv =  'reg_@modelo.' + prop.nombre 
    if prop.tipo =='s':
        strv =  'reg_@modelo.' + prop.nombre 
    if prop.tipo =='r':
        strv =  'reg_@modelo.' + prop.nombre 
    if prop.tipo == 'f':
        mode_for = Modelo.objects.get(nombre = prop.foranea,proyecto = modelo.proyecto)
        strv = 'reg_@modelo.' + prop.nombre + '.' + mode_for.nombreborrar
    strv = strv.replace('@modelo', modelo.nombre)
    return strv

def VistaDashBoard(modelo, proyecto):

    strv = 'class Dash@modeloView(FormView):' + '\n'
    strv += '\t# Definir el modelo a utilizar' + '\n'
    strv += '#@[p_dash_' + modelo.nombre + '_01]' + '\n' 
    strv += '\tform_class = Dash@modeloForm' + '\n'
    strv += '#@[p_dash_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t# Especificar el template HTML' + '\n'
    strv += '#@[p_dash_' + modelo.nombre + '_03]' + '\n' 
    strv += '\ttemplate_name = "' + modelo.aplicacion.nombre + '/' + 'dash_' + modelo.nombre + '.html"' + '\n'
    strv += '#@[p_dash_' + modelo.nombre + '_04]' + '\n' 
    strv += '\tdef get_success_url(self):' + '\n'
    strv += '# Retorna al HTML de la lista de registros del modelo' + '\n'
    strv += '\t\treturn reverse_lazy("@aplicacion:listar_@modelo")' + '\n'
    strv += '\t# Prepara los context para el HTML' + '\n'
    strv += '\tdef get_context_data(self,**kwargs):' + '\n'
    strv += '#@[p_dash_' + modelo.nombre + '_05]' + '\n' 
    strv += '\t\tcontext = super(Dash@modeloView, self).get_context_data(**kwargs)' + '\n'
    strv = strv.replace('@aplicacion',modelo.aplicacion.nombre)
    lista = []
    listaTexto=[]
    lista_retorno,listaTexto = RecursivoListasRetorno(modelo,lista,listaTexto)
    strTexto = ''
    for reg in lista_retorno:
        if strTexto == '':
            strTexto = reg
        else:
            strTexto += ',' + reg
    strv += '\t\t' + strTexto + ' = Dash@modelo()' + '\n'
    strv += '\t\treturn context' + '\n'
    strv += '\n'
    strv += 'def Dash@modelo():' + '\n'
    for reg in lista:    
        strv += '\t' + reg + ' = []' + '\n'
    for reg in listaTexto:    
        strv += '\t' + reg + ' = []' + '\n'

       # ('b','Boolean'),
       #  ('d','Decimal'),
       #  ('e','Hora'),
       #  ('f','Foranea'),
       #  ('h','RichText'),
       #  ('i','Entero'),
       #  ('l','Entero largo'),
       #  ('m','Entero pequeno'),
       #  ('n','Fecha'),
       #  ('p','Imagen'),
       #  ('r','Radio Button'),
       #  ('s','String'),
       #  ('t','Hora y Fecha'),
       #  ('u','Usuario'),
       #  ('x','Text Field'),

    strv += '\tconexion=sqlite3.connect("db.sqlite3")' + '\n'

    listac = []
    RetornarListaModelos(modelo,listac)
    strSelect = ''
    for grupo in listac:
        strInner = ''
        strt = ''
        strFrom = ''
        lm = grupo.split(',')
        strt = ''
        strLista = 'lista'
        columnas = ''
        for i in range(len(lm)):
            mod = Modelo.objects.get(id=int(lm[i]))
            strLista += '_' + mod.nombre
            for prop in Propiedad.objects.filter(modelo = mod, dashboard = True):
                if prop.tipo == 'f':
                    mf = Modelo.objects.get(nombre=prop.foranea,proyecto=modelo.proyecto)
                    for propf in Propiedad.objects.filter(modelo=mf,dashboard=True):
                        if propf.tipo == 'f':
                            mff = Modelo.objects.get(nombre=propf.foranea,proyecto=modelo.proyecto)
                            if columnas == '':
                                columnas = "'" + mff.nombre + "'"
                            else:
                                columnas += ",'" + mff.nombre + "'"
                            if strt == '':
                                strt += '@aplicacion_' + mff.nombre + '.' + mff.nombreborrar
                            else:
                                strt += ',@aplicacion_' + mff.nombre + '.' + mff.nombreborrar
                            strInner += " inner join @aplicacion_" + mff.nombre
                            strInner += " on @aplicacion_" + mf.nombre + "." + propf.nombre + "_id = " + '@aplicacion_' + mff.nombre + '.id' 
                        else:
                            if columnas == '':
                                columnas = "'" + mf.nombre + "_" + propf.nombre + "'"
                            else:
                                columnas += ",'" + mf.nombre + "_" + propf.nombre + "'"
                            if strt == '':
                                strt += '@aplicacion_' + mf.nombre + '.' + propf.nombre
                            else:
                                strt += ',@aplicacion_' + mf.nombre + '.' + propf.nombre
                    # np += '_id'
                    strInner += " inner join @aplicacion_" + mf.nombre
                    strInner += " on @aplicacion_" + mod.nombre + "." + prop.nombre + "_id = " + '@aplicacion_' + mf.nombre + '.id' 

                else:
                    np = prop.nombre
                    if columnas == '':
                        columnas = "'" + np + "'"
                    else:
                        columnas += ",'" + np + "'"
                    if strt == '':
                        strt += '@aplicacion_' + mod.nombre + '.' + np
                    else:
                        strt += ',@aplicacion_' + mod.nombre + '.' + np
            if mod.padre != 'nada':
                mod_1 = Modelo.objects.get(id=int(lm[i-1]))
                strInner += " inner join @aplicacion_" + mod.nombre
                strInner += " on @aplicacion_" + mod.nombre + "." + mod_1.nombre + "_id = " + '@aplicacion_' + mod_1.nombre + '.id' 
            else:
                strFrom = ' from @aplicacion_' + mod.nombre + " "
        if strt != '':
            strSelect = 'select  @propiedades @from @inner'
            strSelect = strSelect.replace('@inner',strInner)
            strSelect = strSelect.replace('@from',strFrom)
            strSelect = strSelect.replace('@propiedades',strt)
            strSelect = strSelect.replace('@aplicacion',modelo.aplicacion.nombre)
            # obtener el nombre de la lista
            strv += '\tlista = conexion.execute("' + strSelect + '")' + '\n'
            strv += '\tfor fila in lista:' + '\n'
            strv += '\t\t' + strLista + '.append(fila)' + '\n'
            strv += '\t' + strLista + ' = pd.DataFrame(' + strLista + ')' + '\n'
            strv += '\t' + strLista + '.columns = [' + columnas + ']' + '\n'
    strv += '\tconexion.close()' + '\n'

    strr = ''
    for reg in lista:
        if strr == '':
            strr = reg
        else:
            strr += ',' + reg
    strv += '\treturn ' + strr + '\n' 
    strv += '\n'
    return strv

def RetornarListaModelos(modelo,lista):
    if modelo.padre == 'nada':
        lista.append(str(modelo.id))
    else:
        prev = str(modelo.id)
        mod = copy.copy(modelo)
        while mod.padre != 'nada':
            mod = Modelo.objects.get(nombre=mod.padre, proyecto=modelo.proyecto)
            prev = str(mod.id) + ',' + prev
        lista.append(prev)
    for mod_hijo in Modelo.objects.filter(padre=modelo.nombre, proyecto=modelo.proyecto):
        RetornarListaModelos(mod_hijo, lista)

def VistaFill(modelo, proyecto):
    strv = 'class Fill@modeloView(FormView):' + '\n'
    strv += '\t# Definir el modelo a utilizar' + '\n'
    strv += '#@[p_fill_' + modelo.nombre + '_01]' + '\n' 
    strv += '\tform_class = Fill@modeloForm' + '\n'
    strv += '#@[p_fill_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t# Especificar el template HTML' + '\n'
    strv += '\ttemplate_name = "@aplicacion/@modelo_fill.html"' + '\n\n'
    strv += '#@[p_fill_' + modelo.nombre + '_03]' + '\n' 
    strv += '\tdef get_success_url(self):' + '\n'
    strv += '#@[p_fill_' + modelo.nombre + '_04]' + '\n' 
    strv += '\t\treturn reverse_lazy("@aplicacion:fill_@modelo")' + '\n'

    strv += '\tdef get_context_data(self,**kwargs):' + '\n'
    strv += '\t\tcontext = super(Fill@modeloView, self).get_context_data(**kwargs)' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_01]' + '\n' 
    strv += '\t\tcontext["nombremodelo"] = "@modelo"' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_02]' + '\n' 
    strv += '\t\ttry:' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_03]' + '\n' 
    strv += '\t\t\tdestruye = self.request.GET.get("destruye")' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_04]' + '\n' 
    strv += '\t\t\tif destruye:' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_05]' + '\n' 
    strv += '\t\t\t\tpass' + '\n'
    lista = []
    BarreModelosFill(modelo,'',lista,'\t\t\t\t')
    for txt in lista:
        strv += txt + '\n'
    strv += '\t\texcept Exception as e:' + '\n'
    strv += '\t\t\tprint(str(e))' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_06]' + '\n' 
    strv += '\t\treturn context' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_07]' + '\n' 
    strv += '\tdef get_form(self,form_class=None):' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_08]' + '\n' 
    strv += '\t\tform = super(Fill@modeloView, self).get_form()' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_09]' + '\n' 
    strv += '\t\t#Modificar en tiempo real' + '\n'
    strv += '\t\tform.fields["destruye"].widget = forms.CheckboxInput()' + '\n'
    strv += '#@[p_fill_context_' + modelo.nombre + '_10]' + '\n' 
    strv += '\t\treturn form' + '\n'

    strv = strv.replace('@modelo', modelo.nombre)
    strv = strv.replace('@aplicacion', modelo.aplicacion.nombre)
    return strv

def BarreModelosFill(modelo,papa,lista,tabs):
    lista.append(tabs + 'numero_' + modelo.nombre + 's = range(random.randint(6,30))')
    lista.append(tabs + 'for num_' + modelo.nombre + ' in numero_' + modelo.nombre + 's:')
    lista.append(tabs + '\t' + 'nuevo_' + modelo.nombre + ' = ' + modelo.nombre + '()')
    FillPropiedad(modelo,lista,tabs+'\t')
    tabs += '\t'
    if papa != '':
        lista.append(tabs + 'nuevo_' + modelo.nombre + '.' + papa + ' = nuevo_' + papa )
    lista.append(tabs + 'nuevo_' + modelo.nombre + '.save()')
    for mod in Modelo.objects.filter(padre=modelo.nombre,proyecto=modelo.proyecto):
        papa = modelo.nombre
        BarreModelosFill(mod,papa,lista,tabs)

import random
def FillPropiedad(modelo,lista,tabs):
        # ('b','Boolean'),
        # ('d','Decimal'),
        # ('e','Hora'),
        # ('f','Foranea'),
        # ('h','RichText'),
        # ('i','Entero'),
        # ('l','Entero largo'),
        # ('m','Entero pequeno'),
        # ('n','Fecha'),
        # ('p','Imagen'),
        # ('r','Radio Button'),
        # ('s','String'),
        # ('t','Hora y Fecha'),
        # ('u','Usuario'),
        # ('x','Text Field'),

    for prop in Propiedad.objects.filter(modelo=modelo):
        nombre = prop.modelo.nombre
        fill = prop.randomfill
        if prop.tipo == 's' or prop.tipo == 'x' or prop.tipo == 'h':
            if fill == '':
                RandomVacio(prop,lista,tabs)
                lista.append(tabs + 'nuevo_' + prop.modelo.nombre + '.' + prop.nombre + ' = random.choice(' + 'lista_' + prop.nombre + '' + ')')
            else:
                fill = fill.split(',')
                txt = ''
                for os in fill:
                    if txt == '':
                        txt = '"' + os + '"'
                    else:
                        txt += ',' + '"' + os + '"'
                fill = txt
                lista.append(tabs + 'valor = random.choice((' + '[' + fill + ']' + '))')
                lista.append(tabs + 'nuevo_' + prop.modelo.nombre + '.' + prop.nombre + ' = valor')
        if prop.tipo == 'b':
            lista.append(tabs + 'nuevo_' + nombre + '.' + prop.nombre + ' = random.choice([True, False])')
        if prop.tipo == 'd':
            if fill == '':
                fill = '120,350'
            lista.append(tabs + 'nuevo_' + nombre + '.' + prop.nombre + ' = random.uniform(' + fill + ')')
        if prop.tipo == 'e':
            if fill == '':
                fill = '2000,1,1;2023,12,31'.split(';')
            else:
                fill = fill.split(';')
            txt = ''
            lista.append(tabs + 'inicio = datetime.date(' + fill[0] + ')')
            lista.append(tabs + 'final =  datetime.date(' + fill[1] + ')')
            lista.append(tabs + 'random_date = inicio + (final - inicio) * random.random()')
            lista.append(tabs + 'dia = (random_date.day)')
            lista.append(tabs + 'mes = (random_date.month)')
            lista.append(tabs + 'anio = (random_date.year)')
            lista.append(tabs + 'hora = (random_date.hour)')
            lista.append(tabs + 'minuto = (random_date.minute)')
            lista.append(tabs + 'segundo = (random_date.second)')
            lista.append(tabs + 'nuevo_' + prop.modelo.nombre + '.' + prop.nombre + ' = datetime.time(hora,minuto,segundo)')
            # lista.append(tabs + 'nuevo_' + nombre + '.' + prop.nombre + ' = ' + str('"10:23:16"'))
        if prop.tipo == 'f':
            lista.append(tabs + 'lista_' + prop.foranea + ' = ' + prop.foranea + '.objects.all()')
            lista.append(tabs + 'codigo_' + prop.foranea + ' = lista_' + prop.foranea + '[random.randint(0,lista_' + prop.foranea + '.count()-1)]')
            lista.append(tabs + 'nuevo_' + prop.modelo.nombre + '.' + prop.foranea + ' = codigo_' + prop.foranea)
        if prop.tipo == 'i' or prop.tipo == 'l' or prop.tipo == 'm':
            if fill == '':
                fill = '100000,999999'
            lista.append(tabs + 'nuevo_' + nombre + '.' + prop.nombre + ' = random.randint(' + fill + ')')
        if prop.tipo == 'n':
            if fill == '':
                fill = '2000,1,1;2023,12,31'.split(';')
            else:
                fill = fill.split(';')
            txt = ''
            lista.append(tabs + 'inicio = datetime.datetime(' + fill[0] + ')')
            lista.append(tabs + 'final =  datetime.datetime(' + fill[1] + ')')
            lista.append(tabs + 'random_date = inicio + (final - inicio) * random.random()')
            lista.append(tabs + 'dia = (random_date.day)')
            lista.append(tabs + 'mes = (random_date.month)')
            lista.append(tabs + 'anio = (random_date.year)')
            lista.append(tabs + 'nuevo_' + prop.modelo.nombre + '.' + prop.nombre + ' = datetime.date(anio,mes,dia)')
        if prop.tipo == 'r':
            if fill == '':
                fill = 'p,primero;s,segundo;t,tercero;c,cuarto;q,quinto'.split(';')
            else:
                fill = fill.split(';')
            txt = ''
            for os in fill:
                if txt == '':
                    txt = '"' + os.split(',')[0] + '"'
                else:
                    txt += ',' + '"' + os.split(',')[0] + '"'
            fill = txt
            lista.append(tabs + 'nuevo_' + prop.modelo.nombre + '.' + prop.nombre + ' = random.choice((' + '[' + fill + ']' + '))')
        if prop.tipo == 't':
            if fill == '':
                fill = '2000,1,1;2023,12,31'.split(';')
            else:
                fill = fill.split(';')
            txt = ''
            lista.append(tabs + 'inicio = datetime.datetime(' + fill[0] + ')')
            lista.append(tabs + 'final =  datetime.datetime(' + fill[1] + ')')
            lista.append(tabs + 'random_date = inicio + (final - inicio) * random.random()')
            lista.append(tabs + 'dia = random_date.day')
            lista.append(tabs + 'mes = random_date.month')
            lista.append(tabs + 'anio = random_date.year')
            lista.append(tabs + 'hora = random_date.hour')
            lista.append(tabs + 'minuto = random_date.minute')
            lista.append(tabs + 'segundo = random_date.second')
            lista.append(tabs + 'nuevo_' + prop.modelo.nombre + '.' + prop.nombre + ' = datetime.datetime(anio,mes,dia,hora,minuto,segundo)')
        if prop.tipo == 'u':
            lista.append(tabs + 'nuevo_' + prop.modelo.nombre + '.' + prop.nombre + ' = self.request.user')

def RandomVacio(prop, lista,tabs):
    valoreselegir = prop.valoreselegir
    prefijo = 'Campo '
    if prop.valoreselegir != 1:
        valoreselgir = prop.valoreselegir                
    if prop.prefijofill != '':
        prefijo = prop.prefijofill
    lista.append(tabs + 'lista_' + prop.nombre + '=[]')
    lista.append(tabs + 'for i in range(' + str(valoreselegir) + '):')
    lista.append(tabs + '\t' + 'lista_' + prop.nombre + '.append(' + '"' + prefijo + ' "' + ' + str(i))')    

# def FormaDash(nombreModelo,proyecto,lista,tab,modelo):
#     for modhijo in Modelo.objects.filter(padre=nombreModelo,proyecto=proyecto):
#         # Buscar el modelo primer hijo del modelo raiz
#         nivSup = False
#         idSup = modhijo.id
#         modSup = modhijo
#         while not nivSup:
#             idSup = Modelo.objects.get(nombre=modSup.padre,proyecto=proyecto).id
#             if idSup == modelo.id:
#                 nivSup = True
#             else:
#                 modSup = Modelo.objects.get(id=idSup)

#         # lista.append(tab + '\t' + 'strTexto_' + modhijo.nombre + ' = [] ' + '\n')
#         lista.append(tab + '\t' + 'if ' + modhijo.nombre + '.objects.filter(' + nombreModelo + '= reg_' + nombreModelo + ').count()==0:' + '\n')
#         lista.append(tab + '\t\tfor reg in strTexto_' + nombreModelo + ':' + '\n')
#         lista.append(tab + '\t\t\tstrTexto_' + modhijo.nombre + '.append(reg)' + '\n')
#         # Busca todos los niveles a partir del modhijo
#         listaHijo=[]
#         strp = '"No' + modhijo.nombre  + '"'
#         lista.append(tab + '\t\t' + 'strTexto_' + modhijo.nombre + '.append(' + strp + ')\n')
#         RecursivoModelosHijo(modhijo,listaHijo)
#         if len(listaHijo) > 0:
#             for hijo in listaHijo:
#                 strp = '"No' + hijo.nombre + '"'
#                 lista.append(tab + '\t\t' + 'strTexto_' + modhijo.nombre + '.append(' + strp + ')\n')
#         lista.append(tab + '\t\t' + 'lista_' + modSup.nombre + '.append(strTexto_' + modhijo.nombre + ')\n')
#         lista.append(tab + '\t\t' + 'strTexto_' + modhijo.nombre + ' = []\n')

#         lista.append(tab + '\t' + 'else:' + '\n')
#         lista.append(tab + '\t\t' + 'for reg_' + modhijo.nombre + ' in ' + modhijo.nombre + '.objects.filter(' + nombreModelo + ' = reg_' + nombreModelo + '):' + '\n') 

#         lista.append(tab + '\t\t\tfor reg in strTexto_' + nombreModelo + ':' + '\n')
#         lista.append(tab + '\t\t\t\tstrTexto_' + modhijo.nombre + '.append(reg)' + '\n')

#         strp = ''
#         for prop in Propiedad.objects.filter(modelo=modhijo):
#             if prop.dashboard:
#                 strp = PropiedadDash(prop,modhijo)
#                 lista.append(tab + '\t\t\t' + 'strTexto_' + modhijo.nombre + '.append(' + strp + ')\n')

#         if Modelo.objects.filter(padre=modhijo.nombre,proyecto=proyecto).count() == 0:
#             # Estamos en el ultimo nivel de la rama
#             # Buscamos el modelo padre despues del primer hijo del proyecto
#             lista.append(tab + '\t\t\t' + 'lista_' + modSup.nombre + '.append(strTexto_' + modhijo.nombre + ')\n')        # lista.append(tab + '\tpass' + '\n')



#         strv = ''
#         strp = ''
#         for prop in Propiedad.objects.filter(modelo=modhijo):
#             if prop.dashboard:
#                 if strp == '':
#                     strp = PropiedadDash(prop,modhijo)
#                 else:
#                     strp += ' + "," + '+ PropiedadDash(prop,modhijo)
#         # Es el ultimo nivel para el modelo

#         FormaDash(modhijo.nombre,proyecto, lista,tab + '\t\t',modelo)

#         lista.append(tab + '\t\t\t' + 'strTexto_' + modhijo.nombre + ' = []\n')

# def FormaDash(nombreModelo,proyecto,lista,tab,modelo):
#     for modhijo in Modelo.objects.filter(padre=nombreModelo,proyecto=proyecto):
#         # Buscar el modelo primer hijo del modelo raiz
#         nivSup = False
#         idSup = modhijo.id
#         modSup = modhijo
#         while not nivSup:
#             idSup = Modelo.objects.get(nombre=modSup.padre,proyecto=proyecto).id
#             if idSup == modelo.id:
#                 nivSup = True
#             else:
#                 modSup = Modelo.objects.get(id=idSup)
#         listaHijo=[]
#         strp = ''
#         RecursivoModelosHijo(modhijo,listaHijo)
#         lista.append(tab + '\t' + 'for reg_' + modhijo.nombre + ' in ' + modhijo.nombre + '.objects.filter(' + nombreModelo + ' = reg_' + nombreModelo + '):' + '\n') 
#         recPref,recPrefSup = RecursivoPrefijo(modhijo,proyecto)
#         lista.append(tab + '\t\tfor reg in strTexto_' + recPrefSup + ':' + '\n')
#         lista.append(tab + '\t\t\tstrTexto_' + recPref + '.append(reg)' + '\n')
#         strp = ''
#         for prop in Propiedad.objects.filter(modelo=modhijo):
#             if prop.dashboard:
#                 strp = PropiedadDash(prop,modhijo)
#                 lista.append(tab + '\t\t' + 'strTexto_' + recPref + '.append(' + strp + ')\n')
#                 # Ver si la propiedad es 'f'
#                 if prop.tipo == 'f':
#                     mode_extra = Modelo.objects.get(nombre = prop.foranea,proyecto = modelo.proyecto)
#                     for pro in Propiedad.objects.filter(modelo=mode_extra):
#                         if pro.dashboard:
#                             if pro.tipo == 'f':
#                                 mode_extra_for = Modelo.objects.get(nombre = pro.foranea,proyecto = modelo.proyecto)
#                                 strv += '\t\treg_' + mode_extra_for.nombre + ' = ' + mode_extra_for.nombre + '.objects.get(id=' + 'reg_@modelo.' + prop.nombre + '.' + mode_extra_for.nombre + '.id' + ')' + '\n'
#                                 if strv == '':
#                                     strp += 'reg_' + mode_extra_for.nombre + '.' + mode_extra_for.nombreborrar
#                                 else:
#                                     strp += ',reg_' + mode_extra_for.nombre + '.' + mode_extra_for.nombreborrar
#                             else:
#                                 strv += '\t\treg_' + mode_extra.nombre + ' = ' + mode_extra.nombre + '.objects.get(id=' + 'reg_@modelo.' + prop.nombre + '.id'  + ')' + '\n'
#                                 if strp == '':
#                                     strp += 'reg_' + mode_extra.nombre + '.' + pro.nombre
#                                 else:
#                                     strp += ',reg_' + mode_extra.nombre + '.' + pro.nombre


#         lista.append(tab + '\t\t' + 'lista_' + recPref + '.append(strTexto_' + recPref + ')\n')        # lista.append(tab + '\tpass' + '\n')
#         strv = ''
#         strp = ''
#         for prop in Propiedad.objects.filter(modelo=modhijo):
#             if prop.dashboard:
#                 if strp == '':
#                     strp = PropiedadDash(prop,modhijo)
#                 else:
#                     strp += ' + "," + '+ PropiedadDash(prop,modhijo)
#         # Es el ultimo nivel para el modelo

#         FormaDash(modhijo.nombre,proyecto, lista,tab + '\t',modelo)

#         lista.append(tab + '\t\t' + 'strTexto_' + recPref + ' = []\n')

def RecursivoPrefijo(modelo,proyecto):
    mod = copy.copy(modelo)
    strPrefijoSup = ''
    strPrefijo = mod.nombre
    while mod.padre != 'nada':
        mod = Modelo.objects.get(nombre=mod.padre,proyecto=proyecto)
        strPrefijo = mod.nombre + '_' + strPrefijo
        if strPrefijoSup == '':
            strPrefijoSup = mod.nombre
        else:
            strPrefijoSup = mod.nombre + '_' + strPrefijoSup
    return strPrefijo,strPrefijoSup

from .models import ReporteNuevo

def VistaReporteEscalonado(proyecto, aplicacion, modelo, strr, stri):

    strr = strr.replace("@modelo",modelo.nombre)
    strr = strr.replace("@aplicacion",aplicacion.nombre)

    if modelo.reportsize == 'L':
        strr = strr.replace("@size",'letter')
    else:
        strr = strr.replace("@size",'A4')
        
    if modelo.reportorientation == 'L':
        strr = strr.replace("@orientacion",'landscape')
    else:
        strr = strr.replace("@orientacion",'portrait')

    # # lee la configuarcion del reporte
    reporte = ReporteNuevo.objects.get(reportesize=modelo.reportsize,orientacion=modelo.reportorientation)
    # # lee la configuarcion del reporte
    lista = []
    listatitulos = []
    listatotales = []
    RecursivoReporte(lista,listatitulos,listatotales,modelo,1,proyecto,reporte)
    strRec = ''
    for txt in listatitulos:
        strRec += txt
    strr = strr.replace('@controltitulos',strRec)
    strRec = ''
    for txt in lista:
        strRec += txt
    strr = strr.replace('@recorrido',strRec)
    strRec = ''
    for txt in listatotales:
        strRec += txt
    strr = strr.replace('@totales',strRec)
    # Impresion de la lista
    strr = strr.replace("@primeralinea",str(reporte.primeralinea))
    strr = strr.replace("@maxlineas",str(reporte.maxlineas))

    return strr, reporte

# def RecursivoReporte(lista,listatitulos,listatotales,modelo,nivel,proyecto,reporte,lineaix=0, datosix=0, titulox=0,padre=''):

#     if nivel == 1:
#         lineaix = modelo.lineaix
#         datosix = modelo.datoinicialx
#         titulox = modelo.titulox

#     tab = '    ' * nivel
#     dostab = '    ' * (nivel+1)
#     trestab = '    ' * (nivel+2)

#     listatitulos.append('    primer_' + modelo.nombre + ' = True\n')

#     strr = ''

#     # Titulo
#     strp = ''
#     delta = 0
#     pos = 1
#     identa = 0

#     if modelo.identacionautomatica and nivel>1:
#         identa  = (nivel-1)

#     if padre == '':
#         padre = modelo.nombre
#         strr += tab + 'for reg_@modelo in @modelo.objects.all():' + '\n'
#     else:
#         strr += tab + 'for reg_@modelo in @modelo.objects.filter(' + padre + '=' + 'reg_' + padre + '):' + '\n'
#         padre = modelo.nombre

#     strr += dostab + 'if primer_@modelo:' + '\n'
#     strr += trestab + 'datos_titulo = []' + '\n'
#     strr += trestab + 'datos_titulo.append([' + "'" + '@titulo' + "'" + ',@titulox])' + '\n'
#     strr += trestab + 'datos_titulo.append([@fecha,@fechax])' + '\n'
#     strr += trestab + 'datos_titulo.append(@iniciolineax)' + '\n'
#     strr += trestab + 'datos_titulo.append(@finallineax)' + '\n'
#     strr += trestab + 'datos_titulo.append(@grosor)' + '\n'

#     if modelo.identacionautomatica and nivel>1:
#         strr = strr.replace('@iniciolineax',str(lineaix+identa))
#         strr = strr.replace('@titulox',str(titulox+identa))
#     else:
#         strr = strr.replace('@iniciolineax',str(modelo.lineaix))
#         strr = strr.replace('@titulox',str(modelo.titulox))

#     strr = strr.replace('@fechax',str(modelo.fechax))
#     strr = strr.replace('@titulo',str(modelo.titulolista))
#     strr = strr.replace('@grosor',str(modelo.grosorlinea))

#     if nivel == 1:
#         strr = strr.replace('@fecha','True')
#     else:
#         strr = strr.replace('@fecha','False')

#     # Nombres de columnas
#     for prop in Propiedad.objects.filter(modelo = modelo):
#         if pos ==1:
#             pos +=1
#             if modelo.identacionautomatica and nivel>1:    
#                 strp += str(datosix + identa) + ',' + "'" + prop.nombre + "'"
#             else:
#                 strp += str(modelo.datoinicialx + identa) + ',' + "'" + prop.nombre + "'"
#         else:
#             strp += ',' + str(delta + identa) + ',' + "'" + prop.nombre + "'"
#         delta += modelo.datoinicialx + prop.anchoenreporte

#     strr += trestab  + 'datos_titulo.append([' + strp + '])' + '\n'
#     strr += trestab  + 'Acomoda(datos_detalle,datos_reporte,primeralinea,True,datos_titulo)' + '\n'
#     strr += trestab  + 'primer_@modelo=False' + '\n'

#     # Habilitar titulos de hijos

#     for modhijo in Modelo.objects.filter(padre=modelo.nombre,proyecto=proyecto):
#         strr += dostab  + 'primer_@modelohijo=True' + '\n'
#         strr = strr.replace('@modelohijo',modhijo.nombre)
        
#     strr += dostab + 'datos_reporte[0] += 1' + '\n'
#     strr += dostab + 'Acomoda(datos_detalle,datos_reporte,primeralinea,False,datos_titulo)' + '\n'

#     # Datos

#     strp = ''
#     delta = 0
#     pos = 1
#     identa = 0

#     if modelo.identacionautomatica and nivel>1:
#         identa  = (nivel-1)

#     for prop in Propiedad.objects.filter(modelo = modelo):
#         if prop.totaliza and (prop.tipo == 'd' or prop.tipo == 'i' or prop.tipo == 'l' or prop.tipo == 'm'):
#             listatotales.append('    total_' + modelo.nombre + '_' + prop.nombre + ' = 0' + '\n')
#             strr += dostab + 'nu_@propiedad = ' + "'" + '{:.2f}' + "'" + '.format(float(reg_@modelo.@propiedad))' + '\n'
#             strr += dostab + 'total_@modelo_@propiedad += float(reg_@modelo.@propiedad)' + '\n'
#             strr = strr.replace('@propiedad',prop.nombre)
#             strr = strr.replace('@modelo',modelo.nombre)
#             if pos ==1:
#                 pos +=1
#                 if modelo.identacionautomatica and nivel>1:        
#                     strr += dostab + 'datos_detalle.append([1,[' + "'" + 'Helvetica' + "'" + ',9,colors.black],[' + str(datosix + identa) + ',primeralinea-datos_reporte[1]],str(nu_' + prop.nombre + '),' + "'" + 'r' + "'" + '])' + '\n'
#                 else:
#                     strr += dostab + 'datos_detalle.append([1,[' + "'" + 'Helvetica' + "'" + ',9,colors.black],[' + str(modelo.datoinicialx + identa) + ',primeralinea-datos_reporte[1]],str(nu_' + prop.nombre + '),' + "'" + 'r' + "'" + '])' + '\n'
#             else:
#                 strr += dostab + 'datos_detalle.append([1,[' + "'" + 'Helvetica' + "'" + ',9,colors.black],[' + str(delta + identa) + ',primeralinea-datos_reporte[1]],str(nu_' + prop.nombre + '),' + "'" + 'r' + "'" + '])' + '\n'
        
#             if modelo.identacionautomatica and nivel>1:            
#                 delta += datosix + prop.anchoenreporte
#             else:
#                 delta += modelo.datoinicialx + prop.anchoenreporte
#         elif prop.tipo == 'p':
#             strr += dostab + 'try:' + '\n'
#             strr += trestab + 'cd = os.getcwd()' + '\n'
#             strr += trestab + 'img = cd + ' + "'" + '/' + "'" + ' + reg_cuenta.foto.url' + '\n'
#             strr += dostab + 'except:' + '\n'
#             strr += trestab + 'pass' + '\n'     
#             if pos ==1:
#                 pos +=1
#                 if modelo.identacionautomatica and nivel>1:            
#                     strr += dostab + 'datos_detalle.append([8,img,[' + str(datosix + identa) + ',primeralinea-datos_reporte[1]],[1/2.5,1/2.5]])' + '\n'
#                 else:
#                     strr += dostab + 'datos_detalle.append([8,img,[' + str(modelo.datoinicialx + identa) + ',primeralinea-datos_reporte[1]],[1/2.5,1/2.5]])' + '\n'
#             else:
#                 strr += dostab + 'datos_detalle.append([8,img,[' + str(delta + identa) + ',primeralinea-datos_reporte[1]],[1/2.5,1/2.5]])' + '\n'  
#         else:
#             if pos ==1:
#                 pos +=1
#                 if modelo.identacionautomatica and nivel>1:            
#                     strr += dostab + 'datos_detalle.append([1,[' + "'" + 'Helvetica' + "'" + ',9,colors.black],[' + str(datosix + identa) + ',primeralinea-datos_reporte[1]],str(reg_@modelo.' + prop.nombre + '),' + "'" + 'l' + "'" + '])' + '\n'
#                 else:
#                     strr += dostab + 'datos_detalle.append([1,[' + "'" + 'Helvetica' + "'" + ',9,colors.black],[' + str(modelo.datoinicialx + identa) + ',primeralinea-datos_reporte[1]],str(reg_@modelo.' + prop.nombre + '),' + "'" + 'l' + "'" + '])' + '\n'
#             else:
#                 strr += dostab + 'datos_detalle.append([1,[' + "'" + 'Helvetica' + "'" + ',9,colors.black],[' + str(delta + identa) + ',primeralinea-datos_reporte[1]],str(reg_@modelo.' + prop.nombre + '),' + "'" + 'l' + "'" + '])' + '\n'
        
#             if modelo.identacionautomatica and nivel>1:            
#                 delta += datosix + prop.anchoenreporte
#             else:
#                 delta += modelo.datoinicialx + prop.anchoenreporte

#     strr += dostab + 'datos_reporte[1] += 0.4' + '\n'

#     strr = strr.replace('@modelo',modelo.nombre)            

#     lista.append(strr)

#     for mod in Modelo.objects.filter(padre=modelo,proyecto=proyecto):
#         RecursivoReporte(lista,listatitulos,listatotales,mod,nivel+1,proyecto,modelo.nombre,lineaix,datosix,titulox,padre)

#     strp = ''
#     delta = 0
#     pos = 1
#     identa = 0

#     if modelo.identacionautomatica and nivel>1:
#         identa  = (nivel-1)

#     flgExisteTotaliza = False

#     strexp = ''
#     for prop in Propiedad.objects.filter(modelo = modelo):
#         if prop.totaliza and (prop.tipo == 'd' or prop.tipo == 'i' or prop.tipo == 'l' or prop.tipo == 'm'):
#             flgExisteTotaliza = True
#             strexp += dostab + 'total = ' + "'" + '{:.2f}' + "'" + '.format(float(total_@modelo_@propiedad))' + '\n'
#             strexp = strexp.replace('@propiedad',prop.nombre)
#             strexp = strexp.replace('@modelo',modelo.nombre)
#             if pos ==1:
#                 pos +=1
#                 if modelo.identacionautomatica and nivel>1:        
#                     strexp += dostab + 'datos_detalle.append([1,[' + "'" + 'Helvetica' + "'" + ',9,colors.black],[' + str(datosix + identa) + ',primeralinea-datos_reporte[1]],str(total),' + "'" + 'r' + "'" + '])' + '\n'
#                 else:
#                     strexp += dostab + 'datos_detalle.append([1,[' + "'" + 'Helvetica' + "'" + ',9,colors.black],[' + str(modelo.datoinicialx + identa) + ',primeralinea-datos_reporte[1]],str(total),' + "'" + 'r' + "'" + '])' + '\n'
#             else:
#                 strexp += dostab + 'datos_detalle.append([1,[' + "'" + 'Helvetica' + "'" + ',9,colors.black],[' + str(delta + identa) + ',primeralinea-datos_reporte[1]],str(total),' + "'" + 'r' + "'" + '])' + '\n'
        
#         else:
#             if pos == 1:
#                 pos += 1

#         if modelo.identacionautomatica and nivel>1:            
#             delta += datosix + prop.anchoenreporte
#         else:
#             delta += modelo.datoinicialx + prop.anchoenreporte

#     strs = tab + 'if not primer_@modelo:' + '\n'

#     if flgExisteTotaliza:
#         strs += dostab + 'datos_reporte[0] += 2' + '\n'
#         strs += dostab + 'Acomoda(datos_detalle,datos_reporte,primeralinea,False,datos_titulo)' + '\n'
#         if modelo.identacionautomatica and nivel>1:        
#             strs += dostab + 'datos_detalle.append([4,[@iniciolineax,primeralinea-datos_reporte[1]+0.2,@finallineax,primeralinea-datos_reporte[1]+0.2,0.3]])' + '\n'
#             strs = strs.replace('@iniciolineax',str(lineaix+identa))
#         else:
#             strs += dostab + 'datos_detalle.append([4,[@iniciolineax,primeralinea-datos_reporte[1]+0.2,@finallineax,primeralinea-datos_reporte[1]+0.2,0.3]])' + '\n'
#             strs = strs.replace('@iniciolineax',str(modelo.lineaix+identa))

#         strs += dostab + 'datos_reporte[1] += 0.13' + '\n'
#         strs += strexp
#         strs += dostab + 'datos_reporte[1] += 0.3' + '\n'
#         strs += dostab + 'datos_detalle.append([4,[@iniciolineax,primeralinea-datos_reporte[1]+0.2,@finallineax,primeralinea-datos_reporte[1]+0.2,0.3]])' + '\n'
#         strs += dostab + 'datos_detalle.append([4,[@iniciolineax,primeralinea-datos_reporte[1]+0.15,@finallineax,primeralinea-datos_reporte[1]+0.15,0.3]])' + '\n'
#         if modelo.identacionautomatica and nivel>1:        
#             strs = strs.replace('@iniciolineax',str(lineaix+identa))
#         else:
#             strs = strs.replace('@iniciolineax',str(modelo.lineaix+identa))        
#         strs += dostab + 'datos_reporte[1] += 0.3' + '\n'
#     else:
#         strs += dostab + 'datos_reporte[0] += 2' + '\n'
#         strs += dostab + 'Acomoda(datos_detalle,datos_reporte,primeralinea,False,datos_titulo)' + '\n'

#         strs += dostab + 'datos_detalle.append([4,[@iniciolineax,primeralinea-datos_reporte[1]+0.2,@finallineax,primeralinea-datos_reporte[1]+0.2,0.3]])' + '\n'
#         strs += dostab + 'datos_detalle.append([4,[@iniciolineax,primeralinea-datos_reporte[1]+0.15,@finallineax,primeralinea-datos_reporte[1]+0.15,0.3]])' + '\n'
        
#         if modelo.identacionautomatica and nivel>1:        
#             strs = strs.replace('@iniciolineax',str(lineaix+identa))
#         else:
#             strs = strs.replace('@iniciolineax',str(modelo.lineaix+identa))
        
#         strs += dostab + 'datos_reporte[1] += 0.8' + '\n'

#     strs = strs.replace('@modelo',modelo.nombre)

#     lista.append(strs)

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table,TableStyle, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape, A4, portrait

def VistaReportePlatypus(listaestilos,listatitulocolumnas,proyecto, aplicacion, modelo, strr, reporte,maxpuntos,adhoc,rep):

    strr = strr.replace('@maxpuntos', maxpuntos)

    if modelo.reportsize == 'L':
        strr = strr.replace('@reportsize', 'letter')
    else:
        strr = strr.replace('@reportsize', 'A4')
    if modelo.reportorientation == 'P':
        strr = strr.replace('@orientacion', 'portrait')
    else:        
        strr = strr.replace('@orientacion', 'landscape')
    strr = strr.replace('@ml', modelo.margenes.split(',')[0])
    strr = strr.replace('@mr', modelo.margenes.split(',')[1])
    strr = strr.replace('@mt', modelo.margenes.split(',')[2])
    strr = strr.replace('@mb', modelo.margenes.split(',')[3])
    # Fonts
    font_encabezado = modelo.font_encabezado.split(',')
    font_titulo = modelo.font_titulo.split(',')
    font_columnas = modelo.font_columnas.split(',')
    font_texto = modelo.font.split(',')
    font_totales = modelo.font_totales.split(',')
    strr = strr.replace('@fontTituloSize', str(font_titulo[1]))
    strr = strr.replace('@fontTitulo', font_titulo[0] )
    strr = strr.replace('@fontColumnasSize', str(font_columnas[1]))
    strr = strr.replace('@fontColumnas', font_columnas[0] )
    strr = strr.replace('@fontEncabezadoSize', str(font_encabezado[1]))
    strr = strr.replace('@fontEncabezado', font_encabezado[0] )
    strr = strr.replace('@fontTotalesSize', str(font_totales[1]))
    strr = strr.replace('@fontTotales', font_totales[0] )
    strr = strr.replace('@fontSize', str(font_texto[1]))
    strr = strr.replace('@font', font_texto[0] )

    strr = strr.replace('@titulo', modelo.titulolista)
    strr = strr.replace('@aplicacion', aplicacion.nombre)
    strr = strr.replace('@proyecto', proyecto.nombre)
    strr = strr.replace('@modelo', modelo.nombre)

    if reporte == None:
        strr = strr.replace('@nombrereporte', modelo.nombre)
        texto_reporte = ''
    elif adhoc == 'adhoc':
        strr = strr.replace('@nombrereporte', reporte.nombre)
        texto_reporte = reporte.codigo
    else:
        strr = strr.replace('@nombrereporte', reporte.nombre)
        texto_reporte = reporte.texto

    lista = []
    if adhoc != '':
        RecursivoPlatypusAdHoc(modelo,lista,listaestilos,listatitulocolumnas,0,1,0,texto_reporte,'    ',10,1,rep)
    else:
        RecursivoPlatypus(modelo,lista,listaestilos,listatitulocolumnas,0,1,0,texto_reporte,'    ',10,1,rep)

    strv = ''
    for texto in lista:
        strv += texto + '\n'

    strr = strr.replace('@barridomodelos', strv)

    return strr

def RecursivoPlatypus(modelo, lista, listaestilos,listatitulocolumnas,espacio, tabs,col,texto_reporte,ntabs,delta,numrep,rep):

    fe = modelo.font_encabezado.split(',')
    fti = modelo.font_titulo.split(',')
    fc = modelo.font_columnas.split(',')
    ft = modelo.font.split(',')
    fto = modelo.font_totales.split(',')

    nombre = modelo.nombre
    hay_modelo = False
    ancho = ''
    suma=0 
    conModelo = False

    if texto_reporte != '':
        if SeListaModelo(modelo, json.loads(texto_reporte)['propiedades']):
            conModelo = True

    if modelo.padre != 'nada':
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + 'if ' + nombre + '.objects.filter(' + modelo.padre + ' = reg_' + modelo.padre + ').count() > 0:')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        ntabs += '    '

    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    listatitulocolumnas.append('def TituloColumnas' + nombre + '(historia):')
    listatitulocolumnas.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    listatitulocolumnas.append('\t' + '# titulo')
    listatitulocolumnas.append('\t' + 'historia.append(Spacer(1,15))')
    listatitulocolumnas.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    listatitulocolumnas.append('\t' + 'data = [[' + "'" + modelo.titulolista + "'" + ']]')
    listatitulocolumnas.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    listatitulocolumnas.append('\t' + 'tbl = Table(data)')
    listatitulocolumnas.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    listatitulocolumnas.append('\t' + 'tbl.setStyle(EstiloTitulo' + nombre + '(' + "'" + fti[0] + "'" + ',' + str(fti[1]) + '))')
    listatitulocolumnas.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    if texto_reporte == '' or conModelo == True:
        listatitulocolumnas.append('\t' + 'historia.append(tbl)')
    listatitulocolumnas.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    listatitulocolumnas.append('\t' + 'historia.append(Spacer(1,' + str(fti[1]) + '))')
    listatitulocolumnas.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    if modelo.padre != 'nada':
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        hay_modelo,ancho,suma = ColumnasReporte(lista,listatitulocolumnas,texto_reporte,modelo,delta,ntabs,fc,espacio,col,conModelo)
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
    # Definimos las variables a totalizar
    lista_prop = Propiedad.objects.filter(modelo=modelo,totaliza=1,enreporte=1)

    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    for prop in lista_prop:
        lista.append(ntabs + 'total_' + prop.nombre + ' = 0')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append(ntabs + 'TituloColumnas' + nombre + '(historia)')
    if modelo.padre == 'nada':
        hay_modelo,ancho,suma = ColumnasReporte(lista,listatitulocolumnas,texto_reporte,modelo,delta,ntabs+ '',fc,espacio,col,conModelo)
        lista.append(ntabs + 'for reg_' + nombre + ' in ' + nombre + '.objects.all():')
    else:
        algo = modelo.padre + '=' + 'reg_' + modelo.padre
        lista.append(ntabs + 'for reg_' + nombre + ' in ' + nombre + '.objects.filter(' + algo + '):')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1

    lista.append(ntabs + '    # datos')

    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1

    data = '[['
    data_tot = '[['
    flgTotaliza = False
    if not hay_modelo:
        num = 1
        flgYaPuso = False
        for prop in Propiedad.objects.filter(modelo=modelo):
            if prop.enreporte:
                if prop.totaliza:
                    flgTotaliza = True
                    if data_tot == '[[':
                        data_tot += 'Paragraph(' + 'str(total_' + prop.nombre + '), ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                    else:
                        data_tot += ',Paragraph(' + 'str(total_' + prop.nombre + '), ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                    lista.append(ntabs + '    ' + 'total_' + prop.nombre + ' += ' + 'reg_' + nombre + '.' + prop.nombre)
                else:
                    if not flgYaPuso:
                        flgYaPuso = True
                        if data_tot == '[[':
                            data_tot += 'Paragraph(' + '"Totales", ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                        else:
                            data_tot += ',Paragraph(' + '"Totales", ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                    else:
                        if data_tot == '[[':
                            data_tot += 'Paragraph(' + '""' + ', ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                        else:
                            data_tot += ',Paragraph(' + '""' + ', ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                strComa = ','
                if data == '[[':
                    strComa = ''
                data, data_tot = PropiedadesEnReporte(prop,data,data_tot,lista,ntabs,strComa,nombre,ft, modelo)

    else:
        lista.append('# Listado de zonas')
        lista_zonas = json.loads(texto_reporte)['propiedades']
        if SeListaModelo(modelo,lista_zonas):
            flgYaPuso = False
            for zona in lista_zonas:
                if int(zona['zonaid']) == modelo.id:
                    prop = Propiedad.objects.get(id=zona['propid'])
                    # Totaliza
                    if prop.totaliza:
                        flgTotaliza = True
                        lista.append(ntabs + '    ' + 'total_' + prop.nombre + ' += ' + 'reg_' + modelo.nombre + '.' + prop.nombre)
                        if data_tot == '[[':
                            data_tot += 'Paragraph(' + 'str(total_' + prop.nombre + '), ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                        else:
                            data_tot += ',Paragraph(' + 'str(total_' + prop.nombre + '), ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                    else:
                        if not flgYaPuso:
                            if data_tot =='[[':
                                data_tot += 'Paragraph(' + '"Totales", ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                            else:
                                data_tot += ',Paragraph(' + '"Totales", ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                            flgYaPuso = True
                            # data_tot += ',Paragraph(' + '""' + ', ParrafoEstiloTexto' + nombre + '(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'
                        else:
                            if data_tot =='[[':
                                data_tot += 'Paragraph(' + '""' + ', ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                            else:
                                data_tot += ',Paragraph(' + '""' + ', ParrafoEstiloTotales' + nombre + '(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                    strComa = ','
                    if data == '[[':
                        strComa = ''

                    data, data_tot = PropiedadesEnReporte(prop,data,data_tot,lista,ntabs,strComa,nombre,ft, modelo)

    lista.append('#@[p_reporte_' + nombre + str(numrep) + '_' + rep + ']')
    numrep+=1

    if data == '[[':
        data += ']]'
    else:
        data += ']]'

    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append(ntabs + '    ' + 'data =' + data)
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    lista.append(ntabs + '    ' + 'tbl = Table(data, colWidths=[' + ancho + '])')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    lista.append(ntabs + '    ' + 'tbl.setStyle(tbl_estilo_texto)')
    numrep +=1
    if texto_reporte == '' or hay_modelo == True:
        lista.append(ntabs + '    ' + 'historia.append(tbl)')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1

    # estilos

    if modelo.colortitulo[0] == '#':
        txt= "'" + modelo.colortitulo + "'"
    else:
        txt = 'colors.' + modelo.colortitulo

    listaestilos.append('def EstiloTitulo' + nombre + '(font,size):')
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append("\testilo = TableStyle([('FONT', (0, 0), (-1, -1), font),")
    listaestilos.append("\t\t\t\t\t('FONTSIZE', (0, 0), (-1, -1), size),")
    listaestilos.append("\t\t\t\t\t('TEXTCOLOR',(0,0),(-1,-1)," + txt + "),")
    listaestilos.append("\t\t\t\t\t('VALIGN',(0,0),(-1,-1),'MIDDLE')])")
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append('\treturn estilo')

    listaestilos.append('def EstiloTexto' + nombre + '():')
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append("\testilo = TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE')])")
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append('\treturn estilo')

    if modelo.colorcolumnas[0] == '#':
        txt = "'" + modelo.colorcolumnas + "'"
    else:
        txt = 'colors.' + modelo.colorcolumnas

    glc = str(modelo.grosorlinea)

    listaestilos.append('def EstiloColumnas' + nombre + '(col,size):')
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append("\testilo = TableStyle([('VALIGN',(col,-1),(-1,-1),'MIDDLE'),")
    listaestilos.append("\t\t\t\t\t('LINEBELOW',(col,-1),(-1,-1)," + glc + ", colors.gray),")
    listaestilos.append("\t\t\t\t\t('LINEABOVE',(col,-1),(-1,-1)," + glc + ", colors.gray),")
    listaestilos.append("\t\t\t\t\t('BOTTOMPADDING',(col,-1),(-1,-1),size),")
    listaestilos.append("\t\t\t\t\t('TEXTCOLOR',(col,0),(-1,-1)," + txt + "),")
    listaestilos.append('\t\t\t\t\t])')
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append('\treturn estilo')

    listaestilos.append('def ParrafoEstiloColumnas' + nombre + '(font, size,align):')
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append("\testilo = ParagraphStyle(name = 'Normal', fontSize = size, fontName=font, alignment=align, textColor = " + txt + ")")
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append('\treturn estilo')

    if modelo.colortexto[0] == '#':
        txt= "'" + modelo.colortexto + "'"
    else:
        txt= 'colors.' + modelo.colortexto

    listaestilos.append('def ParrafoEstiloTexto' + nombre + '(font,size, align):')
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append("\testilo = ParagraphStyle(name = 'Normal', fontSize = size, fontName=font,alignment=align, textColor = " + txt + ")")
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append('\treturn estilo')

    if modelo.colortotales[0] == '#':
        txt= "'" + modelo.colortotales + "'"
    else:
        txt = 'colors.' + modelo.colortotales

    listaestilos.append('def EstiloTotales' + nombre + '(col):')
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append("\testilo = TableStyle([('VALIGN',(col,0),(-1,-1),'MIDDLE'),")
    listaestilos.append("\t\t\t\t\t('LINEABOVE',(col,0),(-1,-1),0.25, colors.gray),")
    listaestilos.append("\t\t\t\t\t('TEXTCOLOR',(col,0),(-1,-1), " + txt + "),")
    listaestilos.append('\t\t\t\t\t])')
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append('\treturn estilo')

    listaestilos.append('def ParrafoEstiloTotales' + nombre + '(font,size, align):')
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append("\testilo = ParagraphStyle(name = 'Normal', fontSize = size, fontName=font,alignment=align, textColor = " + txt + ")")
    listaestilos.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    listaestilos.append('\treturn estilo')

    for mod in Modelo.objects.filter(padre = nombre,proyecto=modelo.proyecto):
        numrep += 1
        RecursivoPlatypus(mod, lista, listaestilos,listatitulocolumnas, espacio, tabs+1,col,texto_reporte,ntabs + "    ",delta+20,numrep,rep)

    if flgTotaliza:
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        data_tot += ']]'
        lista.append(ntabs + 'data =' + data_tot)
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + 'tblt = Table(data, colWidths=[' + ancho + '])')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + 'tblt.setStyle(EstiloTotales@modelo(0))')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + 'historia.append(tblt)')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1

    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    if modelo.saltopagina:
        lista.append(ntabs + '    ' + 'pagebreak = PageBreak()')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + '    ' + 'historia.append(pagebreak)')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + '    ' + 'TituloColumnas' + nombre + '(historia)')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')

    numrep+=1

def PropiedadesEnReporte(prop, data, data_tot, lista, ntabs, strComa,nombre, ft, modelo):
    if prop.tipo == 'i' or prop.tipo == 'l' or prop.tipo == 'm' or prop.tipo == 'd':
        # Propiedad numerica
        data += strComa + 'Paragraph(' + 'str(reg_' + nombre + '.' + prop.nombre + '), ParrafoEstiloTexto' + nombre + '(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'
    elif prop.tipo == 'f':
        nombreself = Modelo.objects.get(nombre=prop.foranea,proyecto=modelo.proyecto).nombreborrar
        data += strComa + 'Paragraph(' + 'str(reg_' + nombre + '.' + prop.nombre + '.' + nombreself + '), ParrafoEstiloTexto' + nombre + '(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'
    elif prop.tipo == 'p':
        lista.append(ntabs + '    ' + 'cd = os.getcwd()') 
        lista.append(ntabs + '    ' + 'if reg_' + nombre + '.' + prop.nombre + ':')
        lista.append(ntabs + '        ' + prop.nombre + ' = cd + reg_' + modelo.nombre + '.' + prop.nombre + '.url')
        lista.append(ntabs + '        ' + 'im_' + prop.nombre + ' = Image(' + prop.nombre + ', 15,15)')
        lista.append(ntabs + '    ' + 'else:')
        lista.append(ntabs + '        ' + 'im_' + prop.nombre + ' = ' + "''")
        data += ',im_' + prop.nombre
    elif prop.tipo == 'r':
        texto='['
        for radio in prop.textobotones.split(';'):
            if texto == '[':
                texto += "('" + radio.split(',')[0] + "' , '" + radio.split(',')[1] + "')"
            else:
                texto += ",('" + radio.split(',')[0] + "' , '" + radio.split(',')[1] + "')"
        texto += ']'
        lista.append(ntabs + '    rb_' + prop.nombre + ' = ' + "''")
        lista.append(ntabs + '    for radio in ' + texto + ':')
        lista.append(ntabs + '        if reg_' + nombre + '.' + prop.nombre + ' == radio[0]:')
        lista.append(ntabs + '            rb_' + prop.nombre + ' = radio[1]')
        data += strComa + 'Paragraph(rb_' + prop.nombre + ', ParrafoEstiloTexto' + nombre + '(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'
    elif prop.tipo == 't' or prop.tipo == 'n':
        if prop.formatofecha != '':
            lista.append(ntabs + '    ' + prop.nombre + '=' + 'reg_' + nombre + '.' + prop.nombre + '.strftime("' + prop.formatofecha + '")')
            data += strComa + 'Paragraph(' + prop.nombre + ', ParrafoEstiloTexto' + nombre + '(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'
        else:
            data += strComa + 'Paragraph(' + 'str(reg_' + nombre + '.' + prop.nombre + '), ParrafoEstiloTexto' + nombre + '(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'
    else:
        data += strComa + 'Paragraph(' + 'str(reg_' + nombre + '.' + prop.nombre + '), ParrafoEstiloTexto' + nombre + '(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'

    if prop.alineacion == 'l':
        data = data.replace('@ali','TA_LEFT')
        data_tot = data_tot.replace('@ali','TA_LEFT')
    elif prop.alineacion == 'r':
        data = data.replace('@ali','TA_RIGHT')
        data_tot = data_tot.replace('@ali','TA_RIGHT')
    else:
        data = data.replace('@ali','TA_CENTER')
        data_tot = data_tot.replace('@ali','TA_CENTER')
    return data, data_tot

def RecursivoPlatypusAdHoc(modelo, lista, listaestilos,listatitulocolumnas, espacio, tabs,col,texto_reporte,ntabs,delta,numrep,rep):

    strCols = []
    
    fe = modelo.font_encabezado.split(',')
    fti = modelo.font_titulo.split(',')
    fc = modelo.font_columnas.split(',')
    ft = modelo.font.split(',')
    fto = modelo.font_totales.split(',')

    nombre = modelo.nombre
    hay_modelo = False
    ancho = ''
    suma=0 
    conModelo = False

    lista.append('#@[p_reporte_' + modelo.nombre + str(numrep) + '_' + rep + ']')
    numrep+=1
    lista.append(ntabs + '# titulo')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    lista.append(ntabs + 'historia.append(Spacer(1,15))')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    lista.append(ntabs + 'data = [[' + "'" + modelo.titulolista + "'" + ']]')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    lista.append(ntabs + 'tbl = Table(data)')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    lista.append(ntabs + 'tbl.setStyle(EstiloTitulo@modelo(' + "'" + fti[0] + "'" + ',' + str(fti[1]) + '))')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    lista.append(ntabs + 'historia.append(tbl)')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1
    lista.append(ntabs + 'historia.append(Spacer(1,15))')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep +=1

    # desglosa el codigo
    txt_fields = ''
    lista_final = ''
    for txt in texto_reporte.split('\n'):
        if txt != '':
            if txt[0:6].strip() == 'fields':
                txt_fields = txt
                strCols,ancho,suma = ColumnasReporteAdHoc(lista,listatitulocolumnastxt,modelo,delta,ntabs,fc,espacio,col,conModelo,'adhoc')        
                break
            else:
                lista_final = ''
                for ch in txt:
                    if ch == '=':
                        break
                    lista_final += ch
                lista_final = lista_final.strip()
                lista.append(ntabs + txt)

    # Ve si hay totalizadores
    flgTotaliza = False
    try:
        lista.append('#@[p_reporte_' + modelo.nombre + str(numrep) + '_' + rep + ']')
        numrep+=1
        for parte in strCols:
            if parte.split(',')[5] == 't' and (parte.split(',')[4] == 'd' or parte.split(',')[4] == 'i'):
                flgTotaliza = True
                lista.append(ntabs + 'total_' + parte.split(',')[3] + ' = 0')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
    except:
        pass

    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append(ntabs + lista_final + '.query = pickle.loads(pickle.dumps(' + lista_final + '.query))')

    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append(ntabs + 'for os in ' + lista_final + ':')

    lista.append(ntabs + '    # datos')

    data = '[['
    data_tot = '[['

    for parte in strCols:
        if data == '[[':
            data += "''"
        # tipo de campo
        stx = ''
        if parte.split(',')[4] == 'd' or parte.split(',')[4] == 'd':
            id = '"' + parte.split(',')[3] + '"'
            if parte.split(',')[4] == 'd':
                dd = '"{:.2f}".format(os[' + id + '])'
            else:
                dd = '"{:.0f}".format(os[' + id + '])'
            data += ',Paragraph(' + dd + ', ParrafoEstiloTexto@modelo(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'
            if parte.split(',')[5] == 't':
                if data_tot == '[[':
                    data_tot += "''"
                id = '"' + parte.split(',')[3] + '"'
                dd = '"{:.2f}".format(total_' + parte.split(',')[3] + ')'
                flgTotaliza = True
                data_tot += ',Paragraph(' + dd + ', ParrafoEstiloTotales@modelo(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
                lista.append(ntabs + '    ' + 'total_' + parte.split(',')[3] + ' += os["' + parte.split(',')[3] + '"]')
        #     if data_tot == '[[':
        #         data_tot += "''"
        #     data_tot += ',Paragraph(' + '""' + ', ParrafoEstiloTotales@modelo(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'

        # elif parte.split(',')[4] == 'i':
        #     data += ',Paragraph(' + 'str(os["' + parte.split(',')[3] + '"]), ParrafoEstiloTexto@modelo(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'
        #     if parte.split(',')[5] == 't':
        #         flgTotaliza = True
        #         data_tot += ',Paragraph(' + dd + ', ParrafoEstiloTotales@modelo(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
        else:
            if data_tot == '[[':
                data_tot += "''"
            data_tot += ',Paragraph(' + '""' + ', ParrafoEstiloTotales@modelo(' + "'" + fto[0] + "'" + ',' + str(fto[1]) + ',@ali))'
            data += ',Paragraph(' + 'os["' + parte.split(',')[3] + '"], ParrafoEstiloTexto@modelo(' + "'" + ft[0] + "'" + ',' + str(ft[1]) + ',@ali))'

        alin_col = parte.split(',')[2]
        if alin_col == 'l':
            data = data.replace('@ali','TA_LEFT')
            data_tot = data_tot.replace('@ali','TA_LEFT')
        elif alin_col == 'r':
            data = data.replace('@ali','TA_RIGHT')
            data_tot = data_tot.replace('@ali','TA_RIGHT')
        else:
            data = data.replace('@ali','TA_CENTER')
            data_tot = data_tot.replace('@ali','TA_CENTER')

    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1

    if data == '[[':
        data += ']]'
    else:
        data += ",''" + ']]'


    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append(ntabs + '    ' + 'data =' + data)
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append(ntabs + '    ' + 'tbl = Table(data, colWidths=[' + ancho + '])')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append(ntabs + '    ' + 'tbl.setStyle(tbl_estilo_texto)')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append(ntabs + '    ' + 'historia.append(tbl)')
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1
    lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
    numrep+=1

    if flgTotaliza:
        if data_tot == '[[':
            data_tot += ']]'
        else:
            data_tot += ",''" + ']]'
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + 'data =' + data_tot)
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + 'tbl = Table(data, colWidths=[' + ancho + '])')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + 'tbl.setStyle(EstiloTotales@modelo(0))')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1
        lista.append(ntabs + 'historia.append(tbl)')
        lista.append('#@[p_reporte_' + nombre + '_' + rep + '_' + str(numrep) + ']')
        numrep+=1

    # for modelo in Modelo.objects.filter(padre = modelo.nombre,proyecto=modelo.proyecto):
    #     RecursivoPlatypusAdHoc(modelo, lista, espacio, tabs+1,col,texto_reporte,fe,fti,fc,ft,ntabs + "    ",delta+20)
    # lista.append(ntabs + 'historia.append(Spacer(1,15))')

def SeListaModelo(modelo,lista_zonas):
    for zona in lista_zonas:
        if int(zona['zonaid']) == modelo.id:
            return True
            break
    return False

def ColumnasReporte(lista,listatitulocolumnas,texto_reporte,modelo,delta,ntabs,fc,espacio,col,conModelo):
    listatitulocolumnas.append('\t' + '# columnas')
    # ancho = str(espacio)
    suma = 0
    data = '[['
    hay_modelo= False

    # verifica si hay reporte de zonas para el modelo
    if texto_reporte != '':
        lista_zonas = json.loads(texto_reporte)['propiedades']
        for zona in lista_zonas:
            if int(zona['zonaid']) == modelo.id:
                hay_modelo = True
                break

    if not hay_modelo:
        ancho = ''
        for prop in Propiedad.objects.filter(modelo=modelo):
            if prop.enreporte:
                # data = ColumnasReporte(prop,ancho,espacio,data,suma,modelo)
                if ancho == '':
                    ancho += str(prop.anchoenreporte)
                    suma += prop.anchoenreporte + delta
                else:
                    ancho += ',' + str(prop.anchoenreporte)
                    suma += prop.anchoenreporte
                txt_columna = prop.textocolumna
                if prop.textocolumna == '':
                    txt_columna = prop.nombre
                if data == '[[':
                    data += 'Paragraph(' + "'" + txt_columna + "'" + ', ParrafoEstiloColumnas' + modelo.nombre + '(' + "'" + fc[0] + "'" + ',' + str(fc[1]) + ',@ali))'
                else:
                    data += ',Paragraph(' + "'" + txt_columna + "'" + ', ParrafoEstiloColumnas' + modelo.nombre + '(' + "'" + fc[0] + "'" + ',' + str(fc[1]) + ',@ali))'

                if prop.alineacion == 'l':
                    data = data.replace('@ali','TA_LEFT')
                elif prop.alineacion == 'r':
                    data = data.replace('@ali','TA_RIGHT')
                else:
                    data = data.replace('@ali','TA_CENTER')
    else:
        lista_zonas = json.loads(texto_reporte)['propiedades']
        ancho = ''
        for zona in lista_zonas:
            if int(zona['zonaid']) == modelo.id:
                prop = Propiedad.objects.get(id=zona['propid'])
                if ancho == '':
                    ancho += str(prop.anchoenreporte)
                else:
                    ancho += ',' + str(prop.anchoenreporte)
                suma += int(zona['delta']) + prop.anchoenreporte
                txt_columna = prop.textocolumna
                if prop.textocolumna == '':
                    txt_columna = prop.nombre
                if data == '[[':
                    # data += "'',"
                    data += 'Paragraph(' + "'" + txt_columna + "'" + ', ParrafoEstiloColumnas' + modelo.nombre + '(' + "'" + fc[0] + "'" + ',' + str(fc[1]) + ',@ali))'
                else:
                    data += ',Paragraph(' + "'" + txt_columna + "'" + ', ParrafoEstiloColumnas' + modelo.nombre + '(' + "'" + fc[0] + "'" + ',' + str(fc[1]) + ',@ali))'

                if prop.alineacion == 'l':
                    data = data.replace('@ali','TA_LEFT')
                elif prop.alineacion == 'r':
                    data = data.replace('@ali','TA_RIGHT')
                else:
                    data = data.replace('@ali','TA_CENTER')

    if data == '[[':
        data += ']]'
    else:
        data += ']]'

    if ancho=='':
        ancho = '0'
    listatitulocolumnas.append('\t' + 'data =' + data)
    listatitulocolumnas.append('\t' + 'tbl = Table(data, colWidths=[' + ancho + '])')
    # desplazamiento dentro de columnas
    size = modelo.font_columnas.split(',')[1]
    listatitulocolumnas.append('\t' + 'tbl.setStyle(EstiloColumnas' + modelo.nombre + '(' + str(col) + ',' + str(size) + '))')
    if texto_reporte == '' or conModelo == True:
        listatitulocolumnas.append('\t' + 'historia.append(tbl)')

    return hay_modelo,ancho,suma

def ColumnasReporteAdHoc(lista,listatitulocolumnas,texto_reporte,modelo,delta,ntabs,fc,espacio,col,conModelo,adhoc):
    lista.append(ntabs + '# columnas')
    # ancho = str(espacio)
    suma = 0
    data = '[['
    hay_modelo= False
    ancho = ''
    # encontrar las columnas
    strCol = ''
    for ch in texto_reporte:
        if ch == '(':
            strCol = ''
        elif ch == ')':
            break
        else:
            strCol += ch
    strCols = strCol.split("|")
    for columna in strCols:
        parte = columna.split(',')
        ancho_col = parte[1]
        nombre_col = parte[0]                
        alin_col = parte[2]
        if ancho == '':
            ancho += str(delta) + ',' + ancho_col
            suma += int(ancho_col) + delta
        else:
            ancho += ',' + ancho_col
            suma += int(ancho_col)
        if data == '[[':
            data += 'Paragraph(' + "'" + nombre_col + "'" + ', ParrafoEstiloColumnas@modelo(' + "'" + fc[0] + "'" + ',' + str(fc[1]) + ',@ali))'
        else:
            data += ',Paragraph(' + "'" + nombre_col + "'" + ', ParrafoEstiloColumnas@modelo(' + "'" + fc[0] + "'" + ',' + str(fc[1]) + ',@ali))'
        
        if alin_col == 'l':
            data = data.replace('@ali','TA_LEFT')
        elif alin_col == 'r':
            data = data.replace('@ali','TA_RIGHT')
        else:
            data = data.replace('@ali','TA_CENTER')


    if data == '[[':
        data += ']]'
    else:
        data += ",''" + ']]'

    if ancho=='':
        ancho = '0'
    listatitulocolumnas.append(ntabs + 'data =' + data)
    listatitulocolumnas.append(ntabs + 'tbl = Table(data, colWidths=[' + ancho + '])')
    listatitulocolumnas.append(ntabs + 'tbl.setStyle(EstiloColumnas@modelo(' + str(col) + '))')
    listatitulocolumnas.append(ntabs + 'historia.append(tbl)')

    return strCols,ancho,suma

def ListaFinal():

    lista = []    
    lista.append('def ListaFinal(lista,le):')
    lista.append("\tlista_final = []")
    lista.append("\tfor elemento in lista:")
    lista.append("\t\tif len(elemento[1].split(',')) == 0:")
    lista.append("\t\t\tlista_final.append([elemento,'+'])")
    lista.append("\t\telse:")
    lista.append("\t\t\tif len(elemento[1].split(',')) == 1:")

    lista.append("\t\t\t\tif le[0] == elemento[1].split(',')[0]:")
    lista.append("\t\t\t\t\tlista_final.append([elemento,'-'])")
    lista.append("\t\t\t\telse:")
    lista.append("\t\t\t\t\tlista_final.append([elemento,'+'])")

    lista.append("\t\t\telif len(elemento[1].split(',')) < len(le):")
    lista.append("\t\t\t\tpasa=True")
    lista.append("\t\t\t\tfor i in range(len(elemento[1].split(','))-1):")
    lista.append("\t\t\t\t\tif le[i] != elemento[1].split(',')[i]:")
    lista.append("\t\t\t\t\t\tpasa=False")
    lista.append("\t\t\t\t\t\tbreak")
    lista.append("\t\t\t\tif pasa:")
    lista.append("\t\t\t\t\tlista_final.append([elemento,'+'])")
    lista.append("\t\t\telif len(elemento[1].split(',')) == len(le):")

    lista.append("\t\t\t\tif elemento[1].split(',') == le:")
    lista.append("\t\t\t\t\tlista_final.append([elemento,'-'])")
    lista.append("\t\t\t\telse:")

    lista.append("\t\t\t\t\tpasa=True")
    lista.append("\t\t\t\t\tfor i in range(len(le)-1):")
    lista.append("\t\t\t\t\t\tif le[i] != elemento[1].split(',')[i]:")
    lista.append("\t\t\t\t\t\t\tpasa=False")
    lista.append("\t\t\t\t\t\t\tbreak")
    lista.append("\t\t\t\t\tif pasa:")
    lista.append("\t\t\t\t\t\tlista_final.append([elemento,'+'])")

    lista.append("\t\t\telif len(elemento[1].split(',')) > len(le) and len(elemento[1].split(',')) - len(le) ==1:")
    lista.append("\t\t\t\tpasa=True")
    lista.append("\t\t\t\tfor i in range(len(le)):")
    lista.append("\t\t\t\t\tif le[i] != elemento[1].split(',')[i]:")
    lista.append("\t\t\t\t\t\tpasa=False")
    lista.append("\t\t\t\t\t\tbreak")
    lista.append("\t\t\t\tif pasa:")
    lista.append("\t\t\t\t\tlista_final.append([elemento,'+'])")
    lista.append("\treturn lista_final")

    strTexto=''
    for texto in lista:
        strTexto+=texto + '\n'
    return strTexto

def ArbolNavegacion(modelo):
    lista=[]
    lista = RecursivoArbolImport(modelo,lista)
    lista.append("def Arbol@modelo(esquema,identa):")
    lista.append("\tlista=[]")
    # lista = RecursivoArbolNudos(0,lista,modelo)
    lista.append("\tle = esquema.split(',')")
    lista = RecursivoArbolFor(modelo,lista,0,'\t',modelo.nombre,'nudo0',0,0,modelo.nombre,'reg_' + modelo.nombre,modelo.id, '"0"',0,'0')
    lista.append('\treturn lista')

    strTexto=''
    for texto in lista:
        strTexto+=texto + '\n'
    return strTexto

def RecursivoArbolImport(modelo,lista):
    stri = "from @aplicacion.models import @nombre"
    stri=stri.replace('@aplicacion',modelo.aplicacion.nombre)
    stri=stri.replace('@nombre',modelo.nombre)
    lista.append(stri)
    for modelo_hijo in Modelo.objects.filter(padre=modelo.nombre, proyecto=modelo.proyecto):
        RecursivoArbolImport(modelo_hijo,lista)
    return lista

def RecursivoArbolNudos(contador,lista,modelo):
    if not "\tnudo" + str(contador) + ' = ' + "'0'" in lista:
        lista.append('\tnudo' + str(contador) + ' = ' + "'0'")
    for modelo_hijo in Modelo.objects.filter(padre=modelo.nombre, proyecto=modelo.proyecto):
        RecursivoArbolNudos(contador+1,lista,modelo_hijo)
    return lista

def RecursivoArbolFor(modelo,lista,inicio,tabs,padre,nudo,contador,ident,papa,modelo_arriba,id_papa,listapadreid, indice,raiz):
    lp = ''
    if inicio == 0:
        stri=tabs + 'for reg_@modelo in @modelo.objects.all():' + '\n'
        stri=stri.replace('@modelo',modelo.nombre)
        # lista.append(tabs+stri)
        stri += tabs + '\t' + 'lista.append([str(reg_@modelo.id),0, "+","@modelo",reg_@modelo.@nombreborrar,reg_@modelo.id,' + listapadreid + ',reg_@modelo.id])' + '\n'
        # stri += 'lista.append([reg_@modelo,' + nudo + ',' + str(ident) + ',' + 'reg_' + papa + ',' + '""' + ',' + '""' + ',' + '"' + modelo.aplicacion.nombre + '"' + ',' + '"' + modelo.nombre + '"' + ',' + '""' + ',' + '"' + papa + '"' + ',' + 'reg_' + papa + '.id' + '])' + '\n'
        stri += tabs + '\tif le[' + str(indice) + '] != "" and le[' + str(indice) + '] == str(reg_@modelo.id):' + '\n'
        stri += tabs + '\t\tlista[len(lista)-1] = [str(reg_@modelo.id),0, "-","@modelo",reg_@modelo.@nombreborrar,reg_@modelo.id,' + listapadreid + ',reg_@modelo.id]' + '\n'
        stri=stri.replace('@modelo',modelo.nombre)
        stri=stri.replace('@nombreborrar',modelo.nombreborrar)
        lista.append(stri)
        lp = "str(reg_@modelo.id)"
        listapadreid = lp
        lp=lp.replace('@modelo',modelo.nombre)
        listapadreid = lp
        raiz = 'reg_@modelo.id'
        raiz=raiz.replace('@modelo',modelo.nombre)
    else:
        lp = listapadreid + ' + ' + "','" + ' + ' + 'str(reg_@modelo.id)'
        lp = lp.replace('@modelo',modelo.nombre)
        stri = tabs + 'for reg_@modelo in @modelo.objects.filter(@padre=reg_@padre):' + '\n'
        stri += tabs + '\tlista.append([' + lp + ',' + str(ident) + ',"+","@modelo",reg_@modelo.@nombreborrar,' + raiz + ',' + listapadreid + ',reg_@modelo.id])' + '\n'
        stri += tabs + '\tif le[' + str(indice) + '] != "" and le[' + str(indice) + '] == str(reg_@modelo.id):' + '\n'
        stri += tabs + '\t\tlista[len(lista)-1] = [' + lp + ',' + str(ident) + ',"-","@modelo",reg_@modelo.@nombreborrar,' + raiz + ',' + listapadreid + ',reg_@modelo.id]' + '\n'
        stri=stri.replace('@modelo',modelo.nombre)
        stri=stri.replace('@padre',padre)
        stri=stri.replace('@nombreborrar',modelo.nombreborrar)
        # nudo_anterior = nudo
        # nudo = nudo + "+" + "','" +"+" + 'nudo' + str(contador)
        # lista.append(tabs + nudo)
        # lista.append(tabs+stri)
        # stri = tabs + '\tlista.append([reg_@modelo,' + nudo + ',' + str(ident) + ',' + 'reg_' + papa + ',' + '"' + modelo_arriba + '"' + ',' + 'reg_' + modelo_arriba + '.id' + ',' + '"' + modelo.aplicacion.nombre + '"' + ',' + '"' + modelo.nombre + '"' + ',' + nudo_anterior + ',' + '"' + papa + '"' + ',' + 'reg_' + papa + '.id' + '])'
        stri=stri.replace('@modelo',modelo.nombre)
        lista.append(stri)
    for modelo_hijo in Modelo.objects.filter(padre=modelo.nombre, proyecto=modelo.proyecto):
        RecursivoArbolFor(modelo_hijo,lista,1,tabs+'\t\t',modelo.nombre,nudo,contador+1,ident+20,papa, modelo.nombre,id_papa,lp,indice+1,raiz)
        # stri = 'nudo' + str(contador+1)  + ' = str(int(nudo' + str(contador+1) + ')+1)'
        # lista.append(tabs + '\t\t' + stri)
        # stri = 'nudo' + str(contador+2) + ' = ' + "'0'"
        # lista.append(tabs + '\t\t' + stri)
    if inicio == 0:
        pass
        # stri = 'nudo0 = str(int(nudo0) + 1)'
        # lista.append(tabs + '\t' + stri)        
        # stri = 'nudo1 = ' + "'0'"
        # lista.append(tabs + '\t' + stri)
    return lista

def RecursivoUrl(modelo,aplicacion,obj,lista, retorno):
    for modelo_hijo in Modelo.objects.filter(padre=modelo.nombre, proyecto=modelo.proyecto):
        RecursivoUrl(modelo_hijo,modelo_hijo.aplicacion.nombre,modelo_hijo.nombre,lista,retorno)
    if aplicacion != '':
        lista.append('\t\t\t\t\t\t\t{% if obj.3 == ' + '"' + modelo.nombre + '"' + ' %}')
        if not retorno:
            lista.append("\t\t\t\t\t\t\t\t<a style='text-decoration: none; color:white;' href='{% url @com" + aplicacion + ":editar_" + obj + "@com obj.7 %}?padre={{obj.6}},&raiz={{obj.5}}'>{{obj.4}}")
        else:
            lista.append("\t\t\t\t\t\t\t\t<a style='text-decoration: none; color:white;' href='{% url @com" + aplicacion + ":editar_" + obj + "@com obj.7 %}?padre={{obj.6}},&raiz={{obj.5}}'>{{obj.4}}")
        lista.append('\t\t\t\t\t\t\t{% endif %}')
        lista.append("\t\t\t\t\t\t\t\t</a>")
    return lista

# Crear base.html para el proyecto

def CrearBaseProyectoEstandar(proyecto,modelo):
    # Crear la seccion
    if modelo == None:
        seccion = secp()
        seccion.nombre = 'Seccion_Principal'
        seccion.proyecto = proyecto
        seccion.save()
    else:
        seccion = secm()
        seccion.nombre = 'Seccion_Principal'
        seccion.modelo = modelo
        seccion.save()

    # Crear la fila logo titulo
    if modelo == None:
        fila = filap()
    else:
        fila = filam()
    fila.nombre = 'Logo_Titulo'
    fila.seccion = seccion
    fila.altura = 10
    fila.borde = True
    fila.save()

    # Crear las columna del logo
    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'Logo'
    columna.fila = fila
    columna.secciones = 3
    columna.borde = True
    columna.funcion = 'o'
    # columna.textocolumna = 'LOGO'
    columna.save()
    # Crear las columna del titulo
    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'Titulo'
    columna.fila = fila
    columna.secciones = 9
    columna.borde = True
    columna.funcion = 't'
    # columna.textocolumna = 'TITULO'
    columna.save()

    # Crear la fila busqueda menu
    if modelo == None:
        fila = filap()
    else:
        fila = filam()
    fila.nombre = 'Busqueda_Menu'
    fila.seccion = seccion
    fila.altura = 10
    fila.borde = True
    fila.save()

    # Crear las columna de busqueda
    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'Busqueda'
    columna.fila = fila
    columna.secciones = 3
    columna.borde = True
    columna.funcion = 'o'
    # columna.textocolumna = 'BUSQUEDA'
    columna.save()
    # Crear las columna del menu
    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'Menu'
    columna.fila = fila
    columna.secciones = 9
    columna.borde = True
    columna.funcion = 'm'
    # columna.textocolumna = 'MENU'
    columna.save()
    
    # Crear la fila central
    if modelo == None:
        fila = filap()
    else:
        fila = filam()
    fila.nombre = 'Central'
    fila.seccion = seccion
    fila.altura = 60
    fila.borde = True
    fila.save()

    # Crear las columna de la izquierda
    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'Centro_Izquierda'
    columna.fila = fila
    columna.secciones = 1
    columna.borde = True
    # columna.textocolumna = 'IZQUIERDA'
    columna.save()
    # Crear las columna del centro
    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'Centro'
    columna.fila = fila
    columna.secciones = 10
    columna.borde = True
    columna.funcion = 'd'
    # columna.textocolumna = 'CENTRO'
    columna.save()
    # Crear las columna de la derecha
    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'Centro_Derecha'
    columna.fila = fila
    columna.secciones = 1
    # columna.textocolumna = 'DERECHA'
    columna.borde = True
    columna.save()
    
    # Crear la fila del pie
    if modelo == None:
        fila = filap()
    else:
        fila = filam()
    fila.nombre = 'Pie'
    fila.seccion = seccion
    fila.altura = 10
    fila.borde = True
    fila.save()

    # Crear las columna del pie
    if modelo == None:
        columna = colp()
    else:
        columna = colm()
    columna.nombre = 'Pie'
    columna.fila = fila
    columna.secciones = 12
    columna.borde = True
    # columna.textocolumna = 'PIE'
    columna.save()

def CrearBaseProyecto(proyecto, base, dc, directorio,directoriogenesis,nombre,etapa,usuario):
    return CrearBaseHtml(None, proyecto, base, dc, directorio,directoriogenesis,nombre,etapa,usuario,'proyecto')

def CrearBaseModelo(modelo, proyecto, base, dc):
    return CrearBaseHtml(modelo,proyecto,base,dc)
    # strcss = ''
    # seccion = secm.objects.get(modelo=modelo)
    # stri = '<main class="seccion container">' + '\n'
    # strcss += '.seccion{' + '\n'
    # strcss += 'background: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
    # strcss = strcss.replace('@direccion_degrade', seccion.degradado)
    # strcss = strcss.replace('@coloruno', seccion.color1)
    # strcss = strcss.replace('@colordos', seccion.color2)
    # strcss += '}' + '\n'
    # # Desglosar las filas
    # for fila in filam.objects.filter(seccion=seccion):
    #     stri += '\t<div class="fila_' + fila.nombre + ' row">' + '\n'
    #     strcss += '.fila_' + fila.nombre + '{' + '\n'
    #     strcss += 'background: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
    #     strcss = strcss.replace('@direccion_degrade', fila.degradado)
    #     strcss = strcss.replace('@coloruno', fila.color1)
    #     strcss = strcss.replace('@colordos', fila.color2)
    #     strcss += '}' + '\n'
    #     for columna in colm.objects.filter(fila=fila):
    #         if columna.funcion == 'l':
    #             stri += '\t\t<!-- #@[p_base_03] -->' + '\n'
    #             stri += '\t\t<div class="logo texto_logo col-' + str(columna.secciones) +  '" >@texto' + '\n'
    #             if proyecto.avatar:
    #                 stri += '\t\t\t<!-- #@[p_base_04] -->' + '\n'
    #                 stri += "\t\t\t<img id='logo' alt=" + dc + dc + " src=" + dc + "{% static 'core/img/logo.png' %}" + dc + ">" + "\n"
    #                 stri += '\t\t\t<!-- #@[p_base_05] -->' + '\n'
    #                 stri += '\t\t</div>' + '\n'
    #                 stri += '\t\t<!-- #@[p_base_06] -->' + '\n'
    #             strcss += '.logo {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'

    #             if proyecto.justificacionhorizontallogo == 'c':
    #                 strcss = strcss.replace('@jh','center')
    #             if proyecto.justificacionhorizontallogo == 'i':
    #                 strcss = strcss.replace('@jh','start')
    #             if proyecto.justificacionhorizontallogo == 'd':
    #                 strcss = strcss.replace('@jh','end')
    #             if proyecto.justificacionverticallogo == 'c':
    #                 strcss = strcss.replace('@jv','center')
    #             if proyecto.justificacionverticallogo == 's':
    #                 strcss = strcss.replace('@jv','start')
    #             if proyecto.justificacionverticallogo == 'i':
    #                 strcss = strcss.replace('@jv','end')

    #             strcss += 'background: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
    #             strcss = strcss.replace('@direccion_degrade', columna.degradado)
    #             strcss = strcss.replace('@coloruno', columna.color1)
    #             strcss = strcss.replace('@colordos', columna.color2)

    #             if columna.textocolumna != '':
    #                 stri = stri.replace('@texto', columna.textocolumna)
    #             else:
    #                 stri = stri.replace('@texto', '')

    #             if columna.borde:
    #                 strcss += 'border: 1pt solid gray;\n'

    #             strcss += '}' + '\n'

    #             strcss += '.texto_logo {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'
    #             if columna.justificacionhorizontaltexto == 'c':
    #                 strcss = strcss.replace('@jh','center')
    #             if columna.justificacionhorizontaltexto == 'i':
    #                 strcss = strcss.replace('@jh','start')
    #             if columna.justificacionhorizontaltexto == 'd':
    #                 strcss = strcss.replace('@jh','end')
    #             if columna.justificacionverticaltexto == 'c':
    #                 strcss = strcss.replace('@jv','center')
    #             if columna.justificacionverticaltexto == 's':
    #                 strcss = strcss.replace('@jv','start')
    #             if columna.justificacionverticaltexto == 'i':
    #                 strcss = strcss.replace('@jv','end')
    #             try:
    #                 strcss += 'font-family:' + columna.fonttexto.split(',')[0] + ';\n'
    #                 strcss += 'font-size:' + columna.fonttexto.split(',')[1] + ';\n'
    #                 strcss += 'font-weight:' + columna.fonttexto.split(',')[2] + ';\n'
    #             except:
    #                 pass
    #             strcss += 'color:' + columna.colortexto + ';\n'
                
                
    #             strcss += '}' + '\n'

    #             strcss += '#logo {' + '\n'
    #             strcss += 'width: ' + str(proyecto.avatarwidth) + 'px;\n'                    
    #             strcss += 'height: ' + str(proyecto.avatarheight) + 'px;\n'
    #             strcss += '}' + '\n'

    #         elif columna.funcion == 't':
    #             stri += '\t\t<div class="titulo texto_titulo col-' + str(columna.secciones) +  '" >@texto' + '\n'
    #             stri += '\t\t\t<!-- #@[p_base_07] -->' + '\n'
    #             if proyecto.imagentitulo:
    #                 stri += "\t\t\t<img id='titulo' alt=" + dc + dc + " src=" + dc + "{% static 'core/img/imagentitulo.png' %}" + dc + " width=" + dc + "@imagentitulowidthpx" + dc + " height=" + dc + "@imagentituloheightpx" + dc + " >\n"
    #             else:
    #                 stri += '\t\t\t' + proyecto.titulo + '\n'

    #             stri += '\t\t\t<!-- #@[p_base_08] -->' + '\n'
    #             stri += '\t\t</div>\n'
    #             stri += '\t\t<!-- #@[p_base_09] -->' + '\n'
    #             strcss += '.titulo {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'

    #             if proyecto.justificacionhorizontaltitulo == 'c':
    #                 strcss = strcss.replace('@jh','center')
    #             if proyecto.justificacionhorizontaltitulo == 'i':
    #                 strcss = strcss.replace('@jh','start')
    #             if proyecto.justificacionhorizontaltitulo == 'd':
    #                 strcss = strcss.replace('@jh','end')
    #             if proyecto.justificacionverticaltitulo == 'c':
    #                 strcss = strcss.replace('@jv','center')
    #             if proyecto.justificacionverticaltitulo == 's':
    #                 strcss = strcss.replace('@jv','start')
    #             if proyecto.justificacionverticaltitulo == 'i':
    #                 strcss = strcss.replace('@jv','end')

    #             strcss += 'background: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
    #             strcss = strcss.replace('@direccion_degrade', columna.degradado)
    #             strcss = strcss.replace('@coloruno', columna.color1)
    #             strcss = strcss.replace('@colordos', columna.color2)

    #             if columna.textocolumna != '':
    #                 stri = stri.replace('@texto', columna.textocolumna)
    #             else:
    #                 stri = stri.replace('@texto', '')

    #             if columna.borde:
    #                 strcss += 'border: 1pt solid gray;\n'

    #             strcss += '}' + '\n'

    #             strcss += '.texto_titulo {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'
    #             if columna.justificacionhorizontaltexto == 'c':
    #                 strcss = strcss.replace('@jh','center')
    #             if columna.justificacionhorizontaltexto == 'i':
    #                 strcss = strcss.replace('@jh','start')
    #             if columna.justificacionhorizontaltexto == 'd':
    #                 strcss = strcss.replace('@jh','end')
    #             if columna.justificacionverticaltexto == 'c':
    #                 strcss = strcss.replace('@jv','center')
    #             if columna.justificacionverticaltexto == 's':
    #                 strcss = strcss.replace('@jv','start')
    #             if columna.justificacionverticaltexto == 'i':
    #                 strcss = strcss.replace('@jv','end')
    #             try:
    #                 strcss += 'font-family:' + columna.fonttexto.split(',')[0] + ';\n'
    #                 strcss += 'font-size:' + columna.fonttexto.split(',')[1] + ';\n'
    #                 strcss += 'font-weight:' + columna.fonttexto.split(',')[2] + ';\n'
    #             except:
    #                 pass
    #             strcss += 'color:' + columna.colortexto + ';\n'
                
    #             strcss += '}' + '\n'

    #             strcss += '#titulo {' + '\n'
    #             strcss += 'width: ' + str(proyecto.imagentitulowidth) + 'px;\n'                    
    #             strcss += 'height: ' + str(proyecto.imagentituloheight) + 'px;\n'
    #             strcss += '}' + '\n'

    #         elif columna.funcion == 'b':
    #             stri += '<!-- #@[p_base_10] -->' + '\n'
    #             stri += '\t\t<div class="busqueda texto_busqueda col-' + str(columna.secciones) +  '" >@texto' + '\n'
    #             stri += '\t\t\t<!-- #@[p_base_11] -->' + '\n'
    #             stri += '\t\t\t<div class="row no-gutters align-items-center d-flex">' + '\n'
    #             stri += '\t\t\t\t<!-- #@[p_base_12] -->' + '\n'
    #             stri += '\t\t\t\t<div class="col-10 col-md-10 ">' + '\n'
    #             stri += '\t\t\t\t\t<!-- #@[p_base_13] -->' + '\n'
    #             stri += '\t\t\t\t\t<input type="text" id="textob" name="textob" placeholder="Datos del nombre o descripcion">' + '\n'
    #             stri += '\t\t\t\t\t<!-- #@[p_base_14] -->' + '\n'
    #             stri += '\t\t\t\t</div>' + '\n'
    #             stri += '\t\t\t\t<!-- #@[p_base_15] -->' + '\n'
    #             stri += '\t\t\t\t<div class="col-2 col-md-2 ">' + '\n'
    #             stri += '\t\t\t\t\t<!-- #@[p_base_16] -->' + '\n'
    #             stri += '\t\t\t\t\t<a href="" id="link-busqueda" class="btn btn-white" ><img src="{% static "core/img/lupa.png" %}" alt=""></a>' + '\n'
    #             stri += '\t\t\t\t\t<!-- #@[p_base_17] -->' + '\n'
    #             stri += '\t\t\t\t</div>' + '\n'
    #             stri += '\t\t\t\t<!-- #@[p_base_18] -->' + '\n'
    #             stri += '\t\t\t</div>' + '\n'
    #             stri += '<!-- #@[p_base_19] -->' + '\n'
    #             stri += '\t\t</div>\n'
    #             stri += '<!-- #@[p_base_20] -->' + '\n'

    #             strcss += '.busqueda {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'

    #             strcss += 'background: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
    #             strcss = strcss.replace('@direccion_degrade', columna.degradado)
    #             strcss = strcss.replace('@coloruno', columna.color1)
    #             strcss = strcss.replace('@colordos', columna.color2)

    #             if columna.textocolumna != '':
    #                 stri = stri.replace('@texto', columna.textocolumna)
    #             else:
    #                 stri = stri.replace('@texto', '')

    #             if columna.borde:
    #                 strcss += 'border: 1pt solid gray;\n'

    #             strcss += '}' + '\n'

    #             strcss += '.texto_busqueda {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'
    #             if columna.justificacionhorizontaltexto == 'c':
    #                 strcss = strcss.replace('@jh','center')
    #             if columna.justificacionhorizontaltexto == 'i':
    #                 strcss = strcss.replace('@jh','start')
    #             if columna.justificacionhorizontaltexto == 'd':
    #                 strcss = strcss.replace('@jh','end')
    #             if columna.justificacionverticaltexto == 'c':
    #                 strcss = strcss.replace('@jv','center')
    #             if columna.justificacionverticaltexto == 's':
    #                 strcss = strcss.replace('@jv','start')
    #             if columna.justificacionverticaltexto == 'i':
    #                 strcss = strcss.replace('@jv','end')
    #             try:
    #                 strcss += 'font-family:' + columna.fonttexto.split(',')[0] + ';\n'
    #                 strcss += 'font-size:' + columna.fonttexto.split(',')[1] + ';\n'
    #                 strcss += 'font-weight:' + columna.fonttexto.split(',')[2] + ';\n'
    #             except:
    #                 pass
    #             strcss += 'color:' + columna.colortexto + ';\n'
                
    #             strcss += '}' + '\n'

    #         elif columna.funcion == 'm':
    #             stri += '\t\t<!-- #@[p_base_21] -->' + '\n'
    #             stri += '\t\t<div class="menu texto_menu col-' + str(columna.secciones) +  '" >@texto' + '\n'
    #             stri += '\t\t\t<!-- #@[p_base_22] -->' + '\n'
    #             stri += '\t\t\t{% block menu %}{% endblock %}' + '\n'
    #             stri += '\t\t\t<!-- #@[p_base_23] -->' + '\n'
    #             stri += '\t\t</div>\n'
    #             if columna.textocolumna != '':
    #                 stri = stri.replace('@texto', columna.textocolumna)
    #             else:
    #                 stri = stri.replace('@texto', '')

    #             strcss += '.menu {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'

    #             strcss += 'background: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
    #             strcss = strcss.replace('@direccion_degrade', columna.degradado)
    #             strcss = strcss.replace('@coloruno', columna.color1)
    #             strcss = strcss.replace('@colordos', columna.color2)

    #             if columna.textocolumna != '':
    #                 stri = stri.replace('@texto', columna.textocolumna)
    #             else:
    #                 stri = stri.replace('@texto', '')
                
    #             if columna.borde:
    #                 strcss += 'border: 1pt solid gray;\n'

    #             strcss += '}' + '\n'

    #             strcss += '.texto_menu {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'
    #             if columna.justificacionhorizontaltexto == 'c':
    #                 strcss = strcss.replace('@jh','center')
    #             if columna.justificacionhorizontaltexto == 'i':
    #                 strcss = strcss.replace('@jh','start')
    #             if columna.justificacionhorizontaltexto == 'd':
    #                 strcss = strcss.replace('@jh','end')
    #             if columna.justificacionverticaltexto == 'c':
    #                 strcss = strcss.replace('@jv','center')
    #             if columna.justificacionverticaltexto == 's':
    #                 strcss = strcss.replace('@jv','start')
    #             if columna.justificacionverticaltexto == 'i':
    #                 strcss = strcss.replace('@jv','end')
    #             try:
    #                 strcss += 'font-family:' + columna.fonttexto.split(',')[0] + ';\n'
    #                 strcss += 'font-size:' + columna.fonttexto.split(',')[1] + ';\n'
    #                 strcss += 'font-weight:' + columna.fonttexto.split(',')[2] + ';\n'
    #             except:
    #                 pass
    #             strcss += 'color:' + columna.colortexto + ';\n'
                
    #             strcss += '}' + '\n'
    #         elif columna.funcion == 'd':
    #             stri += '\t\t<!-- #@[p_base_21] -->' + '\n'
    #             stri += '\t\t<div class="menu texto_menu col-' + str(columna.secciones) +  '" >@texto' + '\n'
    #             stri += '\t\t\t<!-- #@[p_base_22] -->' + '\n'
    #             stri += '\t\t\t<div class="container" >' + '\n'
    #             stri += '\t\t\t\t{% block cuerpo %}{% endblock %}' + '\n'
    #             stri += '\t\t\t<!-- #@[p_base_23] -->' + '\n'
    #             stri += '\t\t\t</div>\n'
    #             stri += '\t\t</div>\n'
    #             if columna.textocolumna != '':
    #                 stri = stri.replace('@texto', columna.textocolumna)
    #             else:
    #                 stri = stri.replace('@texto', '')

    #             strcss += '.menu {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'

    #             strcss += 'background: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
    #             strcss = strcss.replace('@direccion_degrade', columna.degradado)
    #             strcss = strcss.replace('@coloruno', columna.color1)
    #             strcss = strcss.replace('@colordos', columna.color2)

    #             if columna.textocolumna != '':
    #                 stri = stri.replace('@texto', columna.textocolumna)
    #             else:
    #                 stri = stri.replace('@texto', '')
                
    #             if columna.borde:
    #                 strcss += 'border: 1pt solid gray;\n'

    #             strcss += '}' + '\n'

    #             strcss += '.texto_menu {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'
    #             if columna.justificacionhorizontaltexto == 'c':
    #                 strcss = strcss.replace('@jh','center')
    #             if columna.justificacionhorizontaltexto == 'i':
    #                 strcss = strcss.replace('@jh','start')
    #             if columna.justificacionhorizontaltexto == 'd':
    #                 strcss = strcss.replace('@jh','end')
    #             if columna.justificacionverticaltexto == 'c':
    #                 strcss = strcss.replace('@jv','center')
    #             if columna.justificacionverticaltexto == 's':
    #                 strcss = strcss.replace('@jv','start')
    #             if columna.justificacionverticaltexto == 'i':
    #                 strcss = strcss.replace('@jv','end')
    #             try:
    #                 strcss += 'font-family:' + columna.fonttexto.split(',')[0] + ';\n'
    #                 strcss += 'font-size:' + columna.fonttexto.split(',')[1] + ';\n'
    #                 strcss += 'font-weight:' + columna.fonttexto.split(',')[2] + ';\n'
    #             except:
    #                 pass
    #             strcss += 'color:' + columna.colortexto + ';\n'
                
    #             strcss += '}' + '\n'
    #         else:
    #             stri += '\t\t<!-- #@[p_base_21] -->' + '\n'
    #             stri += '\t\t<div class="' + columna.nombre + ' texto_' + columna.nombre + ' col-' + str(columna.secciones) +  '" >@texto' + '\n'
    #             stri += '\t\t\t<!-- #@[p_base_22] -->' + '\n'
    #             stri += '\t\t\t<!-- #@[p_base_23] -->' + '\n'
    #             stri += '\t\t</div>\n'
    #             if columna.textocolumna != '':
    #                 stri = stri.replace('@texto', columna.textocolumna)
    #             else:
    #                 stri = stri.replace('@texto', '')

    #             strcss += '.' + columna.nombre + ' {' + '\n'
    #             strcss += 'background: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
    #             strcss = strcss.replace('@direccion_degrade', columna.degradado)
    #             strcss = strcss.replace('@coloruno', columna.color1)
    #             strcss = strcss.replace('@colordos', columna.color2)

    #             if columna.textocolumna != '':
    #                 stri = stri.replace('@texto', columna.textocolumna)
    #             else:
    #                 stri = stri.replace('@texto', '')

    #             if columna.borde:
    #                 strcss += 'border: 1pt solid gray;\n'

    #             strcss += '}' + '\n'

    #             strcss += '.texto_' + columna.nombre + ' {' + '\n'
    #             strcss += 'display: flex; align-items: @jv; justify-content: @jh;'
    #             if columna.justificacionhorizontaltexto == 'c':
    #                 strcss = strcss.replace('@jh','center')
    #             if columna.justificacionhorizontaltexto == 'i':
    #                 strcss = strcss.replace('@jh','start')
    #             if columna.justificacionhorizontaltexto == 'd':
    #                 strcss = strcss.replace('@jh','end')
    #             if columna.justificacionverticaltexto == 'c':
    #                 strcss = strcss.replace('@jv','center')
    #             if columna.justificacionverticaltexto == 's':
    #                 strcss = strcss.replace('@jv','start')
    #             if columna.justificacionverticaltexto == 'i':
    #                 strcss = strcss.replace('@jv','end')
    #             try:
    #                 strcss += 'font-family:' + columna.fonttexto.split(',')[0] + ';\n'
    #                 strcss += 'font-size:' + columna.fonttexto.split(',')[1] + ';\n'
    #                 strcss += 'font-weight:' + columna.fonttexto.split(',')[2] + ';\n'
    #             except:
    #                 pass
    #             strcss += 'color:' + columna.colortexto + ';\n'
                
    #             strcss += '}' + '\n'

    #     stri += '<!-- #@[p_base_24] -->' + '\n'
    #     stri += '\t</div>' + '\n'
    #     stri += '<!-- #@[p_base_25] -->' + '\n'
    # stri += '</main>' + '\n'
    # base = base.replace('@css', strcss)
    # base = base.replace('@html', stri)
    # return base

def CrearBaseHtml(modelo,proyecto,base,dc,directorio,directoriogenesis,nombre,etapa,usuario,nombrebase):
    strcss = ''
    nombre = proyecto.nombre
    if nombrebase == 'principal':
        seccion = secpr.objects.get(proyecto=proyecto)
    elif nombrebase == 'proyecto':
        seccion = secp.objects.get(proyecto=proyecto)
    else:
        seccion = secm.objects.get(modelo=modelo)

    ns = seccion.nombre

    # css de gradiente de seccion
    strcss += '\t.' + ns + '{' + '\n'
    # css de borde de seccion
    if seccion.borde:
        strcss += '\t\tborder: 1pt solid gray;' + '\n'
    else:
        strcss += '\t\tborder: none;' + '\n'
    strcss += '\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
    strcss = strcss.replace('@direccion_degrade', seccion.degradado)
    strcss = strcss.replace('@coloruno', seccion.color1)
    strcss = strcss.replace('@colordos', seccion.color2)
    strcss += '\t\theight:' + seccion.altura + ';' + '\n'
    strcss += '\t}' + '\n'

    # codigo html de seccion
    stri = '\t<main class="' + ns + ' container">' + '\n'
    # Desglosar las filas
    listaFila = []
    if nombrebase == 'principal':
        listaFila = filapr.objects.filter(seccion=seccion)
    elif nombrebase == 'proyecto':
        listaFila = filap.objects.filter(seccion=seccion)
    else:
        listaFila = filam.objects.filter(seccion=seccion)

    for fila in listaFila:
        nf = fila.nombre
        # css de fila
        strcss += '\t.' + nf + '{' + '\n'
        # css de borde de fila
        if fila.borde:
            strcss += '\t\tborder: 1pt solid gray;' + '\n'
        else:
            strcss += '\t\tborder: none;' + '\n'
        strcss += '\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
        strcss = strcss.replace('@direccion_degrade', fila.degradado)
        strcss = strcss.replace('@coloruno', fila.color1)
        strcss = strcss.replace('@colordos', fila.color2)
        strcss += '\t\theight:' + fila.altura + ';' + '\n'
        strcss += '\t}' + '\n'
        # codigo html de fila
        stri += '\t\t<div class="' + nf + ' row mt-@secciones">' + '\n'
        stri = stri.replace('@secciones',str(proyecto.separacionsecciones))
        # Desglose de columnas
        listacolumnas = []
        if nombrebase == 'principal':
            listacolumnas = colpr.objects.filter(fila=fila)
        elif nombrebase == 'proyecto':
            listacolumnas = colp.objects.filter(fila=fila)
        else:
            listacolumnas = colm.objects.filter(fila=fila)

        for columna in listacolumnas:
            nc = columna.nombre
            # css de columnas
            strcss += '\t.' + nc + '{' + '\n'
            strcss += '\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
            strcss = strcss.replace('@direccion_degrade', columna.degradado)
            strcss = strcss.replace('@coloruno', columna.color1)
            strcss = strcss.replace('@colordos', columna.color2)
            # css de borde de columna
            if columna.borde:
                strcss += '\t\tborder: 1pt solid gray;' + '\n'
            else:
                strcss += '\t\tborder: none;' + '\n'
            # # font del texto de columna
            # try:
            #     strcss += '\t\tfont-family:' + columna.fonttexto.split(',')[0] + ';\n'
            #     strcss += '\t\tfont-size:' + columna.fonttexto.split(',')[1] + 'pt;\n'
            #     strcss += '\t\tfont-weight:' + columna.fonttexto.split(',')[2] + ';\n'
            # except:
            #     strcss += '\t\tfont-family:Sans-serif;\n'
            #     strcss += '\t\tfont-size:10pt;\n'
            #     strcss += '\t\tfont-weight:500;\n'
            strcss += '\t\theight:auto;' + '\n'
            strcss += '\t\tdisplay: flex; align-items: @jv; justify-content: @jh;' + '\n'
            try:
                strcss += '\t\tmargin-top:' + columna.margeninterno.split(',')[0] + ';' + '\n'
                strcss += '\t\tmargin-right:' + columna.margeninterno.split(',')[1] + ';' + '\n'
                strcss += '\t\tmargin-bottom:' + columna.margeninterno.split(',')[2] + ';' + '\n'
                strcss += '\t\tmargin-left:' + columna.margeninterno.split(',')[3] + ';' + '\n'
            except:
                strcss += '\t\tmargin: 0px;' + '\n'
            strcss += '\t}' + '\n'

            # justificacion dentro de la columna
            if nombrebase != 'principal':
                if columna.funcion == 'l':   #logo
                    if proyecto.avatar:
                        if proyecto.justificacionhorizontallogo == 'c':
                            strcss = strcss.replace('@jh','center')
                        if proyecto.justificacionhorizontallogo == 'i':
                            strcss = strcss.replace('@jh','start')
                        if proyecto.justificacionhorizontallogo == 'd':
                            strcss = strcss.replace('@jh','end')
                        if proyecto.justificacionverticallogo == 'c':
                            strcss = strcss.replace('@jv','center')
                        if proyecto.justificacionverticallogo == 's':
                            strcss = strcss.replace('@jv','start')
                        if proyecto.justificacionverticallogo == 'i':
                            strcss = strcss.replace('@jv','end')
                    else:
                        strcss = strcss.replace('@jh',columna.justificacionhorizontaltexto)
                        strcss = strcss.replace('@jv',columna.justificacionverticaltexto)
                elif columna.funcion == 't':   #titulo
                    if proyecto.imagentitulo or proyecto.titulo != '':
                        if proyecto.justificacionhorizontaltitulo == 'c':
                            strcss = strcss.replace('@jh','center')
                        if proyecto.justificacionhorizontaltitulo == 'i':
                            strcss = strcss.replace('@jh','start')
                        if proyecto.justificacionhorizontaltitulo == 'd':
                            strcss = strcss.replace('@jh','end')
                        if proyecto.justificacionverticaltitulo == 'c':
                            strcss = strcss.replace('@jv','center')
                        if proyecto.justificacionverticaltitulo == 's':
                            strcss = strcss.replace('@jv','start')
                        if proyecto.justificacionverticaltitulo == 'i':
                            strcss = strcss.replace('@jv','end')
                    else:
                        strcss = strcss.replace('@jh',columna.justificacionhorizontaltexto)
                        strcss = strcss.replace('@jv',columna.justificacionverticaltexto)
                elif columna.funcion == 'm':
                    if proyecto.justificacionmenu == 'c':
                        strcss = strcss.replace('@jh','center')
                    if proyecto.justificacionmenu == 'i':
                        strcss = strcss.replace('@jh','start')
                    if proyecto.justificacionmenu == 'd':
                        strcss = strcss.replace('@jh','end')
                    strcss = strcss.replace('@jv','center')
                else:
                    strcss = strcss.replace('@jh',columna.justificacionhorizontaltexto)
                    strcss = strcss.replace('@jv',columna.justificacionverticaltexto)

            # dimension imagen dentro de la columna
            if nombrebase != 'principal':
                if columna.funcion == 'l':   #logo
                    # css de columna de logo
                    strcss += '\t.' + nc + ' img{' + '\n'
                    strcss += '\t\tmax-width: @ancho;\n'                    
                    strcss += '\t\tmax-height: @alto;\n'
                    strcss += '\t\twidth: @ancho;\n'                    
                    strcss += '\t\theight: @alto;\n'
                    if proyecto.avatar:
                        strcss = strcss.replace('@ancho',str(proyecto.avatarwidth) + 'px')                
                        strcss = strcss.replace('@alto',str(proyecto.avatarheight) + 'px')
                    else:
                        strcss = strcss.replace('@ancho',columna.dimensionesimagen.split(',')[0])                
                        strcss = strcss.replace('@alto',columna.dimensionesimagen.split(',')[1])                
                    strcss += '\t}' + '\n'
                elif columna.funcion == 't':   #titulo
                    # css de columna de titulo
                    strcss += '\t.' + nc + ' img{' + '\n'
                    strcss += '\t\tmax-width: @ancho;\n'                    
                    strcss += '\t\tmax-height: @alto;\n'
                    strcss += '\t\twidth: @ancho;\n'                    
                    strcss += '\t\theight: @alto;\n'
                    if proyecto.imagentitulo:
                        strcss = strcss.replace('@ancho',str(proyecto.imagentitulowidth) + 'px')                
                        strcss = strcss.replace('@alto',str(proyecto.imagentituloheight) + 'px')
                    else:
                        strcss = strcss.replace('@ancho',columna.dimensionesimagen.split(',')[0])                
                        strcss = strcss.replace('@alto',columna.dimensionesimagen.split(',')[1])                
                    strcss += '\t}' + '\n'
                else:
                    strcss += '\t.' + nc + ' img{' + '\n'
                    strcss += '\t\tmax-width: @ancho;\n'                    
                    strcss += '\t\tmax-height: @alto;\n'
                    strcss += '\t\twidth: @ancho;\n'                    
                    strcss += '\t\theight: @alto;\n'
                    strcss += '\t}' + '\n'
                    strcss = strcss.replace('@ancho',columna.dimensionesimagen.split(',')[0])                
                    strcss = strcss.replace('@alto',columna.dimensionesimagen.split(',')[1])                
            else:
                if columna.imagen:
                    strcss += '\t.' + nc + ' img{' + '\n'
                    strcss += '\t\tmax-width: @ancho;\n'                    
                    strcss += '\t\tmax-height: @alto;\n'
                    strcss += '\t\twidth: @ancho;\n'                    
                    strcss += '\t\theight: @alto;\n'
                    strcss = strcss.replace('@ancho',columna.dimensionesimagen.split(',')[0])                
                    strcss = strcss.replace('@alto',columna.dimensionesimagen.split(',')[1])                
                    strcss += '\t}' + '\n'

            # font y color de los textos
            strcss += '\t.' + nc + ' span{' + '\n'
            if nombrebase != 'principal' and columna.funcion=='t' and proyecto.titulo != '':
                strcss += '\t\tfont-family:' + proyecto.fonttitulo.split(',')[0] + ';\n'
                strcss += '\t\tfont-size:' + proyecto.fonttitulo.split(',')[1] + 'pt;\n'
                strcss += '\t\tfont-weight:' + proyecto.fonttitulo.split(',')[2] + ';\n'
                strcss += '\t\tcolor:' + proyecto.colortitulo + ';\n'
            else:
                strcss += '\t\tfont-family:' + columna.fonttexto.split(',')[0] + ';\n'
                strcss += '\t\tfont-size:' + columna.fonttexto.split(',')[1] + 'pt;\n'
                strcss += '\t\tfont-weight:' + columna.fonttexto.split(',')[2] + ';\n'
                strcss += '\t\tcolor:' + columna.colortexto + ';\n'
            strcss += '\t}' + '\n'

            # html de columna
            if columna.secciones > 0:
                stri += "\t\t\t<div  class='col-" + str(columna.secciones) + " " + nc + "'>" + '\n'
                if nombrebase == 'principal':
                    if columna.ingresosistema:
                        if columna.imagen:
                            # recuperar el nombre del archivo de imagen
                            nombre_imagen = os.path.basename(columna.imagen.url)
                            # copiar imagen a directorio core
                            CopiaImagenes(directorio + nombre + "/core/static/core/img/" + nombre_imagen , 'proyectos', columna.imagen.url,directoriogenesis + 'media/main/',nombre,etapa,usuario,True )
                            stri += "\t\t\t<a href='{% url 'core:home' %}''><img class='imagen' alt=" + dc + dc + " src=" + dc + "{% static 'core/img/" + nombre_imagen + "' %}" + dc + "></a>" + "\n"
                        else:
                            stri += "\t\t\t<a href='{% url " + '"' + 'core:home' + '"' + " %}'><span>" + columna.textocolumna + "</span></a>\n"
                    else:
                        stri += "\t\t\t<span>" + columna.textocolumna + "</span>\n"
                else:
                    if columna.funcion == 'l':      #logo
                        if proyecto.avatar:
                            stri += "\t\t\t\t<img class='logo' alt=" + dc + dc + " src=" + dc + "{% static 'core/img/logo.png' %}" + dc + ">" + "\n"
                        elif columna.imagen:
                            # recuperar el nombre del archivo de imagen
                            nombre_imagen = os.path.basename(columna.imagen.url)
                            # copiar imagen a directorio core
                            CopiaImagenes(directorio + nombre + "/core/static/core/img/" + nombre_imagen , 'proyectos', columna.imagen.url,directoriogenesis + 'media/main/',nombre,etapa,usuario,True )
                            stri += "\t\t\t\t<img class='logo' + alt=" + dc + dc + " src=" + dc + "{% static 'core/img/" + nombre_imagen + "' %}" + dc + ">" + "\n"
                        else:
                            stri += "\t\t\t<span>" + columna.textocolumna + "</span>\n"

                    elif columna.funcion == 't':    #titulo
                        if proyecto.imagentitulo:
                            stri += "\t\t\t\t<img class='titulo' alt=" + dc + dc + " src=" + dc + "{% static 'core/img/imagentitulo.png' %}" + dc + " width=" + dc + "@imagentitulowidthpx" + dc + " height=" + dc + "@imagentituloheightpx" + dc + " >\n"
                        elif proyecto.titulo != '':
                            stri += "\t\t\t<span>" + proyecto.titulo + "</span>\n"
                        elif columna.imagen:
                            # recuperar el nombre del archivo de imagen
                            nombre_imagen = os.path.basename(columna.imagen.url)
                            # copiar imagen a directorio core
                            CopiaImagenes(directorio + nombre + "/core/static/core/img/" + nombre_imagen , 'proyectos', columna.imagen.url,directoriogenesis + 'media/main/',nombre,etapa,usuario,True )
                            stri += "\t\t\t\t<img class='titulo' + alt=" + dc + dc + " src=" + dc + "{% static 'core/img/" + nombre_imagen + "' %}" + dc + ">" + "\n"
                        else:
                            stri += "\t\t\t<span>" + columna.textocolumna + "</span>\n"
                    elif columna.funcion == 'b':
                        stri += '\t\t\t\t\t<div class="col-11 col-md-11 ">' + '\n'
                        stri += '\t\t\t\t\t\t<input type="text" style="width: 100%;" id="textob" name="textob" placeholder="Datos del nombre o descripcion">' + '\n'
                        stri += '\t\t\t\t\t</div>' + '\n'
                        stri += '\t\t\t\t\t<div class="col-1 col-md-1 ">' + '\n'
                        stri += '\t\t\t\t\t\t<a href="" id="link-busqueda" class="btn btn-white" ><img src="{% static "core/img/lupa.png" %}" alt=""></a>' + '\n'
                        stri += '\t\t\t\t\t</div>' + '\n'
                    elif columna.funcion == 'm':
                        # stri += '\t\t\t<div class="menu texto_menu col-' + str(columna.secciones) +  '" >' + '\n'
                        stri += '\t\t\t\t{% block menu %}{% endblock %}' + '\n'
                        # stri += '\t\t\t</div>\n'
                    elif columna.funcion == 'd':
                        # stri += '\t\t\t<div class="datos texto_datos col-' + str(columna.secciones) +  '" >' + '\n'
                        stri += '\t\t\t\t{% block cuerpo %}{% endblock %}' + '\n'
                        # stri += '\t\t\t</div>\n'
                    else:
                        if columna.imagen:
                            # recuperar el nombre del archivo de imagen
                            nombre_imagen = os.path.basename(columna.imagen.url)
                            # copiar imagen a directorio core
                            CopiaImagenes(directorio + nombre + "/core/static/core/img/" + nombre_imagen , 'proyectos', columna.imagen.url,directoriogenesis + 'media/main/',nombre,etapa,usuario,True )
                            stri += "\t\t\t\t<img class='imagen' + alt=" + dc + dc + " src=" + dc + "{% static 'core/img/" + nombre_imagen + "' %}" + dc + ">" + "\n"
                        else:
                            stri += "\t\t\t<span>" + columna.textocolumna + "</span>\n"

                stri += '\t\t\t</div>' + '\n' # fin de columna

        stri += '\t\t</div>' + '\n' # fin de fila

    stri += '\t</main>' + '\n' # fin de seccion

    base = base.replace('@html', stri)
    base = base.replace('@css', strcss)
    base = base.replace('@ckeditor', '')
    return base

# def CrearBaseHtml(modelo, proyecto, base, dc,directorio,directoriogenesis,nombre,etapa,usuario):
#     strcss = ''
#     ni = 1
#     if modelo == None:
#         seccion = secp.objects.get(proyecto=proyecto)
#     else:
#         seccion = secm.objects.get(modelo=modelo)

#     ns = seccion.nombre
#     strcss += '\t\t.' + seccion.nombre + '{' + '\n'
#     strcss += '/*#@[p_seccion_css_' + ns + '_01]*/' + '\n'
#     strcss += '\t\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
#     strcss = strcss.replace('@direccion_degrade', seccion.degradado)
#     strcss = strcss.replace('@coloruno', seccion.color1)
#     strcss = strcss.replace('@colordos', seccion.color2)
#     if seccion.borde:
#         strcss += '\t\tborder: 1pt solid gray;'
#     else:
#         strcss += '\t\tborder: none;'
#     strcss += '\t\t\theight: ' + str(seccion.altura) + ';' + '\n'
#     strcss += '/*#@[p_seccion_css_' + ns + '_02]*/' + '\n'
#     strcss += '\t\t}' + '\n'

#     stri = '<!-- #@[p_base_01] -->' + '\n'
#     stri += '\t<main class="' + seccion.nombre + ' container">' + '\n'

#     # Dejar el codigo por si algun momento la seccion vuelve a tener imagen
#     # if seccion.imagen:
#     #     if modelo == None:
#     #         CopiaImagenes(directorio + nombre + "/core/static/core/img/imagen_seccion_proyecto.png", 'proyectos', seccion.imagen.url,directoriogenesis + 'media/main/',nombre,etapa,usuario,True )
#     #         base = base.replace("@estilobody","background: url({% static 'core/img/imagen_seccion_proyecto.png' %}) no-repeat center center fixed;background-size: cover;-moz-background-size: cover;-webkit-background-size: cover;-o-background-size: cover;background-color: transparent;")
#     #     else:
#     #         CopiaImagenes(directorio + nombre + "/core/static/core/img/imagen_seccion_modelo_" + modelo.nombre + ".png", 'proyectos', seccion.imagen.url,directoriogenesis + 'media/main/',nombre,etapa,usuario,True )
#     #         base = base.replace("@estilobody","background: url({% static 'core/img/imagen_seccion_modelo_" + modelo.nombre + ".png' %}) no-repeat center center fixed;background-size: cover;-moz-background-size: cover;-webkit-background-size: cover;-o-background-size: cover;background-color: transparent;")
#     # else:
#     #     base = base.replace('@estilobody','')

#     base = base.replace('@estilobody','')

#     # Desglosar las filas

#     if modelo == None:
#         listaFila = filap.objects.filter(seccion=seccion)
#     else:
#         listaFila = filam.objects.filter(seccion=seccion)

#     Nfila = 1
#     for fila in listaFila:
#         nf = fila.nombre
#         strcss += '\t\t.' + fila.nombre + '{' + '\n'
#         strcss += '/*#@[p_fila_' + nf + '_01]*/' + '\n'
#         strcss += '\t\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
#         strcss = strcss.replace('@direccion_degrade', fila.degradado)
#         strcss = strcss.replace('@coloruno', fila.color1)
#         strcss = strcss.replace('@colordos', fila.color2)
#         strcss += '\t\t\theight: ' + str(fila.altura) + ';' + '\n'
#         if fila.borde:
#             strcss += '\t\t\tborder: 1pt solid gray;\n'
#         else:
#             strcss += '\t\t\tborder: none;\n'
#         strcss += '/*#@[p_fila_' + nf + '_02]*/' + '\n'
#         strcss += '\t\t}' + '\n'

#         stri += '<!-- #@[p_fila_' + nf + '_03] -->' + '\n'
#         stri += '\t\t<div class="' + fila.nombre + ' row mb-@separacion">' + '\n'
#         stri = stri.replace('@separacion', str(proyecto.separacionsecciones))
#         if modelo == None:
#             listaColumna = colp.objects.filter(fila=fila)
#         else:
#             listaColumna = colm.objects.filter(fila=fila)

#         Ncolumna = 1
#         for columna in listaColumna:
#             nc = columna.nombre
#             if columna.funcion == 'l':
#                 strcss += '\t\t.' + fila.nombre + ' .texto_logo{' + '\n'
#                 strcss += '/*#@[p_columna_logo_' + nc + '_01]*/' + '\n'
#                 if columna.borde:
#                     strcss += '\t\t\tborder: 1pt solid gray;\n'
#                 else:
#                     strcss += '\t\t\tborder: none;\n'
#                 strcss += '\t\t\theight:100%;' + '\n'
#                 strcss += '\t\t\tdisplay: flex; align-items: @jv; justify-content: @jh;' + '\n'
#                 if proyecto.avatar:
#                     if proyecto.justificacionhorizontallogo == 'c':
#                         strcss = strcss.replace('@jh','center')
#                     if proyecto.justificacionhorizontallogo == 'i':
#                         strcss = strcss.replace('@jh','start')
#                     if proyecto.justificacionhorizontallogo == 'd':
#                         strcss = strcss.replace('@jh','end')
#                     if proyecto.justificacionverticallogo == 'c':
#                         strcss = strcss.replace('@jv','center')
#                     if proyecto.justificacionverticallogo == 's':
#                         strcss = strcss.replace('@jv','start')
#                     if proyecto.justificacionverticallogo == 'i':
#                         strcss = strcss.replace('@jv','end')
#                 else:
#                     strcss = strcss.replace('@jh',columna.justificacionhorizontaltexto)
#                     strcss = strcss.replace('@jv',columna.justificacionverticaltexto)
#                     if columna.imagen:
#                         CopiaImagenes(directorio + nombre + "/core/static/core/img/" + nombre_imagen , 'proyectos', columna.imagen.url,directoriogenesis + 'media/main/',proyecto.nombre,etapa,usuario,True )
#                     else:
#                         try:
#                             strcss += '\t\t\tfont-family:' + columna.fonttexto.split(',')[0] + ';\n'
#                             strcss += '\t\t\tfont-size:' + columna.fonttexto.split(',')[1] + 'pt;\n'
#                             strcss += '\t\t\tfont-weight:' + columna.fonttexto.split(',')[2] + ';\n'
#                         except:
#                             strcss += '\t\t\tfont-family:Sans-serif;\n'
#                             strcss += '\t\t\tfont-size:10pt;\n'
#                             strcss += '\t\t\tfont-weight:500;\n'
#                         strcss += '\t\t\tcolor:' + columna.colortexto + ';\n'
#                 strcss += '\t\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
#                 strcss = strcss.replace('@direccion_degrade', columna.degradado)
#                 strcss = strcss.replace('@coloruno', columna.color1)
#                 strcss = strcss.replace('@colordos', columna.color2)
#                 strcss += '/*#@[p_columna_logo_' + nc + '_02]*/' + '\n'
#                 strcss += '}' + '\n'
#                 if proyecto.avatar:
#                     strcss += '\t\t.' + fila.nombre + ' .texto_logo' + ' .logo {' + '\n'
#                     strcss += '/*#@[p_columna_logo_' + nc + '_03]*/' + '\n'
#                     strcss += '\t\t\twidth: ' + str(proyecto.avatarwidth) + 'px;\n'                    
#                     strcss += '\t\t\theight: ' + str(proyecto.avatarheight) + 'px;\n'
#                     strcss += '/*#@[p_columna_logo_' + nc + '_04]*/' + '\n'
#                     strcss += '\t\t}' + '\n'
#                 elif columna.imagen:
#                     strcss += '\t\t.' + fila.nombre + ' .texto_logo' + ' .logo {' + '\n'
#                     strcss += '/*#@[p_columna_logo_' + nc + '_05]*/' + '\n'
#                     try:
#                         strcss += '\t\t\twidth: ' + columna.dimensionesimagen.split(',')[0] + ';\n'                    
#                         strcss += '\t\t\theight: ' + columna.dimensionesimagen.split(',')[1] + ';\n'
#                     except:
#                         strcss += '\t\t\twidth: 20px;\n'                    
#                         strcss += '\t\t\theight: 20px;\n'
#                     strcss += '/*#@[p_columna_logo_' + nc + '_06]*/' + '\n'
#                     strcss += '\t\t}' + '\n'

#                 stri += '<!-- #@[p_columna_logo_' + nc + '_07] -->' + '\n'
#                 stri += '\t\t\t<div class="logo texto_logo col-' + str(columna.secciones) +  '" >@texto' + '\n'
#                 stri += '<!-- #@[p_columna_logo_' + nc + '_08] -->' + '\n'
#                 if proyecto.avatar:
#                     stri += "\t\t\t\t<img class='logo' alt=" + dc + dc + " src=" + dc + "{% static 'core/img/logo.png' %}" + dc + ">" + "\n"
#                 elif columna.imagen:
#                     # recuperar el nombre del archivo de imagen
#                     nombre_imagen = os.path.basename(columna.imagen.url)
#                     stri += "\t\t\t\t<img class='logo' + alt=" + dc + dc + " src=" + dc + "{% static 'core/img/" + nombre_imagen + "' %}" + dc + ">" + "\n"
#                 stri += '<!-- #@[p_columna_logo_' + nc + '_09] -->' + '\n'
#                 stri += '\t\t\t</div>' + '\n'
#                 stri += '<!-- #@[p_columna_logo_' + nc + '_10] -->' + '\n'

#                 if not proyecto.avatar:
#                     if columna.textocolumna != '':
#                         stri = stri.replace('@texto', columna.textocolumna)
#                     else:
#                         stri = stri.replace('@texto', '')

#             elif columna.funcion == 't':
#                 strcss += '\t\t.' + fila.nombre + ' .texto_titulo {' + '\n'
#                 strcss += '/*#@[p_columna_titulo_' + nc + '_01]*/' + '\n'
#                 strcss += '\t\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
#                 if columna.borde:
#                     strcss += '\t\t\tborder: 1pt solid gray;\n'
#                 else:
#                     strcss += '\t\t\tborder: none;\n'
#                 strcss += '\t\t\theight:100%;' + '\n'
#                 strcss = strcss.replace('@direccion_degrade', columna.degradado)
#                 strcss = strcss.replace('@coloruno', columna.color1)
#                 strcss = strcss.replace('@colordos', columna.color2)
#                 strcss += '\t\t\tdisplay: flex; align-items: @jv; justify-content: @jh;' + '\n'
#                 if proyecto.imagentitulo or proyecto.titulo != '':
#                     if proyecto.justificacionhorizontaltitulo == 'c':
#                         strcss = strcss.replace('@jh','center')
#                     if proyecto.justificacionhorizontaltitulo == 'i':
#                         strcss = strcss.replace('@jh','start')
#                     if proyecto.justificacionhorizontaltitulo == 'd':
#                         strcss = strcss.replace('@jh','end')
#                     if proyecto.justificacionverticaltitulo == 'c':
#                         strcss = strcss.replace('@jv','center')
#                     if proyecto.justificacionverticaltitulo == 's':
#                         strcss = strcss.replace('@jv','start')
#                     if proyecto.justificacionverticaltitulo == 'i':
#                         strcss = strcss.replace('@jv','end')
#                 else:
#                     strcss = strcss.replace('@jh',columna.justificacionhorizontaltexto)
#                     strcss = strcss.replace('@jv',columna.justificacionverticaltexto)
#                     if columna.imagen:
#                         CopiaImagenes(directorio + nombre + "/core/static/core/img/" + nombre_imagen , 'proyectos', columna.imagen.url,directoriogenesis + 'media/main/',proyecto.nombre,etapa,usuario,True )
#                     else:
#                         try:
#                             strcss += '\t\t\tfont-family:' + columna.fonttexto.split(',')[0] + ';\n'
#                             strcss += '\t\t\tfont-size:' + columna.fonttexto.split(',')[1] + 'pt;\n'
#                             strcss += '\t\t\tfont-weight:' + columna.fonttexto.split(',')[2] + ';\n'
#                         except:
#                             strcss += '\t\t\tfont-family:Sans-serif;\n'
#                             strcss += '\t\t\tfont-size:10pt;\n'
#                             strcss += '\t\t\tfont-weight:500;\n'
#                         strcss += '\t\t\tcolor:' + columna.colortexto + ';\n'
#                 strcss += '/*#@[p_columna_titulo_' + nc + '_02]*/' + '\n'
#                 strcss += '\t\t}' + '\n'

#                 if proyecto.imagentitulo:
#                     strcss += '\t\t.' + fila.nombre + ' .texto_titulo .titulo {' + '\n'
#                     strcss += '/*#@[p_columna_titulo_' + nc + '_03]*/' + '\n'
#                     strcss += '\t\t\twidth: ' + str(proyecto.imagentitulowidth) + 'px;\n'                    
#                     strcss += '\t\t\theight: ' + str(proyecto.imagentituloheight) + 'px;\n'
#                     strcss += '/*#@[p_columna_titulo_' + nc + '_04]*/' + '\n'
#                     strcss += '\t\t}' + '\n'
#                 elif columna.imagen:
#                     strcss += '\t\t.' + fila.nombre + ' .texto_logo' + ' .logo {' + '\n'
#                     strcss += '/*#@[p_columna_titulo_' + nc + '_05]*/' + '\n'
#                     try:
#                         strcss += '\t\t\twidth: ' + columna.dimensionesimagen.split(',')[0] + ';\n'                    
#                         strcss += '\t\t\theight: ' + columna.dimensionesimagen.split(',')[1] + ';\n'
#                     except:
#                         strcss += '\t\t\twidth: 80px;\n'                    
#                         strcss += '\t\t\theight: 20px;\n'
#                     strcss += '/*#@[p_columna_titulo_' + nc + '_06]*/' + '\n'
#                     strcss += '\t\t}' + '\n'

#                 stri += '\t\t\t<div class="titulo texto_titulo col-' + str(columna.secciones) +  '" >@texto' + '\n'
#                 stri += '<!-- #@[p_columna_titulo_' + nc + '_07] -->' + '\n'
#                 if proyecto.imagentitulo:
#                     stri += "\t\t\t\t<img class='titulo' alt=" + dc + dc + " src=" + dc + "{% static 'core/img/imagentitulo.png' %}" + dc + " width=" + dc + "@imagentitulowidthpx" + dc + " height=" + dc + "@imagentituloheightpx" + dc + " >\n"
#                 elif columna.imagen:
#                     # recuperar el nombre del archivo de imagen
#                     nombre_imagen = os.path.basename(columna.imagen.url)
#                     stri += "\t\t\t\t<img class='titulo' + alt=" + dc + dc + " src=" + dc + "{% static 'core/img/" + nombre_imagen + "' %}" + dc + ">" + "\n"
#                 elif proyecto.titulo:
#                     stri += '\t\t\t\t' + proyecto.titulo + '\n'
#                 stri += '<!-- #@[p_columna_titulo_' + nc + '_08] -->' + '\n'
#                 stri += '\t\t\t</div>\n'
#                 stri += '<!-- #@[p_base_columna_titulo_' + nc + '_09] -->' + '\n'

#                 if not proyecto.imagentitulo and proyecto.titulo == '':
#                     if columna.textocolumna != '':
#                         stri = stri.replace('@texto', columna.textocolumna)
#                     else:
#                         stri = stri.replace('@texto', '')

#             elif columna.funcion == 'b':
#                 strcss += '\t\t.' + fila.nombre + ' .texto_busqueda {' + '\n'
#                 strcss += '/*#@[p_columna_busqueda_' + nc + '_01]*/' + '\n'
#                 strcss += '\t\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
#                 strcss = strcss.replace('@direccion_degrade', columna.degradado)
#                 strcss = strcss.replace('@coloruno', columna.color1)
#                 strcss = strcss.replace('@colordos', columna.color2)
#                 if columna.borde:
#                     strcss += '\t\t\tborder: 1pt solid gray;\n'
#                 else:
#                     strcss += '\t\t\tborder: none;\n'
#                 strcss += '/*#@[p_columna_busqueda_' + nc + '_02]*/' + '\n'
#                 strcss += '\t\t\theight:100%;}' + '\n'

#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_03] -->' + '\n'
#                 stri += '\t\t\t<div class="busqueda texto_busqueda col-' + str(columna.secciones) +  '" >' + '\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_05] -->' + '\n'
#                 stri += '\t\t\t\t<div class="row no-gutters align-items-center d-flex">' + '\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_06] -->' + '\n'
#                 stri += '\t\t\t\t\t<div class="col-10 col-md-10 ">' + '\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_07] -->' + '\n'
#                 stri += '\t\t\t\t\t\t<input type="text" id="textob" name="textob" placeholder="Datos del nombre o descripcion">' + '\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_08] -->' + '\n'
#                 stri += '\t\t\t\t\t</div>' + '\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_09] -->' + '\n'
#                 stri += '\t\t\t\t\t<div class="col-2 col-md-2 ">' + '\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_10] -->' + '\n'
#                 stri += '\t\t\t\t\t\t<a href="" id="link-busqueda" class="btn btn-white" ><img src="{% static "core/img/lupa.png" %}" alt=""></a>' + '\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_11] -->' + '\n'
#                 stri += '\t\t\t\t\t</div>' + '\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_12] -->' + '\n'
#                 stri += '\t\t\t\t</div>' + '\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_13] -->' + '\n'
#                 stri += '\t\t\t</div>\n'
#                 stri += '<!-- #@[p_base_busqueda_' + nc + '_14] -->' + '\n'

#             elif columna.funcion == 'm':
#                 strcss += '\t\t.' + fila.nombre + ' .texto_menu {' + '\n'
#                 strcss += '/*#@[p_columna_menu_' + nc + '_01]*/' + '\n'
#                 strcss += '\t\t\tdisplay: flex; justify-content: @jh;' + '\n'
#                 strcss += '\t\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
#                 strcss = strcss.replace('@direccion_degrade', columna.degradado)
#                 strcss = strcss.replace('@coloruno', columna.color1)
#                 strcss = strcss.replace('@colordos', columna.color2)

#                 if columna.borde:
#                     strcss += '\t\t\tborder: 1pt solid gray;\n'
#                 else:
#                     strcss += '\t\t\tborder: none;\n'
#                 strcss += '\t\t\theight:100%;' + '\n'
#                 strcss += '\t\t\tdisplay: flex; align-items: @jv; justify-content: @jh;' + '\n'
#                 if proyecto.justificacionmenu == 'c':
#                     strcss = strcss.replace('@jh','center')
#                 if proyecto.justificacionmenu == 'i':
#                     strcss = strcss.replace('@jh','start')
#                 if proyecto.justificacionmenu == 'd':
#                     strcss = strcss.replace('@jh','end')
#                 try:
#                     strcss += '\t\t\tfont-family:' + proyecto.fontmenu.split(',')[0] + ';\n'
#                     strcss += '\t\t\tfont-size:' + proyecto.fontmenu.split(',')[1] + 'pt;\n'
#                     strcss += '\t\t\tfont-weight:' + proyecto.fontmenu.split(',')[2] + ';\n'
#                 except:
#                     pass
#                 strcss += '\t\t\tcolor:' + proyecto.colormenu + ';\n'
#                 strcss += '/*#@[p_columna_menu_' + nc + '_02]*/' + '\n'
#                 strcss += '\t\t}' + '\n'

#                 stri += '<!-- #@[p_base_menu_' + nc + '_03] -->' + '\n'
#                 stri += '\t\t\t<div class="menu texto_menu col-' + str(columna.secciones) +  '" >' + '\n'
#                 stri += '<!-- #@[p_base_menu_' + nc + '_04] -->' + '\n'
#                 stri += '\t\t\t\t{% block menu %}{% endblock %}' + '\n'
#                 stri += '<!-- #@[p_base_menu_' + nc + '_05] -->' + '\n'
#                 stri += '\t\t\t</div>\n'

#             elif columna.funcion == 'd':
#                 strcss += '\t\t.' + fila.nombre + ' .texto_datos {' + '\n'
#                 strcss += '/*#@[p_columna_datos_' + nc + '_01]*/' + '\n'
#                 strcss += '\t\t\tpadding: 10px 10px 10px 10px;' + '\n'
#                 strcss += '\t\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
#                 strcss = strcss.replace('@direccion_degrade', columna.degradado)
#                 strcss = strcss.replace('@coloruno', columna.color1)
#                 strcss = strcss.replace('@colordos', columna.color2)
#                 if columna.borde:
#                     strcss += '\t\t\tborder: 1pt solid gray;\n'
#                 else:
#                     strcss += '\t\t\tborder: none;\n'
#                 strcss += '/*#@[p_columna_datos_' + nc + '_02]*/' + '\n'
#                 strcss += '\t\theight:100%;}' + '\n'

#                 stri += '<!-- #@[p_base_datos_' + nc + '_03] -->' + '\n'
#                 stri += '\t\t\t<div class="datos texto_datos col-' + str(columna.secciones) +  '" >' + '\n'
#                 stri += '<!-- #@[p_base_datos_' + nc + '_04] -->' + '\n'
#                 stri += '\t\t\t\t{% block cuerpo %}{% endblock %}' + '\n'
#                 stri += '<!-- #@[p_base_datos_' + nc + '_05] -->' + '\n'
#                 stri += '\t\t\t</div>\n'
#             else:
#                 strcss += '\t\t.texto_' + columna.nombre + ' {' + '\n'
#                 strcss += '/*#@[p_columna_otros_' + nc + '_01]*/' + '\n'
#                 strcss += '\t\t\tbackground: linear-gradient(to @direccion_degrade, @coloruno, @colordos);' + '\n'
#                 strcss = strcss.replace('@direccion_degrade', columna.degradado)
#                 strcss = strcss.replace('@coloruno', columna.color1)
#                 strcss = strcss.replace('@colordos', columna.color2)

#                 if columna.borde:
#                     strcss += '\t\t\tborder: 1pt solid gray;\n'
#                 else:
#                     strcss += '\t\t\tborder: none;\n'

#                 strcss += '\t\t\theight:100%;' + '\n'
#                 strcss += '\t\t\tdisplay: flex; align-items: @jv; justify-content: @jh;' + '\n'
#                 strcss = strcss.replace('@jh',columna.justificacionhorizontaltexto)
#                 strcss = strcss.replace('@jv',columna.justificacionverticaltexto)
#                 try:
#                     strcss += '\t\t\tfont-family:' + columna.fonttexto.split(',')[0] + ';\n'
#                     strcss += '\t\t\tfont-size:' + columna.fonttexto.split(',')[1] + 'pt;\n'
#                     strcss += '\t\t\tfont-weight:' + columna.fonttexto.split(',')[2] + ';\n'
#                 except:
#                     pass
#                 strcss += '\t\t\tcolor:' + columna.colortexto + ';\n'
#                 strcss += '/*#@[p_columna_otros_' + nc + '_02]*/' + '\n'
#                 strcss += '\t\t}' + '\n'

#                 stri += '<!-- #@[p_base_columna_' + nc + '_03] -->' + '\n'
#                 stri += '\t\t\t<div class="' + columna.nombre + ' texto_' + columna.nombre + ' col-' + str(columna.secciones) +  '" >@texto' + '\n'
#                 stri += '@imagen' + '\n'
#                 stri += '<!-- #@[p_base_columna_' + nc + '_04] -->' + '\n'
#                 stri += '\t\t\t</div>\n'
#                 if columna.textocolumna != '':
#                     stri = stri.replace('@texto', columna.textocolumna)
#                 else:
#                     stri = stri.replace('@texto', '')

#                 if not columna.imagen :
#                     if columna.textocolumna != '':
#                         stri = stri.replace('@texto', columna.textocolumna)
#                     else:
#                         stri = stri.replace('@texto', '')

#                     stri = stri.replace('@imagen','')
#                 else:
#                     if modelo == None:
#                         CopiaImagenes(directorio + nombre + "/core/img/imagen_columna_proyecto_" + str(ni) + "_" + proyecto.nombre + ".png", 'proyectos', columna.imagen.url,directoriogenesis + 'media/main/',nombre,etapa,usuario,True )
#                         stri = stri.replace("@imagen", "\t\t\t\t<img id='titulo' alt=" + dc + dc + " src=" + dc + "{% static '/core/img/imagen_columna_proyecto_" + str(ni) + "_" + proyecto.nombre + ".png' %}" + dc + " width=" + dc + "@imagentitulowidthpx" + dc + " height=" + dc + "@imagentituloheightpx" + dc + " >\n")
#                         print('entro en columna',nc, columna.funcion,stri)
#                     else:
#                         print('columna imagen ',nc,columna.imagen.url)
#                         CopiaImagenes(directorio + nombre + "/core/img/imagen_columna_modelo_" + str(ni) + "_" + modelo.nombre + ".png", 'proyectos', columna.imagen.url,directoriogenesis + 'media/main/',nombre,etapa,usuario,True )
#                         stri = stri.replace("@imagen", "\t\t\t\t<img id='titulo' alt=" + dc + dc + " src=" + dc + "{% static '/core/img/imagen_columna_modelo_" + str(ni) + "_" + modelo.nombre + ".png' %}" + dc + " width=" + dc + "@imagentitulowidthpx" + dc + " height=" + dc + "@imagentituloheightpx" + dc + " >\n")
#                     ni += 1
#             Ncolumna += 28
#         stri += '<!-- #@[p_fila_' + nf + '_02] -->' + '\n'
#         stri += '\t\t</div>' + '\n'
#         Nfila += 2
#     stri += '\t</main>' + '\n'
#     base = base.replace('@css', strcss)
#     base = base.replace('@html', stri)
#     base = base.replace('@ckeditor', '')
#     return base

def AsignaFonts(font,par,strFont):
    strt = font.split(',')
    strFont = strFont.replace('@' + par + 'fontfamily', "'" + strt[0] + "'")
    strFont = strFont.replace('@' + par + 'fontsize', strt[1])
    strFont = strFont.replace('@' + par + 'fontweight', strt[2])
    return strFont

def NumeroPorcentaje(par,valor,texto):
    if valor <0:
        texto = texto.replace(par,str(valor*-1) + '%')
    else:
        texto = texto.replace(par,str(valor) + 'px')
    return texto

def AsignaJustificacion(hv, justi, par, strJusti):
    if hv == 'h':
        if justi == 'i':
            strj = 'justify-content-start'
        if justi == 'd':
            strj = 'justify-content-end'
        if justi == 'c':
            strj = 'justify-content-center'
        strJusti = strJusti.replace(par, strj)

    if hv == 'v':
        if justi == 's':
            strj = 'align-items-start'
        if justi == 'c':
            strj = 'align-items-center'
        if justi == 'i':
            strj = 'align-items-end'
        strJusti = strJusti.replace(par, strj)

    return strJusti

def LeerArchivoEnTexto(archivo, etapa, nombreProyecto,usuario):
    strTexto = ''
    try:
        with open(archivo) as file_object:
            for line in file_object:
                strTexto += line 
    except Exception as e:
        errores = ErroresCreacion()
        errores.etapa = etapa
        errores.paso = "Leer el archivo en Texto: " + archivo
        errores.proyecto = nombreProyecto
        errores.usuario = usuario
        errores.descripcion = e
        errores.severo = True
        errores.save()
    return strTexto

def CopiarArchivos(origen,destino,etapa,nombreProyecto,usuario,borraPrevio):

    if borraPrevio:
        try:
            os.remove(destino)
        except:
            pass

    try:
        shutil.copy(origen, destino)
    except  Exception as e:
        errores = ErroresCreacion()
        errores.etapa = etapa
        errores.paso = "Copiar el archivo: " + origen + " en: " + destino
        errores.proyecto = nombreProyecto
        errores.usuario = usuario
        errores.descripcion = e
        errores.severo = True
        errores.save()

def CrearDirectorio(nombreDirectorio, etapa, nombreProyecto, usuario,borraPrevio):

    if borraPrevio:
        try:
            shutil.rmtree(nombreDirectorio)
        except Exception as e:
            print('error de directorio', str(e))
            pass

    try:
        os.mkdir(nombreDirectorio)
    except Exception as e:
        errores = ErroresCreacion()
        errores.etapa = etapa
        errores.paso = "Crear el directorio: " + nombreDirectorio
        errores.proyecto = nombreProyecto
        errores.usuario = usuario
        errores.descripcion = e
        errores.severo = True
        errores.save()
        
def EscribirEnArchivo(archivo,texto,etapa,nombreProyecto,usuario):

    try:
        with open(archivo, 'w') as file_object:
            file_object.write(texto)
    except Exception as e:
        errores = ErroresCreacion()
        errores.etapa = etapa
        errores.paso = "No se escribio en el archivo: " + archivo
        errores.proyecto = nombreProyecto
        errores.usuario = usuario
        errores.descripcion = e
        errores.severo = True
        errores.save()

def AplicacionConObjetoRaiz(aplicacion):
    for mod in Modelo.objects.filter(aplicacion=aplicacion):
        if mod.padre == 'nada':
            return True
    return False

def ProcesoPersonalizacion(proyecto,aplicacion,archivo,directorio,stri,nombre,etapa,usuario):
    stri = EscribePersonalizacion(proyecto,aplicacion,archivo,stri)
    #Sin lineas de personalizacion
    if not proyecto.conetiquetaspersonalizacion:
        stri = QuitaLineasPersonalizacion(stri)

    EscribirArchivo(directorio + archivo,etapa,nombre,stri,usuario,True)

def EscribirArchivo(nombreArchivo, etapa,nombreProyecto,texto,usuario,borraPrevio):

    if borraPrevio:
        try:
            os.remove(nombreArchivo)
        except:
            pass

    try:
        with open(nombreArchivo, 'w') as file_object:
            file_object.write(texto)
    except  Exception as e:
        errores = ErroresCreacion()
        errores.etapa = etapa
        errores.paso = "Escribir archivo: " + nombreArchivo
        errores.proyecto = nombreProyecto
        errores.usuario = usuario
        errores.descripcion = e
        errores.severo = True
        errores.save()

def EscribePersonalizacion(proyecto, nombre_aplicacion, archivo, texto):
    strLineaNueva = ''
    # Leer todas las personalizaciones
    # Ver si cada una de ellas esta en el texto
    # Si esta entonces leer el texto con Returns hasta encontrar el tag de personalizacion
    # Reemplazar en la linea los [] por ()
    # Incorporar la linea en el texto
    # Incorporar el codigo de personalizacion de la base en el texto
    # Incorporar en el texto #@()

    lista_perso = Personaliza.objects.filter(usuario=proyecto.usuario, 
                                        proyecto=proyecto, 
                                        aplicacion=nombre_aplicacion, 
                                        archivo=archivo)
    
    for perso in lista_perso:
        if perso.tag in texto:
            lineas = texto.split('\n')
            for linea in lineas:
                if perso.tag in linea:
                    if '<!-- ' in linea:
                        # archivo html
                        strLineaNueva += '<!-- #@(' + perso.tag + ') -->' + '\n'
                    elif '/*' in linea:
                        # archivo css
                        strLineaNueva += '/* #@(' + perso.tag + ') */' + '\n'
                    else:
                        strLineaNueva += '#@(' + perso.tag + ')' + '\n'                        
                    strcodi=perso.codigo.split('\n')
                    for strCod in strcodi:
                        strLineaNueva += strCod + '\n'
                    if '<!-- ' in linea:
                        # archivo html
                        strLineaNueva += '<!-- #@() -->' + '\n'
                    elif '/*' in linea:
                        # archivo css
                        strLineaNueva += '/* #@() */' + '\n'
                    else:
                        strLineaNueva += '#@()' + '\n'
                else:
                    strLineaNueva += linea +'\n'
            texto = strLineaNueva
            strLineaNueva = ''
    return texto

def QuitaLineasPersonalizacion(texto):
    strLineaNueva = ''
    lineas = texto.split('\n')
    for linea in lineas:
        if not '#@[' in linea:
            strLineaNueva += linea + '\n'

    return strLineaNueva

def AplicacionTienePropiedades(aplicacion):
    flgCrear = False
    for modelo in Modelo.objects.filter(aplicacion=aplicacion):
        if Propiedad.objects.filter(modelo=modelo).count() > 0:
            flgCrear = True
            break
    return flgCrear

def PropiedadesEnLista(modelo,Propiedad,tabs):
    strlr = ''
    strlt = ''
    strtt = ''
    columnashijos = 0
    for propiedad in Propiedad.objects.filter(modelo=modelo):
        num = 1
        if propiedad.enlista:
            columnashijos += propiedad.numerocolumnas

            # Propiedades que se totalizan

            if propiedad.totaliza:
                if propiedad.enmobile:
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                    num += 1
                    strtt += '\t\t\t\t\t\t<div class="col-12 col-md-@numerocolumnas d-flex @justificaciontextocolumna dato_@nombrecolumnapropiedad">' + '\n'
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                    num += 1
                else:
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                    num += 1
                    strtt += '\t\t\t\t\t\t<div class="d-none d-md-flex col-md-@numerocolumnas d-flex @justificaciontextocolumna  dato_@nombrecolumnapropiedad">' + '\n'
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                    num += 1
                strtt += '\t\t\t\t\t\t\t@totalizacolumna' + '\n'
                strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strtt += '\t\t\t\t\t\t</div>' + '\n'
                strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strtt = strtt.replace('@totalizacolumna','{{@total_propiedad}}')
                strtt = strtt.replace('@total_propiedad','total_' + propiedad.nombre)
            else:
                strtt = strtt.replace('@totalizacolumna','')
                if propiedad.enmobile:
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                    num += 1
                    strtt += '\t\t\t\t\t\t<div class="col-12 col-md-@numerocolumnas d-flex @justificaciontextocolumna dato_@nombrecolumnapropiedad">' + '\n'
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                    num += 1
                    strtt += '\t\t\t\t\t\t</div>' + '\n'
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                else:
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                    num += 1
                    strtt += '\t\t\t\t\t\t<div class="d-none d-md-flex col-md-@numerocolumnas d-flex @justificaciontextocolumna  dato_@nombrecolumnapropiedad">' + '\n'
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                    num += 1
                    strtt += '\t\t\t\t\t\t</div>' + '\n'
                    strtt += '<!-- #@[p_modelo_totaliza_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                    num += 1

            if propiedad.enmobile:
                strlt += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strlt += tabs + '\t\t\t\t\t<div class="col-12 col-md-@numerocolumnas d-flex @justificaciontextocolumna align-self-center @uppercase columna_propiedad_@nombrecolumnapropiedad">' + '\n'
                strlt += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
            else:
                strlt += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strlt += tabs + '\t\t\t\t\t<div class="d-none d-md-flex col-md-@numerocolumnas d-flex @justificaciontextocolumna  align-self-center @uppercase columna_propiedad_@nombrecolumnapropiedad">' + '\n'
                strlt += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
            strlt += tabs + '\t\t\t\t\t\t@textocolumnapropiedad' + '\n'
            strlt += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
            num += 1
            strlt += tabs + '\t\t\t\t\t</div>' + '\n'
            strlt += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
            num += 1

            if propiedad.enmobile:
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strlr += tabs + '\t\t\t\t\t\t<div class="col-12 col-md-@numerocolumnas d-flex @justificaciontextocolumna dato_@nombrecolumnapropiedad">' + '\n'
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
            else:
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strlr += tabs + '\t\t\t\t\t\t<div class="d-none d-md-flex col-md-@numerocolumnas d-flex @justificaciontextocolumna dato_@nombrecolumnapropiedad">' + '\n'
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1


            if propiedad.tipo == 'r':
                strlb = propiedad.textobotones.split(';')
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                for txc in strlb:
                    tx = txc.split(',')
                    if propiedad.linkparaedicion:
                        if propiedad.modelo.proyecto.conroles:
                            strlr += tabs + '\t\t\t\t\t\t\t{% if  puede_editar %}' + '\n'
                            strlr += tabs + '\t\t\t\t\t\t\t\t{% if obj.' + propiedad.nombre + ' == ' + "'" + tx[0] + "'" + ' %}<a href="{% url ' + "'" + '@aplicacion:editar_@modelo' + "'" + ' obj.id %}">' + '@rol' + tx[1] + '@finrol' + '</a>{% endif %}' + '\n'
                            strlr += tabs + '\t\t\t\t\t\t\t{% elif puede_ver %}' + '\n'
                            strlr += tabs + '\t\t\t\t\t\t\t{% if obj.' + propiedad.nombre + ' == ' + "'" + tx[0] + "'" + ' %}<a href="{% url ' + "'" + '@aplicacion:editar_@modelo' + "'" + ' obj.id %}">' + '@rol' + tx[1] + '@finrol' + '</a>{% endif %}' + '\n'
                            strlr += tabs + '\t\t\t\t\t\t\t{% endif %}' + '\n'
                        else:
                            strlr += tabs + '\t\t\t\t\t\t\t{% if obj.' + propiedad.nombre + ' == ' + "'" + tx[0] + "'" + ' %}<a href="{% url ' + "'" + '@aplicacion:editar_@modelo' + "'" + ' obj.id %}">' + '@rol' + tx[1] + '@finrol' + '</a>{% endif %}' + '\n'
                    else:
                        strlr += tabs + '\t\t\t\t\t\t\t{% if obj.' + propiedad.nombre + ' == ' + "'" + tx[0] + "'" + ' %}' + '@rol' + tx[1] + '@finrol' + '{% endif %}' + '\n'
                strlr += tabs + '\t\t\t\t\t\t</div>' + '\n'
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
            elif propiedad.tipo != 'p':
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                if propiedad.linkparaedicion:
                    if propiedad.modelo.proyecto.conroles:
                        strlr += tabs + '\t\t\t\t\t\t\t{% if  puede_editar %}' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t\t<a href="{% url ' + "'" + '@aplicacion:editar_@modelo' + "'" + ' obj.id %}">@rol{{obj.@nombrepropiedad@formatofecha}}@finrol</a>' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t{% elif puede_ver_' + propiedad.nombre + ' %}' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t\t@rol{{obj.@nombrepropiedad@formatofecha}}@finrol' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t{% endif %}' + '\n'
                    else:
                        strlr += tabs + '\t\t\t\t\t\t\t<a href="{% url ' + "'" + '@aplicacion:editar_@modelo' + "'" + ' obj.id %}">@rol{{obj.@nombrepropiedad@formatofecha}}@finrol</a>' + '\n'
                else:
                    strlr += tabs + '\t\t\t\t\t\t\t@rol{{obj.@nombrepropiedad@formatofecha}}@finrol' + '\n'
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strlr += tabs + '\t\t\t\t\t\t</div>' + '\n'
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
            else:
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strlr += tabs + '\t\t\t\t\t\t\t{% if obj.@nombrepropiedad %}' + '\n'
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                if propiedad.linkparaedicion:
                    if propiedad.modelo.proyecto.conroles:
                        strlr += tabs + '\t\t\t\t\t\t\t{% if  puede_editar %}' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t\t<a href="{% url ' + "'" + '@aplicacion:editar_@modelo' + "'" + ' obj.id %}">' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t\t\t@rol<img src="{{obj.@nombrepropiedad.url}}" width="20px" height="20px" alt="">@finrol' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t\t</a>' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t{% elif puede_ver_' + propiedad.nombre + ' %}' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t{% endif %}' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t\t<a href="{% url ' + "'" + '@aplicacion:editar_@modelo' + "'" + ' obj.id %}">' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t\t\t@rol<img src="{{obj.@nombrepropiedad.url}}" width="20px" height="20px" alt="">@finrol' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t\t</a>' + '\n'
                    else:
                        strlr += tabs + '\t\t\t\t\t\t\t<a href="{% url ' + "'" + '@aplicacion:editar_@modelo' + "'" + ' obj.id %}">' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t\t@rol<img src="{{obj.@nombrepropiedad.url}}" width="20px" height="20px" alt="">@finrol' + '\n'
                        strlr += tabs + '\t\t\t\t\t\t\t</a>' + '\n'
                
                else:
                    strlr += tabs + '\t\t\t\t\t\t\t\t@rol<img src="{{obj.@nombrepropiedad.url}}" width="20px" height="20px" alt="">@finrol' + '\n'
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strlr += tabs + '\t\t\t\t\t\t\t{% endif %}' + '\n'
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
                strlr += tabs + '\t\t\t\t\t\t</div>' + '\n'
                strlr += '<!-- #@[p_modelo_list_' + propiedad.nombre + '_' + str(num) + '] -->' + '\n'
                num += 1
            
            ff = ''
            if propiedad.formatofecha != '':
                ff = '| date:' + "'" + propiedad.formatofecha.replace('%','') + "'"

            if modelo.proyecto.conroles:
                strlr = strlr.replace('@rol','{% if puede_ver_@nombrepropiedad %}')
                strlr = strlr.replace('@finrol','{% endif %}')
            else:
                strlr = strlr.replace('@rol','')
                strlr = strlr.replace('@finrol','')

            strlr = strlr.replace('@formatofecha', ff)
            strlt = strlt.replace('@numerocolumnas', str(propiedad.numerocolumnas))
            strtt = strtt.replace('@numerocolumnas', str(propiedad.numerocolumnas))
            strlr = strlr.replace('@numerocolumnas', str(propiedad.numerocolumnas))
            strlr = strlr.replace('@nombrepropiedad', propiedad.nombre)
            strtt = strtt.replace('@nombrepropiedad', propiedad.nombre)

            # Textos de columna
            if propiedad.textocolumna != '':
                strlt = strlt.replace('@textocolumnapropiedad', propiedad.textocolumna)
            else:
                strlt = strlt.replace('@textocolumnapropiedad', propiedad.nombre)
            strlt = strlt.replace('@nombrecolumnapropiedad', propiedad.nombre)
            strlr = strlr.replace('@nombrecolumnapropiedad', propiedad.nombre)
            strtt = strtt.replace('@nombrecolumnapropiedad', propiedad.nombre)

            # Mayusculas columna
            strlt = UpperLower(modelo.mayusculascolumnas,'@uppercase',strlt)

            #justificacion columnas
            strlt = AsignaJustificacion('h',propiedad.justificaciontextocolumna,'@justificaciontextocolumna',strlt)
            strlr = AsignaJustificacion('h',propiedad.justificaciontextocolumna,'@justificaciontextocolumna',strlr)
            strtt = AsignaJustificacion('h',propiedad.justificaciontextocolumna,'@justificaciontextocolumna',strtt)

    return (strlt,strlr,columnashijos,strtt)

def UpperLower(mayu,par,texto):
    if mayu:
        texto = texto.replace(par, 'text-uppercase')
    else:
        texto = texto.replace(par, '')
    return texto

def AsignaTexto(textoOficial, textoAlterno,textoAreemplazar,strTexto ):
    try:
        strteb = textoOficial.split(',')
        strTexto = strTexto.replace(textoAreemplazar.split(',')[0], strteb[0])
        strTexto = strTexto.replace(textoAreemplazar.split(',')[1], strteb[1])
    except:
        strteb = textoAlterno.split(',')
        strTexto = strTexto.replace(textoAreemplazar.split(',')[0], strteb[0])
        strTexto = strTexto.replace(textoAreemplazar.split(',')[1], strteb[1])
    return strTexto

def Etiquetas(modelo,strt,strcss,tabs,directorio,nombre,etapa,usuario):
    #etiquetas
    strcss = AsignaFonts(modelo.fontlabelmodelo,'label'+modelo.nombre,strcss)
    strcss = strcss.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)

    # controles

    strctl = IncludeModeloFormulario(modelo,tabs,directorio,nombre,etapa,usuario)
    strt = strt.replace('@controles', tabs + "\t\t\t\t{% include 'core/includes/formulario_" + modelo.nombre + ".html'%}")

    # Dash
    if modelo.padre == 'nada':
        strctl = IncludeModeloFormularioDash(modelo,tabs,directorio,nombre,etapa,usuario)
        strt = strt.replace('@controles', tabs + "\t\t\t\t{% include 'core/includes/formulario_dash_" + modelo.nombre + ".html'%}")

    texto = []
    texto.append(strt)
    texto.append(strcss)

    return texto

def EtiquetasDash(modelo,strt,strcss,tabs,directorio,nombre,etapa,usuario):
    #etiquetas
    strcss = AsignaFonts(modelo.fontlabelmodelo,'label'+modelo.nombre,strcss)
    strcss = strcss.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)

    # controles
    if modelo.padre == 'nada':
        strctl = IncludeModeloFormularioDash(modelo,tabs,directorio,nombre,etapa,usuario)
        strt = strt.replace('@controles', tabs + "\t\t\t\t{% include 'core/includes/formulario_dash_" + modelo.nombre + ".html'%}")

    texto = []
    texto.append(strt)
    texto.append(strcss)

    return texto

def IncludeModeloFormulario(modelo, tabs,directorio,nombre,etapa,usuario):
    if modelo.controlesautomaticos:
        strctl = tabs + '\t\t\t\t\t\t\t{{form.as_p}}'
    else:
        strctl = ''
        numero = 1
        for propiedad in Propiedad.objects.filter(modelo=modelo): 
            if propiedad.noestaenformulario == False:
                if propiedad.etiqueta == '':
                    propiedad.etiqueta = propiedad.nombre
                    propiedad.save()
                if propiedad.etiquetaarriba:
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero) + '] -->' + '\n'
                    strctl += tabs + '\t\t<div class="row" >' + '\n'
                    strctl += tabs + '\t\t\t<div class="col font_label_' + modelo.nombre + '">' + propiedad.etiqueta + '</div>' + '\n'
                    strctl += tabs + '\t\t</div>' + '\n'
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+1) + '] -->' + '\n'
                    if propiedad.tipo == 'p': 
                        strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+2) + '] -->' + '\n'
                        strctl += tabs + '\t\t\t\t<div class="row">' + '\n'
                        strctl += tabs + '\t\t\t\t\t<div class="col">' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t{% if ' + modelo.nombre + '.' + propiedad.nombre + ' %}' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t\t<img src="{{' + modelo.nombre + '.' + propiedad.nombre + '.url}}" width="50px" height="50px" alt="">' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t{% endif %}' + '\n'
                        strctl += tabs + '\t\t\t\t\t</div>' + '\n'
                        strctl += tabs + '\t\t\t\t</div>' + '\n'
                        strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+3) + '] -->' + '\n'
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+4) + '] -->' + '\n'
                    strctl += tabs + '\t\t\t\t<div class="row mb-4 mt-1">' + '\n'
                    strctl += tabs + '\t\t\t\t\t<div class="col">' + '\n'
                    if not modelo.proyecto.conroles:
                        strctl += tabs + '\t\t\t\t\t\t{{form.' + propiedad.nombre + '}}' + '\n'
                    else:
                        strctl += tabs + '\t\t\t\t\t\t{% if puede_' + propiedad.nombre + ' and puede_ver_' + propiedad.nombre + ' %}' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t\t{{form.' + propiedad.nombre + '}}' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t{% elif not puede_' + propiedad.nombre + ' and puede_ver_' + propiedad.nombre + ' %}' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t\t{{' + modelo.nombre + "." + propiedad.nombre + '}}' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t{% endif %}' + '\n'
                    strctl += tabs + '\t\t\t\t\t</div>' + '\n'
                    strctl += tabs + '\t\t\t\t</div>' + '\n'
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+5) + '] -->' + '\n'
                else:
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+6) + '] -->' + '\n'
                    strctl += tabs + '\t\t\t\t<div class="row mt-2" >' + '\n'
                    strctl += tabs + '\t\t\t\t\t<div id="font_label_' + modelo.nombre + '"' + '  class="col-2 col-md-' + str(modelo.numerocolumnaslabels) + ' font-label-' + modelo.nombre + '">' + propiedad.etiqueta + '</div>' + '\n'
                    strctl += tabs + '\t\t\t\t\t<div class="col-10 col-md-' + str(modelo.numerocolumnascontroles) + '">' + '\n'
                    if not modelo.proyecto.conroles:
                        strctl += tabs + '\t\t\t\t\t\t{{form.' + propiedad.nombre + '}}' + '\n'
                    else:
                        strctl += tabs + '\t\t\t\t\t\t{% if puede_' + propiedad.nombre + ' and puede_ver_' + propiedad.nombre + ' %}' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t\t{{form.' + propiedad.nombre + '}}' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t{% elif not puede_' + propiedad.nombre + ' and puede_ver_' + propiedad.nombre + ' %}' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t\t{{' + modelo.nombre + "." + propiedad.nombre + '}}' + '\n'
                        strctl += tabs + '\t\t\t\t\t\t{% endif %}' + '\n'
                    strctl += tabs + '\t\t\t\t\t</div>' + '\n'
                    strctl += tabs + '\t\t\t\t</div>' + '\n'
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+7) + '] -->' + '\n'
            numero += 8
    EscribirArchivo(directorio + nombre + "/" + 'core/templates/core/includes/formulario_' + modelo.nombre + '.html',etapa,nombre,strctl,usuario,True)
    return strctl

def IncludeModeloFormularioDash(modelo, tabs,directorio,nombre,etapa,usuario):
    if modelo.controlesautomaticos:
        strctl = tabs + '\t\t\t\t\t\t\t<table>'
        strctl += tabs + '\t\t\t\t\t\t\t\t{{form.as_table}}'
        strctl += tabs + '\t\t\t\t\t\t\t</table>'
    else:
        strctl = ''
        numero = 1
        lista= []
        RecursivoPropiedadDash(modelo,lista,numero,tabs)
        # for propiedad in Propiedad.objects.filter(modelo=modelo): 
        #     if propiedad.dashboard:
        #         if propiedad.noestaenformulario == False:
        #             if propiedad.etiqueta == '':
        #                 propiedad.etiqueta = propiedad.nombre
        #                 propiedad.save()
        #             if propiedad.etiquetaarriba:
        #                 strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero) + '] -->' + '\n'
        #                 strctl += tabs + '\t\t<div class="row" >' + '\n'
        #                 strctl += tabs + '\t\t\t<div class="col font-label-' + modelo.nombre + '">' + propiedad.etiqueta + '</div>' + '\n'
        #                 strctl += tabs + '\t\t</div>' + '\n'
        #                 strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+1) + '] -->' + '\n'
        #                 strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+4) + '] -->' + '\n'
        #                 strctl += tabs + '\t\t\t\t<div class="row mb-4 mt-1">' + '\n'
        #                 strctl += tabs + '\t\t\t\t\t<div class="col">' + '\n'
        #                 strctl += tabs + '\t\t\t\t\t\t{{form.' + propiedad.nombre + '}}' + '\n'
        #                 strctl += tabs + '\t\t\t\t\t</div>' + '\n'
        #                 strctl += tabs + '\t\t\t\t</div>' + '\n'
        #                 strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+5) + '] -->' + '\n'
        #             else:
        #                 strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+6) + '] -->' + '\n'
        #                 strctl += tabs + '\t\t\t\t<div class="row mt-2" >' + '\n'
        #                 strctl += tabs + '\t\t\t\t\t<div id="font-label-' + modelo.nombre + '"' + '  class="col-2 col-md-' + str(modelo.numerocolumnaslabels) + ' font-label-' + modelo.nombre + '">' + propiedad.etiqueta + '</div>' + '\n'
        #                 strctl += tabs + '\t\t\t\t\t<div class="col-10 col-md-' + str(modelo.numerocolumnascontroles) + '">' + '\n'
        #                 strctl += tabs + '\t\t\t\t\t\t{{form.' + propiedad.nombre + '}}' + '\n'
        #                 strctl += tabs + '\t\t\t\t\t</div>' + '\n'
        #                 strctl += tabs + '\t\t\t\t</div>' + '\n'
        #                 strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+7) + '] -->' + '\n'
        #     numero += 8
        strctl = ''
        for tx in lista:
            strctl += tx

    EscribirArchivo(directorio + nombre + "/" + 'core/templates/core/includes/formulario_dash_' + modelo.nombre + '.html',etapa,nombre,strctl,usuario,True)
    return strctl

def RecursivoPropiedadDash(modelo,lista,numero,tabs):
    strctl = ''
    for propiedad in Propiedad.objects.filter(modelo=modelo): 
        if propiedad.dashboard:
            if propiedad.noestaenformulario == False:
                if propiedad.etiqueta == '':
                    propiedad.etiqueta = propiedad.nombre
                    propiedad.save()
                if propiedad.etiquetaarriba:
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero) + '] -->' + '\n'
                    strctl += tabs + '\t\t<div class="row" >' + '\n'
                    strctl += tabs + '\t\t\t<div class="col font-label-' + modelo.nombre + '">' + propiedad.etiqueta + '</div>' + '\n'
                    strctl += tabs + '\t\t</div>' + '\n'
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+1) + '] -->' + '\n'
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+4) + '] -->' + '\n'
                    strctl += tabs + '\t\t\t\t<div class="row mb-4 mt-1">' + '\n'
                    strctl += tabs + '\t\t\t\t\t<div class="col">' + '\n'
                    strctl += tabs + '\t\t\t\t\t\t{{form.' + propiedad.nombre + '}}' + '\n'
                    strctl += tabs + '\t\t\t\t\t</div>' + '\n'
                    strctl += tabs + '\t\t\t\t</div>' + '\n'
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+5) + '] -->' + '\n'
                else:
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+6) + '] -->' + '\n'
                    strctl += tabs + '\t\t\t\t<div class="row mt-2" >' + '\n'
                    strctl += tabs + '\t\t\t\t\t<div id="font-label-' + modelo.nombre + '"' + '  class="col-2 col-md-' + str(modelo.numerocolumnaslabels) + ' font-label-' + modelo.nombre + '">' + propiedad.etiqueta + '</div>' + '\n'
                    strctl += tabs + '\t\t\t\t\t<div class="col-10 col-md-' + str(modelo.numerocolumnascontroles) + '">' + '\n'
                    strctl += tabs + '\t\t\t\t\t\t{{form.' + propiedad.nombre + '}}' + '\n'
                    strctl += tabs + '\t\t\t\t\t</div>' + '\n'
                    strctl += tabs + '\t\t\t\t</div>' + '\n'
                    strctl += '<!-- #@[p_modelo_controles_' + propiedad.nombre + '_' + str(numero+7) + '] -->' + '\n'
                numero+=8    
    lista.append(strctl)
    for mod in Modelo.objects.filter(padre=modelo.nombre,proyecto=modelo.proyecto):
        RecursivoPropiedadDash(mod,lista,numero,tabs)

def AplicacionReal(modelo,texto,proyecto):
    # Encuentra la aplicacion real
    msp = Modelo.objects.get(nombre=modelo.padre, proyecto=proyecto)
    while msp.padre != 'nada':
        msp = Modelo.objects.get(nombre=msp.padre,proyecto=proyecto)
    texto = texto.replace('@aplicacionreal', Aplicacion.objects.get(id=msp.aplicacion.id).nombre)
    return texto

def CrearEsquemaSeguridad(proyecto, aplicacion):
    # Crear en la base de datos la aplicacion seguridad
    try:

        if proyecto.conroles:
            try:
                modelo.objects.get(nombre='rol',aplicacion=aplicacion, proyecto=proyecto).delete()
            except:
                pass

            modelo = Modelo()
            modelo.nombre = 'rol'
            modelo.descripcion = "Roles para la seguridad"
            modelo.aplicacion = aplicacion
            modelo.proyecto = proyecto
            modelo.nombreself = 'self.nombre'
            modelo.nombreborrar = 'nombre'
            modelo.textolinknuevomodelo = 'Nuevo Rol'
            modelo.textoopcionmenu = 'Rol'
            modelo.listastaff = True
            modelo.save()

            # Propiedades del modelo

            propiedad = Propiedad()
            propiedad.nombre  = 'nombre'
            propiedad.descripcion = 'Nombre del Rol'
            propiedad.tipo = 's'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Rol'
            propiedad.numerocolumnas = 3
            propiedad.etiqueta = 'Nombre'
            propiedad.save()

            propiedad = Propiedad()
            propiedad.nombre  = 'descripcion'
            propiedad.descripcion = 'Descripcion del Rol'
            propiedad.tipo = 'x'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Descripcion'
            propiedad.numerocolumnas = 7
            propiedad.etiqueta = 'Descripcion'
            propiedad.save()

            modelo = Modelo()
            modelo.nombre = 'modelo_rol'
            modelo.descripcion = 'Modelos cuya funcion esta sujeta a roles'
            modelo.padre = 'rol'
            modelo.nombreself = 'self.nombre'
            modelo.nombreborrar = 'nombre'
            modelo.aplicacion = aplicacion
            modelo.proyecto = proyecto
            modelo.textolinknuevomodelo = 'Nuevo Modelo'
            modelo.listastaff = True
            modelo.save()

            propiedad = Propiedad()
            propiedad.nombre  = 'nombre'
            propiedad.descripcion = 'Nombre del Modelo'
            propiedad.tipo = 's'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Modelo'
            propiedad.numerocolumnas = 2
            propiedad.etiqueta = 'Nombre'
            propiedad.save()
            
            propiedad = Propiedad()
            propiedad.nombre  = 'puedelistar'
            propiedad.descripcion = 'Si el rol permite el listado de los registros del modelo'
            propiedad.tipo = 'b'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Lista'
            propiedad.numerocolumnas = 2
            propiedad.etiqueta = 'Puede listar'
            propiedad.valorinicial = 'True'
            propiedad.save()
            
            propiedad = Propiedad()
            propiedad.nombre  = 'puedeinsertar'
            propiedad.descripcion = 'Si el rol permite la insercion de registros del modelo'
            propiedad.tipo = 'b'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Inserta'
            propiedad.numerocolumnas = 2
            propiedad.etiqueta = 'Puede insertar'
            propiedad.valorinicial = 'True'
            propiedad.save()

            propiedad = Propiedad()
            propiedad.nombre  = 'puedeeditar'
            propiedad.descripcion = 'Si el role permite la edicion de registros del modelo'
            propiedad.tipo = 'b'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Edita'
            propiedad.numerocolumnas = 2
            propiedad.etiqueta = 'Puede editar'
            propiedad.valorinicial = 'True'
            propiedad.save()

            propiedad = Propiedad()
            propiedad.nombre  = 'puedeborrar'
            propiedad.descripcion = 'Si el role permite borrar los registros del modelo'
            propiedad.tipo = 'b'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Borra'
            propiedad.numerocolumnas = 2
            propiedad.etiqueta = 'Puede borrar'
            propiedad.valorinicial = 'True'
            propiedad.save()

            modelo = Modelo()
            modelo.nombre = 'propiedad_rol'
            modelo.descripcion = 'Propiedades de los Modelos cuya funcion esta sujeta a roles'
            modelo.padre = 'modelo_rol'
            modelo.nombreself = 'self.nombre'
            modelo.nombreborrar = 'nombre'
            modelo.aplicacion = aplicacion
            modelo.proyecto = proyecto
            modelo.textolinknuevomodelo = 'Nueva Propiedad'
            modelo.listastaff = True
            modelo.save()

            propiedad = Propiedad()
            propiedad.nombre  = 'nombre'
            propiedad.descripcion = 'Nombre de la Propiedad'
            propiedad.tipo = 's'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Propiedad'
            propiedad.numerocolumnas = 4
            propiedad.etiqueta = 'Nombre'
            propiedad.save()
            
            propiedad = Propiedad()
            propiedad.nombre  = 'puedever'
            propiedad.descripcion = 'Si el rol permite ver la propiedad'
            propiedad.tipo = 'b'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Ver'
            propiedad.numerocolumnas = 2
            propiedad.etiqueta = 'Puede ver'
            propiedad.valorinicial = 'True'
            propiedad.save()

            propiedad = Propiedad()
            propiedad.nombre  = 'puedeasignarvalor'
            propiedad.descripcion = 'Si el rol permite la asignacion de un valor a la propiedad'
            propiedad.tipo = 'b'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Asignar'
            propiedad.numerocolumnas = 2
            propiedad.etiqueta = 'Puede asignar valor'
            propiedad.valorinicial = 'True'
            propiedad.save()

            propiedad = Propiedad()
            propiedad.nombre  = 'puedeeditar'
            propiedad.descripcion = 'Si el rol permite el cambio de un valor a la propiedad'
            propiedad.tipo = 'b'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Editar'
            propiedad.numerocolumnas = 2
            propiedad.etiqueta = 'Puede editar'
            propiedad.valorinicial = 'True'
            propiedad.save()

            try:
                modelo.objects.get(nombre='usuariorol',aplicacion=aplicacion, proyecto=proyecto).delete()
            except:
                pass

            modelo = Modelo()
            modelo.nombre = 'usuariorol'
            modelo.descripcion = 'Asignacion de usuarios a roles'
            modelo.nombreself = 'self.usuario'
            modelo.nombreborrar = 'usuario'
            modelo.aplicacion = aplicacion
            modelo.proyecto = proyecto
            modelo.textolinknuevomodelo = 'Nuevo Usuario'
            modelo.textoopcionmenu = 'Asignacion'
            modelo.listastaff = True
            modelo.save()

            propiedad = Propiedad()
            propiedad.nombre  = 'usuario'
            propiedad.descripcion = 'Usuario al que se le asigna el Rol'
            propiedad.tipo = 's'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Usuario'
            propiedad.numerocolumnas = 9
            propiedad.etiqueta = 'Usuario'
            propiedad.save()

            modelo = Modelo()
            modelo.nombre = 'rolusuario'
            modelo.descripcion = 'Rol que se asigna al usuario'
            modelo.nombreself = 'self.rol.nombre'
            modelo.nombreborrar = 'rol.nombre'
            modelo.padre = 'usuariorol'
            modelo.aplicacion = aplicacion
            modelo.proyecto = proyecto
            modelo.textolinknuevomodelo = 'Nuevo Rol'
            modelo.listastaff = True
            modelo.save()

            propiedad = Propiedad()
            propiedad.nombre  = 'rol'
            propiedad.foranea = 'rol'
            propiedad.descripcion = 'Rol que se asigna'
            propiedad.tipo = 'f'
            propiedad.modelo = modelo
            propiedad.textocolumna = 'Rol'
            propiedad.numerocolumnas = 9
            propiedad.etiqueta = 'Nombre'
            propiedad.etiqueta = 'Rol'
            propiedad.save()

    except:
        pass

def LeerArchivo(archivo, etapa, nombreProyecto,usuario):
    contents = ''
    try:
        with open(archivo) as file_object:
            contents = file_object.read()
    except  Exception as e:
        errores = ErroresCreacion()
        errores.etapa = etapa
        errores.paso = "Leer el archivo: " + archivo
        errores.proyecto = nombreProyecto
        errores.usuario = usuario
        errores.descripcion = e
        errores.severo = True
        errores.save()
    return contents

def ConstruyeBaseHtmlGeneral(proyecto,directorio,nombre,dt,dc,stri,directoriogenesis,etapa,usuario):

    # LOGO
    strAvatar = ''
    # Copiar el logo del proyecto a la direccion core/img

    if proyecto.avatar:
        strAvatar = "<img alt=" + dc + dc + " src=" + dc + "{% static 'core/img/logo.png' %}" + dc + ">" + "\n"
        # Copiar el logo del Proyecto en el directorio core/img
        CopiaImagenes(directorio + nombre + "/core/static/core/img/logo.png", 'proyectos', proyecto.avatar.url,directoriogenesis + 'media/proyectos/',nombre,etapa,usuario,True )

    stri = stri.replace("@logo",strAvatar)

    # Justificacion del logo
    stri = AsignaJustificacion('h',proyecto.justificacionhorizontallogo,'@justificacionlogohorizontal',stri)
    stri = AsignaJustificacion('v',proyecto.justificacionverticallogo,'@justificacionlogovertical',stri)

    # TITULO
    strTitulo = ''
    
    if proyecto.imagentitulo:
        strTitulo = "<img alt=" + dc + dc + " src=" + dc + "{% static 'core/img/imagentitulo.png' %}" + dc + " width=" + dc + "@imagentitulowidthpx" + dc + " height=" + dc + "@imagentituloheightpx" + dc + " >"
        # Copiar el logo del titulo en el directorio core/img
        CopiaImagenes(directorio + nombre + "/core/static/core/img/imagentitulo.png", 'proyectos', proyecto.imagentitulo.url,directoriogenesis + 'media/proyectos/',nombre,etapa,usuario,True )
    else:
        if proyecto.titulo != '':
            strTitulo = proyecto.titulo
        else:
            strTitulo = proyecto.nombre

    stri = stri.replace("@titulo",strTitulo)

    if proyecto.imagentitulo:
        stri = stri.replace("@imagentitulowidth",str(proyecto.imagentitulowidth))
        stri = stri.replace("@imagentituloheight",str(proyecto.imagentituloheight))

    # Justificacion del titulo
    stri = AsignaJustificacion('h',proyecto.justificacionhorizontaltitulo,'@justificaciontitulohorizontal',stri)
    stri = AsignaJustificacion('v',proyecto.justificacionverticaltitulo,'@justificaciontitulovertical',stri)
    
    # Dimensiones del columnas

    if proyecto.numerocolumnaenizquierda > 0:
        stri = stri.replace("@12numerocolumnaenizquierda",str(12))
    if proyecto.numerocolumnaenderecha > 0:
        stri = stri.replace("@12numerocolumnaenderecha",str(12))
    if proyecto.numerocolumnamenu > 0:
        stri = stri.replace("@12numerocolumnamenu",str(12))
    if proyecto.numerocolumnalogo > 0:
        stri = stri.replace("@12numerocolumnalogo",str(12))
    if proyecto.numerocolumnatitulo > 0:
        stri = stri.replace("@12numerocolumnatitulo",str(12))
    if proyecto.numerocolumnalogin > 0:
        stri = stri.replace("@12numerocolumnalogin",str(12))
    if proyecto.numerocolumnamedioizquierda > 0:
        stri = stri.replace("@12numerocolumnamedioizquierda",str(12))
    if proyecto.numerocolumnamediocentro > 0:
        stri = stri.replace("@12numerocolumnamediocentro",str(12))
    if proyecto.numerocolumnamedioderecha > 0:
        stri = stri.replace("@12numerocolumnamedioderecha",str(12))
    if proyecto.numerocolumnabumederecha > 0:
        stri = stri.replace("@12numerocolumnabumederecha",str(12))
    if proyecto.numerocolumnabumeizquierda > 0:
        stri = stri.replace("@12numerocolumnabumeizquierda",str(12))

    stri = stri.replace("@12numerocolumnaenizquierda",str(0))
    stri = stri.replace("@12numerocolumnaenderecha",str(0))
    stri = stri.replace("@12numerocolumnamenu",str(0))
    stri = stri.replace("@12numerocolumnalogo",str(0))
    stri = stri.replace("@12numerocolumnatitulo",str(0))
    stri = stri.replace("@12numerocolumnalogin",str(0))
    stri = stri.replace("@12numerocolumnamedioizquierda",str(0))
    stri = stri.replace("@12numerocolumnamediocentro",str(0))
    stri = stri.replace("@12numerocolumnamedioderecha",str(0))
    stri = stri.replace("@12numerocolumnabumederecha",str(0))
    stri = stri.replace("@12numerocolumnabumeizquierda",str(0))

    stri = stri.replace("@numerocolumnaenizquierda",str(proyecto.numerocolumnaenizquierda))
    stri = stri.replace("@numerocolumnaenderecha",str(proyecto.numerocolumnaenderecha))
    # if proyecto.menuscontiguos:
    stri = stri.replace("@numerocolumnamenu",str(proyecto.numerocolumnamenu))
    # else:
    #     stri = stri.replace("@numerocolumnamenu",str(int(proyecto.numerocolumnamenu/2)))
    stri = stri.replace("@numerocolumnalogo",str(proyecto.numerocolumnalogo))
    stri = stri.replace("@numerocolumnatitulo",str(proyecto.numerocolumnatitulo))
    stri = stri.replace("@numerocolumnalogin",str(proyecto.numerocolumnalogin))
    stri = stri.replace("@numerocolumnamedioizquierda",str(proyecto.numerocolumnamedioizquierda))
    stri = stri.replace("@numerocolumnamediocentro",str(proyecto.numerocolumnamediocentro))
    stri = stri.replace("@numerocolumnamedioderecha",str(proyecto.numerocolumnamedioderecha))
    stri = stri.replace("@numerocolumnabumederecha",str(proyecto.numerocolumnabumederecha))
    stri = stri.replace("@numerocolumnabumeizquierda",str(proyecto.numerocolumnabumeizquierda))

# Crear la busqueda en base.html
    strseg = ''
    if proyecto.conbusqueda:
        # Leer el archivo seguridad.html de textfiles
        if proyecto.menuscontiguos:
            # strseg = TextFiles.objects.get(file = "conbusqueda_contiguo.html").texto
            strseg = LeerArchivoEnTexto(dt + "conbusqueda_contiguo.html",etapa,nombre,usuario)
        else:
            # strseg = TextFiles.objects.get(file = "conbusqueda.html").texto
            strseg = LeerArchivoEnTexto(dt + "conbusqueda.html",etapa,nombre,usuario)
    else:
        strseg = LeerArchivoEnTexto(dt + "sinbusqueda.html",etapa,nombre,usuario)

    stri = stri.replace('@busqueda',strseg)

    stri = stri.replace("@numerocolumnabusqueda",str(proyecto.numerocolumnabusqueda))

    if proyecto.numerocolumnabusqueda > 0:
        stri = stri.replace("@12numerocolumnabusqueda",str(12))

    stri = stri.replace("@12numerocolumnabusqueda",str(0))

    # separacion secciones
    stri = stri.replace("@separacion",str(proyecto.separacionsecciones))

    return stri

def CssBaseGeneral(proyecto,stri,directorio,nombre,directoriogenesis,etapa,usuario):
    stri = stri.replace("@colorpaginaprincipal",str(proyecto.colorpaginaprincipal))
    stri = stri.replace("@segundocolorpaginaprincipal",str(proyecto.segundocolorpaginaprincipal))
    stri = stri.replace("@colorfondomenu",str(proyecto.colorfondomenu))

    if proyecto.degradehaciaarriba:
        stri = stri.replace("@direccion_degrade",'top')
    else:
        stri = stri.replace("@direccion_degrade",'bottom')


    stri = stri.replace("@alto-logo",str(proyecto.avatarheight))
    stri = stri.replace("@ancho-logo",str(proyecto.avatarwidth))


    stri = AsignaFonts(proyecto.fontmenu,'menu',stri)
    stri = stri.replace('@coloropcionmenu',proyecto.colormenu)


    stri = AsignaFonts(proyecto.fonttitulo,'titulo',stri)
    stri = stri.replace('@colortitulo',proyecto.colortitulo)

    stri = NumeroPorcentaje('@alto-fila-enizcede',proyecto.altofilaenizcede,stri)
    stri = NumeroPorcentaje('@alto-columna-enizquierda',proyecto.altocolumnaenizquierda,stri)
    stri = NumeroPorcentaje('@alto-columna-logo',proyecto.altocolumnalogo,stri)
    stri = NumeroPorcentaje("@alto-columna-titulo", proyecto.altocolumnatitulo,stri)
    stri = NumeroPorcentaje("@alto-columna-login", proyecto.altocolumnalogin,stri)
    stri = NumeroPorcentaje("@alto-columna-enderecha", proyecto.altocolumnaenderecha,stri)
    stri = NumeroPorcentaje("@alto-fila-bume", proyecto.altofilabume,stri)
    stri = NumeroPorcentaje("@alto-columna-busqueda", proyecto.altocolumnabusqueda,stri)
    stri = NumeroPorcentaje("@alto-columna-menu", proyecto.altocolumnamenu,stri)
    stri = NumeroPorcentaje("@alto-fila-medio", proyecto.altofilamedio,stri)
    stri = NumeroPorcentaje("@alto-columna-medio-izquierda", proyecto.altocolumnamedioizquierda,stri)
    stri = NumeroPorcentaje("@alto-columna-medio-centro", proyecto.altocolumnamediocentro,stri)
    stri = NumeroPorcentaje("@alto-columna-medio-derecha", proyecto.altocolumnamedioderecha,stri)
    stri = NumeroPorcentaje("@alto-fila-pie", proyecto.altofilapie,stri)
    stri = NumeroPorcentaje("@alto-columna-pie", proyecto.altocolumnapie,stri)
    stri = NumeroPorcentaje("@alto-columna-bume-derecha",proyecto.altocolumnabumederecha,stri)
    stri = NumeroPorcentaje("@alto-columna-bume-izquierda", proyecto.altocolumnabumeizquierda,stri)


    stri = stri.replace("@color-fila-enizcede", proyecto.colorfilaenizcede)
    stri = stri.replace("@color-columna-enizquierda", proyecto.colorcolumnaenizquierda)
    stri = stri.replace("@color-columna-logo", proyecto.colorcolumnalogo)
    stri = stri.replace("@color-columna-titulo", proyecto.colorcolumnatitulo)
    stri = stri.replace("@color-columna-login", proyecto.colorcolumnalogin)
    stri = stri.replace("@color-columna-enderecha", proyecto.colorcolumnaenderecha)
    stri = stri.replace("@color-fila-bume", proyecto.colorfilabume)
    stri = stri.replace("@color-columna-busqueda", proyecto.colorcolumnabusqueda)
    stri = stri.replace("@color-columna-menu", proyecto.colorcolumnamenu)
    stri = stri.replace("@color-menu", proyecto.colormenu)
    stri = stri.replace("@color-fila-medio", proyecto.colorfilamedio)
    stri = stri.replace("@color-columna-medio-izquierda", proyecto.colorcolumnamedioizquierda)
    stri = stri.replace("@color-columna-medio-centro", proyecto.colorcolumnamediocentro)
    stri = stri.replace("@color-columna-medio-derecha", proyecto.colorcolumnamedioderecha)
    stri = stri.replace("@color-fila-pie", proyecto.colorfilapie)
    stri = stri.replace("@color-columna-pie", proyecto.colorcolumnapie)
    stri = stri.replace("@color-columna-bume-izquierda", proyecto.colorcolumnabumeizquierda)
    stri = stri.replace("@color-columna-bume-derecha", proyecto.colorcolumnabumederecha)


    strBorde = str(proyecto.enanchoborde) + 'pt solid ' + proyecto.encolorborde
    if (proyecto.enborde and proyecto.numerocolumnaenizquierda == 0) or not proyecto.enborde:
        stri = stri.replace("@enbordei", 'none')
    stri = stri.replace("@enbordei", strBorde)

    if (proyecto.enborde and proyecto.numerocolumnaenderecha == 0) or not proyecto.enborde:
        stri = stri.replace("@enborded", 'none')
    stri = stri.replace("@enborded", strBorde)

    if (proyecto.enborde and proyecto.numerocolumnalogo == 0) or not proyecto.enborde:
        stri = stri.replace("@enbordel", 'none')
    stri = stri.replace("@enbordel", strBorde)

    if (proyecto.enborde and proyecto.numerocolumnatitulo == 0) or not proyecto.enborde:
        stri = stri.replace("@enbordet", 'none')
    stri = stri.replace("@enbordet", strBorde)

    if (proyecto.enborde and proyecto.numerocolumnalogin == 0) or not proyecto.enborde:
        stri = stri.replace("@enbordea", 'none')
    stri = stri.replace("@enbordea", strBorde)

    strBorde = str(proyecto.bumeanchoborde) + 'pt solid ' + proyecto.bumecolorborde
    if (proyecto.bumeborde and proyecto.numerocolumnabumeizquierda == 0) or not proyecto.bumeborde:
        stri = stri.replace("@bumebordei", 'none')
    stri = stri.replace("@bumebordei", strBorde)

    if (proyecto.bumeborde and proyecto.numerocolumnabumederecha == 0) or not proyecto.bumeborde:
        stri = stri.replace("@bumeborded", 'none')
    stri = stri.replace("@bumeborded", strBorde)

    if (proyecto.bumeborde and proyecto.numerocolumnabusqueda == 0) or not proyecto.bumeborde:
        stri = stri.replace("@bumebordeb", 'none')
    stri = stri.replace("@bumebordeb", strBorde)

    if (proyecto.bumeborde and proyecto.numerocolumnamenu == 0) or not proyecto.bumeborde:
        stri = stri.replace("@bumebordem", 'none')
    stri = stri.replace("@bumebordem", strBorde)

    strBorde = str(proyecto.cenanchoborde) + 'pt solid ' + proyecto.cencolorborde
    if (proyecto.cenborde and proyecto.numerocolumnamedioizquierda == 0) or not proyecto.cenborde:
        stri = stri.replace("@cenbordei", 'none')
    stri = stri.replace("@cenbordei", strBorde)

    if (proyecto.cenborde and proyecto.numerocolumnamediocentro == 0) or not proyecto.cenborde:
        stri = stri.replace("@cenbordec", 'none')
    stri = stri.replace("@cenbordec", strBorde)

    if (proyecto.cenborde and proyecto.numerocolumnamedioderecha == 0) or not proyecto.cenborde:
        stri = stri.replace("@cenborded", 'none')
    stri = stri.replace("@cenborded", strBorde)

    stri = stri.replace("@avatarheight", str(proyecto.avatarwidth))
    stri = stri.replace("@imagentitulowidth", str(proyecto.imagentitulowidth))
    stri = stri.replace("@avatarheight", str(proyecto.avatarheight))
    stri = stri.replace("@imagentituloheight", str(proyecto.imagentituloheight))

    stri = stri.replace('@posYfila-bume', str(0))

    # Texto medio
    stri = AsignaFonts(proyecto.fonttextomedio,'textomedio',stri)
    stri = stri.replace("@color-texto-medio", str(proyecto.colortextomedio))


    stri = AsignaFonts(proyecto.fonttextovolver,'volver',stri)
    stri = stri.replace("@color-volver",proyecto.colortextovolver)

    strckeditor = ".django-ckeditor-widget, .cke_editor_id_@control {" + "\n"
    strckeditor += "width: 100% !important;" + "\n"
    strckeditor += "max-width: 821px !important;" "\n"
    strckeditor += "}" + "\n"
    strcss = ''
    for md in Modelo.objects.filter(proyecto=proyecto):
        for pr in Propiedad.objects.filter(modelo=md):
            if pr.tipo == 'h':
                strcss += strckeditor
                strcss = strcss.replace('@control', pr.nombre )
    stri = stri.replace('@ckeditor', strcss)

    # Ver si existe un fondo de la pagina principal
    strBody = ''
    if proyecto.imagenpaginaprincipal:
        strBody = "background: url({% static " + "'" + "core/img/imagen-fondo-pagina-principal.png" + "'" + " %}) no-repeat center center fixed;"
        strBody += "background-size: cover;"
        strBody += "-moz-background-size: cover;"
        strBody += "-webkit-background-size: cover;"
        strBody +="-o-background-size: cover;"
        strBody +="background-color: transparent;"    
    stri = stri.replace('@estilo',strBody)

    # Copiar fondo de la pagina principal a core/img
    if proyecto.imagenpaginaprincipal:
        CopiaImagenes(directorio + nombre + "/core/static/core/img/imagen-fondo-pagina-principal.png", 'proyectos', proyecto.imagenpaginaprincipal.url,directoriogenesis + 'media/proyectos/',nombre,etapa,usuario,True )

    # Copiar imagen primera pagina
    if proyecto.imagenmedio:
        CopiaImagenes(directorio + nombre + "/core/static/core/img/imagen-medio.png", 'proyectos', proyecto.imagenmedio.url,directoriogenesis + 'media/proyectos/',nombre,etapa,usuario,True )

    return stri
    # pass

def CrearMenus(proyecto, dt, etapa,nombre,usuario, directorio, directoriogenesis):
    # MENUS

    strTemp=''
    strMenu = LeerArchivoEnTexto(dt + 'menu_core_contiguo.html',etapa,nombre,usuario)

    # Procesar los css

    strMenuCss = '.navbar li a {' + '\n'
    strMenuCss += '\tline-height: 20px;' + '\n'
    strMenuCss += '\theight: 20px;' + '\n'
    strMenuCss += '\tpadding-top: 0;' + '\n'
    strMenuCss += '\tpadding-bottom: 0;' + '\n'
    strMenuCss += '}' + '\n'

    strMenuCss += '#opcionmenu{' + '\n'
    strMenuCss += '\tcolor:@coloropcionmenu;' + '\n'
    strMenuCss += '\tfont-family: @menufontfamily;' + '\n'
    strMenuCss += '\tfont-size: @menufontsizept;' + '\n'
    strMenuCss += '\tfont-weight:@menufontweight;' + '\n'
    strMenuCss += '\t/*#@[p_estilos_14]*/' + '\n'
    strMenuCss += '}' + '\n'

    strMenuCss = AsignaFonts(proyecto.fontmenu,'menu',strMenuCss)
    strMenuCss = strMenuCss.replace('@coloropcionmenu',proyecto.colormenu)

    strMenu = strMenu.replace('@css',strMenuCss)

    # Copiar las imagenes propuestas en opciones de seguridad
    CopiarArchivos(dt + "registration/loginSF.png", directorio + nombre + "/core/static/core/img/loginSF.png",etapa,nombre, usuario,True)
    CopiarArchivos(dt + "registration/logoutSF.png", directorio + nombre + "/core/static/core/img/logoutSF.png",etapa,nombre, usuario,True)
    CopiarArchivos(dt + "registration/registroSF.png", directorio + nombre + "/core/static/core/img/registroSF.png",etapa,nombre, usuario,True)
    CopiarArchivos(dt + "registration/perfilSF.png", directorio + nombre + "/core/static/core/img/perfilSF.png",etapa,nombre, usuario,True)
    CopiarArchivos(dt + "registration/homeSF.png", directorio + nombre + "/core/static/core/img/homeSF.png",etapa,nombre, usuario,True)
    CopiarArchivos(dt + "registration/rolesSF.png", directorio + nombre + "/core/static/core/img/rolesSF.png",etapa,nombre, usuario,True)
    CopiarArchivos(dt + "registration/asignacionesSF.png", directorio + nombre + "/core/static/core/img/asignacionesSF.png",etapa,nombre, usuario,True)

    strMenu = AsignaJustificacion('h',proyecto.justificacionmenu,'@justificacion',strMenu)

    # Lista de aplicaciones
    strMenuItem = ''
    contador = 1

    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
        if aplicacion.nombre != 'core' and aplicacion.nombre != 'registration' and aplicacion.nombre != 'seguridad':

            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador) + '] -->' + '\n'
            strMenuItem += '\t\t<li class="nav-item dropdown">' + '\n'
            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+1) + '] -->' + '\n'
            strMenuItem += '\t\t\t<a id="opcionmenu" class="nav-link dropdown-toggle opcionmenu" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" data-toggle="tooltip" title="@tooltip">' + '\n'
            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+2) + '] -->' + '\n'
            if aplicacion.imagenmenu:
                strMenuItem += '\t\t\t\t<img class="me-1" src="{% static "core/img/@aplicacion.png" %}"  width="20px" height="20px" alt="" data-toggle="tooltip" title="Ingreso a @opcionaplicacion">' + '\n'
                strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+3) + '] -->' + '\n'
                CopiaImagenes(directorio + nombre + "/core/static/core/img/" + aplicacion.nombre + '.png', 'proyectos', aplicacion.imagenmenu.url,directoriogenesis + 'media/proyectos/',nombre,etapa,usuario,True )
            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+4) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t@opcionaplicacion' + '\n'
            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+5) + '] -->' + '\n'
            strMenuItem += '\t\t\t</a>' + '\n'
            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+6) + '] -->' + '\n'
            strMenuItem += '\t\t\t<ul class="dropdown-menu">' + '\n'
            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+7) + '] -->' + '\n'
            strMenuItem += '@modelos'
            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+8) + '] -->' + '\n'
            strMenuItem += '\t\t\t</ul>' + '\n'
            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+9) + '] -->' + '\n'
            strMenuItem += '\t\t</li>' + '\n'
            strMenuItem += '<!-- #@[p_menu_aplicacion_' + str(contador+10) + '] -->' + '\n'

            contador += 10

            if aplicacion.textoenmenu == '':
                aplicacion.textoenmenu = aplicacion.nombre
                aplicacion.save()
            strMenuItem = strMenuItem.replace('@opcionaplicacion',aplicacion.textoenmenu)
            strMenuItem = strMenuItem.replace('@tooltip',aplicacion.tooltip)
            strMenuItem = strMenuItem.replace('@aplicacion',aplicacion.nombre)

            # Ver si la aplicacion tiene modelos que no son dependientes
            strMenuItemModelo = ''
            contadorModelo =1
            for msp in Modelo.objects.filter(aplicacion=aplicacion):
                if msp.padre == 'nada':
                    strMenuItemModelo += '<!-- #@[p_menu_modelo_' + str(contadorModelo) + '] -->' + '\n'
                    strMenuItemModelo += '\t\t\t\t<li>' + '\n'
                    strMenuItemModelo += '<!-- #@[p_menu_modelo_' + str(contadorModelo+1) + '] -->' + '\n'
                    strMenuItemModelo += '\t\t\t\t\t<a class="dropdown-item" href="{% url "@aplicacion:listar_@modelo" %}" data-toggle="tooltip" title="@tooltip">' + '\n'
                    strMenuItemModelo += '<!-- #@[p_menu_modelo_' + str(contadorModelo+2) + '] -->' + '\n'
                    if msp.imagenmenu:
                        strMenuItemModelo += '\t\t\t\t\t\t<img class="me-1" src="{% static "core/img/@modelo.png" %}"  width="20px" height="20px" alt="" data-toggle="tooltip" title="Ingreso a @opcionmodelo">' + '\n'
                        strMenuItemModelo += '<!-- #@[p_menu_modelo_' + str(contadorModelo+3) + '] -->' + '\n'
                        CopiaImagenes(directorio + nombre + "/core/static/core/img/" + msp.nombre + '.png', 'proyectos', msp.imagenmenu.url,directoriogenesis + 'media/proyectos/',nombre,etapa,usuario,True )
                    strMenuItemModelo += '<!-- #@[p_menu_modelo_' + str(contadorModelo+4) + '] -->' + '\n'
                    strMenuItemModelo += '\t\t\t\t\t\t@opcionmodelo</a>' + '\n'
                    strMenuItemModelo += '\t\t\t\t\t</a>' + '\n'
                    strMenuItemModelo += '<!-- #@[p_menu_modelo_' + str(contadorModelo+5) + '] -->' + '\n'
                    strMenuItemModelo += '\t\t\t\t</li>' + '\n'
                    strMenuItemModelo += '<!-- #@[p_menu_modelo_' + str(contadorModelo+6) + '] -->' + '\n'

                    contadorModelo += 6

                    if msp.textoopcionmenu == '':
                        msp.textoopcionmenu = msp.nombre
                        msp.save()

                    strMenuItemModelo = strMenuItemModelo.replace('@opcionmodelo',msp.textoopcionmenu)
                    strMenuItemModelo = strMenuItemModelo.replace('@modelo',msp.nombre)
                    strMenuItemModelo = strMenuItemModelo.replace("@tooltip",msp.tooltip)
                    strMenuItemModelo = strMenuItemModelo.replace("@aplicacion",aplicacion.nombre)

            strMenuItem = strMenuItem.replace('@modelos', strMenuItemModelo)

    contador = 1
    if proyecto.conseguridad == True:
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador) + '] -->' + '\n'
        strMenuItem += '\t\t<li class="nav-item dropdown">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+1) + '] -->' + '\n'
        strMenuItem += '\t\t\t<a id="opcionmenu" class="nav-link dropdown-toggle opcionmenu" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+2) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t<img class="me-1" src="{% static "core/img/seguridadSF.png" %}"  style="max-width: 15%;max-height: 60%;width: 15%; height: 50%;" alt="" data-toggle="tooltip" title="Ingreso a generales">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+3) + '] -->' + '\n'
        strMenuItem += '\t\t\t\tSeguridad' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+4) + '] -->' + '\n'
        strMenuItem += '\t\t\t</a>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+5) + '] -->' + '\n'
        strMenuItem += '\t\t\t<ul class="dropdown-menu">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+6) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t{% if not request.user.is_authenticated %}' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+7) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t<li>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+8) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t<a class="dropdown-item" href="{% url "registration:registro" %}">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+9) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t\t<img class="me-1" src="{% static "core/img/registroSF.png" %}"  style="max-width: 15%;max-height: 60%;width: 15%; height: 50%;" alt="" data-toggle="tooltip" title="Ingreso a generales">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+10) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t\tRegistro' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+11) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t</a>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+12) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t</li>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+13) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t<li>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+14) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t<a class="dropdown-item" href="{% url "login" %}">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+15) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t\t<img class="me-1" src="{% static "core/img/loginSF.png" %}"  style="max-width: 15%;max-height: 60%;width: 15%; height: 50%;" alt="" data-toggle="tooltip" title="Ingreso a generales">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+16) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t\tLogin' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+17) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t</a>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+18) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t</li>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+19) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t{% else %}' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+20) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t<li>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+21) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t<a class="dropdown-item" href="{% url "registration:profile" %}">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+22) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t\t<img class="me-1" src="{% static "core/img/registroSF.png" %}"  style="max-width: 15%;max-height: 60%;width: 15%; height: 50%;" alt="" data-toggle="tooltip" title="Ingreso a generales">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+23) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t\tPerfil' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+24) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t</a>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+25) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t</li>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+26) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t<li>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+27) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t<a class="dropdown-item" href="{% url "logout" %}">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+28) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t\t<img class="me-1" src="{% static "core/img/loginSF.png" %}"  style="max-width: 15%;max-height: 60%;width: 15%; height: 50%;" alt="" data-toggle="tooltip" title="Ingreso a generales">' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+29) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t\tLogout' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+30) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t\t</a>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+31) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t\t</li>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+32) + '] -->' + '\n'
        strMenuItem += '\t\t\t\t{% endif %}' + '\n'

        if proyecto.conroles:
            strMenuItem += '\t\t\t\t<li>' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+8) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t\t<a class="dropdown-item" href="{% url "seguridad:listar_rol" %}">' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+9) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t\t\t<img class="me-1" src="{% static "core/img/rolesSF.png" %}"  style="max-width: 15%;max-height: 60%;width: 15%; height: 50%;" alt="" data-toggle="tooltip" title="Ingreso a generales">' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+10) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t\t\tRoles' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+11) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t\t</a>' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+12) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t</li>' + '\n'

            strMenuItem += '\t\t\t\t<li>' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+8) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t\t<a class="dropdown-item" href="{% url "seguridad:listar_usuariorol" %}">' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+9) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t\t\t<img class="me-1" src="{% static "core/img/asignacionesSF.png" %}"  style="max-width: 15%;max-height: 60%;width: 15%; height: 50%;" alt="" data-toggle="tooltip" title="Ingreso a generales">' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+10) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t\t\tAsignacion' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+11) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t\t</a>' + '\n'
            strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+12) + '] -->' + '\n'
            strMenuItem += '\t\t\t\t</li>' + '\n'


        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+33) + '] -->' + '\n'
        strMenuItem += '\t\t\t</ul>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+34) + '] -->' + '\n'
        strMenuItem += '\t\t</li>' + '\n'
        strMenuItem += '<!-- #@[p_menu_seguridad_' + str(contador+35) + '] -->' + '\n'

    strMenu = strMenu.replace('@opciones',strMenuItem)
    return strMenu

def CrearHome(proyecto,dt,etapa,nombre,usuario):
    # Copiar el archivo home.html
    # stri = TextFiles.objects.get(file = "home.html").texto
    stri = LeerArchivoEnTexto(dt + "home.html",etapa,nombre,usuario)
    stra= ''
    if proyecto.imagenmedio:
        stra = "<img src=" + '"' + "{% static 'core/img/imagen-medio.png' %}" + '"' + " alt=" + '"' + '"' + " style=" + '"' + "width: 100%;height: 100%;" + '"' + ">" + "\n"
        stri = stri.replace("@imagenmedio",stra)
    else:
        stra = "<span class=" + '"' + "textomedio" + '"' + ">@textomedio</span>" + "\n"
        stra=stra.replace("@textomedio",proyecto.textomedio)
        stri = stri.replace("@imagenmedio",stra)

    # Ver si utiliza su base.html particular
    stri = stri.replace('@base', 'base'+ proyecto.nombre)

    return stri

def CrearEstilosCss(proyecto, directorio, nombre,etapa,usuario, dt):
    # Leer el archivo estilos.css
    # stri = TextFiles.objects.get(file = "estilos.css").texto
    stri = LeerArchivoEnTexto(dt + "estilos.css",etapa,nombre,usuario)
    # Color de la pagina principal
    stri = stri.replace("@colorpaginaprincipal",str(proyecto.colorpaginaprincipal))
    stri = stri.replace("@segundocolorpaginaprincipal",str(proyecto.segundocolorpaginaprincipal))
    stri = stri.replace("@colorfondomenu",str(proyecto.colorfondomenu))
    if proyecto.degradehaciaarriba:
        stri = stri.replace("@direccion_degrade",'top')
    else:
        stri = stri.replace("@direccion_degrade",'bottom')

    # Tamanio del logo del proyecto
    stri = stri.replace("@alto-logo",str(proyecto.avatarheight))
    stri = stri.replace("@ancho-logo",str(proyecto.avatarwidth))

    # font del menu
    stri = AsignaFonts(proyecto.fontmenu,'menu',stri)
    stri = stri.replace('@coloropcionmenu',proyecto.colormenu)

    # Font del titulo
    stri = AsignaFonts(proyecto.fonttitulo,'titulo',stri)
    stri = stri.replace('@colortitulo',proyecto.colortitulo)

    # Alto de filas y columnas
    stri = NumeroPorcentaje('@alto-fila-enizcede',proyecto.altofilaenizcede,stri)
    stri = NumeroPorcentaje('@alto-columna-enizquierda',proyecto.altocolumnaenizquierda,stri)
    stri = NumeroPorcentaje('@alto-columna-logo',proyecto.altocolumnalogo,stri)
    stri = NumeroPorcentaje("@alto-columna-titulo", proyecto.altocolumnatitulo,stri)
    stri = NumeroPorcentaje("@alto-columna-login", proyecto.altocolumnalogin,stri)
    stri = NumeroPorcentaje("@alto-columna-enderecha", proyecto.altocolumnaenderecha,stri)
    stri = NumeroPorcentaje("@alto-fila-bume", proyecto.altofilabume,stri)
    stri = NumeroPorcentaje("@alto-columna-busqueda", proyecto.altocolumnabusqueda,stri)
    stri = NumeroPorcentaje("@alto-columna-menu", proyecto.altocolumnamenu,stri)
    stri = NumeroPorcentaje("@alto-fila-medio", proyecto.altofilamedio,stri)
    stri = NumeroPorcentaje("@alto-columna-medio-izquierda", proyecto.altocolumnamedioizquierda,stri)
    stri = NumeroPorcentaje("@alto-columna-medio-centro", proyecto.altocolumnamediocentro,stri)
    stri = NumeroPorcentaje("@alto-columna-medio-derecha", proyecto.altocolumnamedioderecha,stri)
    stri = NumeroPorcentaje("@alto-fila-pie", proyecto.altofilapie,stri)
    stri = NumeroPorcentaje("@alto-columna-pie", proyecto.altocolumnapie,stri)
    stri = NumeroPorcentaje("@alto-columna-bume-derecha",proyecto.altocolumnabumederecha,stri)
    stri = NumeroPorcentaje("@alto-columna-bume-izquierda", proyecto.altocolumnabumeizquierda,stri)


    # Color de fondo de la columna principal del encabezado
    stri = stri.replace("@color-fila-enizcede", proyecto.colorfilaenizcede)
    stri = stri.replace("@color-columna-enizquierda", proyecto.colorcolumnaenizquierda)
    stri = stri.replace("@color-columna-logo", proyecto.colorcolumnalogo)
    stri = stri.replace("@color-columna-titulo", proyecto.colorcolumnatitulo)
    stri = stri.replace("@color-columna-login", proyecto.colorcolumnalogin)
    stri = stri.replace("@color-columna-enderecha", proyecto.colorcolumnaenderecha)
    stri = stri.replace("@color-fila-bume", proyecto.colorfilabume)
    stri = stri.replace("@color-columna-busqueda", proyecto.colorcolumnabusqueda)
    stri = stri.replace("@color-columna-menu", proyecto.colorcolumnamenu)
    stri = stri.replace("@color-menu", proyecto.colormenu)
    stri = stri.replace("@color-fila-medio", proyecto.colorfilamedio)
    stri = stri.replace("@color-columna-medio-izquierda", proyecto.colorcolumnamedioizquierda)
    stri = stri.replace("@color-columna-medio-centro", proyecto.colorcolumnamediocentro)
    stri = stri.replace("@color-columna-medio-derecha", proyecto.colorcolumnamedioderecha)
    stri = stri.replace("@color-fila-pie", proyecto.colorfilapie)
    stri = stri.replace("@color-columna-pie", proyecto.colorcolumnapie)
    stri = stri.replace("@color-columna-bume-izquierda", proyecto.colorcolumnabumeizquierda)
    stri = stri.replace("@color-columna-bume-derecha", proyecto.colorcolumnabumederecha)

    # Bordes
    strBorde = str(proyecto.enanchoborde) + 'pt solid ' + proyecto.encolorborde
    if (proyecto.enborde and proyecto.numerocolumnaenizquierda == 0) or not proyecto.enborde:
        stri = stri.replace("@enbordei", 'none')
    stri = stri.replace("@enbordei", strBorde)

    if (proyecto.enborde and proyecto.numerocolumnaenderecha == 0) or not proyecto.enborde:
        stri = stri.replace("@enborded", 'none')
    stri = stri.replace("@enborded", strBorde)

    if (proyecto.enborde and proyecto.numerocolumnalogo == 0) or not proyecto.enborde:
        stri = stri.replace("@enbordel", 'none')
    stri = stri.replace("@enbordel", strBorde)

    if (proyecto.enborde and proyecto.numerocolumnatitulo == 0) or not proyecto.enborde:
        stri = stri.replace("@enbordet", 'none')
    stri = stri.replace("@enbordet", strBorde)

    if (proyecto.enborde and proyecto.numerocolumnalogin == 0) or not proyecto.enborde:
        stri = stri.replace("@enbordea", 'none')
    stri = stri.replace("@enbordea", strBorde)

    strBorde = str(proyecto.bumeanchoborde) + 'pt solid ' + proyecto.bumecolorborde
    if (proyecto.bumeborde and proyecto.numerocolumnabumeizquierda == 0) or not proyecto.bumeborde:
        stri = stri.replace("@bumebordei", 'none')
    stri = stri.replace("@bumebordei", strBorde)

    if (proyecto.bumeborde and proyecto.numerocolumnabumederecha == 0) or not proyecto.bumeborde:
        stri = stri.replace("@bumeborded", 'none')
    stri = stri.replace("@bumeborded", strBorde)

    if (proyecto.bumeborde and proyecto.numerocolumnabusqueda == 0) or not proyecto.bumeborde:
        stri = stri.replace("@bumebordeb", 'none')
    stri = stri.replace("@bumebordeb", strBorde)

    if (proyecto.bumeborde and proyecto.numerocolumnamenu == 0) or not proyecto.bumeborde:
        stri = stri.replace("@bumebordem", 'none')
    stri = stri.replace("@bumebordem", strBorde)

    strBorde = str(proyecto.cenanchoborde) + 'pt solid ' + proyecto.cencolorborde
    if (proyecto.cenborde and proyecto.numerocolumnamedioizquierda == 0) or not proyecto.cenborde:
        stri = stri.replace("@cenbordei", 'none')
    stri = stri.replace("@cenbordei", strBorde)

    if (proyecto.cenborde and proyecto.numerocolumnamediocentro == 0) or not proyecto.cenborde:
        stri = stri.replace("@cenbordec", 'none')
    stri = stri.replace("@cenbordec", strBorde)

    if (proyecto.cenborde and proyecto.numerocolumnamedioderecha == 0) or not proyecto.cenborde:
        stri = stri.replace("@cenborded", 'none')
    stri = stri.replace("@cenborded", strBorde)

    
    # Dimensiones img logo y titulo
    stri = stri.replace("@avatarheight", str(proyecto.avatarwidth))
    stri = stri.replace("@imagentitulowidth", str(proyecto.imagentitulowidth))
    stri = stri.replace("@avatarheight", str(proyecto.avatarheight))
    stri = stri.replace("@imagentituloheight", str(proyecto.imagentituloheight))

    # Opcion de Busqueda
    # Copiar el archivo lupa.png
    CopiarArchivos(dt + "lupa.png",directorio + nombre + "/core/static/core/img/lupa.png",etapa,nombre,usuario,True)

    # Regularizar la posicion del texto de busqueda y del menu
    stri = stri.replace('@posYfila-bume', str(0))

    # Texto medio
    stri = AsignaFonts(proyecto.fonttextomedio,'textomedio',stri)
    stri = stri.replace("@color-texto-medio", str(proyecto.colortextomedio))
    
    stri = AsignaFonts(proyecto.fonttextovolver,'volver',stri)
    stri = stri.replace("@color-volver",proyecto.colortextovolver)

    # css para ckeditor de todas las propiedades RichTextBox
    strckeditor = ".django-ckeditor-widget, .cke_editor_id_@control {" + "\n"
    strckeditor += "width: 100% !important;" + "\n"
    strckeditor += "max-width: 821px !important;" "\n"
    strckeditor += "}" + "\n"
    strcss = ''

    for md in Modelo.objects.filter(proyecto=proyecto):
        for pr in Propiedad.objects.filter(modelo=md):
            if pr.tipo == 'h':
                strcss += strckeditor
                strcss = strcss.replace('@control', pr.nombre )

    stri = stri.replace('@ckeditor', strcss)

    return stri

def CrearModelosSinBase(proyecto,etapa,nombre,usuario,directorio,dt):
    strSinBasecss = ''
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
        if aplicacion.nombre != 'core' and aplicacion.nombre != 'registration':
            for modelo in Modelo.objects.filter(aplicacion=aplicacion):
                if modelo.sinbasedatos != False:
                    # strSinBase = TextFiles.objects.get(file = "modelo_sinbase.html").texto
                    strSinBase = LeerArchivoEnTexto(dt + 'modelo_sinbase.html',etapa,nombre,usuario)
                    # strcss = TextFiles.objects.get(file = "modelo_sinbase.css").texto
                    strcss = LeerArchivoEnTexto(dt + 'modelo_sinbase.css',etapa,nombre,usuario)
                    strSinBase = strSinBase.replace('@aplicacion',aplicacion.nombre)
                    strcss = strcss.replace('@modelo',modelo.nombre)
                    strSinBasecss += strcss
                    strcss = ''
                    ProcesoPersonalizacion(proyecto,aplicacion.nombre,modelo.nombre + "_sinbase.html",directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/",strSinBase,nombre,etapa,usuario)
    return strSinBasecss

def CrearModelosList(proyecto,etapa,nombre,usuario, directorio, dt):
    strcssTotal = ''
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
        # Grabar el modelo si su aplicacion tiene modelos con propiedades
        if AplicacionTienePropiedades(aplicacion):                
            if aplicacion.nombre != 'core' and aplicacion.nombre != 'registration':
                for modelo in Modelo.objects.filter(aplicacion=aplicacion):
                    if modelo.sinbasedatos == False:
                        strlr = ''
                        strlt = ''
                        columnashijos = 0
                        if modelo.padre == 'nada':
                            # Leer el archivo modelo_lista.html de tet files
                            # strModeloList = TextFiles.objects.get(file = "modelo_list.html").texto
                            strModeloList = LeerArchivoEnTexto(dt + 'modelo_list.html',etapa,nombre,usuario)

                            # cambiar los css de este archivo

                            try:
                                strModeloList = AsignaFonts(modelo.fonttitulolista,'titulolista',strModeloList)
                            except:
                                strModeloList = AsignaFonts('Arial,10,normal','titulolista',strModeloList)


                            strModeloList = strModeloList.replace('@colortitulolista', modelo.colortitulolista)
                            strModeloList = strModeloList.replace('@colorfondotitulolista', modelo.colorfondotitulolista)
                            strModeloList = NumeroPorcentaje('@altotitulolista', modelo.altotitulolista,strModeloList)

                            strModeloList = strModeloList.replace('@colorfondocomentariolista', modelo.colorfondocomentariolista)
                            strModeloList = strModeloList.replace('@colorcomentariolista', modelo.colorcomentariolista)


                            try:
                                strModeloList = AsignaFonts(modelo.fontcomentariolista,'comentariolista',strModeloList)
                            except:
                                strModeloList = AsignaFonts('Arial,10,normal','comentariolista',strModeloList)

                            strModeloList = strModeloList.replace('@colorfondocolumnaslista', modelo.colorfondocolumnaslista)
                            strModeloList = strModeloList.replace('@colorcolumnaslista', modelo.colorcolumnaslista)
                            strModeloList = strModeloList.replace('@altocolumnaslista', str(modelo.altocolumnas))

                            try:
                                strModeloList = AsignaFonts(modelo.fontcolumnaslista,'columnaslista',strModeloList)
                            except:
                                strModeloList = AsignaFonts('Arial,10,normal','columnaslista',strModeloList)

                            # DATOS LISTA
                            try:
                                strModeloList = AsignaFonts(modelo.fonttextolista,'textolista',strModeloList)
                            except:
                                strModeloList = AsignaFonts('Arial,10,normal','textolista',strModeloList)

                            strModeloList = strModeloList.replace('@colortextolista', modelo.colortextolista)
                            strModeloList = strModeloList.replace('@colorfondotextolista', modelo.colorfondotextolista)
                            try:
                                strModeloList = AsignaFonts(modelo.fonteditarborrar,'editarborrar',strModeloList)
                            except:
                                strModeloList = AsignaFonts('Arial,10,normal','editarborrar',strModeloList)

                            strModeloList = strModeloList.replace('@coloreditarborrar', modelo.coloreditarborrar)


                            try:
                                strModeloList = AsignaFonts(modelo.fontlinknuevomodelo,'nuevomodelo',strModeloList)
                            except:
                                strModeloList = AsignaFonts('Arial,10,normal','nuevomodelo',strModeloList)


                            strModeloList = strModeloList.replace('@colorlinknuevomodelo', modelo.colorlinknuevomodelo)

                            strModeloList = strModeloList.replace('@modelo',modelo.nombre)




                            # strModeloListBusqueda = TextFiles.objects.get(file = "modelo_list_busqueda.html").texto
                            strModeloListBusqueda=LeerArchivoEnTexto(dt + 'modelo_list_busqueda.html',etapa,nombre,usuario)
                            if modelo.buscadorlista:
                                strModeloList=strModeloList.replace('@busqueda',strModeloListBusqueda)
                            else:
                                strModeloList=strModeloList.replace('@busqueda','')

                            # Lee el archivo css para cada modelo
                            # strcss = TextFiles.objects.get(file = "modelo_list.css").texto
                            strcss = LeerArchivoEnTexto(dt + 'modelo_list.css',etapa,nombre,usuario)
                            # Define el margin top del modelo_list

                            lista = PropiedadesEnLista(modelo,Propiedad,'')
                            strlt = lista[0]
                            strlr = lista[1]
                            columnashijos = lista[2]
                            strtt = lista[3]

                            strModeloList = strModeloList.replace('@listatitulos', strlt)
                            strModeloList = strModeloList.replace('@listaregistros', strlr)

                            # resto de columnas
                            # strModeloList = strModeloList.replace('@restocolumnas', str(10-columnashijos))

                            # TITULO DE LA LISTA
                            try:
                                strcss = AsignaFonts(modelo.fonttitulolista,'titulolista',strcss)
                            except:
                                strcss = AsignaFonts('Arial,10,normal','titulolista',strcss)

                            strcss = strcss.replace('@colortitulolista', modelo.colortitulolista)
                            strcss = strcss.replace('@colorfondotitulolista', modelo.colorfondotitulolista)
                            strcss = NumeroPorcentaje('@altotitulolista', modelo.altotitulolista,strcss)

                            strModeloList = strModeloList.replace('@titulolista', '\t\t\t\t\t\t\t\t\t' + modelo.titulolista)
                            strModeloList = UpperLower(modelo.mayusculastitulolista,'@uppercasetitulo',strModeloList)

                            strModeloList = AsignaJustificacion('h', modelo.justificacionhorizontaltitulolista,'@justificacionhorizontaltitulolista',strModeloList)
                            strModeloList = AsignaJustificacion('v', modelo.justificacionverticaltitulolista,'@justificacionverticaltitulolista',strModeloList)

                            # COMENTARIO LISTA
                            strcss = strcss.replace('@colorfondocomentariolista', modelo.colorfondocomentariolista)
                            strcss = strcss.replace('@colorcomentariolista', modelo.colorcomentariolista)
                            strModeloList = strModeloList.replace('@comentariolista', '\t\t\t\t\t\t\t\t\t\t' + modelo.comentariolista)

                            try:
                                strcss = AsignaFonts(modelo.fontcomentariolista,'comentariolista',strcss)
                            except:
                                strcss = AsignaFonts('Arial,10,normal','comentariolista',strcss)

                            #COLUMNAS DE LA LISTA
                            strcss = strcss.replace('@colorfondocolumnaslista', modelo.colorfondocolumnaslista)
                            strcss = strcss.replace('@colorcolumnaslista', modelo.colorcolumnaslista)
                            strcss = strcss.replace('@altocolumnaslista', str(modelo.altocolumnas))

                            try:
                                strcss = AsignaFonts(modelo.fontcolumnaslista,'columnaslista',strcss)
                            except:
                                strcss = AsignaFonts('Arial,10,normal','columnaslista',strcss)

                            if modelo.columnaslistaconborde:
                                strModeloList = strModeloList.replace('@conborde', 'border ')
                            else:
                                strModeloList = strModeloList.replace('@conborde', '')

                            # DATOS LISTA
                            try:
                                strcss = AsignaFonts(modelo.fonttextolista,'textolista',strcss)
                            except:
                                strcss = AsignaFonts('Arial,10,normal','textolista',strcss)

                            strcss = strcss.replace('@colortextolista', modelo.colortextolista)
                            strcss = strcss.replace('@colorfondotextolista', modelo.colorfondotextolista)

                            # EDITAR BORRAR

                            # Ve si se utiliza la opcion editar en la lista
                            strEditar = ''
                            if modelo.editarenlista:  
                                if modelo.proyecto.conroles:
                                    strEditar += '\t\t\t\t\t\t{% if puede_editar %}\n'       
                                strEditar += '<!-- #@[p_modelo_editar_list_01] -->\n'
                                strEditar += '\t\t\t\t\t\t<div id="edita_@modelo" class="col-12 col-md-1 edita_@modelo">\n' 
                                strEditar += '<!-- #@[p_modelo_editar_list_02] -->\n'
                                strEditar += '\t\t\t\t\t\t\t<a href="{% url ' + "'" + '@aplicacion:editar_@modelo' + "'" + ' obj.id %}">@textoeditar</a>\n'
                                strEditar += '<!-- #@[p_modelo_editar_list_03] -->\n'
                                strEditar += '\t\t\t\t\t\t</div>\n'
                                strEditar += '<!-- #@[p_modelo_editar_list_04] -->\n'
                                if modelo.proyecto.conroles:
                                    strEditar += '\t\t\t\t\t\t{% endif %}\n'       
                                strModeloList = strModeloList.replace('@editarenlista',strEditar)
                            else:
                                strModeloList = strModeloList.replace('@editarenlista','')

                            if modelo.proyecto.conroles:
                                strModeloList = strModeloList.replace('@ifconroles','{% if puede_borrar %}')
                                strModeloList = strModeloList.replace('@endifconroles','{% endif %}')
                            else:
                                strModeloList = strModeloList.replace('@ifconroles','')
                                strModeloList = strModeloList.replace('@endifconroles','')

                            try:
                                strcss = AsignaFonts(modelo.fonteditarborrar,'editarborrar',strcss)
                            except:
                                strcss = AsignaFonts('Arial,10,normal','editarborrar',strcss)

                            strcss = strcss.replace('@coloreditarborrar', modelo.coloreditarborrar)
                            strModeloList = AsignaTexto(modelo.textoeditarborrar,"editar,borrar","@textoeditar,@textoborrar",strModeloList)

                            #link nuevo
                            try:
                                strcss = AsignaFonts(modelo.fontlinknuevomodelo,'nuevomodelo',strcss)
                            except:
                                strcss = AsignaFonts('Arial,10,normal','nuevomodelo',strcss)


                            strcss = strcss.replace('@colorlinknuevomodelo', modelo.colorlinknuevomodelo)

                            # NUEVO Y ROLES

                            if modelo.proyecto.conroles:
                                strModeloList = strModeloList.replace('@ifnuevoconroles','{% if puede_insertar %}')
                                strModeloList = strModeloList.replace('@endifnuevoconroles','{% endif %}')
                            else:
                                strModeloList = strModeloList.replace('@ifnuevoconroles','')
                                strModeloList = strModeloList.replace('@endifnuevoconroles','')

                            strModeloList = strModeloList.replace('@textolinknuevomodelo', modelo.textolinknuevomodelo)

                            #link boton
                            if modelo.linknuevomodelo:
                                strModeloList = strModeloList.replace('@linknuevomodelo', 'btn btn-block btn-' + modelo.colorbotonlinknuevomodelo)
                            else:
                                strModeloList = strModeloList.replace('@linknuevomodelo', '')

                            # Forma el css total del proyecto
                            strcss = strcss.replace('@modelo',modelo.nombre)
                            strcssTotal += strcss

                            strModeloList = strModeloList.replace('@listacolumnas', strlt)
                            strModeloList = strModeloList.replace('@listadatos', strlr)
                            strModeloList = strModeloList.replace('@totaliza', strtt)
                            strModeloList = strModeloList.replace('@modelo', modelo.nombre)
                            strModeloList = strModeloList.replace('@aplicacion', aplicacion.nombre)

                            # # Sin lineas de personalizacion
                            # if not proyecto.conetiquetaspersonalizacion:
                            #     strModeloList = rutinas.QuitaLineasPersonalizacion(strModeloList)                
                            # strModeloList = EscribePersonalizacion(proyecto,aplicacion,modelo.nombre + '_list.html',strModeloList)

                            # Ver si utiliza su base.html particular
                            if secm.objects.filter(modelo = modelo).count() > 0 and modelo.usabaseparticular:
                                strModeloList = strModeloList.replace('@base', 'base'+ modelo.nombre)
                            else:
                                strModeloList = strModeloList.replace('@base', 'base')

                            # tiene_dash = False
                            # for propiedad in Propiedad.objects.filter(modelo=modelo):
                            #     if propiedad.dashboard:
                            #         tiene_dash=True
                            #         break
                            if TieneDash(modelo):
                                str_dash = '<!-- #@[p_modelo_dash_list_01] -->' + '\n'
                                str_dash += '\t\t\t\t<a class="nuevo_@modelo" href="{% url ' + "'" + '@aplicacion:dash_@modelo' + "'" + '%}">Dash</a>' + '\n'
                                str_dash += '<!-- #@[p_modelo_dash_list_02] -->' + '\n'
                                strModeloList = strModeloList.replace('@dash', str_dash)
                                strModeloList = strModeloList.replace('@modelo', modelo.nombre)
                                strModeloList = strModeloList.replace('@aplicacion', aplicacion.nombre)
                            else:
                                strModeloList = strModeloList.replace('@dash', '')

                            str_fill = '<!-- #@[p_modelo_fill_list_01] -->' + '\n'
                            str_fill += '\t\t\t\t<a class="nuevo_@modelo" href="{% url ' + "'" + '@aplicacion:fill_@modelo' + "'" + '%}">Fill</a>' + '\n'
                            str_fill += '<!-- #@[p_modelo_fill_list_02] -->' + '\n'
                            str_fill = str_fill.replace('@modelo', modelo.nombre)
                            str_fill = str_fill.replace('@aplicacion', aplicacion.nombre)
                            strModeloList = strModeloList.replace('@fill', str_fill)
                            strModeloList = strModeloList.replace('@bordecomentario', 'border' if modelo.bordecomentariolista else '')
                            strModeloList = strModeloList.replace('@bordeexterior', 'border' if modelo.bordeexteriorlista else '')

                            ProcesoPersonalizacion(proyecto,aplicacion.nombre,modelo.nombre + "_list.html",directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/",strModeloList,nombre,etapa,usuario)
    return strcssTotal

def CrearModelosInsercion(proyecto, etapa,nombre,usuario,directorio, dt):
    strcssTotal = ''
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        # Grabar el modelo si su aplicacion tiene modelos con propiedades
        if AplicacionTienePropiedades(aplicacion) and aplicacion.nombre!= 'core' and aplicacion.nombre != 'registration':                
            for modelo in Modelo.objects.filter(aplicacion=aplicacion):
                if modelo.sinbasedatos == False:
                    # Leer el archivo modelo_lista.html de tet files
                    # strModeloInserta = TextFiles.objects.get(file = "modelo_inserta.html").texto
                    strModeloInserta = LeerArchivoEnTexto(dt + 'modelo_inserta.html',etapa,nombre,usuario)

                    # Procesa los css

                    strModeloInserta = strModeloInserta.replace('@modelo',modelo.nombre)

                    strModeloInserta = AsignaFonts(modelo.fonttituloinserta,'tituloinserta',strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colortituloinserta', modelo.colortituloinserta)
                    strModeloInserta = NumeroPorcentaje('@altofilatituloinserta', modelo.altofilatituloinserta,strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colorfondofilatituloinserta', modelo.colorfondofilatituloinserta)
                    strModeloInserta = strModeloInserta.replace('@colorfondotituloinserta', modelo.colorfondotituloinserta)

                    strModeloInserta = AsignaFonts(modelo.fontcomentarioinserta,'comentarioinserta',strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colorcomentarioinserta', modelo.colorcomentarioinserta)
                    strModeloInserta = strModeloInserta.replace('@colorfondocomentarioinserta', modelo.colorfondocomentarioinserta)
                    strModeloInserta = strModeloInserta.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)

                    strModeloInserta = AsignaFonts(modelo.fontlabelmodelo,'label'+modelo.nombre,strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)


                    # Lee el archivo css para cada modelo
                    # strcss = TextFiles.objects.get(file = "modelo_inserta.css").texto
                    strcss = LeerArchivoEnTexto(dt + 'modelo_inserta.css',etapa,nombre,usuario) 
                    strcss = strcss.replace('@modelo',modelo.nombre)
                    strModeloInserta = strModeloInserta.replace('@modelo', modelo.nombre)
                    strModeloInserta = strModeloInserta.replace('@aplicacion', aplicacion.nombre)
                    
                    # codigo para el Titulo del form
                    stra = ''
                    if modelo.padre == 'nada':
                        stra += modelo.tituloinserta + '\n'
                    else:    
                        modelo_padre = Modelo.objects.get(nombre=modelo.padre , proyecto=proyecto)
                        if modelo_padre.padre != 'nada': # el modelo es nieto
                            modelo_abuelo = Modelo.objects.get(nombre=modelo_padre.padre , proyecto=proyecto)
                            stra += '<div class="" style="float: left;">Nuevo modelo: &nbsp@modelo&nbsp&nbsp</div>' + '\n'
                            stra += '<div class=""><a href="{% url ' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ' @modelopadre_id %}?@modeloabuelo_id={{@modeloabuelo_id}}">(Volver)</a></div>' + '\n'
                            stra = stra.replace('@modeloabuelo', modelo_abuelo.nombre)        
                        else: # el modelo es hijo
                            stra += '<div class="" style="float: left">Nuevo modelo: &nbsp@modelo</div>' + '\n'
                            stra += '<div class="" >&nbsp&nbsp<a href="{% url ' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ' @modelopadre_id %}">(Volver)</a></div>' + '\n'
                        stra = stra.replace('@aplicacionpadre', Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre)        
                        stra = stra.replace('@modelopadre', modelo_padre.nombre)        
                    stra = stra.replace('@modelo', modelo.nombre)        
                    strModeloInserta = strModeloInserta.replace('@tituloinserta', '\t\t\t\t' + stra)
                    strModeloInserta = UpperLower(modelo.mayusculastituloinserta,'@uppercasetitulo',strModeloInserta)

                    #titulo pagina
                    strcss = AsignaFonts(modelo.fonttituloinserta,'tituloinserta',strcss)
                    strcss = strcss.replace('@colortituloinserta', modelo.colortituloinserta)
                    strcss = NumeroPorcentaje('@altofilatituloinserta', modelo.altofilatituloinserta,strcss)
                    # strcss = strcss.replace('@altofilatituloinserta', str(modelo.altofilatituloinserta))
                    strcss = strcss.replace('@colorfondofilatituloinserta', modelo.colorfondofilatituloinserta)
                    strcss = strcss.replace('@colorfondotituloinserta', modelo.colorfondotituloinserta)

                    # Justificacion titulo inserta
                    strModeloInserta = AsignaJustificacion('h', modelo.justificacionhorizontaltituloinserta,'@justificacionhorizontaltituloinserta',strModeloInserta)
                    strModeloInserta = AsignaJustificacion('v', modelo.justificacionverticaltituloinserta,'@justificacionverticaltituloinserta',strModeloInserta)

                    #comentario pagina
                    strcss = AsignaFonts(modelo.fontcomentarioinserta,'comentarioinserta',strcss)
                    strcss = strcss.replace('@colorcomentarioinserta', modelo.colorcomentarioinserta)
                    strcss = strcss.replace('@colorfondocomentarioinserta', modelo.colorfondocomentarioinserta)
                    strcss = strcss.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)
                    strModeloInserta = strModeloInserta.replace('@comentarioinserta', '\t\t\t\t\t' + modelo.comentarioinserta)

                    # columnas que organizan el cuerpo en insercion
                    strModeloInserta = strModeloInserta.replace('@numerocolumnasizquierdainserta', str(modelo.numerocolumnasizquierdainserta))
                    strModeloInserta = strModeloInserta.replace('@numerocolumnasmodeloinserta', str(modelo.numerocolumnasmodeloinserta))
                    strModeloInserta = strModeloInserta.replace('@numerocolumnasderechainserta', str(modelo.numerocolumnasderechainserta))

                    texto = Etiquetas(modelo,strModeloInserta,strcss,'\t\t\t',directorio,nombre,etapa,usuario)
                    strModeloInserta =  texto[0]
                    strcss = texto[1]

                    strcssTotal += strcss

                    # strModeloInserta = EscribePersonalizacion(proyecto,aplicacion,modelo.nombre + '_form.html',strModeloInserta)

                    #Sin lineas de personalizacion
                    if not proyecto.conetiquetaspersonalizacion:
                        strModeloInserta = QuitaLineasPersonalizacion(strModeloInserta)

                    # bordecomentario
                    strModeloInserta = strModeloInserta.replace('@bordecomentario', 'border' if modelo.bordecomentarioinserta else '')
                    strModeloInserta = strModeloInserta.replace('@bordeexterior', 'border' if modelo.bordeexteriorinserta else '')
                    strModeloInserta = strModeloInserta.replace('@bordeformulario', 'border' if modelo.bordeformularioinserta else '')

                    # Graba el archivo
                    ProcesoPersonalizacion(proyecto,aplicacion.nombre,modelo.nombre + "_form.html",directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/",strModeloInserta,nombre,etapa,usuario)
                    # rutinas.EscribirArchivo(directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/" + modelo.nombre + "_form.html" ,etapa,nombre, strModeloInserta,True)

    return strcssTotal

def CrearModelosUpdate(proyecto, etapa,nombre,usuario,directorio, appCore, dt, directoriogenesis,dc ):

    strcssTotal = ''
    strcsshijototal = ''

    # Imagen o texto de volver en pantallas de update
    strTextoVolver = proyecto.textovolver
    if proyecto.imagenvolver:
        strTextoVolver = "<img height=" + '"' + "25px" + '"' + " widht=" + '"' + "25px" + '"' + "alt=" + dc + dc + " src=" + dc + "{% static 'core/img/volver.png' %}" + dc + ">" + "\n"
        CopiaImagenes(directorio + nombre + "/core/static/core/img/volver.png", 'proyectos', proyecto.imagenvolver.url,directoriogenesis + 'media/proyectos/',nombre,etapa,usuario,True )
    else:
        strTextoVolver = "<span class=" + '"' + "volver" + '"' + ">" + proyecto.textovolver + "</span>"

    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        # Grabar el modelo si su aplicacion tiene modelos con propiedades
        if AplicacionTienePropiedades(aplicacion) and aplicacion.nombre!= 'core' and aplicacion.nombre != 'registration':                

            for modelo in Modelo.objects.filter(aplicacion=aplicacion):
                if modelo.sinbasedatos == False:
                    strModeloUpdate= ''
                    if modelo.hijoscontiguos:
                        # strModeloUpdate = TextFiles.objects.get(file = "modelo_update_contiguo.html").texto
                        strModeloUpdate = LeerArchivoEnTexto(dt + 'modelo_update_contiguo.html',etapa,nombre,usuario)
                        strhc = "@listahijos" + '\n'
                        strhc += "     </div>" + '\n'
                        strhc += "     <div class=" + '"' + "col-12 d-none col-md-@numerocolumnasderechaupdate" + '"' + "></div>" + '\n'
                        strhc += "   </div>" + '\n'
                        strhc += "   <div class=" + '"' + "row pie-lista" + '"' + "></div>" + '\n'
                        strhc += "  </div>" + '\n'
                        strModeloUpdate = strModeloUpdate.replace('@update', strhc)
                    else:
                        # strModeloUpdate = TextFiles.objects.get(file = "modelo_update_abajo.html").texto
                        strModeloUpdate = LeerArchivoEnTexto(dt + 'modelo_update_abajo.html',etapa,nombre,usuario)
                        strha  = "    </div>" + '\n'
                        strha += "    <div class=" + '"' + "row" + '"' + ">" + '\n'
                        strha += "       <div class=" + '"' + "col-12 rounded" + '"' + ">" + '\n'
                        strha += "@listahijos" + '\n'      
                        strha += "       </div>" + '\n'
                        strha += "     </div>" + '\n'
                        strha += "     <div class=" + '"' + "row pie-lista" + '"' + ">" + '\n'
                        strha += "     </div>" + '\n'
                        strha += "    </div>" + '\n'
                        strModeloUpdate = strModeloUpdate.replace('@update', strha)

                        strTv = ''
                        lista = []
                        strTx = ''
                        if modelo.treeview:
                            RecursivoUrl(modelo, '', '',lista, False)
                            for tx in lista:
                                strTx += tx + '\n'
                            # Despliega los registros treeview
                            strTv = "\t\t<div class='col-12 d-none d-md-block col-md-@columnastreeview mt-2 pt-3'  style='font-weight: @weightfont; font-name: @namefont; font-size: @sizefontpt; background-color: @colorfondotreeview; color:white;'>" + '\n'
                            strTv += "\t\t\t{% for obj in listar %}" + '\n'
                            strTv += "\t\t\t\t{% if obj.2 == '+' %}" + '\n'

                            strTv += "\t\t\t\t\t<div class='row' style='padding-left: {{obj.1}}px; '>" + '\n'
                            strTv += "\t\t\t\t\t\t<div class='col-1'>" + '\n'
                            strTv += "\t\t\t\t\t\t\t<a style='text-decoration: none; color:white;' href='{% url @com" + modelo.aplicacion.nombre + ":editar_" + modelo.nombre + "@com obj.5 %}?padre={{obj.0}},'>" + '\n'
                            strTv += "\t\t\t\t\t\t\t\t{{obj.2}}" + '\n'
                            strTv += "\t\t\t\t\t\t\t</a>" + '\n'
                            strTv += "\t\t\t\t\t\t</div>" + '\n'
                            strTv += "\t\t\t\t\t\t<div class='col-10'>" + '\n'
                            strTv += "\t\t\t\t\t\t\t{% if obj.3 == '" + modelo.nombre + "' %}" + '\n'
                            strTv += "\t\t\t\t\t\t\t\t<a style='text-decoration: none; color:white;' href='{% url @com@raiz_aplicacion:editar_@raiz_modelo@com obj.5 %}?padre={{obj.6}},&raiz={{obj.5}}'>{{obj.4}}</a>" + '\n'
                            strTv = strTv.replace('@raiz_aplicacion',modelo.aplicacion.nombre)
                            strTv = strTv.replace('@raiz_modelo',modelo.nombre)
                            strTv += "\t\t\t\t\t\t\t{% else %}" + '\n'
                            strTv += strTx
                            strTv += "\t\t\t\t\t\t\t{% endif %}" + '\n'
                            strTv += "\t\t\t\t\t\t</div>" + '\n'
                            strTv += "\t\t\t\t\t</div>" + '\n'

                            strTv += "\t\t\t\t{% else %}" + '\n'

                            strTv += "\t\t\t\t\t<div class='row' style='padding-left: {{obj.1}}px; '>" + '\n'
                            strTv += "\t\t\t\t\t\t<div class='col-1'>" + '\n'
                            strTv += "\t\t\t\t\t\t\t<a style='text-decoration: none; color:white;' href='{% url @com" + modelo.aplicacion.nombre + ":editar_" + modelo.nombre + "@com obj.5 %}?padre={{obj.6}},&raiz={{obj.5}}'>" + '\n'
                            strTv += "\t\t\t\t\t\t\t\t{{obj.2}}" + '\n'
                            strTv += "\t\t\t\t\t\t\t</a>" + '\n'
                            strTv += "\t\t\t\t\t\t</div>" + '\n'
                            strTv += "\t\t\t\t\t\t<div class='col-10'>" + '\n'
                            strTv += "\t\t\t\t\t\t\t{% if obj.3 == '" + modelo.nombre + "' %}" + '\n'
                            strTv += "\t\t\t\t\t\t\t\t<a style='text-decoration: none; color:white;' href='{% url @com@raiz_aplicacion:editar_@raiz_modelo@com obj.5 %}?padre={{obj.6}},&raiz={{obj.5}}'>{{obj.4}}</a>" + '\n'
                            strTv = strTv.replace('@raiz_aplicacion',modelo.aplicacion.nombre)
                            strTv = strTv.replace('@raiz_modelo',modelo.nombre)
                            strTv += "\t\t\t\t\t\t\t{% else %}" + '\n'
                            strTx = ''
                            lista = []
                            RecursivoUrl(modelo, '', '',lista, True)
                            for tx in lista:
                                strTx += tx + '\n'
                            strTv += strTx
                            strTv += "\t\t\t\t\t\t\t{% endif %}" + '\n'
                            strTv += "\t\t\t\t\t\t</div>" + '\n'
                            strTv += "\t\t\t\t\t</div>" + '\n'

                            strTv += "\t\t\t\t{% endif %}" + '\n'
                            strTv += "\t\t\t{% endfor %}" + '\n'
                            strTv += "\t\t</div>" + '\n'
                            strTv = strTv.replace('@com','"')
                            fonttreeview = modelo.fonttreeview.split(',')
                            strTv = strTv.replace('@weightfont',fonttreeview[2])
                            strTv = strTv.replace('@sizefont',fonttreeview[1])
                            strTv = strTv.replace('@namefont','"' + fonttreeview[0] + '"')
                            strTv = strTv.replace('@columnastreeview',str(modelo.columnastreeview))
                            strTv = strTv.replace('@colorfondotreeview',str(modelo.colorfondotreeview))
                            strModeloUpdate = strModeloUpdate.replace('@datossintreeview',str(12 - modelo.columnastreeview))
                            strModeloUpdate = strModeloUpdate.replace('@colextratreeview','<div class="col-@columnastreeview"></div>')
                            strModeloUpdate = strModeloUpdate.replace('@columnastreeview',str(modelo.columnastreeview))
                        else:
                            strModeloUpdate = strModeloUpdate.replace('@colextratreeview','')
                            strModeloUpdate = strModeloUpdate.replace('@datossintreeview','12')

                        strModeloUpdate = strModeloUpdate.replace('@treeview',strTv)


                    # Procesa los css del archivo

                    strModeloUpdate = strModeloUpdate.replace('@modelo',modelo.nombre)
                    
                    strModeloUpdate = AsignaFonts(modelo.fonttituloupdate,'tituloupdate',strModeloUpdate)
                    strModeloUpdate = strModeloUpdate.replace('@colortituloupdate', modelo.colortituloupdate)
                    strModeloUpdate = NumeroPorcentaje('@altofilatituloupdate', modelo.altofilatituloupdate,strModeloUpdate)
                    strModeloUpdate = strModeloUpdate.replace('@colorfondotituloupdate', modelo.colorfondotituloupdate)
                    strModeloUpdate = strModeloUpdate.replace('@colorfondofilatituloupdate', modelo.colorfondofilatituloupdate)


                    strModeloUpdate = AsignaFonts(modelo.fontcomentarioupdate,'comentarioupdate',strModeloUpdate)
                    strModeloUpdate = strModeloUpdate.replace('@colorcomentarioupdate', modelo.colorcomentarioupdate)
                    strModeloUpdate = strModeloUpdate.replace('@colorfondocomentarioupdate', modelo.colorfondocomentarioupdate)


                    strModeloUpdate = AsignaFonts(modelo.fontlabelmodelo,'label'+modelo.nombre,strModeloUpdate)
                    strModeloUpdate = strModeloUpdate.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)
                    strModeloUpdate = UpperLower(modelo.mayusculastituloupdate,'@uppercasetitulo',strModeloUpdate)
                    strModeloUpdate = strModeloUpdate.replace('@bordeexterior', 'border' if modelo.bordeexteriorupdate else '')
                    strModeloUpdate = strModeloUpdate.replace('@bordeformulario', 'border' if modelo.bordeformularioupdate else '')

                    strCssFin = ''
                    for modelohijo in Modelo.objects.filter(padre=modelo.nombre , proyecto = proyecto):
                        # Leer el css para la lista de hijos
                        # strcsshijo = TextFiles.objects.get(file = "modelo_list_hijo.css").texto
                        strcsshijo = LeerArchivoEnTexto(dt + 'modelo_hijo.css',etapa,nombre,usuario)
                        strcsshijo = strcsshijo.replace('@modelohijo',modelohijo.nombre)

                        strcsshijo = AsignaFonts(modelohijo.fonttitulolista,'titulolista' + modelohijo.nombre, strcsshijo)
                        strcsshijo = strcsshijo.replace('@colortitulolista' + modelohijo.nombre, modelohijo.colortitulolista)
                        strcsshijo = strcsshijo.replace('@colorfondotitulolista' + modelohijo.nombre, modelohijo.colorfondotitulolista)
                        strcsshijo = NumeroPorcentaje('@altotitulolista' + modelohijo.nombre, modelohijo.altotitulolista,strcsshijo)

                        strcsshijo = strcsshijo.replace('@colorfondocomentariolista' + modelohijo.nombre, modelohijo.colorfondocomentariolista)
                        strcsshijo = strcsshijo.replace('@colorcomentariolista' + modelohijo.nombre, modelohijo.colorcomentariolista)

                        try:
                            strcsshijo = AsignaFonts(modelohijo.fontcomentariolista,'comentariolista' + modelohijo.nombre,strcsshijo)
                        except:
                            strcsshijo = AsignaFonts('Arial,10,normal','comentariolista' + modelohijo.nombre,strcsshijo)


                        strcsshijo = AsignaFonts(modelohijo.fontcolumnaslista,"columnaslista" + modelohijo.nombre,strcsshijo)                            
                        strcsshijo = strcsshijo.replace('@colorcolumnaslista' + modelohijo.nombre,modelohijo.colorcolumnaslista)
                        strcsshijo = strcsshijo.replace('@colorfondocolumnaslista' + modelohijo.nombre,modelohijo.colorfondocolumnaslista)
                        strcsshijo = strcsshijo.replace('@altocolumnaslista' + modelohijo.nombre,str(modelohijo.altocolumnas))


                        strcsshijo = AsignaFonts(modelohijo.fonttextolista,"textolista" + modelohijo.nombre,strcsshijo)                            
                        strcsshijo = strcsshijo.replace('@colortextolista' + modelohijo.nombre,modelohijo.colortextolista)
                        strcsshijo = strcsshijo.replace('@colorfondotextolista' + modelohijo.nombre,modelohijo.colorfondotextolista)


                        strcsshijo = AsignaFonts(modelohijo.fonteditarborrar,'editarborrar' + modelohijo.nombre,strcsshijo)
                        strcsshijo = strcsshijo.replace('@coloreditarborrar' + modelohijo.nombre, modelohijo.coloreditarborrar)

                        #link nuevo
                        try:
                            strcsshijo = AsignaFonts(modelohijo.fontlinknuevomodelo,'nuevomodelo' + modelohijo.nombre,strcsshijo)
                        except:
                            strcsshijo = AsignaFonts('Arial,10,normal','nuevomodelo' + modelohijo.nombre,strcsshijo)

                        strcsshijo = strcsshijo.replace('@colorlinknuevomodelo' + modelohijo.nombre, modelohijo.colorlinknuevomodelo)


                        strCssFin += strcsshijo
                        strcsshijo = ''

                    strModeloUpdate = strModeloUpdate.replace('@hijos',strCssFin)


                    # Lee el archivo css para cada modelo
                    # strcss = TextFiles.objects.get(file = "modelo_update.css").texto
                    strcss = LeerArchivoEnTexto(dt + 'modelo_update.css',etapa,nombre,usuario)
                    strcss = strcss.replace('@modelo',modelo.nombre)
                    
                    # for propiedad in Propiedad.objects.filter(modelo=modelo):
                    #     if propiedad.enlista:
                    #         strt = strt.replace('@nombre', modelo.nombre + '.' + propiedad.nombre)
                    #         break

                    # codigo para la referencia del form
                    stra = ''

                    strModeloRaiz = ''
                    strAplicacionRaiz = ''
                    if modelo.padre =='nada': # modelo padre
                        stra = modelo.tituloupdate + "&nbsp;<a href=" + '"' + "{% url '@aplicacion:listar_@modelo' %}" + '"' + "><span style=" + '"' + "color:green" + '"' + ">{{nombre}}</span></a>"
                        strModeloRaiz = modelo.nombre
                        strAplicacionRaiz = modelo.aplicacion.nombre 
                        # stra = modelo.tituloupdate + '&nbsp;<span style=" + '"' + 'color:green" + '"' + '>{{nombre}}</span>' 
                        # stra = modelo.tituloupdate + '&nbsp;{{nombre}}' 
                    else:
                        modelo_padre = Modelo.objects.get(nombre=modelo.padre , proyecto=proyecto)
                        if modelo_padre.padre != 'nada': # el modelo es nieto
                            modelo_abuelo = Modelo.objects.get(nombre=modelo_padre.padre , proyecto=proyecto)
                            stra += '\t\t\t\t<div class="col">' + '\n'
                            stra += '\t\t\t\t\t<div class="" style="float: left">@modelohijo:&nbsp&nbsp</div>' +'\n'
                            stra += '\t\t\t\t\t<div class="" style="float: left; color:green;"><b>{{nombre}}</b>&nbsp&nbsp</div>' + '\n'
                            stra += '\t\t\t\t\t<div class="" style="float: left;">' + '\n'
                            stra += '\t\t\t\t\t{% if esquema == "sin_treeview" %}' + '\n'
                            stra += '\t\t\t\t\t\t<a href="{% url ' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ' @modelopadre_id %}?@modeloabuelo_id={{@modeloabuelo_id}}">' + strTextoVolver + '</a>' + '\n'
                            stra += '\t\t\t\t\t{% else %}' + '\n'
                            stra += '\t\t\t\t\t\t<a href="{% url ' + "'" + ModeloRaizHtml(modelo,modelo.proyecto)[1] + ':editar_' + ModeloRaizHtml(modelo,modelo.proyecto)[0] + "' " + ModeloRaizHtml(modelo,modelo.proyecto)[0] + '.id %}?esquema={{esquema}}">' + strTextoVolver + '</a>' + '\n'
                            stra += '\t\t\t\t\t{% endif %}' + '\n'
                            stra += '\t\t\t\t\t</div>' + '\n'
                            stra += '\t\t\t\t</div>' + '\n'
                            # stra =  modelo.nombre.upper() + ': <b>{{nombre}}</b>&nbsp&nbsp<a href="{% url ' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ' @modelopadre_id %}?@modeloabuelo_id={{@modeloabuelo_id}}">(Volver)</a>'
                            stra = stra.replace('@modeloabuelo', modelo_abuelo.nombre)        
                        else: # el modelo es hijo
                            stra += '\t\t\t\t<div class="col text-center">' + '\n'
                            stra += '\t\t\t\t\t<div class="" style="float: left;">@modelohijo:&nbsp&nbsp</div>&nbsp' + '\n'
                            stra += '\t\t\t\t\t<div class="" style="float: left; color:green;"><b>{{nombre}}&nbsp&nbsp</b></div>' + '\n'
                            stra += '\t\t\t\t\t<div class="" style="float: left">' + '\n'
                            stra += '\t\t\t\t\t{% if esquema == "sin_treeview" %}' + '\n'
                            stra += '\t\t\t\t\t\t<a href="{% url ' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ' @modelopadre_id %}">' + strTextoVolver + '</a>' + '\n'
                            stra += '\t\t\t\t\t{% else %}' + '\n'
                            stra += '\t\t\t\t\t\t<a href="{% url ' + "'" + ModeloRaizHtml(modelo,modelo.proyecto)[1] + ':editar_' + ModeloRaizHtml(modelo,modelo.proyecto)[0] + "' " + ModeloRaizHtml(modelo,modelo.proyecto)[0] + '.id %}?esquema={{esquema}}">' + strTextoVolver + '</a>' + '\n'
                            stra += '\t\t\t\t\t{% endif %}' + '\n'
                            stra += '\t\t\t\t\t</div>' + '\n'
                            stra += '\t\t\t\t</div>' + '\n'
                        stra = AplicacionReal(modelo,stra,proyecto)
                        stra = stra.replace('@aplicacionpadre', Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre)        
                        stra = stra.replace('@modelopadre', modelo_padre.nombre)        
                        stra = stra.replace('@modelohijo', modelo.nombre)        

                    stra = stra.replace('@tituloupdate', modelo.tituloupdate)        
                    stra = stra.replace('@modelo', modelo.nombre)        

                    strModeloUpdate = strModeloUpdate.replace('@tituloupdate', '\t\t\t\t\t' + stra)

                    #titulo pagina update
                    strcss = AsignaFonts(modelo.fonttituloupdate,'tituloupdate',strcss)
                    strcss = strcss.replace('@colortituloupdate', modelo.colortituloupdate)
                    strcss = NumeroPorcentaje('@altofilatituloupdate', modelo.altofilatituloupdate,strcss)
                    # strcss = strcss.replace('@altofilatituloupdate', str(modelo.altofilatituloupdate))
                    strcss = strcss.replace('@colorfondotituloupdate', modelo.colorfondotituloupdate)
                    strcss = strcss.replace('@colorfondofilatituloupdate', modelo.colorfondofilatituloupdate)

                    # Justificacion titulo update
                    strModeloUpdate = AsignaJustificacion('h', modelo.justificacionhorizontaltituloupdate,'@justificacionhorizontaltituloupdate',strModeloUpdate)
                    strModeloUpdate = AsignaJustificacion('v', modelo.justificacionverticaltituloupdate,'@justificacionverticaltituloupdate',strModeloUpdate)

                    #comentario pagina update
                    strcss = AsignaFonts(modelo.fontcomentarioupdate,'comentarioupdate',strcss)
                    strcss = strcss.replace('@colorcomentarioupdate', modelo.colorcomentarioupdate)
                    strcss = strcss.replace('@colorfondocomentarioupdate', modelo.colorfondocomentarioupdate)
                    strModeloUpdate = strModeloUpdate.replace('@comentarioupdate', '\t\t\t' + modelo.comentarioupdate)

                    # Numero de columnas para organizar la pagina
                    strModeloUpdate = strModeloUpdate.replace('@numerocolumnasizquierdaupdate', str(modelo.numerocolumnasizquierdaupdate))
                    strModeloUpdate = strModeloUpdate.replace('@numerocolumnasmodeloupdate', str(modelo.numerocolumnasmodeloupdate))
                    strModeloUpdate = strModeloUpdate.replace('@numerocolumnasderechaupdate', str(modelo.numerocolumnasderechaupdate))
                    strModeloUpdate = strModeloUpdate.replace('@numerocolumnashijosupdate', str(modelo.numerocolumnashijosupdate))

                    #etiquetas
                    texto = Etiquetas(modelo,strModeloUpdate,strcss,'\t\t\t',directorio,nombre,etapa,usuario)
                    strModeloUpdate =  texto[0]
                    strcss = texto[1]

                    strcssTotal += strcss
                    strcss = ''

                    #lista de modelos hijos
                    strh = ''
                    strBordeHijos = ''
                    strffc = ''
                    for modelohijo in Modelo.objects.filter(padre=modelo.nombre , proyecto = proyecto):
                        # Leer el css para la lista de hijos
                        # strcsshijo = TextFiles.objects.get(file = "modelo_list_hijo.css").texto
                        strcsshijo = LeerArchivoEnTexto(dt + 'modelo_list_hijo.css',etapa,nombre,usuario)
                        strcsshijo = strcsshijo.replace('@modelohijo',modelohijo.nombre)
                        strBordeHijos = 'border'

                        ntabs = ''
                        if modelo.hijoscontiguos:
                            ntabs = ''
                        else:
                            ntabs = '\t\t\t'
                        strlh = ntabs + "\t\t\t<div class=" + '"' + "border rounded mb-3" + '"' + " style=" + '"' + "padding: 5px;" + '"' + ">" + "\n"
                        strlh += "<!-- #@[p_hijo_@hijo_01] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t<div id="lista_@hijo" class="container-fluid lista_@hijo mb-3">' + '\n'
                        strlh += ntabs + '\t\t\t\t\t<div id="fila_titulo_lista_@hijo" class="row mt-2 mb-2 fila_titulo_lista_@hijo ">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_02] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t<div class="col @justificacionverticaltitulolista @justificacionhorizontaltitulolista @uppercasetitulo">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_03] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t<span id="titulo_lista_@hijo" class="titulo_lista_@hijo">' + '\n'
                        strlh += ntabs + '\t\t\t\t\t\t\t\t@titulolista</span>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_04] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t</span>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_05] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_06] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_07] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t<div id=fila_comentario_lista_@hijo class="row mt-2 mb-2 fila_comentario_lista_@hijo ">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_08] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t<div class="col @justificacionverticalcomentariolista @justificacionhorizontalcomentariolista @uppercasecomentario">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_09] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t<span id="comentario_lista_@hijo" class="comentario_lista_@hijo">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_10] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t\t@comentariolista' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_11] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t</span>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_12] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t</div>' + '\n'
                        strlh += ntabs + '\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_13] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t<div id="fila_columnas_@hijo" class="row fila_columnas_@hijo @uppercasecolumnas" >' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_14] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t{% if numero' + modelohijo.nombre + ' > 0 %}' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_15] -->" + "\n"
                        strlh += '@columnashijo' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_16] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t{% endif %}' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_17] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_18] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t{% for obj in lista@hijo %}' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_19] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t<div id="fila_datos_@hijo" class="row  fila_datos_@hijo" >' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_20] -->" + "\n"
                        strlh += '@listaregistroshijo' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_21] -->" + "\n"
                        # strlh += '\t\t\t\t\t\t\t<div class="col-@restocolumnas">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_22] -->" + "\n"
                        # strlh += ntabs + '\t\t\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_23] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t<div class="col-12 col-md-1 edita_@hijo">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_24] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t\t@editahijo' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_25] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_26] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t<div class="col-12 col-md-1 ml-2 borra_@hijo">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_27] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t\t@borrahijo' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_28] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_29] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t<div class="col-1">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_30] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_31] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_32] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t{% endfor %}' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_33] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t<div id="fila_nuevo_@hijo" class="row mt-3 mb-3 fila_nuevo_@hijo">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_34] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t<div class="col">' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_35] -->" + "\n"
                        # Ver si tiene modelo abuelo
                        if modelo.padre != 'nada':
                            modelo_abuelo = Modelo.objects.get(nombre = modelo.padre,proyecto=proyecto)
                            strlh += ntabs + '\t\t\t\t\t\t\t<a class="@linknuevomodelo mt-2" href="{% url ' + "'" + '@aplicacionhijo:crear_@hijo' + "'" + '%}?@modelopadre_id={{ @modelopadre.id }}&@modeloabuelo_id={{ @modeloabuelo_id }}">@textolinknuevomodelo</a>' + '\n' + '\n'
                            strlh = strlh.replace('@modeloabuelo',modelo_abuelo.nombre)
                        else:
                            strlh += ntabs + '\t\t\t\t\t\t\t<a class="@linknuevomodelo mt-2" href="{% url ' + "'" + '@aplicacionhijo:crear_@hijo' + "'" + '%}?@modelopadre_id={{ @modelopadre.id }}">@textolinknuevomodelo</a>' + '\n' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_36] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_37] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_38] -->" + "\n"
                        strlh += ntabs + '\t\t\t\t</div>' + '\n'
                        strlh += ntabs + '\t\t\t</div>' + '\n'
                        strlh += "<!-- #@[p_hijo_@hijo_39] -->" + "\n"

                        # Titulo lista hijos
                        strcsshijo = AsignaFonts(modelohijo.fonttitulolista,'titulolista' + modelohijo.nombre, strcsshijo)
                        strcsshijo = strcsshijo.replace('@colortitulolista' + modelohijo.nombre, modelohijo.colortitulolista)
                        strcsshijo = strcsshijo.replace('@colorfondotitulolista' + modelohijo.nombre, modelohijo.colorfondotitulolista)
                        strcsshijo = NumeroPorcentaje('@altotitulolista' + modelohijo.nombre, modelohijo.altotitulolista,strcsshijo)
                        # strcsshijo = strcsshijo.replace('@altotitulolista' + modelohijo.nombre, str(modelohijo.altotitulolistahijos))

                        # justificacion vertical titulo lista hijos
                        strlh = AsignaJustificacion('v', modelohijo.justificacionverticaltitulolista, '@justificacionverticaltitulolista', strlh)
                        strlh = AsignaJustificacion('h', modelohijo.justificacionhorizontaltitulolista, '@justificacionhorizontaltitulolista', strlh)

                        strlh = strlh.replace('@titulolista', modelohijo.titulolista)
                        strlh = UpperLower(modelohijo.mayusculastitulolista,'@uppercasetitulo',strlh)

                        # COMENTARIO LISTA HIJOS
                        strcsshijo = strcsshijo.replace('@colorfondocomentariolista' + modelohijo.nombre, modelohijo.colorfondocomentariolista)
                        strcsshijo = strcsshijo.replace('@colorcomentariolista' + modelohijo.nombre, modelohijo.colorcomentariolista)
                        strlh = strlh.replace('@comentariolista', modelohijo.comentariolista)

                        try:
                            strcsshijo = AsignaFonts(modelohijo.fontcomentariolista,'comentariolista' + modelohijo.nombre,strcsshijo)
                        except:
                            strcsshijo = AsignaFonts('Arial,10,normal','comentariolista' + modelohijo.nombre,strcsshijo)

                        # strcsshijo = strcsshijo.replace('@altotitulolista' + modelohijo.nombre, str(modelohijo.altotitulolistahijos))

                        # justificacion vertical titulo lista hijos
                        strlh = AsignaJustificacion('v', modelohijo.justificacionverticaltitulolista, '@justificacionverticaltitulolista', strlh)
                        strlh = AsignaJustificacion('h', modelohijo.justificacionhorizontaltitulolista, '@justificacionhorizontaltitulolista', strlh)

                        strlh = strlh.replace('@titulolista', modelohijo.titulolista)

                        # if modelohijo.mayusculastitulolistahijos:
                        #     strlh = strlh.replace('@uppercase', 'text-uppercase')
                        # else:
                        #     strlh = strlh.replace('@uppercase', '')

                        if modelo.hijoscontiguos:
                            lista = PropiedadesEnLista(modelohijo,Propiedad,'')
                        else:
                            lista = PropiedadesEnLista(modelohijo,Propiedad,'\t\t\t\t')
                        strlth = lista[0]
                        strlrh = lista[1]
                        columnashijos = lista[2]

                        # Css de columnas lista hijos
                        strcsshijo = AsignaFonts(modelohijo.fontcolumnaslista,"columnaslista" + modelohijo.nombre,strcsshijo)                            
                        strcsshijo = strcsshijo.replace('@colorcolumnaslista' + modelohijo.nombre,modelohijo.colorcolumnaslista)
                        strcsshijo = strcsshijo.replace('@colorfondocolumnaslista' + modelohijo.nombre,modelohijo.colorfondocolumnaslista)
                        strcsshijo = strcsshijo.replace('@altocolumnaslista' + modelohijo.nombre,str(modelohijo.altocolumnas))
                        # Mayusculas columna
                        strlh = UpperLower(modelohijo.mayusculascolumnas,'@uppercasecolumnas',strlh)

                        # Css de Datos de lista hijos
                        strcsshijo = AsignaFonts(modelohijo.fonttextolista,"textolista" + modelohijo.nombre,strcsshijo)                            
                        strcsshijo = strcsshijo.replace('@colortextolista' + modelohijo.nombre,modelohijo.colortextolista)
                        strcsshijo = strcsshijo.replace('@colorfondotextolista' + modelohijo.nombre,modelohijo.colorfondotextolista)

                        # editar y borrar hijos
                        streh = ''
                        strbh = ''
                        if modelohijo.padre != 'nada': # modelo hijo o nieto
                            modelo_padre = Modelo.objects.get(nombre=modelohijo.padre , proyecto=proyecto)
                            if modelo_padre.padre != 'nada': # modelo nieto
                                modelo_abuelo = Modelo.objects.get(nombre=modelo_padre.padre , proyecto=proyecto)
                                streh += '<a id="editar_borrar_lista-@hijo"  class="editar_borrar_lista_@hijo" href="{% url ' + "'" + '@aplicacionhijo:editar_@hijo' + "'" + ' obj.id %}?@modelopadre_id={{ @modelopadre_id }}&@modeloabuelo_id={{@modeloabuelo_id}}">@textoeditar</a>' + '\n'
                                strbh += '<a id="editar_borrar_lista_@hijo" class="editar_borrar_lista_@hijo" href="{% url ' + "'" + '@aplicacionhijo:borrar_@hijo' + "'" + ' obj.id %}?@modelopadre_id={{ @modelopadre_id }}&@modeloabuelo_id={{@modeloabuelo_id}}">@textoborrar</a>' + '\n'
                                streh = streh.replace('@modeloabuelo', modelo_abuelo.nombre)
                                strbh = strbh.replace('@modeloabuelo', modelo_abuelo.nombre)
                            else: # modelo hijo
                                streh += '<a id="editar_borrar_lista_@hijo" class="editar_borrar_lista_@hijo" href="{% url ' + "'" + '@aplicacionhijo:editar_@hijo' + "'" + ' obj.id %}?@modelopadre_id={{ @modelopadre_id }}">@textoeditar</a>' + '\n'
                                strbh += '<a id="editar_borrar_lista_@hijo" class="editar_borrar_lista_@hijo" href="{% url ' + "'" + '@aplicacionhijo:borrar_@hijo' + "'" + ' obj.id %}?@modelopadre_id={{ @modelopadre_id }}">@textoborrar</a>' + '\n'
                            streh = streh.replace('@modelopadre', modelo_padre.nombre)
                            strbh = strbh.replace('@modelopadre', modelo_padre.nombre)
                        else: # modelo sin padre
                            streh += '<a class="font_editar_borrar_lista_hijos_@modelo" href="{% url ' + "'" + '@aplicacionhijo:editar_@hijo' + "'" + ' obj.id %}?@modelo_id={{ @modelo.id }}">@textoeditar</a>' + '\n'
                            strbh += '<a class="font_editar_borrar_lista_hijos_@modelo" href="{% url ' + "'" + '@aplicacionhijo:borrar_@hijo' + "'" + ' obj.id %}?@modelo_id={{ @modelo.id }}">@textoborrar</a>' + '\n'
                            streh = streh.replace('@modelo', modelohijo.nombre)
                            strbh = strbh.replace('@modelo', modelohijo.nombre)

                        # Encuentra la aplicacion real
                        streh = AplicacionReal(modelohijo,streh,proyecto)
                        strbh = AplicacionReal(modelohijo,strbh,proyecto)

                        #editar borrar
                        strcsshijo = AsignaFonts(modelohijo.fonteditarborrar,'editarborrar' + modelohijo.nombre,strcsshijo)
                        strcsshijo = strcsshijo.replace('@coloreditarborrar' + modelohijo.nombre, modelohijo.coloreditarborrar)

                        #link nuevo
                        try:
                            strcsshijo = AsignaFonts(modelohijo.fontlinknuevomodelo,'nuevomodelo' + modelohijo.nombre,strcsshijo)
                        except:
                            strcsshijo = AsignaFonts('Arial,10,normal','nuevomodelo' + modelohijo.nombre,strcsshijo)

                        strcsshijo = strcsshijo.replace('@colorlinknuevomodelo' + modelohijo.nombre, modelohijo.colorlinknuevomodelo)
                        strlh = strlh.replace('@textolinknuevomodelo', modelohijo.textolinknuevomodelo)

                        #link boton
                        if modelohijo.linknuevomodelo:
                            strlh = strlh.replace('@linknuevomodelo', 'btn btn-block btn-' + modelohijo.colorbotonlinknuevomodelo)
                        else:
                            strlh = strlh.replace('@linknuevomodelo', '')

                        strcsshijototal += strcsshijo
                        strcsshijo = ''


                        streh = AsignaTexto(modelohijo.textoeditarborrar,"editar,borrar","@textoeditar,@textoborrar",streh)
                        strbh = AsignaTexto(modelohijo.textoeditarborrar,"editar,borrar","@textoeditar,@textoborrar",strbh)

                        strlh = strlh.replace('@editahijo', streh)
                        strlh = strlh.replace('@borrahijo', strbh)
                        strlh = strlh.replace('@modelopadre', modelo.nombre)
                        strlh = strlh.replace('@modelohijo', modelohijo.nombre)
                        strlh = strlh.replace('@modelo', modelohijo.nombre)
                        strlh = strlh.replace('@hijo', modelohijo.nombre)
                        strlh = strlh.replace('@aplicacionhijo', modelohijo.aplicacion.nombre)
                        strlh = strlh.replace('@columnashijo', strlth)
                        strlh = strlh.replace('@listaregistroshijo', strlrh)
                        strlh = strlh.replace('@restocolumnas', str(9-columnashijos))

                        strh += strlh

                    strModeloUpdate = strModeloUpdate.replace('@listahijos', strh)

                    # Reemplazos de modelo y aplicacion
                    strModeloUpdate = strModeloUpdate.replace('@aplicacion', aplicacion.nombre)
                    strModeloUpdate = strModeloUpdate.replace('@modelo', modelo.nombre)

                    # bordecomentario
                    strModeloUpdate = strModeloUpdate.replace('@bordecomentario', 'border' if modelo.bordecomentarioupdate else '')

                    # Grabar el html
                    ProcesoPersonalizacion(proyecto,aplicacion.nombre,modelo.nombre + "_update_form.html",directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/",strModeloUpdate,nombre,etapa,usuario)
                    # rutinas.EscribirArchivo(directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/" + modelo.nombre + "_update_form.html" ,etapa,nombre, strModeloUpdate,True)
                
                # Escribir el css del modelo
                ProcesoPersonalizacion(proyecto,appCore.nombre,'modelo_update.css',directorio + nombre + "/core/static/core/css/",strcssTotal,nombre,etapa,usuario)


    return strcsshijototal

def CrearModelosDelete(proyecto,nombre,etapa,directorio,usuario,dt):    

    strcssTotal = ''
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        if AplicacionTienePropiedades(aplicacion) and aplicacion.nombre!= 'core' and aplicacion.nombre != 'registration':                

            for modelo in Modelo.objects.filter(aplicacion=aplicacion):
                if modelo.sinbasedatos == False:
                    # strcss = TextFiles.objects.get(file = "modelo_borra.css").texto
                    strcss = LeerArchivoEnTexto(dt + "modelo_borra.css",etapa,nombre,usuario)
                    strcss =  strcss.replace('@modelo', modelo.nombre)
                    # strModeloBorra = TextFiles.objects.get(file = "modelo_confirm_delete.html").texto
                    strModeloBorra = LeerArchivoEnTexto(dt + "modelo_confirm_delete.html",etapa,nombre,usuario)


                    # Procesa los css

                    strModeloBorra =  strModeloBorra.replace('@modelo', modelo.nombre)
                    strModeloBorra = AsignaFonts(modelo.fonttituloborra,'tituloborra',strModeloBorra)
                    strModeloBorra = strModeloBorra.replace('@colortituloborra', modelo.colortituloborra)
                    strModeloBorra = NumeroPorcentaje('@altofilatituloborra', modelo.altofilatituloborra,strModeloBorra)
                    strModeloBorra = strModeloBorra.replace('@colorfondofilatituloborra', modelo.colorfondofilatituloborra)
                    strModeloBorra = strModeloBorra.replace('@colorfondotituloborra', modelo.colorfondotituloborra)
                    strModeloBorra = AsignaFonts(modelo.fontcomentarioborra,'comentarioborra',strModeloBorra)
                    strModeloBorra = strModeloBorra.replace('@colorcomentarioborra', modelo.colorcomentarioborra)
                    strModeloBorra = strModeloBorra.replace('@colorfondocomentarioborra', modelo.colorfondocomentarioborra)
                    strModeloBorra = AsignaFonts(modelo.fonttextoborra,'textoborra',strModeloBorra)
                    strModeloBorra = strModeloBorra.replace('@colortextoborra', modelo.colortextoborra)
                    strModeloBorra = strModeloBorra.replace('@colorfondotextoborra', modelo.colorfondotextoborra)



                    strModeloBorra =  strModeloBorra.replace('@modelo', modelo.nombre)
                    strModeloBorra =  strModeloBorra.replace('@numerocolumnasizquierdaborra', str(modelo.numerocolumnasizquierdaborra))
                    strModeloBorra =  strModeloBorra.replace('@numerocolumnasmodeloborra', str(modelo.numerocolumnasmodeloborra))
                    strModeloBorra =  strModeloBorra.replace('@numerocolumnasderechaborra', str(modelo.numerocolumnasderechaborra))

                    # Justificacion titulo inserta
                    strModeloBorra = AsignaJustificacion('h', modelo.justificacionhorizontaltituloborra,'@justificacionhorizontaltituloborra',strModeloBorra)
                    strModeloBorra = AsignaJustificacion('v', modelo.justificacionverticaltituloborra,'@justificacionverticaltituloborra',strModeloBorra)

                    # Titulo y texto de borrado
                    strModeloBorra =  strModeloBorra.replace('@tituloborra', modelo.tituloborra)
                    strModeloBorra =  strModeloBorra.replace('@textoborra', modelo.textoborra)
                    strModeloBorra = UpperLower(modelo.mayusculastituloborra,'@uppercasetitulo',strModeloBorra)

                    # cancelar el borrado
                    strcb = ''
                    if modelo.padre != 'nada': # modelo hijo o nieto
                        modelo_padre = Modelo.objects.get(nombre=modelo.padre , proyecto=proyecto)
                        if modelo_padre.padre != 'nada': # modelo nieto
                            modelo_abuelo = Modelo.objects.get(nombre=modelo_padre.padre , proyecto=proyecto)
                            strcb = '<a class="btn btn-danger" href="{% url ' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ' @modelopadre_id %}?@modeloabuelo_id={{@modeloabuelo_id}}">Cancelar</a>'
                            strcb = strcb.replace('@modeloabuelo', modelo_abuelo.nombre)
                        else: # modelo hijo
                            strcb = '<a class="btn btn-danger" href="{% url ' + "'" + '@aplicacionpadre:editar_@modelopadre' + "'" + ' @modelopadre_id %}">Cancelar</a>'
                        strcb = strcb.replace('@aplicacionpadre', Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre)
                        strcb = strcb.replace('@modelopadre', modelo_padre.nombre)
                        # Encuentra la aplicacion real
                        strcb = AplicacionReal(modelo,strcb,proyecto)
                    else: # modelo sin padre
                        strcb = '<a class="btn btn-danger" href="{% url ' + "'" + '@aplicacion:listar_@modelo' + "'" + ' %}">Cancelar</a>'
                        strcb = strcb.replace('@aplicacionreal',aplicacion.nombre)
                        strcb = strcb.replace('@aplicacion', Aplicacion.objects.get(id=modelo.aplicacion.id).nombre)

                    #titulo pagina borra
                    strcss = AsignaFonts(modelo.fonttituloborra,'tituloborra',strcss)
                    strcss = strcss.replace('@colortituloborra', modelo.colortituloborra)
                    strcss = NumeroPorcentaje('@altofilatituloborra', modelo.altofilatituloborra,strcss)
                    # strcss = strcss.replace('@altofilatituloborra', str(modelo.altofilatituloborra))
                    strcss = strcss.replace('@colorfondofilatituloborra', modelo.colorfondofilatituloborra)
                    strcss = strcss.replace('@colorfondotituloborra', modelo.colorfondotituloborra)

                    #comentario pagina borra
                    strcss = AsignaFonts(modelo.fontcomentarioborra,'comentarioborra',strcss)
                    strcss = strcss.replace('@colorcomentarioborra', modelo.colorcomentarioborra)
                    strcss = strcss.replace('@colorfondocomentarioborra', modelo.colorfondocomentarioborra)
                    strModeloBorra = strModeloBorra.replace('@comentarioborra', modelo.comentarioborra)

                    #texto pagina borra
                    strcss = AsignaFonts(modelo.fonttextoborra,'textoborra',strcss)
                    strcss = strcss.replace('@colortextoborra', modelo.colortextoborra)
                    strcss = strcss.replace('@colorfondotextoborra', modelo.colorfondotextoborra)
                    strModeloBorra = strModeloBorra.replace('@textoborra', modelo.textoborra)

                    strModeloBorra = strModeloBorra.replace('@cancelaborrado', strcb)
                    strModeloBorra = strModeloBorra.replace('@textobotonborrado', modelo.textobotonborra)
                    strModeloBorra = strModeloBorra.replace('@aplicacion', aplicacion.nombre)
                    strModeloBorra = strModeloBorra.replace('@modelo', modelo.nombre)

                    # Actualiza css
                    strcssTotal += strcss

                    #Sin lineas de personalizacion
                    if not proyecto.conetiquetaspersonalizacion:
                        strModeloBorra = QuitaLineasPersonalizacion(strModeloBorra)

                    # bordecomentario
                    strModeloBorra = strModeloBorra.replace('@bordecomentario', 'border' if modelo.bordecomentarioborra else '')
                    strModeloBorra = strModeloBorra.replace('@bordeexterior', 'border' if modelo.bordeexteriorborra else '')

                    # Grabar archivos
                    ProcesoPersonalizacion(proyecto,aplicacion.nombre,modelo.nombre + "_confirm_delete.html",directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/",strModeloBorra,nombre,etapa,usuario)

    return strcssTotal

def CrearModelosDash(proyecto, etapa,nombre,usuario,directorio, dt):
    strcssTotal = ''
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        # Grabar el modelo si su aplicacion tiene modelos con propiedades
        if AplicacionTienePropiedades(aplicacion) and aplicacion.nombre!= 'core' and aplicacion.nombre != 'registration':                
            for modelo in Modelo.objects.filter(aplicacion=aplicacion):
                if modelo.sinbasedatos == False:
                    # Leer el archivo modelo_lista.html de tet files
                    # strModeloInserta = TextFiles.objects.get(file = "modelo_inserta.html").texto
                    strModeloInserta = LeerArchivoEnTexto(dt + 'modelo_dash.html',etapa,nombre,usuario)

                    # Procesa los css

                    strModeloInserta = strModeloInserta.replace('@modelo',modelo.nombre)

                    strModeloInserta = AsignaFonts(modelo.fonttituloinserta,'tituloinserta',strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colortituloinserta', modelo.colortituloinserta)
                    strModeloInserta = NumeroPorcentaje('@altofilatituloinserta', modelo.altofilatituloinserta,strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colorfondofilatituloinserta', modelo.colorfondofilatituloinserta)
                    strModeloInserta = strModeloInserta.replace('@colorfondotituloinserta', modelo.colorfondotituloinserta)

                    # strModeloInserta = AsignaFonts(modelo.fontcomentarioinserta,'comentarioinserta',strModeloInserta)
                    # strModeloInserta = strModeloInserta.replace('@colorcomentarioinserta', modelo.colorcomentarioinserta)
                    # strModeloInserta = strModeloInserta.replace('@colorfondocomentarioinserta', modelo.colorfondocomentarioinserta)
                    # strModeloInserta = strModeloInserta.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)

                    strModeloInserta = AsignaFonts(modelo.fontlabelmodelo,'label'+modelo.nombre,strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)


                    # Lee el archivo css para cada modelo
                    strcss = LeerArchivoEnTexto(dt + 'modelo_inserta.css',etapa,nombre,usuario) 
                    strcss = strcss.replace('@modelo',modelo.nombre)
                    strModeloInserta = strModeloInserta.replace('@modelo', modelo.nombre)
                    strModeloInserta = strModeloInserta.replace('@aplicacion', aplicacion.nombre)
                    
                    # codigo para el Titulo del form
                    stra = 'Dash Board de ' + modelo.nombre + '\n'
                    strModeloInserta = strModeloInserta.replace('@tituloinserta', '\t\t\t\t' + stra)

                    #titulo pagina
                    strcss = AsignaFonts(modelo.fonttituloinserta,'tituloinserta',strcss)
                    strcss = strcss.replace('@colortituloinserta', modelo.colortituloinserta)
                    strcss = NumeroPorcentaje('@altofilatituloinserta', modelo.altofilatituloinserta,strcss)
                    # strcss = strcss.replace('@altofilatituloinserta', str(modelo.altofilatituloinserta))
                    strcss = strcss.replace('@colorfondofilatituloinserta', modelo.colorfondofilatituloinserta)
                    strcss = strcss.replace('@colorfondotituloinserta', modelo.colorfondotituloinserta)

                    # Justificacion titulo inserta
                    strModeloInserta = AsignaJustificacion('h', modelo.justificacionhorizontaltituloinserta,'@justificacionhorizontaltituloinserta',strModeloInserta)
                    strModeloInserta = AsignaJustificacion('v', modelo.justificacionverticaltituloinserta,'@justificacionverticaltituloinserta',strModeloInserta)

                    # #comentario pagina
                    # strcss = AsignaFonts(modelo.fontcomentarioinserta,'comentarioinserta',strcss)
                    # strcss = strcss.replace('@colorcomentarioinserta', modelo.colorcomentarioinserta)
                    # strcss = strcss.replace('@colorfondocomentarioinserta', modelo.colorfondocomentarioinserta)
                    # strcss = strcss.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)
                    # strModeloInserta = strModeloInserta.replace('@comentarioinserta', '\t\t\t\t\t' + modelo.comentarioinserta)

                    # columnas que organizan el cuerpo en insercion
                    strModeloInserta = strModeloInserta.replace('@numerocolumnasizquierdainserta', str(modelo.numerocolumnasizquierdainserta))
                    strModeloInserta = strModeloInserta.replace('@numerocolumnasmodeloinserta', str(modelo.numerocolumnasmodeloinserta))
                    strModeloInserta = strModeloInserta.replace('@numerocolumnasderechainserta', str(modelo.numerocolumnasderechainserta))

                    texto = EtiquetasDash(modelo,strModeloInserta,strcss,'\t\t\t',directorio,nombre,etapa,usuario)
                    strModeloInserta =  texto[0]
                    strcss = texto[1]

                    strcssTotal += strcss

                    # strModeloInserta = EscribePersonalizacion(proyecto,aplicacion,modelo.nombre + '_form.html',strModeloInserta)

                    #Sin lineas de personalizacion
                    if not proyecto.conetiquetaspersonalizacion:
                        strModeloInserta = QuitaLineasPersonalizacion(strModeloInserta)

                    # Graba el archivo
                    ProcesoPersonalizacion(proyecto,aplicacion.nombre,"dash_" + modelo.nombre + ".html",directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/",strModeloInserta,nombre,etapa,usuario)
                    # rutinas.EscribirArchivo(directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/" + modelo.nombre + "_dash.html" ,etapa,nombre, strModeloInserta,True)

    return strcssTotal

def CrearModelosFill(proyecto, etapa,nombre,usuario,directorio, dt):
    strcssTotal = ''
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        # Grabar el modelo si su aplicacion tiene modelos con propiedades
        if AplicacionTienePropiedades(aplicacion) and aplicacion.nombre!= 'core' and aplicacion.nombre != 'registration':                
            for modelo in Modelo.objects.filter(aplicacion=aplicacion):
                if modelo.sinbasedatos == False:
                    # Leer el archivo modelo_lista.html de tet files
                    # strModeloInserta = TextFiles.objects.get(file = "modelo_inserta.html").texto
                    strModeloInserta = LeerArchivoEnTexto(dt + 'modelo_fill.html',etapa,nombre,usuario)

                    # Procesa los css

                    strModeloInserta = strModeloInserta.replace('@modelo',modelo.nombre)

                    strModeloInserta = AsignaFonts(modelo.fonttituloinserta,'tituloinserta',strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colortituloinserta', modelo.colortituloinserta)
                    strModeloInserta = NumeroPorcentaje('@altofilatituloinserta', modelo.altofilatituloinserta,strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colorfondofilatituloinserta', modelo.colorfondofilatituloinserta)
                    strModeloInserta = strModeloInserta.replace('@colorfondotituloinserta', modelo.colorfondotituloinserta)

                    # strModeloInserta = AsignaFonts(modelo.fontcomentarioinserta,'comentarioinserta',strModeloInserta)
                    # strModeloInserta = strModeloInserta.replace('@colorcomentarioinserta', modelo.colorcomentarioinserta)
                    # strModeloInserta = strModeloInserta.replace('@colorfondocomentarioinserta', modelo.colorfondocomentarioinserta)
                    # strModeloInserta = strModeloInserta.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)

                    strModeloInserta = AsignaFonts(modelo.fontlabelmodelo,'label'+modelo.nombre,strModeloInserta)
                    strModeloInserta = strModeloInserta.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)


                    # Lee el archivo css para cada modelo
                    strcss = LeerArchivoEnTexto(dt + 'modelo_inserta.css',etapa,nombre,usuario) 
                    strcss = strcss.replace('@modelo',modelo.nombre)
                    strModeloInserta = strModeloInserta.replace('@modelo', modelo.nombre)
                    strModeloInserta = strModeloInserta.replace('@aplicacion', aplicacion.nombre)
                    
                    # codigo para el Titulo del form
                    stra = 'Dash Board de ' + modelo.nombre + '\n'
                    strModeloInserta = strModeloInserta.replace('@tituloinserta', '\t\t\t\t' + stra)

                    #titulo pagina
                    strcss = AsignaFonts(modelo.fonttituloinserta,'tituloinserta',strcss)
                    strcss = strcss.replace('@colortituloinserta', modelo.colortituloinserta)
                    strcss = NumeroPorcentaje('@altofilatituloinserta', modelo.altofilatituloinserta,strcss)
                    # strcss = strcss.replace('@altofilatituloinserta', str(modelo.altofilatituloinserta))
                    strcss = strcss.replace('@colorfondofilatituloinserta', modelo.colorfondofilatituloinserta)
                    strcss = strcss.replace('@colorfondotituloinserta', modelo.colorfondotituloinserta)

                    # Justificacion titulo inserta
                    strModeloInserta = AsignaJustificacion('h', modelo.justificacionhorizontaltituloinserta,'@justificacionhorizontaltituloinserta',strModeloInserta)
                    strModeloInserta = AsignaJustificacion('v', modelo.justificacionverticaltituloinserta,'@justificacionverticaltituloinserta',strModeloInserta)

                    # #comentario pagina
                    # strcss = AsignaFonts(modelo.fontcomentarioinserta,'comentarioinserta',strcss)
                    # strcss = strcss.replace('@colorcomentarioinserta', modelo.colorcomentarioinserta)
                    # strcss = strcss.replace('@colorfondocomentarioinserta', modelo.colorfondocomentarioinserta)
                    # strcss = strcss.replace('@colorlabel' + modelo.nombre, modelo.colorlabelmodelo)
                    # strModeloInserta = strModeloInserta.replace('@comentarioinserta', '\t\t\t\t\t' + modelo.comentarioinserta)

                    # columnas que organizan el cuerpo en insercion
                    strModeloInserta = strModeloInserta.replace('@numerocolumnasizquierdainserta', str(modelo.numerocolumnasizquierdainserta))
                    strModeloInserta = strModeloInserta.replace('@numerocolumnasmodeloinserta', str(modelo.numerocolumnasmodeloinserta))
                    strModeloInserta = strModeloInserta.replace('@numerocolumnasderechainserta', str(modelo.numerocolumnasderechainserta))

                    texto = EtiquetasDash(modelo,strModeloInserta,strcss,'\t\t\t',directorio,nombre,etapa,usuario)
                    strModeloInserta =  texto[0]
                    strcss = texto[1]

                    strcssTotal += strcss

                    # strModeloInserta = EscribePersonalizacion(proyecto,aplicacion,modelo.nombre + '_form.html',strModeloInserta)

                    #Sin lineas de personalizacion
                    if not proyecto.conetiquetaspersonalizacion:
                        strModeloInserta = QuitaLineasPersonalizacion(strModeloInserta)

                    # Graba el archivo
                    ProcesoPersonalizacion(proyecto,aplicacion.nombre,modelo.nombre + "_fill.html",directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/",strModeloInserta,nombre,etapa,usuario)
                    # rutinas.EscribirArchivo(directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre + "/" + modelo.nombre + "_dash.html" ,etapa,nombre, strModeloInserta,True)

    return strcssTotal

def CrearModelosForeign(proyecto, etapa,nombre,usuario, directorio, dt):

    # Manejo de los templates de los modelos hijos que son foreign en otros modelos select
    # strHtml = TextFiles.objects.get(file = "load_hijo.html").texto
    strHtml = LeerArchivoEnTexto(dt + "load_hijo.html",etapa,nombre,usuario)
    # strAjax = TextFiles.objects.get(file = "ajax_load_hijo.html").texto
    strAjax = LeerArchivoEnTexto(dt + "ajax_load_hijo.html",etapa,nombre,usuario)
    strData = " data-@modelos-url=" + '"' + "{% url '@aplicacion:ajax_load_@modelos' %}" + '"'
    strTemplate = ''
    for modelo in Modelo.objects.filter(proyecto=proyecto):
        strAjaxForms = ''
        strLoadData = ''
        for propiedad in Propiedad.objects.filter(modelo=modelo):
            if propiedad.tipo == 'f':
                modelo_foraneo = Modelo.objects.get(nombre=propiedad.foranea,proyecto=proyecto)
                if modelo_foraneo.padre !='nada':
                    # Ver si el padre esta en el mismo modelo
                    for modelo_padre in Modelo.objects.filter(proyecto=proyecto):
                        if modelo_padre.nombre == modelo_foraneo.padre:
                            # Existe el modelo padre la llave foranea
                            # Crear el url para la lista de modelos hijo
                            strTemplate = strHtml
                            strTemplate = strTemplate.replace('@modelo',modelo_foraneo.nombre)
                            strTemplate = strTemplate.replace('@padre',modelo_padre.nombre)
                            strTemplate = strTemplate.replace('@aplicacion',modelo.aplicacion.nombre)
                            strTemplate = strTemplate.replace('@propiedad',modelo_foraneo.nombreborrar)
                            EscribirArchivo(directorio + nombre + "/" + modelo.aplicacion.nombre + "/templates/" + modelo.aplicacion.nombre + "/load_" + modelo_foraneo.nombre + '.html',etapa,nombre,strTemplate,usuario,True)
                            strAjaxForms += strAjax
                            strAjaxForms = strAjaxForms.replace('@modelo',modelo.nombre)
                            strAjaxForms = strAjaxForms.replace('@padre',modelo_padre.nombre)
                            strAjaxForms = strAjaxForms.replace('@foraneo',modelo_foraneo.nombre)
                            strLoadData += strData
                            strLoadData = strLoadData.replace('@modelo',modelo_foraneo.nombre)
                            strLoadData = strLoadData.replace('@aplicacion',modelo.aplicacion.nombre)
                            break

        # Leer el html de insercion y update del modelo con llaves foraneas
        strh = LeerArchivoEnTexto(directorio + nombre + '/' + modelo.aplicacion.nombre + '/templates/' + modelo.aplicacion.nombre + '/' + modelo.nombre + '_form' + '.html',etapa,nombre,usuario)
        strh = strh.replace('@ajaxhijo',strAjaxForms)
        strh = strh.replace('@loaddata',strLoadData)
        EscribirArchivo(directorio + nombre + "/" + modelo.aplicacion.nombre + "/templates/" + modelo.aplicacion.nombre + "/" + modelo.nombre + '_form.html',etapa,nombre,strh,usuario,True)
        strh = LeerArchivoEnTexto(directorio + nombre + '/' + modelo.aplicacion.nombre + '/templates/' + modelo.aplicacion.nombre + '/' + modelo.nombre + '_update_form' + '.html',etapa,nombre,usuario)
        strh = strh.replace('@ajaxhijo',strAjaxForms)
        strh = strh.replace('@loaddata',strLoadData)
        EscribirArchivo(directorio + nombre + "/" + modelo.aplicacion.nombre + "/templates/" + modelo.aplicacion.nombre + "/" + modelo.nombre + '_update_form.html',etapa,nombre,strh,usuario,True)

def CrearPaginaPrincipal(proyecto,etapa,nombre,usuario, dt, dc, directorio, directoriogenesis):

    stri = LeerArchivoEnTexto(dt + "principal.html",etapa,nombre,usuario)

    strPrin = ''
    strCss = ''
    for seccion in secpr.objects.filter(proyecto=proyecto):
        ns = seccion.nombre.replace(' ','_')
        strCss += '.' + ns + '{' + '\n'
        strCss += '/*#@[p_seccion_css_' + ns + '_01]*/' + '\n'
        strCss += 'width:100%;' + '\n'
        strCss += 'height:' + str(seccion.altura) + ';' + '\n'
        strCss += 'background: linear-gradient(to ' + seccion.degradado + ', ' + seccion.color1 + ', ' + seccion.color2 + ');' + '\n'
        if seccion.borde:
            strCss += 'border:  1pt solid white;' + '\n'
        else:
            strCss += 'border: none;' + '\n'
        strCss += '/*#@[p_seccion_css_' + ns + '_02]*/' + '\n'
        strCss += '}' + '\n'
        strPrin += "<div class='container-fluid " + seccion.nombre + "'>\n"
        strPrin += '<!-- #@[p_seccion_' + ns + '_01] -->' + '\n'

        for fila in filapr.objects.filter(seccion=seccion):
            nf = fila.nombre.replace(' ','_')
            strCss += '.' + fila.nombre + '{' + '\n'
            strCss += '/*#@[p_fila_css_' + nf + '_01]*/' + '\n'
            strCss += 'height: ' + str(fila.altura) + ';' + '\n'
            strCss += 'background: linear-gradient(to ' + fila.degradado + ', ' + fila.color1 + ', ' + fila.color2 + ');' + '\n'
            if fila.borde:
                strCss += 'border:  1pt solid black;' + '\n'
            else:
                strCss += 'border: none;' + '\n'
            strCss += '/*#@[p_fila_css_' + nf + '_02]*/' + '\n'
            strCss += '}' + '\n'
            strPrin += "\t<div class='row mt-@secciones" + fila.nombre + "'>" + "\n"
            strPrin = strPrin.replace('@secciones',str(proyecto.separacionsecciones))
            strPrin += '<!-- #@[p_fila_' + nf + '_01] -->' + '\n'
            nc = 0
            for columna in colpr.objects.filter(fila=fila):
                nc = columna.nombre.replace(' ','_')
                strCss += '.' + columna.nombre + '{' + '\n'
                strCss += '/*#@[p_columna_css_' + nc + '_01]*/' + '\n'
                strCss += 'background: linear-gradient(to ' + columna.degradado + ', ' + columna.color1 + ', ' + columna.color2 + ');' + '\n'
                if columna.borde:
                    strCss += "border:  1pt solid black;'" + '\n'
                else:
                    strCss += "border: none;" + '\n'
                strCss += 'display: flex;' + '\n'
                strCss += "justify-content: " + columna.justificacionhorizontaltexto + ";" + '\n'
                strCss += "align-items: " + columna.justificacionverticaltexto + ";" + '\n'
                strCss += '/*#@[p_columna_css_' + nc + '_02]*/' + '\n'
                try:
                    strCss += 'margin-top:' + columna.margeninterno.split(',')[0] + ';' + '\n'
                    strCss += 'margin-right:' + columna.margeninterno.split(',')[1] + ';' + '\n'
                    strCss += 'margin-bottom:' + columna.margeninterno.split(',')[2] + ';' + '\n'
                    strCss += 'margin-left:' + columna.margeninterno.split(',')[3] + ';' + '\n'
                except:
                    strCss += 'margin: 0px;' + '\n'
                strCss += '}' + '\n'
                if columna.imagen:
                    strCss += '.' + columna.nombre + ' img{' + '\n'
                    strCss += '/*#@[p_columna_css_imagen_' + nc + '_01]*/' + '\n'
                    strCss += 'max-width:' + columna.dimensionesimagen.split(',')[0] + ';' + '\n'
                    strCss += 'max-height:' + columna.dimensionesimagen.split(',')[1] + ';' + '\n'
                
                    strCss += '/*#@[p_columna_css_imagen_' + nc + '_02]*/' + '\n'
                    strCss += '}' + '\n'

                ft = columna.fonttexto.split(',')
                strCss += '.' + columna.nombre + ' span{' + '\n'
                strCss += '/*#@[p_columna_css_' + nc + '_03]*/' + '\n'
                strCss += 'font-size:' + ft[1] + 'pt;' + '\n'
                strCss += 'font-family:' + ft[0] + ';' + '\n'
                strCss += 'font-weight:' + ft[2] + ';' + '\n'
                strCss += 'color:' + columna.colortexto + '\n'
                strCss += '/*#@[p_columna_css_' + nc + '_04]*/' + '\n'
                strCss += '}' + '\n'

                strPrin += "\t\t<div  class='col-" + str(columna.secciones) + " " + columna.nombre + "'>" + '\n'
                strPrin += '<!-- #@[p_columna_' + nc + '_01] -->' + '\n'

                if columna.imagen:
                    # recuperar el nombre del archivo de imagen
                    nombre_imagen = os.path.basename(columna.imagen.url)
                    # copiar imagen a directorio core
                    CopiaImagenes(directorio + nombre + "/core/static/core/img/" + nombre_imagen , 'proyectos', columna.imagen.url,directoriogenesis + 'media/main/',nombre,etapa,usuario,True )
                    if columna.ingresosistema:
                        strPrin += '<!-- #@[p_columna_imagen_' + nc + '_01] -->' + '\n'
                        strPrin += "\t\t\t<a href='{% url 'core:home' %}''><img id='imagen_principal_" + str(nc) + "' alt=" + dc + dc + " src=" + dc + "{% static 'core/img/" + nombre_imagen + "' %}" + dc + "></a>" + "\n"
                        strPrin += '<!-- #@[p_columna_imagen_' + nc + '_02] -->' + '\n'
                    else:
                        strPrin += '<!-- #@[p_columna_imagen_' + nc + '_01] -->' + '\n'
                        strPrin += "\t\t\t<img id='imagen_principal_" + str(nc) + "' alt=" + dc + dc + " src=" + dc + "{% static 'core/img/" + nombre_imagen + "' %}" + dc + ">" + "\n"
                else:
                    ft = columna.fonttexto.split(',')
                    if columna.ingresosistema:
                        strPrin += '<!-- #@[p_columna_ingreso_' + nc + '_01] -->' + '\n'
                        strPrin += "\t\t\t<a href='{% url " + '"' + 'core:home' + '"' + " %}'><span>" + columna.textocolumna + "</span></a>\n"
                        strPrin += '<!-- #@[p_columna_ingreso_' + nc + '_02] -->' + '\n'
                    else:
                        strPrin += '<!-- #@[p_columna_ingreso_' + nc + '_01] -->' + '\n'
                        strPrin += "\t\t\t<span>" + columna.textocolumna + "</span>\n"
                        strPrin += '<!-- #@[p_columna_ingreso_' + nc + '_02] -->' + '\n'
                strPrin += '<!-- #@[p_columna_' + nc + '_02] -->' + '\n'
                strPrin += "\t\t</div>\n"
                strPrin += '<!-- #@[p_columna_' + nc + '_01] -->' + '\n'
            strPrin += "\t</div>\n"
            strPrin += '<!-- #@[p_fila_' + nf + '_02] -->' + '\n'
        strPrin += "</div>\n"
        strPrin += '<!-- #@[p_seccion_' + ns + '_02] -->' + '\n'

    stri = stri.replace('@css',strCss)    
    stri = stri.replace('@principal',strPrin)    

    return stri

def CrearJsPropios(proyecto,nombre,usuario,etapa,directorio, dt):

# Crear los archivos js

    # leer el archivo js
    # strjs = TextFiles.objects.get(file = "js_propios.js").texto
    strjs = LeerArchivo(dt + "js_propios.js",etapa,nombre,usuario)
    # variable para el manejo de los js
    strfjs = ''

    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto).order_by('ordengeneracion'):

        for modelo in Modelo.objects.filter(aplicacion=aplicacion).order_by('ordengeneracion'):

            # actualiza el archivo js

            if modelo.buscadorlista:
                if modelo.padre == 'nada':
                    strfjs +=  '// Funcion que se ejecuta cuando se acciona el boton' + '\n'
                    strfjs +=  '// de busqueda en el html del modelo @modelo' + '\n'
                    strfjs +=  '// #@[p_js_busqueda_@modelo_01] //' + '\n'
                    strfjs += '$(function(){' + '\n'
                    strfjs +=  '// #@[p_js_busqueda_@modelo_02] //' + '\n'
                    strfjs += '\tvar enlace = $(' + "'" + '#link_busqueda_@modelo' + "'" + ');' + '\n'
                    strfjs +=  '// #@[p_js_busqueda_@modelo_03] //' + '\n'
                    strfjs += '\tenlace.on(' + "'" + 'click' + "'" + ',function(){' + '\n'
                    strfjs +=  '// #@[p_js_busqueda_@modelo_04] //' + '\n'
                    strfjs += '\tvar texto = $(' + "'" + '#textob@modelo' + "'" + ');' + '\n'
                    strfjs +=  '// #@[p_js_busqueda_@modelo_05] //' + '\n'
                    strfjs += '\tenlace.attr(' + "'" + 'href' + "'" + ',' + "'" + 'http://127.0.0.1:8001/@aplicacion/listar_@modelo?duplica=0&criterio=' + "'" + ' + ' + 'texto.val());' + '\n'
                    strfjs +=  '// #@[p_js_busqueda_@modelo_06] //' + '\n'
                    strfjs += '});' + '\n'
                    strfjs +=  '// #@[p_js_busqueda_@modelo_07] //' + '\n'
                    strfjs += '}())' + '\n'
                    strfjs +=  '// #@[p_js_busqueda_@modelo_08] //' + '\n'

                    strfjs = strfjs.replace('@modelo', modelo.nombre)
                    strfjs = strfjs.replace('@aplicacion', aplicacion.nombre)

    # actualiza el archivo js
    strjs = strjs.replace('@busqueda', strfjs)
    EscribirArchivo(directorio +"/" + nombre + "/core/static/core/js/js_propios.js",etapa,nombre,strjs,usuario,True)

def CrearBaseHtmlModelo(proyecto,directorio,etapa,nombre,usuario,directoriogenesis,dt,dc,appCore):
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
        for modelo in Modelo.objects.filter(aplicacion=aplicacion):
            # if secm.objects.filter(modelo=modelo).count() == 0:
            #     CrearBaseProyectoEstandar(proyecto, modelo)
            striP = LeerArchivoEnTexto(dt + "baseProyecto.html",etapa,nombre,usuario)
            # striP = CssBaseGeneral(proyecto,striP,directorio,nombre,directoriogenesis,etapa,usuario)
            striP = CrearBaseHtml(modelo,proyecto, striP, dc,directorio,directoriogenesis,nombre,etapa,usuario,'modelo')
            ProcesoPersonalizacion(proyecto,appCore.nombre,'base' + modelo.nombre + '.html',directorio + nombre + "/core/templates/core/",striP,nombre,etapa,usuario)

def DesplegarArbol(cambia, proyectoid,request):
    try:
        if not str(proyectoid) in request.session:
            request.session[str(proyectoid)] = True
        else:
            request.session[str(proyectoid)] = cambia
        despliega = DespliegaArbol.objects.get(proyecto = proyectoid)
    except:
        request.session[str(proyectoid)] = True
        despliega = DespliegaArbol()
        despliega.proyecto = proyectoid
    despliega.cambia = cambia
    despliega.save()

def CreaListaDespliegaArbol(proyectoid,request):
    try:
        return request.session[str(proyectoid)]
        # return DespliegaArbol.objects.filter(proyecto = proyectoid)[0].cambia
    except:
        return True
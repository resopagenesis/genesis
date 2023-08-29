from seguridad.models import rol, modelo_rol, propiedad_rol, usuariorol, rolusuario

# Definir si una propiedad puede asignar, listar, editar o borrar una propiedad
def Puede(propiedad,usuario,accion):
    # Encontrar todos los roles para la propiedad
    propis = propiedad_rol.objects.select_related('modelo_rol', 'modelo_rol__rol').filter(nombre=propiedad).values('nombre','puedever','puedeasignarvalor','puedeeditar','modelo_rol__rol')
    # Encontrar los roles a los que el usuario esta asociado
    roles_usuarios = rolusuario.objects.select_related('usuariorol').filter(usuariorol__usuario = usuario).values('rol')
    puede = True
    for fila in propis:
        for role in roles_usuarios:
            if fila['modelo_rol__rol'] == role['rol']:
                puede = puede and fila[accion]
    return puede


# Definir si un usuario puede asignar valor a una propiedad de un modelo
def PuedeAsignar(propiedad,usuario):
    # Encontrar todos los roles para la propiedad
    roles_propiedades = propiedad_rol.objects.filter(nombre=propiedad,puedeasignarvalor=True).select_related('modelo_rol').all()
    # Encontrar todos los roles para el usuario
    roles_usuarios = rolusuario.objects.all().select_related('usuariorol').filter(usuariorol__usuario = usuario)

    puede = False
    for i in roles_propiedades:
        for j in roles_usuarios:
            if i.modelo_rol.rol == j.rol:
                puede = True
                break
        if puede:
            break
    return puede

# Definir si un usuario puede ver una propiedad de un modelo
def PuedeVerPropiedad(propiedad,usuario):
    # Encontrar todos los roles para la propiedad
    roles_propiedades = propiedad_rol.objects.filter(nombre=propiedad,puedever=True).select_related('modelo_rol').all()
    # Encontrar todos los roles para el usuario
    roles_usuarios = rolusuario.objects.all().select_related('usuariorol').filter(usuariorol__usuario = usuario)

    puede = False
    for i in roles_propiedades:
        for j in roles_usuarios:
            if i.modelo_rol.rol == j.rol:
                puede = True
                break
        if puede:
            break
    return puede

# Definir si un usuario puede ver una propiedad de un modelo
def PuedeEditarPropiedad(propiedad,usuario):
    # Encontrar todos los roles para la propiedad
    roles_propiedades = propiedad_rol.objects.filter(nombre=propiedad,puedeeditar=True).select_related('modelo_rol').all()
    # Encontrar todos los roles para el usuario
    roles_usuarios = rolusuario.objects.all().select_related('usuariorol').filter(usuariorol__usuario = usuario)

    puede = False
    for i in roles_propiedades:
        for j in roles_usuarios:
            if i.modelo_rol.rol == j.rol:
                puede = True
                break
        if puede:
            break
    return puede

def PuedeModelo(modelo,usuario,accion):
    # Encontrar todos los roles para el modelo
    modelis = modelo_rol.objects.select_related('rol').filter(nombre=modelo).values('nombre','puedelistar','puedeinsertar','puedeeditar','puedeborrar','rol')
    # Encontrar los roles a los que el usuario esta asociado
    roles_usuarios = rolusuario.objects.select_related('usuariorol').filter(usuariorol__usuario = usuario).values('rol')
    puede = True
    for fila in modelis:
        for role in roles_usuarios:
            if fila['rol'] == role['rol']:
                puede = puede and fila[accion]
    return puede

# Definir si un usuario puede listar los registros de un modelo raiz
def PuedeListar(modelo,usuario):
    # Encontrar los roles para el modelo
    roles_modelos = modelo_rol.objects.filter(nombre=modelo,puedelistar=True).select_related('rol').all()
    # Encontrar los roles para el usuario
    roles_usuarios = rolusuario.objects.all().select_related('usuariorol').filter(usuariorol__usuario = usuario)

    puede = False
    for i in roles_modelos:
        for j in roles_usuarios:
            if i.rol == j.rol:
                puede = True
                break
        if puede:
            break
    return puede

# Definir si un usuario puede insertar registros de un modelo
def PuedeInsertar(modelo,usuario):
    # Encontrar los roles para el modelo
    roles_modelos = modelo_rol.objects.filter(nombre=modelo,puedeinsertar=True).select_related('rol').all()
    # Encontrar los roles para el usuario
    roles_usuarios = rolusuario.objects.all().select_related('usuariorol').filter(usuariorol__usuario = usuario)

    puede = False
    for i in roles_modelos:
        for j in roles_usuarios:
            if i.rol == j.rol:
                puede = True
                break
        if puede:
            break
    return puede

# Definir si un usuario puede editar registros de un modelo
def PuedeEditar(modelo,usuario):
    # Encontrar los roles para el modelo
    roles_modelos = modelo_rol.objects.filter(nombre=modelo,puedeeditar=True).select_related('rol').all()
    # Encontrar los roles para el usuario
    roles_usuarios = rolusuario.objects.all().select_related('usuariorol').filter(usuariorol__usuario = usuario)

    puede = False
    for i in roles_modelos:
        for j in roles_usuarios:
            if i.rol == j.rol:
                puede = True
                break
        if puede:
            break
    return puede

# Definir si un usuario puede borrar registros de un modelo
def PuedeBorrar(modelo,usuario):
    # Encontrar los roles para el modelo
    roles_modelos = modelo_rol.objects.filter(nombre=modelo,puedeborrar=True).select_related('rol').all()
    # Encontrar los roles para el usuario
    roles_usuarios = rolusuario.objects.all().select_related('usuariorol').filter(usuariorol__usuario = usuario)

    puede = False
    for i in roles_modelos:
        for j in roles_usuarios:
            if i.rol == j.rol:
                puede = True
                break
        if puede:
            break
    return puede

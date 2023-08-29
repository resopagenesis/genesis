import sqlite3

conexion=sqlite3.connect("db.sqlite3")
cursor=conexion.execute("select proyectos_proyecto.nombre, "\
                        "proyectos_proyecto.id, "\
                        "modelos_modelo.nombre, modelos_modelo.id, "\
                        "propiedades_propiedad.id, propiedades_propiedad.nombre, "\
                        "reglas_regla.mensaje "
                        "from proyectos_proyecto "\
                        "inner join modelos_modelo "\
                        " on proyectos_proyecto.id = modelos_modelo.proyecto_id "\

                        "inner join propiedades_propiedad "\
                        "on modelos_modelo.id = propiedades_propiedad.modelo_id "\
                        "inner join reglas_regla "\
                        "on propiedades_propiedad.id = reglas_regla.propiedad_id"
                        )
                        
for fila in cursor:
    print(fila)
conexion.close()
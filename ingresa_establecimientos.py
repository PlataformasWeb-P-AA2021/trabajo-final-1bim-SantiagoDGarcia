# Se importa el contenido de "ingresa_datos.py" para reciclar código
from ingresa_datos import *
var = 0
# Se realiza una consulta en el cual se desea obtener especificamente la
# información de el nombre de la provincia y su id dentro de la base de datos
llaves = session.query(Parroquia).all()
# Iteramos la informacion tratada para poder añadir a la base de datos
for x in data:
    # Se itera para comparar el nombre de las parroquias obtenidos en la 
    # consulta(llaves) con el nombre de parroquias que se encuentra en la lista
    # data, ademas de comparar su id, si son iguales , se introduce el id de esa
    # parroquia(i.id) en la creación del Establecimiento
    for i in llaves:
        if x[7] == i.nombre and int(x[6]) == i.id:
            session.add(Establecimiento(id=x[0], nombre=x[1], id_parroquia=i.id, \
                tipo_educacion=x[10], codigo_distrito=x[8] ,sostenimiento=x[9] ,\
                modalidad=x[11], jornada=x[12], acceso=x[13], cantidad_estudiantes=x[14],\
                cantidad_docentes=limpia[var]) )
    var+=1

session.commit()
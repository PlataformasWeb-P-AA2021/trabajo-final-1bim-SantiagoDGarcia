from ingresa_datos import *

var = 0
llaves = session.query(Parroquia).all()
for x in data:
    # Se itera para comparar el nombre de la consulta y determinar el id del club al que pertenece el jugador
    for i in llaves:
        if x[7] == i.nombre and int(x[6]) == i.id:
            session.add(Establecimiento(id=x[0], nombre=x[1], id_parroquia=i.id, tipo_educacion=x[10], codigo_distrito=x[8] ,sostenimiento=x[9] ,modalidad=x[11], jornada=x[12], acceso=x[13], cantidad_estudiantes=x[14], cantidad_docentes=limpia[var]) )
    var+=1

session.commit()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Establecimiento, Provincia, Canton, Parroquia
from sqlalchemy import and_, or_
# Se crea el motor donde desde donde se gestionara la base de datos
engine = create_engine('sqlite:///base.db' )
# Se crea una variable donde se creará la sesión, se selecciona el motor(engine)
Session = sessionmaker(bind=engine)
# Se crea la sesión con la variable anterior declarada
session = Session()
# Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
consulta = session.query(Parroquia).join(Establecimiento)\
    .filter(Establecimiento.jornada == "Nocturna").all()
for x in consulta: 
    print(x)
print("\n__________________________________________________________________________\n")
# Los cantones que tiene establecimientos como número de estudiantes tales como:
# 448, 450, 451, 454, 458, 459
consulta = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(\
    Establecimiento.cantidad_estudiantes == 448, \
    Establecimiento.cantidad_estudiantes == 450, \
    Establecimiento.cantidad_estudiantes == 451, \
    Establecimiento.cantidad_estudiantes == 454, \
    Establecimiento.cantidad_estudiantes == 458, \
    Establecimiento.cantidad_estudiantes == 459)).all()
for x in consulta: 
    print(x)
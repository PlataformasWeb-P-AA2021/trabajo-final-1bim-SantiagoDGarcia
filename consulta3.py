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
# Los cantones que tiene establecimientos con 0 número de profesores
consulta = session.query(Canton).join(Parroquia, Establecimiento)\
    .filter(Establecimiento.cantidad_docentes == 0).all()
for x in consulta: 
    print(x)
print("\n__________________________________________________________________________\n")
# Los establecimientos de la parroquia Catacocha con estudiantes mayores o iguales a 21
consulta = session.query(Establecimiento).join(Parroquia).filter(and_\
    (Parroquia.nombre == "CATACOCHA", Establecimiento.cantidad_estudiantes >= 21 )).all()
for x in consulta: 
    print(x)
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
# Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores 
# y la cadena "Permanente" en tipo de educación
consulta = session.query(Establecimiento).join(Parroquia).filter(and_(
    Establecimiento.cantidad_docentes > 20,\
    Establecimiento.tipo_educacion.like("%Permanente%")))\
    .order_by(Parroquia.nombre).all()
for x in consulta: 
    print(x)
print("\n__________________________________________________________________________\n")
# Todos los establecimientos ordenados por sostenimiento y tengan Sdistrito 11D02
consulta = session.query(Establecimiento).\
    filter(Establecimiento.codigo_distrito == "11D02")\
    .order_by(Establecimiento.sostenimiento).all()
for x in consulta: 
    print(x)
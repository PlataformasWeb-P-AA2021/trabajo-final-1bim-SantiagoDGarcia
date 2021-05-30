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
# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores
consulta = session.query(Establecimiento)\
    .filter(Establecimiento.cantidad_docentes > 100 )\
    .order_by(Establecimiento.cantidad_estudiantes).all()
for x in consulta: 
    print(x)
# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores
print("\n__________________________________________________________________________\n")
consulta = session.query(Establecimiento)\
    .filter(Establecimiento.cantidad_docentes > 100 )\
    .order_by(Establecimiento.cantidad_docentes).all()
for x in consulta: 
    print(x)
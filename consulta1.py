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
# Todos los establecimientos de la provincia de Loja.
consulta = session.query(Establecimiento).join(Parroquia, Canton, Provincia)\
    .filter(Provincia.nombre == "LOJA").all()
for x in consulta: 
    print(x)
print("\n__________________________________________________________________________\n")
# Todos los establecimientos del cantón de Loja.
consulta = session.query(Establecimiento).join(Parroquia, Canton, Provincia)\
    .filter(Canton.nombre == "LOJA").all()
for x in consulta: 
    print(x)
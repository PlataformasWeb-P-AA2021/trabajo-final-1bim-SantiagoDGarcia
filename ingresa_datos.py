from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Establecimiento, Provincia, Canton, Parroquia
import numpy as np
# Se crea el motor donde desde donde se gestionara la base de datos
engine = create_engine('sqlite:///base.db' )
# Se crea una variable donde se creará la sesión, se selecciona el motor o dirrecion (engine)
Session = sessionmaker(bind=engine)
# Se crea la sesión con la variable anterior declarada
session = Session()
# Importación de datos mediante el archivo .csv en variable archivo
archivo = open("data/Listado-Instituciones-Educativas.csv", "r", encoding='utf-8')
# Función anónima para separar mediante pipe la variable archivo
data = list(map(lambda x: x.split("|"), archivo))
# Función anónima para filtrar la variable data y eliminar el encabezado
data = list(filter(lambda x: x[0]!= "Código AMIE", data))
# Función anónima para escoger la ultima posición de data y remplazar el salto de linea
limpia = list(map(lambda x: x[len(x)-1].replace("\n", ""), data))
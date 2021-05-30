# Se importa el contenido de "ingresa_datos.py" para reciclar código
from ingresa_datos import *
# Se guarda en un arreglo bidimensional el código provincia(2) y su nombre (3)
lista = [ [x[2], x[3]] for x in data ]
# Se busca los arreglos unicos mediante el uso de numpy(np) y se asignan en una variable
provincias = np.unique(lista, axis=0)
# Iteramos la lista (provincias) y mediante la variable de sesion que se 
# encuentra en "ingresa_datos" se añade un objeto Provincia con sus propiedades
for x in provincias:
        session.add(Provincia(id=x[0], nombre=x[1]) )
# Finalmente se confirman los cambios mediante el uso de la función commit
session.commit()
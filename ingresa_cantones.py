# Se importa el contenido de "ingresa_datos.py" para reciclar código
from ingresa_datos import *
# Se guarda en un arreglo bidimensional el código canton(4), su nombre(5) y el nombre de la provincia
lista = [ [x[4], x[5], x[3]] for x in data ]
# Se busca los arreglos unicos mediante el uso de numpy(np) y se asignan en una variable
cantones = np.unique(lista, axis=0)
# Se realiza una consulta con el fin de obtener la información de provincias y su PK
# y poder relacionarna como FK dentro de Canton
llaves = session.query(Provincia).all()
# Iteramos la lista (cantones) y obtener la información de cada uno de ellos 
for x in cantones:
        # Se itera para comparar el nombre de las provincias obtenidos en la 
        # consulta(llaves) con el nombre de provincia que se encuentra en la lista
        # cantones, si son iguales , se introduce el id de esa provincia(i.id) en la 
        # creacion del canton
        for i in llaves:
            if x[2] == i.nombre:
                session.add(Canton(id=x[0], nombre=x[1], id_provincia=i.id ) )
# Finalmente se confirman los cambios mediante el uso de la función commit
session.commit()
# Se importa el contenido de "ingresa_datos.py" para reciclar código
from ingresa_datos import *
# Se guarda en un arreglo bidimensional el código parroquia(4), su nombre(5) y el nombre del canton
lista = [ [x[6], x[7], x[5]] for x in data ]
# Se busca los arreglos unicos mediante el uso de numpy(np) y se asignan en una variable
parroquias = np.unique(lista, axis=0)
# Se realiza una consulta con el fin de obtener la información de cantones y su PK
# y poder relacionarna como FK dentro de la parroquia
llaves = session.query(Canton).all()
# Iteramos la lista (parroquias) y obtener la información de cada una de ellas 
for x in parroquias:
        # Se itera para comparar el nombre de los cantones obtenidos en la 
        # consulta(llaves) con el nombre de cantones que se encuentra en la lista
        # parroquias, si son iguales , se introduce el id de ese canton(i.id) en la 
        # creacion de la Parroquia
        for i in llaves:
            if x[2] == i.nombre:
                session.add(Parroquia(id=x[0], nombre=x[1], id_canton=i.id ) )
# Finalmente se confirman los cambios mediante el uso de la función commit
session.commit()
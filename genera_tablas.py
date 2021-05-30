from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
# Se crea el motor donde desde donde se gestionara la base de datos
engine = create_engine('sqlite:///base.db')
# Se declara la variable Base como un objeto de sqlalchemy
Base = declarative_base()

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(String(15), primary_key=True)
    nombre = Column(String(65), nullable=False)
    id_parroquia = Column(Integer, ForeignKey('parroquia.id'))
    tipo_educacion = Column(String(50), nullable=False)
    codigo_distrito = Column(String(50), nullable=False)
    sostenimiento = Column(String(50), nullable=False)
    modalidad = Column(String(50), nullable=False)
    jornada = Column(String(50), nullable=False)
    acceso = Column(String(50), nullable=False)
    cantidad_estudiantes = Column(Integer, nullable=False)
    cantidad_docentes = Column(Integer, nullable=False)
    # Relación con la tabla parroquia
    relacion_parroquia = relationship("Parroquia",back_populates="relacion_establecimiento")
    # Método de representacion de la tabla
    def __repr__(self):
        return "|| Nombre:%s || tipo:%s || distrito:%s || sosten:%s || modalidad:%s || jornada:%s || estudiantes:%s || docentes:%s"% (
                          self.nombre, 
                          self.tipo_educacion,
                          self.codigo_distrito,
                          self.sostenimiento,
                          self.modalidad,
                          self.jornada,
                          self.cantidad_estudiantes,
                          self.cantidad_docentes)
class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    # Relación con la tabla canton
    relacion_canton = relationship("Canton",back_populates="relacion_provincia")
    # Método de representacion de la tabla
    def __repr__(self):
        return "ID:%s || Nombre:%s"% (
                          self.id, 
                          self.nombre)
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    id_provincia = Column(Integer, ForeignKey('provincia.id'))
    # Relación con la tabla parroquia
    relacion_parroquia = relationship("Parroquia", back_populates="relacion_canton")
    # Relación con la tabla provincia
    relacion_provincia = relationship("Provincia", back_populates="relacion_canton")
    # Método de representacion de la tabla
    def __repr__(self):
        return "ID:%s || Nombre:%s"% (
                          self.id, 
                          self.nombre)
class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    id_canton = Column(Integer, ForeignKey('canton.id'))
    # Relación con la tabla establecimiento
    relacion_establecimiento = relationship("Establecimiento", back_populates="relacion_parroquia")
    # Relación con la tabla canton
    relacion_canton = relationship("Canton", back_populates="relacion_parroquia")
    # Método de representacion de la tabla
    def __repr__(self):
        return "ID:%s || Nombre:%s"% (
                          self.id, 
                          self.nombre)

# Se crean las clases mediante el uso de la variable Base
# y seleccionando el motor que declaramos (engine)
Base.metadata.create_all(engine)

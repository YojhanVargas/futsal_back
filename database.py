from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+pymysql://root@localhost:3306/futsal"  # Asegúrate de que la URL sea correcta


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuario"

    Id_Usuario = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String, nullable=False)
    Apellido = Column(String, nullable=False)
    Correo = Column(String, unique=True, nullable=False)
    Contraseña = Column(String, nullable=False)
    Id_Perfil = Column(Integer, nullable=True)
    Rol = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)
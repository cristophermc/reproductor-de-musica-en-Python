from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from getpass import getpass

from modelos import Base

def crear_tablas():
    try:
        print("Conectando a PostgreSQL...")
        password = getpass("Introduce la contraseña de PostgreSQL >>> ")
        controlador_bd = f"postgresql+psycopg2://usrpostgre:{password}@localhost:5432/conciertos"
        engine = create_engine(controlador_bd)

        Base.metadata.create_all(engine)
        print("Tablas creadas correctamente.")

    except Exception as e:
        print(f"Error al conectar o crear tablas... {e}")

if __name__ == "__main__":
    crear_tablas()

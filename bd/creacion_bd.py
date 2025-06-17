import psycopg2
from psycopg2 import Error
from getpass import getpass

try:
    
    con = psycopg2.connect(
        host="localhost",
        user="postgres",
        password=getpass("Escriba su contraseña por defecto del gestor: "),
        port='5432',
        database="postgres")
    con.autocommit = True
    cursor = con.cursor()

    #################
    # CREACION BBDD #
    #################
    cursor.execute('CREATE DATABASE "conciertos";')
    cursor.execute('GRANT ALL ON DATABASE "conciertos" TO usrpostgre WITH GRANT OPTION;')
    cursor.execute('ALTER DATABASE "conciertos" OWNER TO usrpostgre;')
    print("Base de datos 'conciertos' creada con privilegios para 'usrpostgre'.")
    cursor.close()
    con.close()
except:
    print("Hubo un error al crear la base de datos.")
finally:
    if (con):
        cursor.close()
        con.close()


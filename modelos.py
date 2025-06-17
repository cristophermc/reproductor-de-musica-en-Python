from sqlalchemy import create_engine, String, Date, ForeignKey, Float, UniqueConstraint, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date

class Base(DeclarativeBase):
    pass
class Artista(Base):
    '''establecemos la clase Artista que hará de la tabla artistas en la BD'''
    __tablename__ = 'artistas' 
    id_artista: Mapped[int] = mapped_column(primary_key=True) 
    nombre: Mapped[str] = mapped_column(String(40), nullable=False)
    apellidos: Mapped[str] = mapped_column(String(50), nullable=False)
    nombre_artistico: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    nacionalidad: Mapped[str] = mapped_column(String(40), nullable=False)

    albumes: Mapped[list["Album"]] = relationship(back_populates="artista", cascade="all, delete-orphan")#la relación con album
    club: Mapped["Club_fans"] = relationship(back_populates="artista", uselist=False, cascade="all, delete-orphan")


class Album(Base):
    __tablename__ = "albumes"
    id_album:Mapped[int] = mapped_column(primary_key=True)
    titulo:Mapped[str] = mapped_column(String(40), nullable=False)
    año:Mapped[int] = mapped_column(Integer, nullable=False, autoincrement=False)

    artista_id:Mapped[int] = mapped_column(ForeignKey("artistas.id_artista", ondelete="CASCADE"), nullable=False) #la clave ajena se define
    artista:Mapped["Artista"] = relationship(back_populates="albumes")
    canciones: Mapped[list["Cancion"]] = relationship(back_populates="album", cascade="all, delete-orphan")
class Cancion(Base):
    __tablename__ = "canciones"
    id_cancion:Mapped[int] = mapped_column(primary_key=True)
    titulo:Mapped[str] = mapped_column(String(40), nullable=False)
    duracion:Mapped[float] = mapped_column(Float, nullable=True)
    genero:Mapped[str] = mapped_column(String(40), nullable=False)
    enlace_yt:Mapped[str] = mapped_column(String(100), nullable=False)

    album_id: Mapped[int] = mapped_column(ForeignKey("albumes.id_album", ondelete="CASCADE"), nullable=False)
    album: Mapped["Album"] = relationship(back_populates="canciones")
class Club_fans(Base):
    __tablename__ = "clubs_fans"

    id_club: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_fundacion: Mapped[date] = mapped_column(Date, nullable=True)
    pais: Mapped[str] = mapped_column(String(50), nullable=False)
    descripcion: Mapped[str] = mapped_column(String(255), nullable=True)
    num_fans: Mapped[int] = mapped_column(Integer, nullable=False, autoincrement=False)

    id_artista: Mapped[int] = mapped_column(ForeignKey("artistas.id_artista", ondelete="CASCADE"), unique=True, nullable=False)
    artista: Mapped["Artista"] = relationship(back_populates="club")
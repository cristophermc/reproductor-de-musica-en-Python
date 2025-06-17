from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QWidget, QMessageBox, QMainWindow)
from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
import webbrowser
from modelos import Artista, Album, Cancion
from artistas import Ui_Artista
from album import Ui_Album
from cancion import Ui_Cancion
from fan import Ui_Fans
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 580)
        Form.setMinimumSize(820, 580)
        Form.setMaximumSize(820, 580)
        #--------------------------------- Atributos de la clase utilizados -----------------------------------------#
        self.url_buscada = None #en este atributo almaceno las URL que se buscan mediante consultas en tablas
        #------------------------------------------------------------------------------------------------------------#
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(290, 10, 511, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.rbCanciones = QRadioButton(self.groupBox)
        self.rbCanciones.setObjectName(u"rbCanciones")
        self.rbCanciones.setGeometry(QRect(210, 30, 85, 20))
        self.rbCanciones.toggled.connect(lambda:self.abrirVentanaCanciones(Form))
        self.rbArtistas = QRadioButton(self.groupBox)
        self.rbArtistas.setObjectName(u"rbArtistas")
        self.rbArtistas.setGeometry(QRect(40, 30, 70, 20))
        self.rbArtistas.toggled.connect(lambda:self.abrirVentanaArtista(Form))
        self.rbClub = QRadioButton(self.groupBox)
        self.rbClub.setObjectName(u"rbClub")
        self.rbClub.setGeometry(QRect(310, 30, 98, 20))
        self.rbClub.toggled.connect(lambda:self.abrirVentanaClubFans(Form))

        self.rbAlbumes = QRadioButton(self.groupBox)
        self.rbAlbumes.setObjectName(u"rbAlbumes")
        self.rbAlbumes.setGeometry(QRect(120, 30, 98, 20))
        self.rbAlbumes.toggled.connect(lambda:self.abrirVentanaAlbum(Form))



        self.horizontalLayout.addWidget(self.groupBox)

        self.cbArtista = QComboBox(Form)
        self.cbArtista.setObjectName(u"cbArtista")
        self.cbArtista.setGeometry(QRect(20, 230, 141, 22))
        self.cbArtista.currentTextChanged.connect(self.buscar_albumes_por_artista)
        self.cbCancion = QComboBox(Form)
        self.cbCancion.setObjectName(u"cbCancion")
        self.cbCancion.setGeometry(QRect(400, 230, 141, 22))
        self.lblartista = QLabel(Form)
        self.lblartista.setObjectName(u"lblartista")
        self.lblartista.setGeometry(QRect(20, 190, 141, 16))
        font = QFont()
        font.setPointSize(9)
        self.lblartista.setFont(font)
        self.lblcancion = QLabel(Form)
        self.lblcancion.setObjectName(u"lblcancion")
        self.lblcancion.setGeometry(QRect(400, 190, 151, 16))
        self.lblcancion.setFont(font)
        self.btnPlay = QPushButton(Form)
        self.btnPlay.setObjectName(u"btnPlay")
        self.btnPlay.setGeometry(QRect(640, 230, 93, 28))
        self.btnPlay.clicked.connect(self.reproducir)
        font1 = QFont()
        font1.setBold(True)
        self.btnPlay.setFont(font1)
        self.btnPlay.setStyleSheet(u"border-radius:10px;\n"
            "background-color:coral;\n"
            "color:white;\n"
            "")
        self.lblseparador = QLabel(Form)
        self.lblseparador.setObjectName(u"lblseparador")
        self.lblseparador.setGeometry(QRect(-140, 380, 1041, 241))
        self.lblseparador.setStyleSheet(u"background:lightblue;")
        self.cbAlbum = QComboBox(Form)
        self.cbAlbum.setObjectName(u"cbAlbum")
        self.cbAlbum.setGeometry(QRect(210, 230, 141, 22))
        self.cbAlbum.currentTextChanged.connect(self.buscar_canciones_por_album)

        self.lblalbum = QLabel(Form)
        self.lblalbum.setObjectName(u"lblalbum")
        self.lblalbum.setGeometry(QRect(210, 190, 141, 16))
        self.lblalbum.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.buscar_artistas()
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Men\u00fa de opciones", None))
        self.rbCanciones.setText(QCoreApplication.translate("Form", u"Canciones", None))
        self.rbArtistas.setText(QCoreApplication.translate("Form", u"Artistas", None))
        self.rbClub.setText(QCoreApplication.translate("Form", u"Club de fans", None))
        self.rbAlbumes.setText(QCoreApplication.translate("Form", u"Albumes", None))
        self.lblartista.setText(QCoreApplication.translate("Form", u"Seleccione un artista", None))
        self.lblcancion.setText(QCoreApplication.translate("Form", u"Seleccione una canci\u00f3n", None))
        self.btnPlay.setText(QCoreApplication.translate("Form", u"PLAY", None))
        self.lblseparador.setText("")
        self.lblalbum.setText(QCoreApplication.translate("Form", u"Seleccione un album", None))
    #retranslateUi

    def buscar_artistas(self):
        '''busca en la base de datos por artistas para rellenar el CB de artistas:

        1. busca en la base datos por todos los artistas registrados (nombres artisticos simplemente)
        2. todos los registros se colocan en el combobox mediante bucle for
        funcional - check
        '''
        try:
            controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
            engine = create_engine(controlador_bd) # , echo=True)
        except:
            print('Se ha cometido un error al crear engine')
        else:
            Session = sessionmaker(engine)        
            consulta = select(Artista.nombre_artistico)
            try:
                with Session() as session:
                    with session.begin():
                        resultados = session.execute(consulta).scalars().all()  #usamos .scalars() para extraer solo los valores
                        if resultados:
                            self.cbArtista.clear() #se hace al recargar ventana, justo cuando la ventana empieza
                            for nombre in resultados:
                                self.cbArtista.addItem(nombre)
                        else:
                            print('No se han encontrado artistas')
            except Exception as e:
                print(f'Error al consultar: {e}')
    def buscar_albumes_por_artista(self):
        '''busca en la base de datos por artistas seleccionados para rellenar el CB de albumes:

        1. busca en la base datos por el artista que está seleccionado en el combobox por el usuario y extrae su id
        2. y luego lo que va a hacer es iterar con un bucle for para colocar las opciones de los albumes en el combobox disponibles para el artista'''

        try:
            controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
            engine = create_engine(controlador_bd)
        except Exception as e:
            print(f'Error al crear engine: {e}')
            return

        #paso 1: Obtener nombre artístico seleccionado
        nombre_artistico = self.cbArtista.currentText()

        if not nombre_artistico:
            print("No se ha seleccionado ningún artista.")
            return

        Session = sessionmaker(engine)

        try:
            with Session() as session:
                with session.begin():
                    #paso 2: Obtener el id del artista por nombre artístico
                    consulta_id = select(Artista.id_artista).where(Artista.nombre_artistico == nombre_artistico)
                    id_resultado = session.execute(consulta_id).scalar()

                    if id_resultado is None:
                        print("No se encontró el ID del artista.")
                        return

                    #paso 3: Buscar los álbumes con ese id_artista
                    consulta_albumes = select(Album.titulo).where(Album.artista_id == id_resultado)
                    titulos_albumes = session.execute(consulta_albumes).scalars().all()

                    #paso 4: Rellenar el ComboBox
                    self.cbAlbum.clear()
                    if titulos_albumes:
                        for titulo in titulos_albumes:
                            self.cbAlbum.addItem(titulo)
                    if self.cbAlbum.count() == 0:
                        self.cbCancion.clear()
        except Exception as e:
            print(f"Error al consultar: {e}")

    def buscar_canciones_por_album(self):
        '''busca en la base de datos por album seleccionados para rellenar el CB de canciones:

        1. busca en la base datos por el album que está seleccionado en el combobox por el usuario 
        2. todos los registros de albumes los va a colocar en una lista improvisada como atributo de la clase de la ventana
        3. y luego lo que va a hacer es iterar con un bucle for para colocar las opciones de las canciones en el combobox disponibles para el album'''
        try:
            controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
            engine = create_engine(controlador_bd)
        except Exception as e:
            print(f'Error al crear engine: {e}')
            return

        #paso 1: Obtener nombre artístico seleccionado
        nombre_album = self.cbAlbum.currentText()

        if not nombre_album:
            return

        Session = sessionmaker(engine)

        try:
            with Session() as session:
                with session.begin():
                    #paso 2: Obtener el id del artista por nombre artístico
                    consulta_id = select(Album.id_album).where(Album.titulo == nombre_album)
                    id_resultado = session.execute(consulta_id).scalar()

                    if id_resultado is None:
                        print("No se encontró el ID del artista.")
                        return

                    #paso 3: Buscar las canciones con ese id_album
                    consulta_canciones = select(Cancion.titulo).where(Cancion.album_id == id_resultado)
                    titulos_canciones = session.execute(consulta_canciones).scalars().all()

                    #paso 4: Rellenar el ComboBox
                    self.cbCancion.clear()
                    if titulos_canciones:
                        for titulo in titulos_canciones:
                            self.cbCancion.addItem(titulo)

        except Exception as e:
            print(f"Error al consultar: {e}")
    def reproducir(self):
        '''reproduce el URL buscado de la base de datos
        
        1. Busca en la BD por la URL de la canción que esté seleccionada en el combobox actual.
        2. Esa URL la traspasa al atributo de la clase de la ventana.
        3. Se reproduce el URL mediante el atributo de la clase de la ventana pasado como parámetro utilizando la funcionalidad de la librería webbrowser'''
        try:
            controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
            engine = create_engine(controlador_bd)
        except Exception as e:
            print(f'Error al crear engine: {e}')
            return

        #paso 1: obtener el URL de la cancion
        nombre_cancion = self.cbCancion.currentText()

        if not nombre_cancion:
            QMessageBox.warning(None,
                         'Canción no seleccionada.',
                         'No hay canción seleccionada. Por favor, seleccione una si es posible.')
            return

        Session = sessionmaker(engine)

        try:
            with Session() as session:
                with session.begin():
                    #paso 2: se obtiene el URL filtrado por nombre
                    consulta_id = select(Cancion.enlace_yt).where(Cancion.titulo == nombre_cancion)
                    self.url_buscada = session.execute(consulta_id).scalar()

                    if self.url_buscada is None:
                        print("No se encontró el enlace a YT.")
                        return
                    #paso 3: ejecutar el enlace:
                    webbrowser.open(self.url_buscada)
        except Exception as e:
            print(f"Error al consultar: {e}")

#Funciones de traspaso a otras ventanas

    def abrirVentanaArtista(self, mainWindow):
        self.ventArtista = QMainWindow() # Creamos ventana contenedora
        self.ui2 = Ui_Artista() # Creamos ventana del tipo artista
        self.ui2.setupUi(self.ventArtista) # enlazamos con contenedor principal
        self.ventArtista.show() # mostramos la ventana
        mainWindow.close()
    def abrirVentanaAlbum(self,mainWindow):
        self.ventAlbum = QMainWindow() # Creamos ventana contenedora
        self.ui2 = Ui_Album() # Creamos ventana del tipo album
        self.ui2.setupUi(self.ventAlbum) # enlazamos con contenedor principal
        self.ventAlbum.show() # mostramos la ventana
        mainWindow.close()
    def abrirVentanaCanciones(self,mainWindow):
        self.ventCanciones = QMainWindow() # Creamos ventana contenedora
        self.ui2 = Ui_Cancion() # Creamos ventana del tipo canciones
        self.ui2.setupUi(self.ventCanciones) # enlazamos con contenedor principal
        self.ventCanciones.show() # mostramos la ventana
        mainWindow.close()
    def abrirVentanaClubFans(self,mainWindow):
        self.ventFans = QMainWindow() # Creamos ventana contenedora
        self.ui2 = Ui_Fans() # Creamos ventana del tipo club fans
        self.ui2.setupUi(self.ventFans) # enlazamos con contenedor principal
        self.ventFans.show() # mostramos la ventana
        mainWindow.close()


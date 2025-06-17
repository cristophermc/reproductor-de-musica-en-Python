# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cancion.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget, QMainWindow, QMessageBox)
from modelos import Album, Cancion
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine,String, Column, Integer, select, update, delete
class Ui_Cancion(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 580)
        self.modo = None
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(290, 10, 511, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.rbReproductor = QRadioButton(self.groupBox)
        self.rbReproductor.setObjectName(u"rbReproductor")
        self.rbReproductor.setGeometry(QRect(200, 30, 101, 20))
        self.rbReproductor.toggled.connect(lambda:self.abrirVentanaReproductor(Form))

        self.horizontalLayout.addWidget(self.groupBox)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-140, 380, 1041, 241))
        self.label_3.setStyleSheet(u"background:lightblue;")
        self.lnTitulo = QLineEdit(Form)
        self.lnTitulo.setObjectName(u"lnTitulo")
        self.lnTitulo.setGeometry(QRect(110, 140, 191, 22))
        self.lblTitulo = QLabel(Form)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(50, 140, 55, 16))
        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(110, 300, 591, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnAnadir = QPushButton(self.horizontalLayoutWidget_2)
        self.btnAnadir.setObjectName(u"btnAnadir")
        self.btnAnadir.clicked.connect(self.logicaInsertar)

        self.horizontalLayout_2.addWidget(self.btnAnadir)

        self.btnCancelar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.clicked.connect(self.cancelar)

        self.horizontalLayout_2.addWidget(self.btnCancelar)

        self.btnEditar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.clicked.connect(self.logicaModificar)

        self.horizontalLayout_2.addWidget(self.btnEditar)

        self.btnBorrar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnBorrar.setObjectName(u"btnBorrar")
        self.btnBorrar.clicked.connect(self.logicaBorrar)

        self.horizontalLayout_2.addWidget(self.btnBorrar)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 140, 55, 16))
        self.lblDuracion = QLabel(Form)
        self.lblDuracion.setObjectName(u"lblDuracion")
        self.lblDuracion.setGeometry(QRect(340, 140, 55, 16))
        self.lblAlbum = QLabel(Form)
        self.lblAlbum.setObjectName(u"lblAlbum")
        self.lblAlbum.setGeometry(QRect(50, 220, 71, 16))
        self.cbAlbum = QComboBox(Form)
        self.cbAlbum.setObjectName(u"cbAlbum")
        self.cbAlbum.setGeometry(QRect(130, 220, 201, 22))
        self.lblID = QLabel(Form)
        self.lblID.setObjectName(u"lblID")
        self.lblID.setGeometry(QRect(50, 70, 21, 16))
        self.lnID = QLineEdit(Form)
        self.lnID.setObjectName(u"lnID")
        self.lnID.setGeometry(QRect(70, 70, 41, 22))
        self.lnDuracion = QLineEdit(Form)
        self.lnDuracion.setObjectName(u"lnDuracion")
        self.lnDuracion.setGeometry(QRect(400, 140, 61, 22))
        self.lblGenero = QLabel(Form)
        self.lblGenero.setObjectName(u"lblGenero")
        self.lblGenero.setGeometry(QRect(490, 140, 55, 16))
        self.cbGenero = QComboBox(Form)
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.setObjectName(u"cbGenero")
        self.cbGenero.setGeometry(QRect(560, 140, 131, 22))
        self.lblURL = QLabel(Form)
        self.lblURL.setObjectName(u"lblURL")
        self.lblURL.setGeometry(QRect(360, 220, 101, 16))
        self.lnUrl = QLineEdit(Form)
        self.lnUrl.setObjectName(u"lnUrl")
        self.lnUrl.setGeometry(QRect(460, 221, 191, 21))

        self.retranslateUi(Form)
        

        QMetaObject.connectSlotsByName(Form)
        self.lblID.setVisible(False)
        self.lblTitulo.setVisible(False)
        self.lblDuracion.setVisible(False)
        self.lblGenero.setVisible(False)
        self.lblAlbum.setVisible(False)
        self.lblURL.setVisible(False)
        self.lnID.setVisible(False)
        self.lnTitulo.setVisible(False)
        self.lnDuracion.setVisible(False)
        self.cbGenero.setVisible(False)
        self.cbAlbum.setVisible(False)
        self.lnUrl.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.buscarAlbumes()
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Men\u00fa de opciones", None))
        self.rbReproductor.setText(QCoreApplication.translate("Form", u"Reproductor", None))
        self.label_3.setText("")
        self.lblTitulo.setText(QCoreApplication.translate("Form", u"Titulo", None))
        self.btnAnadir.setText(QCoreApplication.translate("Form", u"A\u00f1adir nueva canci\u00f3n", None))
        self.btnCancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btnEditar.setText(QCoreApplication.translate("Form", u"Editar canci\u00f3n", None))
        self.btnBorrar.setText(QCoreApplication.translate("Form", u"Borrar canci\u00f3n", None))
        self.label_2.setText("")
        self.lblDuracion.setText(QCoreApplication.translate("Form", u"Duraci\u00f3n", None))
        self.lblAlbum.setText(QCoreApplication.translate("Form", u"Album", None))
        self.lblID.setText(QCoreApplication.translate("Form", u"ID", None))
        self.lnID.setText("")
        self.lnDuracion.setText("")
        self.lblGenero.setText(QCoreApplication.translate("Form", u"G\u00e9nero", None))
        self.cbGenero.setItemText(0, QCoreApplication.translate("Form", u"rock", None))
        self.cbGenero.setItemText(1, QCoreApplication.translate("Form", u"pop", None))
        self.cbGenero.setItemText(2, QCoreApplication.translate("Form", u"alternativo", None))
        self.cbGenero.setItemText(3, QCoreApplication.translate("Form", u"indie", None))
        self.cbGenero.setItemText(4, QCoreApplication.translate("Form", u"metal", None))
        self.cbGenero.setItemText(5, QCoreApplication.translate("Form", u"kpop", None))
        self.cbGenero.setItemText(6, QCoreApplication.translate("Form", u"nu metal", None))
        self.cbGenero.setItemText(7, QCoreApplication.translate("Form", u"folk", None))
        self.cbGenero.setItemText(8, QCoreApplication.translate("Form", u"country", None))
        self.cbGenero.setItemText(9, QCoreApplication.translate("Form", u"funk", None))
        self.cbGenero.setItemText(10, QCoreApplication.translate("Form", u"techno", None))
        self.cbGenero.setItemText(11, QCoreApplication.translate("Form", u"dubstep", None))
        self.cbGenero.setItemText(12, QCoreApplication.translate("Form", u"poprock", None))
        self.cbGenero.setItemText(13, QCoreApplication.translate("Form", u"hip hop", None))

        self.lblURL.setText(QCoreApplication.translate("Form", u"Enlace Youtube", None))
        self.lnUrl.setPlaceholderText(QCoreApplication.translate("Form", u"pega aqui tu enlace a YouTube", None))
    # retranslateUi
    def abrirVentanaReproductor(self, mainWindow):
            from player import Ui_Form
            self.ventReproductor = QMainWindow() # Creamos ventana contenedora
            self.ui2 = Ui_Form() # Creamos ventana del tipo artista
            self.ui2.setupUi(self.ventReproductor) # enlazamos con contenedor principal
            self.ventReproductor.show() # mostramos la ventana
            mainWindow.close()
    def buscarAlbumes(self):
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
            consulta = select(Album.titulo)
            try:
                with Session() as session:
                    with session.begin():
                        resultados = session.execute(consulta).scalars().all()  #usamos .scalars() para extraer solo los valores
                        if resultados:
                            self.cbAlbum.clear() #se hace al recargar ventana, justo cuando la ventana empieza
                            for nombre in resultados:
                                self.cbAlbum.addItem(nombre)
                        else:
                            print('No se han encontrado artistas')
            except Exception as e:
                print(f'Error al consultar: {e}')
    def volverEstadoInicial(self):
        self.lblID.setVisible(False)
        self.lblTitulo.setVisible(False)
        self.lblDuracion.setVisible(False)
        self.lblGenero.setVisible(False)
        self.lblAlbum.setVisible(False)
        self.lblURL.setVisible(False)
        self.lnID.setVisible(False)
        self.lnTitulo.setVisible(False)
        self.lnDuracion.setVisible(False)
        self.cbGenero.setVisible(False)
        self.cbAlbum.setVisible(False)
        self.lnUrl.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.btnAnadir.setVisible(True)
        self.btnEditar.setVisible(True)
        self.btnEditar.setText("Editar canción")
        self.btnBorrar.setText("Borrar canción")
        self.btnBorrar.setVisible(True)
        self.lnID.clear()
        self.lnTitulo.clear()
        self.lnDuracion.clear()
        self.lnUrl.clear()
        self.lnID.setEnabled(True)
        self.cbGenero.setCurrentIndex(0)
        self.modo = None

    def logicaInsertar(self):
        if not self.modo:
            self.lblTitulo.setVisible(True)
            self.lblDuracion.setVisible(True)
            self.lblGenero.setVisible(True)
            self.lblAlbum.setVisible(True)
            self.lblURL.setVisible(True)
            self.lnTitulo.setVisible(True)
            self.lnDuracion.setVisible(True)
            self.cbGenero.setVisible(True)
            self.cbAlbum.setVisible(True)
            self.lnUrl.setVisible(True)
            self.btnCancelar.setVisible(True)
            self.btnAnadir.setText("Confirmar")
            self.btnEditar.setVisible(False)
            self.btnBorrar.setVisible(False)
            self.modo = 1
            return
        if self.modo == 1:
            if not self.lnTitulo.text():
                QMessageBox.warning(
                    None, 
                    "Campo requerido", 
                    "Por favor, ingrese el título."
                    )
                self.lnTitulo.setFocus()
                return
            if not self.lnDuracion.text():
                QMessageBox.warning(
                    None, 
                    "Campo requerido", 
                    "Por favor, ingrese una duración."
                    )
                self.lnDuracion.setFocus()
                return
            if not self.lnUrl.text():
                QMessageBox.warning(
                    None, 
                    "Campo requerido", 
                    "Por favor, ingrese el enlace a YouTube."
                    )
                self.lnUrl.setFocus()
                return
            else:
                try:
                    controlador_bd = f'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd) # , echo=True)

                except Exception as e:
                    QMessageBox.critical(None, 
                        "Error de conexión", 
                        f"No se pudo conectar a la base de datos.\n{e}"
                        )
                    return

                else:
                    Session = sessionmaker(engine)
                    try:
                        with Session() as session:
                            with session.begin():
                                query_select=select(Album.id_album).where(Album.titulo == self.cbAlbum.currentText())
                                id_album = session.execute(query_select).scalar()
                                if not id_album:
                                    QMessageBox.warning(None, 
                                        "Album no encontrado", 
                                        "No se encontró el album seleccionado."
                                        )
                                    return
                                registro = Cancion(titulo=self.lnTitulo.text(),duracion=self.lnDuracion.text(),genero=self.cbGenero.currentText(), enlace_yt=self.lnUrl.text(), album_id=id_album)
                                session.add(registro)
                                QMessageBox.information(None, "Éxito", "Canción registrada correctamente.")
                                self.modo = None
                                self.btnAnadir.setText("Añadir canción")
                                self.volverEstadoInicial()
                                return
                    except Exception as e:
                        QMessageBox.critical(None, "Error", f"Error al insertar en la base de datos.\n{e}")   
    def logicaModificar(self):
        '''algoritmo de la modificación:
        
        1. El usuario busca primero en la base de datos escribiendo el nombre artistico del usuario. Si se encuentra el nombre artistico, se debe:
        2. Rellenar todos los campos con lo que se encuentre. Se abre el botón de Confirmar y el de Cancelar cuando se pulse de nuevo en el botón Confirmar que se abre.
        3. Se hacen los cambios oportunos en los campos: Se guarda el anterior ID o el anterior Nombre Artistico para poder ejecutar luego la consulta.
        4. Finalmente, el UPDATE se hace en la base de datos.
        
        falta la parte de los dialogos pero de resto OK'''
        if self.modo == None:
            '''la lógica del modo None es simplemente activar los campos de nombre artistico e ID: solamente muestra el botón confirmar'''
            QMessageBox.information(None,
                "Información de la ventana",
                "Escriba en uno de los siguientes campos el filtro de búsqueda para la base de datos."
                )
            self.lnID.setVisible(True)
            self.lblID.setVisible(True)
            self.btnAnadir.setVisible(False)
            self.btnBorrar.setVisible(False)
            self.btnCancelar.setVisible(True)
            self.btnEditar.setText("Confirmar filtro de búsqueda")
            self.lnID.setFocus()
            self.btnCancelar.setVisible(True)
            #se cambia ahora al modo 1 para ejecutar despues la consulta:
            self.modo = 1
            return
        if self.modo == 1:
            if not self.lnID.text():
                QMessageBox.warning(None,
                            "Campos vacios",
                            "Seleccione el campo ID y escriba para buscar."
                            )
                self.lnID.setFocus()
                return
            else:
                try:
                    controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)
                except:
                    print('Se ha cometido un error al crear engine')
                else:
                    Session = sessionmaker(engine)
                    consulta = select(Cancion.id_cancion, Cancion.titulo, Cancion.duracion, Cancion.genero, Cancion.enlace_yt, Cancion.album_id).where(Cancion.id_cancion == self.lnID.text())     
                    try:
                        with Session() as session:
                            with session.begin():
                                resultado = session.execute(consulta).first()
                                if resultado:
                                    '''y ahora se consulta por el nombre para hacer la traducción de ID - nombre artistico'''
                                    consulta_nombre = select(Album.titulo).where(Cancion.album_id == resultado[5])
                                    nombre_album = session.execute(consulta_nombre).scalar()
                                    self.lnID.setText(str(resultado[0]))
                                    self.lnTitulo.setText(str(resultado[1]))
                                    self.lnDuracion.setText(str(resultado[2]))
                                    self.cbGenero.setCurrentText(str(resultado[3]))
                                    self.cbAlbum.setCurrentText(str(nombre_album))
                                    self.lnUrl.setText(str(resultado[4]))
                                    self.lblID.setVisible(True)
                                    self.lblTitulo.setVisible(True)
                                    self.lblDuracion.setVisible(True)
                                    self.lblGenero.setVisible(True)
                                    self.lblAlbum.setVisible(True)
                                    self.lblURL.setVisible(True)
                                    self.lnID.setEnabled(False)
                                    self.lnTitulo.setVisible(True)
                                    self.lnDuracion.setVisible(True)
                                    self.cbGenero.setVisible(True)
                                    self.cbAlbum.setVisible(True)
                                    self.lnUrl.setVisible(True)
                                    self.btnCancelar.setVisible(True)
                                    self.btnEditar.setText("Confirmar")
                                    self.id_provisional = str(resultado[0])
                                    self.modo = 2
                                    return
                                    
                                else:
                                    QMessageBox.warning(None,
                                            "Sin resultados",
                                            "No se han encontrado resultados. Por favor, escriba otro ID."
                                            )
                                self.lnID.setFocus()
                                self.lnID.clear()
                                return
                    except:
                        print('Erroarr al consultar')
                        return          
            
        if self.modo == 2:
            if not self.lnTitulo.text():
                QMessageBox.warning(
                    None, 
                    "Campo vacio", 
                    "Introduzca un título para la canción."
                    )
                self.lnTitulo.setFocus()
                return
            if not self.lnDuracion.text():
                QMessageBox.warning(
                    None, 
                    "Campo vacío", 
                    "Introduzca una duración."
                    )
                self.lnDuracion.setFocus()
                return
            if not self.lnUrl.text():
                QMessageBox.warning(
                    None, 
                    "Campo vacío", 
                    "Introduzca un enlace de YouTube."
                    )
                self.lnUrl.setFocus()
                return
            else: #logica real del update
                try:
                    controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)
                except Exception as e:
                    QMessageBox.critical(
                        None, 
                        "Error al conectar", 
                        f"Error: {e}"
                        )
                    return
                Session = sessionmaker(engine)
                try:
                    with Session() as session:
                        with session.begin():
                            titulo_album = self.cbAlbum.currentText()
                            consulta_id = select(Album.id_album).where(Album.titulo == titulo_album)
                            id_del_album = session.execute(consulta_id).scalar()
                            if not id_del_album:
                                QMessageBox.warning(None, "Error", "No se encontró el artista seleccionado.")
                                return

                            #se debe preparar y ejecutar el update del álbum
                            query_update = (
                                update(Cancion)
                                .where(Cancion.id_cancion == self.lnID.text())
                                .values(
                                    titulo=self.lnTitulo.text(),
                                    duracion=self.lnDuracion.text(),
                                    genero=self.cbGenero.currentText(),
                                    enlace_yt=self.lnUrl.text(),
                                    album_id=id_del_album
                                )
                            )
                            resultado = session.execute(query_update)
                            if resultado.rowcount > 0:
                                QMessageBox.information(
                                    None, 
                                    "Éxito", 
                                    "Canción modificada correctamente."
                                    )
                                self.volverEstadoInicial()
                                return
                            else:
                                QMessageBox.warning(
                                    None, 
                                    "No encontrado", 
                                    "No se encontró la canción para modificar."
                                    )
                                return
                except Exception as e:
                    QMessageBox.critical(
                        None, 
                        "Error en la modificación", 
                        f"{e}"
                        )
                    return
    def logicaBorrar(self):
        if self.modo == None:
            '''la lógica del modo None es simplemente activar los campos de nombre artistico e ID: solamente muestra el botón confirmar'''
            QMessageBox.information(None,
                "Información de la ventana","Escriba en el campo ID un identificador de la base de datos para borrar a un artista existente."
                )        
            self.lnID.setVisible(True)
            self.lblID.setVisible(True)
            self.btnAnadir.setVisible(False)
            self.btnEditar.setVisible(False)
            self.btnBorrar.setVisible(True)
            self.btnBorrar.setText("Confirmar")
            self.btnCancelar.setVisible(True)
            self.lnID.setFocus()

            #se cambia ahora al modo 1 para ejecutar despues la consulta:
            self.modo = 1
            return
            
        if self.modo == 1:
            if self.lnID.text():
                try:
                    controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)
                except:
                    print('Se ha cometido un error al crear engine')
                else:
                    Session = sessionmaker(engine)
                    query_delete = delete(Cancion).where(Cancion.id_cancion == self.lnID.text())
                    try:
                        with Session() as session:
                            with session.begin():
                                resultado = session.execute(query_delete)
                                print(resultado)
                                if resultado.rowcount > 0:
                                    QMessageBox.information(None,
                                    "Borrado exitoso",
                                    f'Se han modificado {resultado.rowcount} registros'
                                    )
                                    self.volverEstadoInicial()
                                else:
                                    QMessageBox.warning(None,
                                    "Error",
                                    "Error en el borrado. Escriba de nuevo el ID."
                                    )
                                    self.lnID.clear()
                                    self.lnID.setFocus()
                                    return
                    except:
                        QMessageBox.warning(None,
                            "Error",
                            "Error en el borrado. Escriba de nuevo el ID."
                                    )
                        self.lnID.clear()
                        self.lnID.setFocus()
                        return
            else:
                QMessageBox.warning(None,
                    "Campo vacío",
                    "Error. Rellene el campo vacío."
                                    )
                self.lnID.setFocus()
                return
    def cancelar(self):
        self.lblID.setVisible(False)
        self.lblTitulo.setVisible(False)
        self.lblDuracion.setVisible(False)
        self.lblGenero.setVisible(False)
        self.lblAlbum.setVisible(False)
        self.lblURL.setVisible(False)
        self.lnID.setVisible(False)
        self.lnTitulo.setVisible(False)
        self.lnDuracion.setVisible(False)
        self.cbGenero.setVisible(False)
        self.cbAlbum.setVisible(False)
        self.lnUrl.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.btnAnadir.setVisible(True)
        self.btnEditar.setVisible(True)
        self.btnEditar.setText("Editar canción")
        self.btnBorrar.setText("Borrar canción")
        self.btnBorrar.setVisible(True)
        self.lnID.clear()
        self.lnTitulo.clear()
        self.lnDuracion.clear()
        self.lnUrl.clear()
        self.lnID.setEnabled(True)
        self.cbGenero.setCurrentIndex(0)
        self.modo = None
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_album.ui'
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
    QSizePolicy, QWidget,QMainWindow, QMessageBox)
from modelos import Artista, Album
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine,String, Column, Integer, select, update, delete
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
class Ui_Album(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 580)
        Form.setMinimumSize(820, 580)
        Form.setMaximumSize(820, 580)
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
        self.lnTitulo.setGeometry(QRect(110, 140, 231, 22))
        self.lblTitulo = QLabel(Form)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(50, 140, 55, 16))
        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(110, 300, 591, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnNuevo = QPushButton(self.horizontalLayoutWidget_2)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.clicked.connect(self.logicaInsercion)

        self.horizontalLayout_2.addWidget(self.btnNuevo)

        self.btnCancelar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.clicked.connect(self.cancelar)

        self.horizontalLayout_2.addWidget(self.btnCancelar)

        self.btnEditar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.clicked.connect(self.logicaModificacion)

        self.horizontalLayout_2.addWidget(self.btnEditar)

        self.btnBorrar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnBorrar.setObjectName(u"btnBorrar")
        self.btnBorrar.clicked.connect(self.logicaBorrado)

        self.horizontalLayout_2.addWidget(self.btnBorrar)

        self.lnAno = QLineEdit(Form)
        self.lnAno.setObjectName(u"lnAno")
        self.lnAno.setGeometry(QRect(450, 140, 81, 22))
        validator_anio = QRegularExpressionValidator(
            QRegularExpression("^(18\d{2}|19\d{2}|20[0-1]\d|202[0-5])$")
        )
        self.lnAno.setValidator(validator_anio)
        self.lnAno.setPlaceholderText("Ej: 1800-2025")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 140, 55, 16))
        self.lblAno = QLabel(Form)
        self.lblAno.setObjectName(u"lblAno")
        self.lblAno.setGeometry(QRect(390, 140, 55, 16))
        self.lblArtista = QLabel(Form)
        self.lblArtista.setObjectName(u"lblArtista")
        self.lblArtista.setGeometry(QRect(50, 220, 71, 16))
        self.cbArtista = QComboBox(Form)
        self.cbArtista.setObjectName(u"cbArtista")
        self.cbArtista.setGeometry(QRect(130, 220, 201, 22))
        self.lblID = QLabel(Form)
        self.lblID.setObjectName(u"lblID")
        self.lblID.setGeometry(QRect(50, 70, 21, 16))
        self.lnID = QLineEdit(Form)
        self.lnID.setObjectName(u"lnID")
        self.lnID.setGeometry(QRect(70, 70, 41, 22))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        #COPIAR Y PEGAR
        self.lnID.setVisible(False)
        self.lnTitulo.setVisible(False)
        self.lnAno.setVisible(False)
        self.cbArtista.setVisible(False)
        self.lblID.setVisible(False)
        self.lblArtista.setVisible(False)
        self.lblTitulo.setVisible(False)
        self.lblAno.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.buscar_artistas()
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Men\u00fa de opciones", None))
        self.rbReproductor.setText(QCoreApplication.translate("Form", u"Reproductor", None))
        self.label_3.setText("")
        self.lblTitulo.setText(QCoreApplication.translate("Form", u"T\u00edtulo", None))
        self.btnNuevo.setText(QCoreApplication.translate("Form", u"Nuevo album", None))
        self.btnCancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btnEditar.setText(QCoreApplication.translate("Form", u"Editar album", None))
        self.btnBorrar.setText(QCoreApplication.translate("Form", u"Borrar album", None))
        self.label_2.setText("")
        self.lblAno.setText(QCoreApplication.translate("Form", u"A\u00f1o", None))
        self.lblArtista.setText(QCoreApplication.translate("Form", u"Artista", None))
        self.lblID.setText(QCoreApplication.translate("Form", u"ID", None))
        self.lnID.setText("")
    # retranslateUi

    def abrirVentanaReproductor(self, mainWindow):
        from player import Ui_Form
        self.ventReproductor = QMainWindow() # Creamos ventana contenedora
        self.ui2 = Ui_Form() # Creamos ventana del tipo artista
        self.ui2.setupUi(self.ventReproductor) # enlazamos con contenedor principal
        self.ventReproductor.show() # mostramos la ventana
        mainWindow.close()
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
    def logicaInsercion(self):
        if not self.modo:
            self.lnTitulo.setVisible(True)
            self.lnAno.setVisible(True)
            self.cbArtista.setVisible(True)
            self.lblAno.setVisible(True)
            self.lblTitulo.setVisible(True)
            self.lblArtista.setVisible(True)
            self.btnCancelar.setVisible(True)
            self.btnEditar.setVisible(False)
            self.btnBorrar.setVisible(False)
            self.modo = 1
            return
        if self.modo == 1:
            if not self.lnTitulo.text():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese el título.")
                self.lnTitulo.setFocus()
                return

            if not self.lnAno.text():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese el año de lanzamiento.")
                self.lnAno.setFocus()
                return
            else: #EL ELSE DEL CRUD
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
                                query_select=select(Artista.id_artista).where(Artista.nombre_artistico == self.cbArtista.currentText())
                                id_del_artista = session.execute(query_select).scalar()
                                if not id_del_artista:
                                    QMessageBox.warning(None, 
                                        "Artista no encontrado", 
                                        "No se encontró el artista seleccionado."
                                        )
                                    return
                                registro = Album(titulo=self.lnTitulo.text(),año=self.lnAno.text(),artista_id=id_del_artista)
                                session.add(registro)
                                QMessageBox.information(None, "Éxito", "Álbum insertado correctamente.")
                                self.modo = None
                                self.btnNuevo.setText("Nuevo álbum")
                                self.establecerVentanaInicial()
                                return
                    except Exception as e:
                        QMessageBox.critical(None, "Error", f"Error al insertar en la base de datos.\n{e}")   
    
    def logicaModificacion(self):
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
            self.btnNuevo.setVisible(False)
            self.btnBorrar.setVisible(False)
            self.btnCancelar.setVisible(True)
            self.btnEditar.setText("Confirmar filtro de búsqueda")
            self.lnID.setFocus()
            #se cambia ahora al modo 1 para ejecutar despues la consulta:
            self.modo = 1
            return
        if self.modo == 1:
            if not self.lnID.text():
                QMessageBox.warning(None,
                            "Campos vacios",
                            "Seleccione uno de los dos campos y escriba para buscar."
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
                    consulta = select(Album.id_album, Album.titulo, Album.año, Album.artista_id).where(Album.id_album == self.lnID.text())     
                    try:
                        with Session() as session:
                            with session.begin():
                                resultado = session.execute(consulta).first()
                                if resultado:
                                    '''y ahora se consulta por el nombre para hacer la traducción de ID - nombre artistico'''
                                    consulta_nombre = select(Artista.nombre_artistico).where(Artista.id_artista == resultado[3])
                                    nombre_artistico = session.execute(consulta_nombre).scalar()
                                    self.lnID.setText(str(resultado[0]))
                                    self.lnTitulo.setText(str(resultado[1]))
                                    self.lnAno.setText(str(resultado[2]))
                                    self.cbArtista.setCurrentText(str(nombre_artistico))
                                    self.lblID.setVisible(True)
                                    self.lblArtista.setVisible(True)
                                    self.lblAno.setVisible(True)
                                    self.lblTitulo.setVisible(True)
                                    self.lnID.setEnabled(False)
                                    self.lnID.setEnabled(True)
                                    self.lnTitulo.setVisible(True)
                                    self.lnAno.setVisible(True)
                                    self.cbArtista.setVisible(True)
                                    self.btnCancelar.setVisible(True)
                                    self.btnEditar.setText("Confirmar")
                                    self.id_provisional = str(resultado[0])
                                    self.modo = 2
                                    return
                                    
                                else:
                                    QMessageBox.warning(None, "ID no encontrado", "No se encontró el álbum para modificar según el ID introducido.")
                                    self.lnID.clear()
                                    self.lnID.setFocus()
                                    return
                    except:
                        QMessageBox.warning(None, "Error de consulta", "Ha habido un error de consulta, por favor, vuelva a intentarlo con otro ID.")
                        self.lnID.clear()
                        self.lnID.setFocus()
                        return          
            
        if self.modo == 2:
            if not self.lnTitulo.text():
                return
            if not self.lnAno.text():
                return
            else: #logica real del update
                try:
                    controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)
                except Exception as e:
                    QMessageBox.critical(None, "Error al conectar", f"Error: {e}")
                    return
                Session = sessionmaker(engine)
                try:
                    with Session() as session:
                        with session.begin():
                            nombre_artistico = self.cbArtista.currentText()
                            consulta_id = select(Artista.id_artista).where(Artista.nombre_artistico == nombre_artistico)
                            artista_id = session.execute(consulta_id).scalar()
                            if not artista_id:
                                QMessageBox.warning(None, "Error", "No se encontró el artista seleccionado.")
                                return

                            #se debe preparar y ejecutar el update del álbum
                            query_update = (
                                update(Album)
                                .where(Album.id_album == self.lnID.text())
                                .values(
                                    titulo=self.lnTitulo.text(),
                                    año=self.lnAno.text(),
                                    artista_id=artista_id
                                )
                            )
                            resultado = session.execute(query_update)
                            if resultado.rowcount > 0:
                                QMessageBox.information(None, "Éxito", "Álbum modificado correctamente.")
                                self.establecerVentanaInicial()
                                return
                            else:
                                QMessageBox.warning(None, "No encontrado", "No se encontró el álbum para modificar.")
                                return
                except Exception as e:
                    QMessageBox.critical(None, "Error en la modificación", f"{e}")
                    return
    def logicaBorrado(self):
        if self.modo == None:
            '''la lógica del modo None es simplemente activar los campos de nombre artistico e ID: solamente muestra el botón confirmar'''
            QMessageBox.information(None,
                "Información de la ventana","Escriba en el campo de nombre de artista para borrar a un artista existente."
                )        
            self.lnID.setVisible(True)
            self.lblID.setVisible(True)
            self.btnNuevo.setVisible(False)
            self.btnEditar.setVisible(False)
            self.btnBorrar.setVisible(True)
            self.btnBorrar.setText("Confirmar")
            self.btnCancelar.setVisible(True)
            self.lnID.setFocus()

            #se cambia ahora al modo 1 para ejecutar despues la consulta:
            self.modo = 1
            return
            
        if self.modo == 1:
            print("Estoy en el modo 1 de borrado")
            if self.lnID.text():
                try:
                    controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)
                except:
                    print('Se ha cometido un error al crear engine')
                else:
                    Session = sessionmaker(engine)
                    try:
                        with Session() as session:
                            with session.begin():
                                album = session.query(Album).filter_by(id_album=self.lnID.text()).first()
                                if album:
                                    session.delete(album)
                                    QMessageBox.information(None, 
                                        "Éxito", 
                                        "Album y canciones asociadas eliminadas."
                                        )
                                    self.establecerVentanaInicial()
                                else:
                                    QMessageBox.warning(None, 
                                        "Error", 
                                        "Album no encontrado."
                                        )
                                    self.lnID.setFocus()
                                    self.lnID.clear()
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
    def establecerVentanaInicial(self):
        self.lnID.setVisible(False)
        self.lnTitulo.setVisible(False)
        self.lnAno.setVisible(False)
        self.cbArtista.setVisible(False)
        self.lblID.setVisible(False)
        self.lblArtista.setVisible(False)
        self.lblTitulo.setVisible(False)
        self.lblAno.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.btnNuevo.setText("Nuevo album")
        self.btnEditar.setText("Editar album")
        self.btnNuevo.setVisible(True)
        self.btnBorrar.setVisible(True)
        self.btnEditar.setVisible(True)
        self.btnCancelar.setVisible(False)
        self.lnTitulo.clear()
        self.lnAno.clear()
        self.lnID.clear()
        self.cbArtista.setCurrentIndex(0)
        self.modo = None
    def cancelar(self):
        self.lnTitulo.clear()
        self.lnAno.clear()
        self.lnID.clear()
        self.cbArtista.setCurrentIndex(0)
        self.lnID.setVisible(False)
        self.lnTitulo.setVisible(False)
        self.lnAno.setVisible(False)
        self.cbArtista.setVisible(False)
        self.lblID.setVisible(False)
        self.lblArtista.setVisible(False)
        self.lblTitulo.setVisible(False)
        self.lblAno.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.btnNuevo.setText("Nuevo album")
        self.btnEditar.setText("Editar album")
        self.btnBorrar.setText("Borrar album")
        self.lnID.setEnabled(True)
        self.btnNuevo.setVisible(True)
        self.btnBorrar.setVisible(True)
        self.btnEditar.setVisible(True)
        self.btnCancelar.setVisible(False)
        self.modo = None



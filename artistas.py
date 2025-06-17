# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_artistas.ui'
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
from modelos import Artista
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine,String, Column, Integer, select, update, delete
class Ui_Artista(object):
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
        self.lnNombre = QLineEdit(Form)
        self.lnNombre.setObjectName(u"lnNombre")
        self.lnNombre.setGeometry(QRect(110, 140, 191, 22))
        self.lblNombre = QLabel(Form)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(50, 140, 55, 16))
        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(110, 300, 591, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnArtista = QPushButton(self.horizontalLayoutWidget_2)
        self.btnArtista.setObjectName(u"btnArtista")
        self.btnArtista.clicked.connect(self.logicaInsercion)

        self.horizontalLayout_2.addWidget(self.btnArtista)

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

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 140, 55, 16))
        self.lblApellidos = QLabel(Form)
        self.lblApellidos.setObjectName(u"lblApellidos")
        self.lblApellidos.setGeometry(QRect(340, 140, 55, 16))
        self.lblNacionalidad = QLabel(Form)
        self.lblNacionalidad.setObjectName(u"lblNacionalidad")
        self.lblNacionalidad.setGeometry(QRect(50, 220, 71, 16))
        self.cbNacionalidad = QComboBox(Form)
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.addItem("")
        self.cbNacionalidad.setObjectName(u"cbNacionalidad")
        self.cbNacionalidad.setGeometry(QRect(130, 220, 201, 22))
        self.lblID = QLabel(Form)
        self.lblID.setObjectName(u"lblID")
        self.lblID.setGeometry(QRect(50, 70, 21, 16))
        self.lnID = QLineEdit(Form)
        self.lnID.setObjectName(u"lnID")
        self.lnID.setGeometry(QRect(70, 70, 41, 22))
        self.lnApellidos = QLineEdit(Form)
        self.lnApellidos.setObjectName(u"lnApellidos")
        self.lnApellidos.setGeometry(QRect(400, 140, 281, 22))
        self.lblNombreArt = QLabel(Form)
        self.lblNombreArt.setObjectName(u"lblNombreArt")
        self.lblNombreArt.setGeometry(QRect(360, 220, 101, 16))
        self.lnApellidos_2 = QLineEdit(Form)
        self.lnApellidos_2.setObjectName(u"lnApellidos_2")
        self.lnApellidos_2.setGeometry(QRect(470, 220, 211, 22))

        self.retranslateUi(Form)
        #COPIAR Y PEGAR DE AQUI PARA CONSTRUIR RAPIDAMENTE LO QUE SE PUEDE VER O NO
        self.lnID.setVisible(False)
        self.lnNombre.setVisible(False)
        self.lnApellidos_2.setVisible(False)
        self.lnApellidos.setVisible(False)
        self.cbNacionalidad.setVisible(False)
        self.lblID.setVisible(False)
        self.lblNombre.setVisible(False)
        self.lblApellidos.setVisible(False)
        self.lblNacionalidad.setVisible(False)
        self.lblNombreArt.setVisible(False)

        self.btnCancelar.setVisible(False)
        

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Men\u00fa de opciones", None))
        self.rbReproductor.setText(QCoreApplication.translate("Form", u"Reproductor", None))
        self.label_3.setText("")
        self.lblNombre.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.btnArtista.setText(QCoreApplication.translate("Form", u"Nuevo artista", None))
        self.btnCancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btnEditar.setText(QCoreApplication.translate("Form", u"Editar artista", None))
        self.btnBorrar.setText(QCoreApplication.translate("Form", u"Borrar artista", None))
        self.label_2.setText("")
        self.lblApellidos.setText(QCoreApplication.translate("Form", u"Apellidos", None))
        self.lblNacionalidad.setText(QCoreApplication.translate("Form", u"Nacionalidad", None))
        self.cbNacionalidad.setItemText(0, QCoreApplication.translate("Form", u"espa\u00f1ola", None))
        self.cbNacionalidad.setItemText(1, QCoreApplication.translate("Form", u"alemana", None))
        self.cbNacionalidad.setItemText(2, QCoreApplication.translate("Form", u"inglesa", None))
        self.cbNacionalidad.setItemText(3, QCoreApplication.translate("Form", u"irlandesa", None))
        self.cbNacionalidad.setItemText(4, QCoreApplication.translate("Form", u"italiana", None))
        self.cbNacionalidad.setItemText(5, QCoreApplication.translate("Form", u"francesa", None))
        self.cbNacionalidad.setItemText(6, QCoreApplication.translate("Form", u"belga", None))
        self.cbNacionalidad.setItemText(7, QCoreApplication.translate("Form", u"danesa", None))
        self.cbNacionalidad.setItemText(8, QCoreApplication.translate("Form", u"coreana", None))
        self.cbNacionalidad.setItemText(9, QCoreApplication.translate("Form", u"japonesa", None))
        self.cbNacionalidad.setItemText(10, QCoreApplication.translate("Form", u"china", None))
        self.cbNacionalidad.setItemText(11, QCoreApplication.translate("Form", u"estadounidense", None))
        self.cbNacionalidad.setItemText(12, QCoreApplication.translate("Form", u"peruana", None))
        self.cbNacionalidad.setItemText(13, QCoreApplication.translate("Form", u"venezolana", None))
        self.cbNacionalidad.setItemText(14, QCoreApplication.translate("Form", u"argentina", None))
        self.cbNacionalidad.setItemText(15, QCoreApplication.translate("Form", u"mexicana", None))
        self.cbNacionalidad.setItemText(16, QCoreApplication.translate("Form", u"australiana", None))
        self.cbNacionalidad.setItemText(17, QCoreApplication.translate("Form", u"africana", None))
        self.cbNacionalidad.setItemText(18, QCoreApplication.translate("Form", u"neozelandesa", None))

        self.lblID.setText(QCoreApplication.translate("Form", u"ID", None))
        self.lnID.setText("")
        self.lnApellidos.setText("")
        self.lblNombreArt.setText(QCoreApplication.translate("Form", u"Nombre artistico", None))
        self.lnApellidos_2.setText("")
    def abrirVentanaReproductor(self, mainWindow):
            '''Método que abre la ventana al reproductor (la ventana de inicio enlazada al main.py)'''
            from player import Ui_Form
            self.ventReproductor = QMainWindow() # Creamos ventana contenedora
            self.ui2 = Ui_Form() # Creamos ventana del tipo reproductor
            self.ui2.setupUi(self.ventReproductor) # enlazamos con contenedor principal
            self.ventReproductor.show() # mostramos la ventana
            mainWindow.close()
    
    def logicaInsercion(self):
        '''Insertar consiste en:
        
        1. Modo None: Se abren los campos de inserción.
        2. Modo 1: El usuario rellena los campos comprobando que todos los campos estén validados.
        El programa inserta en la base de datos cuando el usuario da al botón confirmar.
        '''
        if not self.modo:
            self.lnNombre.setVisible(True)
            self.lnApellidos_2.setVisible(True)
            self.lnApellidos.setVisible(True)
            self.cbNacionalidad.setVisible(True)
            self.lblNombre.setVisible(True)
            self.lblApellidos.setVisible(True)
            self.lblNacionalidad.setVisible(True)
            self.lblNombreArt.setVisible(True)
            self.btnCancelar.setVisible(True)
            self.btnEditar.setVisible(False)
            self.btnBorrar.setVisible(False)
            self.modo = 1
            self.btnArtista.setText("Confirmar")
            return
        elif self.modo == 1:
            if not self.lnNombre.text():
                QMessageBox.warning(
                    None, 
                    "Campo requerido", 
                    "Por favor, ingrese el nombre."
                    )
                self.lnNombre.setFocus()
                return

            if not self.lnApellidos.text():
                QMessageBox.warning(
                    None, 
                    "Campo requerido", 
                    "Por favor, ingrese los apellidos."
                    )
                self.lnApellidos.setFocus()
                return

            if not self.lnApellidos_2.text():
                QMessageBox.warning(
                    None, 
                    "Campo requerido", 
                    "Por favor, ingrese el nombre artístico."
                    )
                self.lnApellidos_2.setFocus()
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
                    registro = Artista(nombre=self.lnNombre.text(), apellidos=self.lnApellidos.text(), nombre_artistico=self.lnApellidos_2.text(), nacionalidad=self.cbNacionalidad.currentText())
                    try:
                        with Session() as session:
                            with session.begin():
                                session.add(registro)
                        QMessageBox.information(None, 
                                    "Éxito", 
                                    "Artista insertado correctamente."
                                    )        
                        self.modo = None
                        self.btnArtista.setText("Nuevo artista")
                        self.establecerVentanaInicial()
                    except Exception as e:
                        QMessageBox.critical(None, 
                            "Error", 
                            f"Error al insertar en la base de datos.\n{e}"
                            )
    def logicaModificacion(self):
        '''algoritmo de la modificación:
        
        1. Modo None: Se abre el campo de modificación: el campo de ID y nombre artístico.
        2. El usuario busca primero en la base de datos escribiendo el nombre artistico del usuario, o su ID, o las dos cosas. Si se encuentra registro, se debe:
                a. Rellenar todos los campos con lo que se encuentre. 
                b. Se abre el botón de Confirmar y el de Cancelar cuando se pulse de nuevo en el botón Confirmar que se abre.
        3. Se hacen los cambios oportunos en los campos. Se presiona confirmar.
        4. Finalmente, el UPDATE se hace en la base de datos. Devuelve al estado inicial. 
        '''
        if self.modo == None:
            '''la lógica del modo None es simplemente activar los campos de nombre artistico e ID.'''
            QMessageBox.information(None,
                                    "Información de la ventana","Escriba en uno de los siguientes campos el filtro de búsqueda para la base de datos."
                                    
                                    )
            
            self.lnID.setVisible(True)
            self.lnApellidos_2.setVisible(True)
            self.lblID.setVisible(True)
            self.lblNombreArt.setVisible(True)
            self.btnArtista.setVisible(False)
            self.btnBorrar.setVisible(False)
            self.btnCancelar.setVisible(True)
            self.btnEditar.setText("Confirmar filtro de búsqueda")
            self.lnID.setFocus()

            #se cambia ahora al modo 1 para ejecutar despues la consulta:
            self.modo = 1
            return
        if self.modo == 1:
            if not self.lnApellidos_2.text() and not self.lnID.text():
                QMessageBox.warning(None,
                            "Campos vacios",
                            "Seleccione uno de los dos campos y escriba para buscar."
                            )
                self.lnID.setFocus()
                return
            if self.lnApellidos_2.text() and self.lnID.text():
                try:
                    controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)
                except:
                    print('Se ha cometido un error al crear engine')
                Session = sessionmaker(engine)
                consulta = select(Artista.id_artista, Artista.nombre, Artista.apellidos, Artista.nombre_artistico, Artista.nacionalidad).where(Artista.id_artista == self.lnID.text())
                try:
                    with Session() as session:
                        with session.begin():
                            resultado = session.execute(consulta).first()
                            if resultado:
                                self.lnID.setText(str(resultado[0]))
                                self.lnNombre.setText(str(resultado[1]))
                                self.lnApellidos.setText(str(resultado[2]))
                                self.lnApellidos_2.setText(str(resultado[3]))
                                self.cbNacionalidad.setCurrentText(str(resultado[4]))
                                self.lnID.setVisible(True)
                                self.lblID.setVisible(True)
                                self.lnID.setEnabled(False)
                                self.lnNombre.setVisible(True)
                                self.lblNombre.setVisible(True)
                                self.lnApellidos.setVisible(True)
                                self.lblApellidos.setVisible(True)
                                self.lnApellidos_2.setVisible(True)
                                self.lblNombreArt.setVisible(True)
                                self.lblNacionalidad.setVisible(True)
                                self.cbNacionalidad.setVisible(True)
                                self.btnCancelar.setVisible(True)
                                self.btnEditar.setText("Confirmar")
                                self.modo = 2
                                return
                            else:
                                QMessageBox.critical(None,
                                "Error en la búsqueda",
                                f"Error. El valor de ID proporcionado no se ha encontrado en la base de datos. Por favor, pruebe otro valor."
                                )
                                self.lnApellidos_2.clear()
                                self.lnID.clear()
                                self.lnID.setFocus()
                                return
                except:
                    QMessageBox.critical(None,
                        "Error en la búsqueda",f"Error. El valor de ID proporcionado no se ha encontrado en la base de datos. Por favor, pruebe otro valor."
                        )
                    self.lnApellidos_2.clear()
                    self.lnID.clear()
                    self.lnID.setFocus()
                    return          
            if not self.lnID.text() and self.lnApellidos_2.text():
                try:
                    controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)
                except:
                    print('Se ha cometido un error al crear engine')
                else:
                    if self.lnApellidos_2.text():
                        Session = sessionmaker(engine)
                        consulta = select(Artista.id_artista, Artista.nombre, Artista.apellidos, Artista.nombre_artistico, Artista.nacionalidad).where(Artista.nombre_artistico == self.lnApellidos_2.text())
                        try:
                            with Session() as session:
                                with session.begin():
                                    resultado = session.execute(consulta).first()
                                    if resultado:
                                        self.lnID.setText(str(resultado[0]))
                                        self.lnNombre.setText(str(resultado[1]))
                                        self.lnApellidos.setText(str(resultado[2]))
                                        self.lnApellidos_2.setText(str(resultado[3]))
                                        self.cbNacionalidad.setCurrentText(str(resultado[4]))
                                        self.lnID.setVisible(True)
                                        self.lblID.setVisible(True)
                                        self.lnID.setEnabled(False)
                                        self.lnNombre.setVisible(True)
                                        self.lblNombre.setVisible(True)
                                        self.lnApellidos.setVisible(True)
                                        self.lblApellidos.setVisible(True)
                                        self.lnApellidos_2.setVisible(True)
                                        self.lblNombreArt.setVisible(True)
                                        self.lblNacionalidad.setVisible(True)
                                        self.cbNacionalidad.setVisible(True)
                                        self.btnCancelar.setVisible(True)
                                        self.btnEditar.setText("Confirmar")
                                        self.modo = 2
                                        return
                                    else:
                                        QMessageBox.critical(None,
                                                "Error en la búsqueda",f"Error. El valor proporcionado no se ha encontrado en la base de datos. Por favor, pruebe otro valor."
                                                
                                                )
                                        self.lnApellidos_2.setFocus()
                                        self.lnApellidos_2.clear()
                                        return
                        except:
                            QMessageBox.critical(None,
                                "Error en la búsqueda",
                                f"Error. El valor proporcionado no se ha encontrado en la base de datos. Por favor, pruebe otro valor."
                                )
                            return
            if not self.lnApellidos_2.text() and self.lnID.text():
                try:
                    controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)
                except:
                    print('Se ha cometido un error al crear engine')
                Session = sessionmaker(engine)
                consulta = select(Artista.id_artista, Artista.nombre, Artista.apellidos, Artista.nombre_artistico, Artista.nacionalidad).where(Artista.id_artista == self.lnID.text())
                try:
                    with Session() as session:
                        with session.begin():
                            resultado = session.execute(consulta).first()
                            if resultado:
                                self.lnID.setText(str(resultado[0]))
                                self.lnNombre.setText(str(resultado[1]))
                                self.lnApellidos.setText(str(resultado[2]))
                                self.lnApellidos_2.setText(str(resultado[3]))
                                self.cbNacionalidad.setCurrentText(str(resultado[4]))
                                self.lnID.setVisible(True)
                                self.lblID.setVisible(True)
                                self.lnID.setEnabled(False)
                                self.lnNombre.setVisible(True)
                                self.lblNombre.setVisible(True)
                                self.lnApellidos.setVisible(True)
                                self.lblApellidos.setVisible(True)
                                self.lnApellidos_2.setVisible(True)
                                self.lblNombreArt.setVisible(True)
                                self.lblNacionalidad.setVisible(True)
                                self.cbNacionalidad.setVisible(True)
                                self.btnCancelar.setVisible(True)
                                self.btnEditar.setText("Confirmar")
                                self.modo = 2
                                return
                            else:
                                QMessageBox.critical(None,
                                "Error en la búsqueda",f"Error. El valor de ID proporcionado no se ha encontrado en la base de datos. Por favor, pruebe otro valor."
                                )
                                self.lnApellidos_2.clear()
                                self.lnID.clear()
                                self.lnID.setFocus()
                                return
                except:
                    QMessageBox.critical(None,
                                "Error en la búsqueda",f"Error. El valor de ID proporcionado no se ha encontrado en la base de datos. Por favor, pruebe otro valor."
                                )
                    self.lnApellidos_2.clear()
                    self.lnID.clear()
                    self.lnID.setFocus()
                    return
            
        if self.modo == 2:
            if not self.lnNombre.text():
                QMessageBox.warning(None,
                                "Campo vacio",f"Error. Rellene el campo nombre antes de confirmar."
                                )
                self.lnNombre.setFocus()
                return
            if not self.lnApellidos.text():
                QMessageBox.warning(None,
                                "Campo vacio",f"Error. Rellene el campo apellidos antes de confirmar."
                                )
                self.lnApellidos.setFocus()
                return
            if not self.lnApellidos_2.text():
                QMessageBox.warning(None,
                                "Campo vacio",f"Error. Rellene el campo nombre artistico antes de confirmar."
                                )
                self.lnApellidos_2.setFocus()
                return
            else: #logica real del update
                try:
                    controlador_bd = 'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)

                except:
                    print('Se ha cometido un error al crear engine')

                else:
                    Session = sessionmaker(engine)
                    query_update = (
                        update(Artista)
                        .where(Artista.id_artista == self.lnID.text())
                        .values(nombre=self.lnNombre.text(), apellidos=self.lnApellidos.text(), nombre_artistico=self.lnApellidos_2.text(), nacionalidad=self.cbNacionalidad.currentText())
                    )
                    try:
                        with Session() as session:
                            with session.begin():
                                resultado = session.execute(query_update)
                                print(resultado)
                                if resultado:
                                    QMessageBox.information(None,
                                    "Registros modificados",f"Se han modificado exitosamente {resultado.rowcount} registros. Volviendo al estado inicial."
                                    
                                    )
                                    
                                    self.establecerVentanaInicial()
                                else:
                                    print('No se ha encontrado al artista')
                                    QMessageBox.critical(None,
                                    "Error en la modificación",f"La modificación no ha salido según lo esperado. Verifique el ID del artista."
                                    
                                    )
                                    return
                    except:
                        QMessageBox.critical(None,
                            "Error en la modificación",
                            f"La modificación no ha salido según lo esperado. Verifique el ID del artista.")
                        
    def logicaBorrado(self):
        '''El usuario busca por el nombre artistico y si se encuentra lo borra automáticamente: 

        1. Cuando modo es None: se abre el campo Nombre artístico y el usuario debe introducir el nombre artístico del artista que quiere borrar.
        2. Modo 1: Se elimina si se encuentra en la base de datos, si no, se retorna y el usuario tiene la posibilidad de escribir otro nombre e intentarlo.'''
        if self.modo == None:
            '''la lógica del modo None es simplemente activar los campos de nombre artistico e ID: solamente muestra el botón confirmar'''
            QMessageBox.information(None,
                                    "Información de la ventana","Escriba en el campo de nombre de artista para borrar a un artista existente."
                                    
                                    )
            
            
            self.lnApellidos_2.setVisible(True)
            self.lblNombreArt.setVisible(True)
            self.btnArtista.setVisible(False)
            self.btnEditar.setVisible(False)
            self.btnBorrar.setVisible(True)
            self.btnBorrar.setText("Confirmar")
            self.btnCancelar.setVisible(True)
            self.lnID.setFocus()

            #se cambia ahora al modo 1 para ejecutar despues la consulta:
            self.modo = 1
            return
            
        if self.modo == 1:
            if self.lnApellidos_2.text():
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
                                artista = session.query(Artista).filter_by(nombre_artistico=self.lnApellidos_2.text()).first()
                                if artista:
                                    session.delete(artista)
                                    QMessageBox.information(None, 
                                        "Éxito", 
                                        "Artista y dependencias eliminadas."
                                        )
                                    self.establecerVentanaInicial()
                                else:
                                    QMessageBox.warning(None, 
                                        "Error de borrado", 
                                        "Artista no encontrado. Por favor, pruebe con otro nombre artístico."
                                        )
                                    self.lnApellidos_2.clear()
                                    self.lnApellidos_2.setFocus()
                                    return
                                
                    except:
                        QMessageBox.warning(None,
                                    "Error",
                                    "Error en el borrado. Escriba de nuevo el nombre artístico."
                                    )
                        self.lnApellidos_2.clear()
                        self.lnApellidos_2.setFocus()
                        return
            else:
                QMessageBox.warning(None,
                                    "Campo vacío",
                                    "Error. Rellene el campo vacío."
                                    )
                self.lnApellidos_2.setFocus()
                return
    def establecerVentanaInicial(self):
        '''devuelve al estado inicial de la ventana con:
        
        1. self.modo reseteado a <i>None</i> para la lógica de las operaciones.
        2. Los botones en su sitio.
        3. Los campos limpios.
        4. Otras variables reseteadas.'''
        self.modo=None
        self.btnArtista.setText("Nuevo artista")
        self.btnEditar.setText("Editar artista")
        self.lnID.setVisible(False)
        self.lnNombre.setVisible(False)
        self.lnApellidos_2.setVisible(False)
        self.lnApellidos.setVisible(False)
        self.cbNacionalidad.setVisible(False)
        self.lblID.setVisible(False)
        self.lblNombre.setVisible(False)
        self.lblApellidos.setVisible(False)
        self.lblNacionalidad.setVisible(False)
        self.lblNombreArt.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.btnEditar.setVisible(True)
        self.btnBorrar.setVisible(True)
        self.btnArtista.setVisible(True)
        self.lnNombre.clear()
        self.lnApellidos.clear()
        self.lnApellidos_2.clear()
        self.cbNacionalidad.setCurrentIndex(0)
        self.lnID.setEnabled(True)
        self.lnID.clear()
        self.btnBorrar.setText("Borrar artista")
        self.btnEditar.setVisible(True)
    def cancelar(self):
        '''Botón cancelar es el homólogo de establecerVentanaInicial, inicialmente separado para mantener una sintaxis clara.'''
        self.modo=None
        self.btnArtista.setText("Nuevo artista")
        self.btnEditar.setText("Editar artista")
        self.lnID.setVisible(False)
        self.lnNombre.setVisible(False)
        self.lnApellidos_2.setVisible(False)
        self.lnApellidos.setVisible(False)
        self.cbNacionalidad.setVisible(False)
        self.lblID.setVisible(False)
        self.lblNombre.setVisible(False)
        self.lblApellidos.setVisible(False)
        self.lblNacionalidad.setVisible(False)
        self.lblNombreArt.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.btnEditar.setVisible(True)
        self.btnBorrar.setVisible(True)
        self.btnArtista.setVisible(True)
        self.lnNombre.clear()
        self.lnApellidos.clear()
        self.lnApellidos_2.clear()
        self.cbNacionalidad.setCurrentIndex(0)
        self.lnID.setEnabled(True)
        self.lnID.clear()
        self.btnBorrar.setText("Borrar artista")
        self.btnEditar.setVisible(True)
    



    
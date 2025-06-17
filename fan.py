# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_fans.ui'
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
    QSizePolicy, QTextEdit, QWidget,QMainWindow, QMessageBox)
from modelos import Artista, Club_fans
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine,String, Column, Integer, select, update, delete
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
class Ui_Fans(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 557)
        Form.setMinimumSize(820, 557)
        Form.setMaximumSize(820, 557)
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
        self.horizontalLayoutWidget_2.setGeometry(QRect(110, 300, 594, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnAnadir = QPushButton(self.horizontalLayoutWidget_2)
        self.btnAnadir.setObjectName(u"btnAnadir")
        self.btnAnadir.clicked.connect(self.logicaInsercion)

        self.horizontalLayout_2.addWidget(self.btnAnadir)

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

        self.btnVer = QPushButton(self.horizontalLayoutWidget_2)
        self.btnVer.setObjectName(u"btnVer")
        self.btnVer.clicked.connect(self.verClub)

        self.horizontalLayout_2.addWidget(self.btnVer)

        self.lblFecha = QLabel(Form)
        self.lblFecha.setObjectName(u"lblFecha")
        self.lblFecha.setGeometry(QRect(330, 140, 111, 16))
        self.lblDescripcion = QLabel(Form)
        self.lblDescripcion.setObjectName(u"lblDescripcion")
        self.lblDescripcion.setGeometry(QRect(50, 220, 71, 16))
        self.lblID = QLabel(Form)
        self.lblID.setObjectName(u"lblID")
        self.lblID.setGeometry(QRect(50, 70, 21, 16))
        self.lnID = QLineEdit(Form)
        self.lnID.setObjectName(u"lnID")
        self.lnID.setGeometry(QRect(70, 70, 41, 22))
        self.lnFecha = QLineEdit(Form)
        self.lnFecha.setObjectName(u"lnFecha")
        self.lnFecha.setGeometry(QRect(430, 140, 111, 22))
        validadorFecha = QRegularExpressionValidator(QRegularExpression("^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"))
        self.lnFecha.setPlaceholderText("Ej: 2000-12-01")
        self.lnFecha.setValidator(validadorFecha)

        self.lblPais = QLabel(Form)
        self.lblPais.setObjectName(u"lblPais")
        self.lblPais.setGeometry(QRect(550, 140, 55, 16))
        self.cbPais = QComboBox(Form)
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.addItem("")
        self.cbPais.setObjectName(u"cbPais")
        self.cbPais.setGeometry(QRect(580, 140, 131, 22))
        self.tEditDescripcion = QTextEdit(Form)
        self.tEditDescripcion.setObjectName(u"tEditDescripcion")
        self.tEditDescripcion.setGeometry(QRect(130, 190, 361, 87))
        self.cbArtista = QComboBox(Form)
        self.cbArtista.setObjectName(u"cbArtista")
        self.cbArtista.setGeometry(QRect(710, 230, 73, 22))
        self.lblArtista = QLabel(Form)
        self.lblArtista.setObjectName(u"lblArtista")
        self.lblArtista.setGeometry(QRect(660, 230, 55, 16))
        self.lnFans = QLineEdit(Form)
        self.lnFans.setObjectName(u"lnFans")
        self.lnFans.setGeometry(QRect(560, 230, 71, 22))
        validadorFans = QRegularExpressionValidator(QRegularExpression("^[1-9][0-9]*$"))
        self.lnFans.setValidator(validadorFans)
        self.lblFans = QLabel(Form)
        self.lblFans.setObjectName(u"lblFans")
        self.lblFans.setGeometry(QRect(510, 230, 51, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.buscar_artistas()
        self.lnNombre.setVisible(False)
        self.lnFans.setVisible(False)
        self.lnFecha.setVisible(False)
        self.lnID.setVisible(False)
        self.cbArtista.setVisible(False)
        self.cbPais.setVisible(False)
        self.tEditDescripcion.setVisible(False)
        self.lblArtista.setVisible(False) 
        self.lblDescripcion.setVisible(False) 
        self.lblFecha.setVisible(False) 
        self.lblID.setVisible(False) 
        self.lblNombre.setVisible(False) 
        self.lblPais.setVisible(False) 
        self.lblFans.setVisible(False)
        self.btnCancelar.setVisible(False)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Men\u00fa de opciones", None))
        self.rbReproductor.setText(QCoreApplication.translate("Form", u"Reproductor", None))
        self.label_3.setText("")
        self.lblNombre.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.btnAnadir.setText(QCoreApplication.translate("Form", u"A\u00f1adir club de fans", None))
        self.btnCancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btnEditar.setText(QCoreApplication.translate("Form", u"Editar club de fans", None))
        self.btnBorrar.setText(QCoreApplication.translate("Form", u"Borrar club de fans", None))
        self.btnVer.setText(QCoreApplication.translate("Form", u"Ver club de fans", None))
        self.lblFecha.setText(QCoreApplication.translate("Form", u"Fecha fundaci\u00f3n", None))
        self.lblDescripcion.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n", None))
        self.lblID.setText(QCoreApplication.translate("Form", u"ID", None))
        self.lnID.setText("")
        self.lnFecha.setText("")
        self.lblPais.setText(QCoreApplication.translate("Form", u"Pa\u00eds", None))
        self.cbPais.setItemText(0, QCoreApplication.translate("Form", u"espa\u00f1a", None))
        self.cbPais.setItemText(1, QCoreApplication.translate("Form", u"alemania", None))
        self.cbPais.setItemText(2, QCoreApplication.translate("Form", u"estados unidos", None))
        self.cbPais.setItemText(3, QCoreApplication.translate("Form", u"irlanda", None))
        self.cbPais.setItemText(4, QCoreApplication.translate("Form", u"reino unido", None))
        self.cbPais.setItemText(5, QCoreApplication.translate("Form", u"peru", None))
        self.cbPais.setItemText(6, QCoreApplication.translate("Form", u"venezuela", None))
        self.cbPais.setItemText(7, QCoreApplication.translate("Form", u"argentina", None))
        self.cbPais.setItemText(8, QCoreApplication.translate("Form", u"china", None))
        self.cbPais.setItemText(9, QCoreApplication.translate("Form", u"corea del sur", None))
        self.cbPais.setItemText(10, QCoreApplication.translate("Form", u"jap\u00f3n", None))
        self.cbPais.setItemText(11, QCoreApplication.translate("Form", u"dinamarca", None))
        self.cbPais.setItemText(12, QCoreApplication.translate("Form", u"italia", None))
        self.cbPais.setItemText(13, QCoreApplication.translate("Form", u"francia", None))
        self.cbPais.setItemText(14, QCoreApplication.translate("Form", u"portugal", None))
        self.cbPais.setItemText(15, QCoreApplication.translate("Form", u"belgica", None))

        self.lblArtista.setText(QCoreApplication.translate("Form", u"Artista", None))
        self.lnFans.setText("")
        self.lblFans.setText(QCoreApplication.translate("Form", u"N\u00ba fans", None))
    # retranslateUi

    def abrirVentanaReproductor(self, mainWindow):
            '''ventana del tipo reproductor que instancia la ventana del reproductor'''
            from player import Ui_Form
            self.ventReproductor = QMainWindow() # Creamos ventana contenedora
            self.ui2 = Ui_Form() # Creamos ventana del tipo REPRODUCTOR
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
    def volverEstadoInicial(self):
        self.modo = None
        self.lnNombre.setVisible(False)
        self.lnFans.setVisible(False)
        self.lnFecha.setVisible(False)
        self.lnID.setVisible(False)
        self.cbArtista.setVisible(False)
        self.cbPais.setVisible(False)
        self.tEditDescripcion.setVisible(False)
        self.lblArtista.setVisible(False) 
        self.lblDescripcion.setVisible(False) 
        self.lblFecha.setVisible(False) 
        self.lblID.setVisible(False) 
        self.lblNombre.setVisible(False) 
        self.lblPais.setVisible(False) 
        self.lblFans.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.btnVer.setVisible(True)
        self.btnVer.setText("Ver club de fans")
        self.btnAnadir.setText("Añadir club de fans")
        self.btnEditar.setText("Editar club de fans")
        self.btnBorrar.setText("Borrar club de fans")
        self.btnAnadir.setVisible(True)
        self.btnEditar.setVisible(True)
        self.btnBorrar.setVisible(True)
        self.lnNombre.clear()
        self.lnID.clear()
        self.lnFecha.clear()
        self.lnFans.clear()
        self.tEditDescripcion.clear()
        self.cbArtista.setCurrentIndex(0)
        self.cbPais.setCurrentIndex(0)
        self.lnID.setEnabled(True)
    def cancelar(self):
        self.modo = None
        self.lnNombre.setVisible(False)
        self.lnFans.setVisible(False)
        self.lnFecha.setVisible(False)
        self.lnID.setVisible(False)
        self.cbArtista.setVisible(False)
        self.cbPais.setVisible(False)
        self.tEditDescripcion.setVisible(False)
        self.lblArtista.setVisible(False) 
        self.lblDescripcion.setVisible(False) 
        self.lblFecha.setVisible(False) 
        self.lblID.setVisible(False) 
        self.lblNombre.setVisible(False) 
        self.lblPais.setVisible(False) 
        self.lblFans.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.btnVer.setVisible(True)
        self.btnVer.setText("Ver club de fans")
        self.btnAnadir.setText("Añadir club de fans")
        self.btnEditar.setText("Editar club de fans")
        self.btnBorrar.setText("Borrar club de fans")
        self.btnAnadir.setVisible(True)
        self.btnEditar.setVisible(True)
        self.btnBorrar.setVisible(True)
        self.lnNombre.clear()
        self.lnID.clear()
        self.lnFecha.clear()
        self.lnFans.clear()
        self.tEditDescripcion.clear()
        self.lnID.setEnabled(True)

    def logicaInsercion(self):
        '''Primero se busca la relación que hay entre el nombre_artístico y el id del artista.
        Luego cuando se obtiene la relación se hace la inserción del nuevo club de fans con el id del artista asociado'''
        if not self.modo:
            self.lnNombre.setVisible(True)
            self.lnFans.setVisible(True)
            self.lnFecha.setVisible(True)
            self.cbArtista.setVisible(True)
            self.cbPais.setVisible(True)
            self.tEditDescripcion.setVisible(True)
            self.lblArtista.setVisible(True) 
            self.lblDescripcion.setVisible(True) 
            self.lblFecha.setVisible(True) 
            self.lblNombre.setVisible(True) 
            self.lblPais.setVisible(True) 
            self.lblFans.setVisible(True)
            self.btnCancelar.setVisible(True)
            self.btnAnadir.setText("Confirmar")
            self.btnVer.setVisible(False)
            self.btnEditar.setVisible(False)
            self.btnBorrar.setVisible(False)
            self.modo = 1
            return
        if self.modo == 1:
            if not self.lnNombre.text():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese el nombre del club.")
                self.lnNombre.setFocus()
                return
            if not self.lnFans.text():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese un número total de fans.")
                self.lnFans.setFocus()
                return
            if not self.lnFecha.text():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese una fecha.")
                self.lnFecha.setFocus()
                return
            if not self.tEditDescripcion.toPlainText():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese alguna descripción que pueda enriquecer la información del club.")
                self.lnFecha.setFocus()
                return
            else:
                try:
                    controlador_bd = f'postgresql+psycopg2://usrpostgre:usrpostgre@localhost:5432/conciertos'
                    engine = create_engine(controlador_bd)

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
                                        "Arrtista no encontrado", 
                                        "No se encontró el artista seleccionado."
                                        )
                                    return
                                registro =Club_fans(nombre=self.lnNombre.text(),fecha_fundacion=self.lnFecha.text(),pais=self.cbPais.currentText(), descripcion=self.tEditDescripcion.toPlainText(), num_fans=self.lnFans.text(), id_artista=id_del_artista)
                                session.add(registro)
                        self.modo = None
                        self.btnAnadir.setText("Añadir club de fans")
                        QMessageBox.information(None, "Éxito", "Club de fans registrado correctamente.")
                        self.volverEstadoInicial()
                        return       
                    except Exception as e:
                        QMessageBox.critical(None, "Error", f"Error al insertar en la base de datos.\n{e}")
                        return
    def logicaModificacion(self):
        '''algoritmo de la modificación:
        
        1. El usuario busca primero en la base de datos escribiendo el nombre artistico del usuario. Si se encuentra el nombre artistico, se debe:
        2. Rellenar todos los campos con lo que se encuentre. Se abre el botón de Confirmar y el de Cancelar cuando se pulse de nuevo en el botón Confirmar que se abre.
        3. Se hacen los cambios oportunos en los campos: Se guarda el anterior ID o el anterior Nombre Artistico para poder ejecutar luego la consulta.
        4. Finalmente, el UPDATE se hace en la base de datos.
        
        '''
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
            self.btnVer.setVisible(False)
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
                    consulta = select(Club_fans.id_club, Club_fans.nombre, Club_fans.fecha_fundacion, Club_fans.pais, Club_fans.descripcion, Club_fans.num_fans, Club_fans.id_artista).where(Club_fans.id_club == self.lnID.text())     
                    try:
                        with Session() as session:
                            with session.begin():
                                resultado = session.execute(consulta).first()
                                if resultado:
                                    '''y ahora se consulta por el nombre para hacer la traducción de ID - nombre artistico'''
                                    consulta_nombre = select(Artista.nombre_artistico).where(Artista.id_artista == resultado[6])
                                    nombre_artistico_art = session.execute(consulta_nombre).scalar()
                                    self.lnID.setText(str(resultado[0]))
                                    self.lnNombre.setText(str(resultado[1]))
                                    self.lnFecha.setText(str(resultado[2]))
                                    self.cbPais.setCurrentText(str(resultado[3]))
                                    self.cbArtista.setCurrentText(str(nombre_artistico_art))
                                    self.tEditDescripcion.setPlainText(str(resultado[4]))
                                    self.lnFans.setText(str(resultado[5]))
                                    self.lblID.setVisible(True)
                                    self.lblNombre.setVisible(True)
                                    self.lblFecha.setVisible(True)
                                    self.lblDescripcion.setVisible(True)
                                    self.lblPais.setVisible(True)
                                    self.lblArtista.setVisible(True)
                                    self.lblFans.setVisible(True)
                                    self.lnID.setEnabled(False)
                                    self.lnNombre.setVisible(True)
                                    self.lnFecha.setVisible(True)
                                    self.lnFans.setVisible(True)
                                    self.tEditDescripcion.setVisible(True)
                                    self.cbArtista.setVisible(True)
                                    self.cbPais.setVisible(True)
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
                                return
                    except:
                        print('Error al consultar')
                        return          
            
        if self.modo == 2:
            if not self.lnNombre.text():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese el nombre del club.")
                self.lnNombre.setFocus()
                return
            if not self.lnFans.text():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese un número total de fans.")
                self.lnFans.setFocus()
                return
            if not self.lnFecha.text():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese una fecha.")
                self.lnFecha.setFocus()
                return
            if not self.tEditDescripcion.toPlainText():
                QMessageBox.warning(None, "Campo requerido", "Por favor, ingrese alguna descripción que pueda enriquecer la información del club.")
                self.lnFecha.setFocus()
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
                            nombre_artistico_artista = self.cbArtista.currentText()
                            consulta_id = select(Artista.id_artista).where(Artista.nombre_artistico == nombre_artistico_artista)
                            id_del_artista = session.execute(consulta_id).scalar()
                            if not id_del_artista:
                                QMessageBox.warning(
                                    None, 
                                    "Error", 
                                    "No se encontró el artista seleccionado."
                                    )
                                return

                            #se debe preparar y ejecutar el update del álbum
                            query_update = (
                                update(Club_fans)
                                .where(Club_fans.id_club == self.lnID.text())
                                .values(
                                    nombre=self.lnNombre.text(),
                                    fecha_fundacion=self.lnFecha.text(),
                                    pais=self.cbPais.currentText(),
                                    descripcion=self.tEditDescripcion.toPlainText(),
                                    num_fans=self.lnFans.text(),
                                    id_artista=id_del_artista
                                )
                            )
                            resultado = session.execute(query_update)
                            if resultado.rowcount > 0:
                                QMessageBox.information(
                                    None, 
                                    "Éxito", 
                                    "Club de fans modificado correctamente."
                                    )
                                self.volverEstadoInicial()
                                return
                            else:
                                QMessageBox.warning(
                                    None, 
                                    "No encontrado", 
                                    "No se encontró club de fans para modificar."
                                    )
                                return
                except Exception as e:
                    QMessageBox.critical(
                        None, 
                        "Error en la modificación", 
                        f"{e}"
                        )
                    return
    def logicaBorrado(self):
        if self.modo == None:
            '''la lógica del modo None es simplemente activar los campos de nombre artistico e ID: solamente muestra el botón confirmar'''
            QMessageBox.information(None,
                "Información de la ventana",
                "Escriba en el campo de nombre de artista para borrar a un artista existente."
                )        
            self.lnID.setVisible(True)
            self.lblID.setVisible(True)
            self.btnAnadir.setVisible(False)
            self.btnVer.setVisible(False)
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
                    query_delete = delete(Club_fans).where(Club_fans.id_club == self.lnID.text())
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
                                    "Error en el borrado. Escriba de nuevo el ID del club."
                                    )
                                    self.lnID.clear()
                                    self.lnID.setFocus()
                                    return
                    except:
                        QMessageBox.warning(None,
                            "Error",
                            "Error en el borrado. Escriba de nuevo el ID del club."
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
    def verClub(self):
        '''Buscamos por ID en el campo que se despliega: Si se encuentra, se despliegan los campos en modo deshabilitado con la informacion del club
        
        2. Se puede repetir la busqueda tantas veces como uno quiera.
        3. El botón cancelar es el botón de retorno'''
        if not self.modo:
            self.lblID.setVisible(True)
            self.lnID.setVisible(True)
            self.lnID.setEnabled(True)
            self.btnCancelar.setVisible(True)
            self.btnAnadir.setVisible(False)
            self.btnVer.setText("Buscar")
            self.btnEditar.setVisible(False)
            self.btnBorrar.setVisible(False)
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
                    consulta = select(Club_fans.id_club, Club_fans.nombre, Club_fans.fecha_fundacion, Club_fans.pais, Club_fans.descripcion, Club_fans.num_fans, Club_fans.id_artista).where(Club_fans.id_club == self.lnID.text())     
                    try:
                        with Session() as session:
                            with session.begin():
                                resultado = session.execute(consulta).first()
                                if resultado:
                                    '''y ahora se consulta por el nombre para hacer la traducción de ID - nombre artistico'''
                                    consulta_nombre = select(Artista.nombre_artistico).where(Artista.id_artista == resultado[6])
                                    nombre_artistico_art = session.execute(consulta_nombre).scalar()
                                    self.lnID.setText(str(resultado[0]))
                                    self.lnNombre.setText(str(resultado[1]))
                                    self.lnFecha.setText(str(resultado[2]))
                                    self.cbPais.setCurrentText(str(resultado[3]))
                                    self.cbArtista.setCurrentText(str(nombre_artistico_art))
                                    self.tEditDescripcion.setPlainText(str(resultado[4]))
                                    self.lnFans.setText(str(resultado[5]))
                                    self.lblID.setVisible(True)
                                    self.lblNombre.setVisible(True)
                                    self.lblFecha.setVisible(True)
                                    self.lblDescripcion.setVisible(True)
                                    self.lblPais.setVisible(True)
                                    self.lblArtista.setVisible(True)
                                    self.lblFans.setVisible(True)
                                    self.lnID.setEnabled(False)
                                    self.lnID.setEnabled(True)
                                    self.lnNombre.setVisible(True)
                                    self.lnFecha.setVisible(True)
                                    self.lnFans.setVisible(True)
                                    self.tEditDescripcion.setVisible(True)
                                    self.cbArtista.setVisible(True)
                                    self.cbPais.setVisible(True)
                                    self.btnCancelar.setVisible(True)
                                    self.lnNombre.setDisabled(True)
                                    self.lnFecha.setDisabled(True)
                                    self.lnFans.setDisabled(True)
                                    self.tEditDescripcion.setDisabled(True)
                                    self.cbArtista.setDisabled(True)
                                    self.cbPais.setDisabled(True)
                                    self.btnCancelar.setDisabled(False)
                                    self.btnEditar.setText("Confirmar")
                                    self.id_provisional = str(resultado[0])
                                    return
                                    
                                else:
                                    QMessageBox.warning(None,
                                            "Sin resultados",
                                            "No se han encontrado resultados. Por favor, escriba otro ID."
                                            )
                                self.lnID.setFocus()
                                return
                    except:
                        print('Error al consultar')
                        return          

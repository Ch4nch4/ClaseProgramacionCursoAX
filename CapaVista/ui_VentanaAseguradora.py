# Form implementation generated from reading ui file 'c:\Users\Zangara\Documents\1-CURSO AX\8460 - TÉCNICAS AVANZADAS DE PROGRAMACIÓN\BBDD\.vscode\LaSegura\CapaVista\VentanaAseguradora.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ventanaAseguradora(object):
    def setupUi(self, ventanaAseguradora):
        ventanaAseguradora.setObjectName("ventanaAseguradora")
        ventanaAseguradora.resize(1153, 838)
        self.centralwidget = QtWidgets.QWidget(ventanaAseguradora)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 520, 671, 229))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_3)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit)
        self.matriculaVehCuloLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.matriculaVehCuloLabel.setObjectName("matriculaVehCuloLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.matriculaVehCuloLabel)
        self.matriculaVehCuloComboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.matriculaVehCuloComboBox.setObjectName("matriculaVehCuloComboBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.matriculaVehCuloComboBox)
        self.carnetDeConducirLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.carnetDeConducirLabel.setObjectName("carnetDeConducirLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.carnetDeConducirLabel)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(40, 260, 671, 201))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.formLayoutWidget_3.setFont(font)
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.txtMatricula = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtMatricula.sizePolicy().hasHeightForWidth())
        self.txtMatricula.setSizePolicy(sizePolicy)
        self.txtMatricula.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtMatricula.setFont(font)
        self.txtMatricula.setObjectName("txtMatricula")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtMatricula)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.txtModelo = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtModelo.sizePolicy().hasHeightForWidth())
        self.txtModelo.setSizePolicy(sizePolicy)
        self.txtModelo.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtModelo.setFont(font)
        self.txtModelo.setObjectName("txtModelo")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtModelo)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.txtAnio = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.txtAnio.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtAnio.setFont(font)
        self.txtAnio.setObjectName("txtAnio")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtAnio)
        self.lblDisplay = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblDisplay.setFont(font)
        self.lblDisplay.setText("")
        self.lblDisplay.setObjectName("lblDisplay")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lblDisplay)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_3.setLayout(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.gridLayout_2)
        self.comboLicenciaConducir = QtWidgets.QComboBox(self.centralwidget)
        self.comboLicenciaConducir.setGeometry(QtCore.QRect(300, 70, 131, 22))
        self.comboLicenciaConducir.setObjectName("comboLicenciaConducir")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(760, 80, 361, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAgregar_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnAgregar_2.setFont(font)
        self.btnAgregar_2.setObjectName("btnAgregar_2")
        self.verticalLayout.addWidget(self.btnAgregar_2)
        self.btnAgregar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setObjectName("btnAgregar")
        self.verticalLayout.addWidget(self.btnAgregar)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.btnExcel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnExcel.setFont(font)
        self.btnExcel.setObjectName("btnExcel")
        self.verticalLayout.addWidget(self.btnExcel)
        self.btnWord = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnWord.setFont(font)
        self.btnWord.setObjectName("btnWord")
        self.verticalLayout.addWidget(self.btnWord)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(41, 113, 118, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.Carnet = QtWidgets.QLineEdit(self.centralwidget)
        self.Carnet.setGeometry(QtCore.QRect(294, 113, 137, 22))
        self.Carnet.setText("")
        self.Carnet.setObjectName("Carnet")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(41, 164, 95, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_5.setObjectName("label_5")
        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(294, 11, 137, 22))
        self.id.setObjectName("id")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(41, 62, 247, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.Nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(294, 164, 137, 22))
        self.Nombre.setObjectName("Nombre")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(41, 11, 46, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        ventanaAseguradora.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventanaAseguradora)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1153, 26))
        self.menubar.setObjectName("menubar")
        ventanaAseguradora.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventanaAseguradora)
        self.statusbar.setObjectName("statusbar")
        ventanaAseguradora.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaAseguradora)
        QtCore.QMetaObject.connectSlotsByName(ventanaAseguradora)

    def retranslateUi(self, ventanaAseguradora):
        _translate = QtCore.QCoreApplication.translate
        ventanaAseguradora.setWindowTitle(_translate("ventanaAseguradora", "MainWindow"))
        self.label_8.setText(_translate("ventanaAseguradora", "Número de Informe:"))
        self.label_9.setText(_translate("ventanaAseguradora", "Fecha Informe"))
        self.label_10.setText(_translate("ventanaAseguradora", "Lugar"))
        self.label_11.setText(_translate("ventanaAseguradora", "Importe Daños"))
        self.matriculaVehCuloLabel.setText(_translate("ventanaAseguradora", "Matricula Vehículo"))
        self.carnetDeConducirLabel.setText(_translate("ventanaAseguradora", "Carnet de Conducir"))
        self.label.setText(_translate("ventanaAseguradora", "Matricula"))
        self.label_2.setText(_translate("ventanaAseguradora", "Modelo"))
        self.label_3.setText(_translate("ventanaAseguradora", "Año"))
        self.btnAgregar_2.setText(_translate("ventanaAseguradora", "Agregar Auto"))
        self.btnAgregar.setText(_translate("ventanaAseguradora", "Agregar Persona"))
        self.pushButton.setText(_translate("ventanaAseguradora", "Vinculas Persona Auto"))
        self.pushButton_2.setText(_translate("ventanaAseguradora", "Vincular Persona Auto informe"))
        self.btnExcel.setText(_translate("ventanaAseguradora", "Autos a Excel"))
        self.btnWord.setText(_translate("ventanaAseguradora", "Autos a Word"))
        self.label_4.setText(_translate("ventanaAseguradora", "Dirección:"))
        self.label_5.setText(_translate("ventanaAseguradora", "Nombre"))
        self.label_7.setText(_translate("ventanaAseguradora", "Licencia de conducir:"))
        self.label_6.setText(_translate("ventanaAseguradora", "ID.:"))

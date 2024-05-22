# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestion.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1280, 780)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.ButtonAccueil = QPushButton(Dialog)
        self.ButtonAccueil.setObjectName(u"ButtonAccueil")
        self.ButtonAccueil.setGeometry(QRect(20, 20, 91, 41))
        font = QFont()
        font.setPointSize(10)
        self.ButtonAccueil.setFont(font)
        self.ButtonGestion = QPushButton(Dialog)
        self.ButtonGestion.setObjectName(u"ButtonGestion")
        self.ButtonGestion.setGeometry(QRect(200, 90, 191, 51))
        self.ButtonGestion.setFont(font)
        self.ButtonPerimetres = QPushButton(Dialog)
        self.ButtonPerimetres.setObjectName(u"ButtonPerimetres")
        self.ButtonPerimetres.setGeometry(QRect(480, 90, 191, 51))
        self.ButtonPerimetres.setFont(font)
        self.ButtonZones = QPushButton(Dialog)
        self.ButtonZones.setObjectName(u"ButtonZones")
        self.ButtonZones.setGeometry(QRect(770, 90, 191, 51))
        self.ButtonZones.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(470, 30, 211, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 150, 521, 51))
        font2 = QFont()
        font2.setPointSize(18)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-color: gray;\n"
"	color: #ffffff; /* Couleur du texte (blanc dans cet exemple) */\n"
"    border: none;\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 201, 521, 491))
        self.lineEditNom = QLineEdit(Dialog)
        self.lineEditNom.setObjectName(u"lineEditNom")
        self.lineEditNom.setGeometry(QRect(40, 710, 113, 22))
        self.lineEditPrenom = QLineEdit(Dialog)
        self.lineEditPrenom.setObjectName(u"lineEditPrenom")
        self.lineEditPrenom.setGeometry(QRect(160, 710, 113, 22))
        self.lineEditMail = QLineEdit(Dialog)
        self.lineEditMail.setObjectName(u"lineEditMail")
        self.lineEditMail.setGeometry(QRect(280, 710, 113, 22))
        self.lineEditAcces = QLineEdit(Dialog)
        self.lineEditAcces.setObjectName(u"lineEditAcces")
        self.lineEditAcces.setGeometry(QRect(400, 710, 113, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 689, 111, 21))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 690, 111, 21))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 690, 111, 21))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(400, 690, 111, 21))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.tableWidget_2 = QTableWidget(Dialog)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        if (self.tableWidget_2.rowCount() < 2):
            self.tableWidget_2.setRowCount(2)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem15)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(650, 200, 421, 131))
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_3 = QTableWidget(Dialog)
        if (self.tableWidget_3.columnCount() < 4):
            self.tableWidget_3.setColumnCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        if (self.tableWidget_3.rowCount() < 5):
            self.tableWidget_3.setRowCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem24)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(650, 380, 421, 351))
        self.ButtonEntrer = QPushButton(Dialog)
        self.ButtonEntrer.setObjectName(u"ButtonEntrer")
        self.ButtonEntrer.setGeometry(QRect(220, 740, 111, 31))
        self.ButtonEntrer.setFont(font)
        self.ButtonAccueil.raise_()
        self.ButtonGestion.raise_()
        self.ButtonPerimetres.raise_()
        self.ButtonZones.raise_()
        self.label.raise_()
        self.tableWidget.raise_()
        self.lineEditNom.raise_()
        self.lineEditPrenom.raise_()
        self.lineEditMail.raise_()
        self.lineEditAcces.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.tableWidget_2.raise_()
        self.tableWidget_3.raise_()
        self.ButtonEntrer.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ButtonAccueil.setText(QCoreApplication.translate("Dialog", u"Accueil", None))
        self.ButtonGestion.setText(QCoreApplication.translate("Dialog", u"Gestion des acc\u00e8s", None))
        self.ButtonPerimetres.setText(QCoreApplication.translate("Dialog", u"P\u00e9rim\u00e8tres", None))
        self.ButtonZones.setText(QCoreApplication.translate("Dialog", u"Identification zones", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Gestion des acc\u00e8s", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Listes des acc\u00e8s", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Nom", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Pr\u00e9nom", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Mail", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Acces p\u00e9rim\u00e8tre", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"B\u00e2timent", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"1", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"2", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"3", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"4", None));
        self.lineEditNom.setText("")
        self.lineEditPrenom.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Nom", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Pr\u00e9nom", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Mail", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Acc\u00e8s p\u00e9rim\u00e8tre", None))
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Nouvelle colonne", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"Pr\u00e9nom", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Mot de passe", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"Mail", None));
        ___qtablewidgetitem13 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"1", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"Module", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"Hygi\u00e8ne", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"Qualit\u00e9", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"RSE", None));
        ___qtablewidgetitem18 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"1", None));
        ___qtablewidgetitem19 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"2", None));
        ___qtablewidgetitem20 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"3", None));
        ___qtablewidgetitem21 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"4", None));
        self.ButtonEntrer.setText(QCoreApplication.translate("Dialog", u"Entrer", None))
    # retranslateUi


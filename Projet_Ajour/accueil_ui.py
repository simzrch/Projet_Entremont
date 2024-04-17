# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accueil.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainProjet(object):
    def setupUi(self, MainProjet):
        if not MainProjet.objectName():
            MainProjet.setObjectName(u"MainProjet")
        MainProjet.resize(1280, 740)
        self.centralwidget = QWidget(MainProjet)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(520, 300, 211, 291))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ButtonDocuments = QPushButton(self.verticalLayoutWidget)
        self.ButtonDocuments.setObjectName(u"ButtonDocuments")

        self.verticalLayout_2.addWidget(self.ButtonDocuments)

        self.ButtonReporting = QPushButton(self.verticalLayoutWidget)
        self.ButtonReporting.setObjectName(u"ButtonReporting")

        self.verticalLayout_2.addWidget(self.ButtonReporting)

        self.ButtonParametres = QPushButton(self.verticalLayoutWidget)
        self.ButtonParametres.setObjectName(u"ButtonParametres")

        self.verticalLayout_2.addWidget(self.ButtonParametres)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(390, 540, 481, 61))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ButtonInformation = QPushButton(self.horizontalLayoutWidget_2)
        self.ButtonInformation.setObjectName(u"ButtonInformation")

        self.horizontalLayout_4.addWidget(self.ButtonInformation)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.ButtonRestriction = QPushButton(self.horizontalLayoutWidget_2)
        self.ButtonRestriction.setObjectName(u"ButtonRestriction")

        self.horizontalLayout_4.addWidget(self.ButtonRestriction)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 50, 271, 191))
        self.label.setPixmap(QPixmap(u"C:/Users/SNIR_admin/Desktop/PAJ/projet_180h/photo/logo_entremont.png"))
        self.ButtonHygiene = QPushButton(self.centralwidget)
        self.ButtonHygiene.setObjectName(u"ButtonHygiene")
        self.ButtonHygiene.setGeometry(QRect(660, 280, 191, 24))
        self.ButtonQualiter = QPushButton(self.centralwidget)
        self.ButtonQualiter.setObjectName(u"ButtonQualiter")
        self.ButtonQualiter.setGeometry(QRect(390, 280, 211, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 1280, 720))
        self.label_2.setPixmap(QPixmap(u"../photo/montagne.png"))
        MainProjet.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.label.raise_()
        self.ButtonHygiene.raise_()
        self.ButtonQualiter.raise_()
        self.statusbar = QStatusBar(MainProjet)
        self.statusbar.setObjectName(u"statusbar")
        MainProjet.setStatusBar(self.statusbar)

        self.retranslateUi(MainProjet)

        QMetaObject.connectSlotsByName(MainProjet)
    # setupUi

    def retranslateUi(self, MainProjet):
        MainProjet.setWindowTitle(QCoreApplication.translate("MainProjet", u"MainProjet", None))
        self.ButtonDocuments.setText(QCoreApplication.translate("MainProjet", u"Documents", None))
        self.ButtonReporting.setText(QCoreApplication.translate("MainProjet", u"Reporting", None))
        self.ButtonParametres.setText(QCoreApplication.translate("MainProjet", u"PARAMETRES", None))
        self.ButtonInformation.setText(QCoreApplication.translate("MainProjet", u"Informations base", None))
        self.ButtonRestriction.setText(QCoreApplication.translate("MainProjet", u"Niveau de restriction", None))
        self.label.setText("")
        self.ButtonHygiene.setText(QCoreApplication.translate("MainProjet", u"Hygi\u00e8ne", None))
        self.ButtonQualiter.setText(QCoreApplication.translate("MainProjet", u"Qualit\u00e9", None))
        self.label_2.setText("")
    # retranslateUi


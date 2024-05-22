# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hygiene.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1400, 802)
        self.ButtonAccueil = QPushButton(Dialog)
        self.ButtonAccueil.setObjectName(u"ButtonAccueil")
        self.ButtonAccueil.setGeometry(QRect(20, 20, 91, 41))
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(230, 30, 991, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonQualiter = QPushButton(self.horizontalLayoutWidget)
        self.ButtonQualiter.setObjectName(u"ButtonQualiter")

        self.horizontalLayout.addWidget(self.ButtonQualiter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ButtonExportxls = QPushButton(self.horizontalLayoutWidget)
        self.ButtonExportxls.setObjectName(u"ButtonExportxls")

        self.horizontalLayout.addWidget(self.ButtonExportxls)

        self.ButtonExportpdf = QPushButton(self.horizontalLayoutWidget)
        self.ButtonExportpdf.setObjectName(u"ButtonExportpdf")

        self.horizontalLayout.addWidget(self.ButtonExportpdf)

        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 90, 201, 501))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonRisques = QPushButton(self.verticalLayoutWidget)
        self.ButtonRisques.setObjectName(u"ButtonRisques")

        self.verticalLayout.addWidget(self.ButtonRisques)

        self.ButtonUnique = QPushButton(self.verticalLayoutWidget)
        self.ButtonUnique.setObjectName(u"ButtonUnique")

        self.verticalLayout.addWidget(self.ButtonUnique)

        self.ButtonVCSA = QPushButton(self.verticalLayoutWidget)
        self.ButtonVCSA.setObjectName(u"ButtonVCSA")

        self.verticalLayout.addWidget(self.ButtonVCSA)

        self.ButtonPAG = QPushButton(self.verticalLayoutWidget)
        self.ButtonPAG.setObjectName(u"ButtonPAG")

        self.verticalLayout.addWidget(self.ButtonPAG)

        self.ButtonRestriction = QPushButton(Dialog)
        self.ButtonRestriction.setObjectName(u"ButtonRestriction")
        self.ButtonRestriction.setGeometry(QRect(50, 650, 151, 51))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 59, 201, 31))
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(231, 91, 731, 661))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(960, 90, 258, 651))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ButtonAccueil.setText(QCoreApplication.translate("Dialog", u"Accueil", None))
        self.ButtonQualiter.setText(QCoreApplication.translate("Dialog", u"Qualit\u00e9", None))
        self.ButtonExportxls.setText(QCoreApplication.translate("Dialog", u"Export XLS", None))
        self.ButtonExportpdf.setText(QCoreApplication.translate("Dialog", u"Export PDF", None))
        self.ButtonRisques.setText(QCoreApplication.translate("Dialog", u"Cahier des risques", None))
        self.ButtonUnique.setText(QCoreApplication.translate("Dialog", u"Document unique", None))
        self.ButtonVCSA.setText(QCoreApplication.translate("Dialog", u"VCSA", None))
        self.ButtonPAG.setText(QCoreApplication.translate("Dialog", u"Plan d'action g\u00e9n\u00e9ral", None))
        self.ButtonRestriction.setText(QCoreApplication.translate("Dialog", u"Niveau de restriction", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Higi\u00e8ne", None))
    # retranslateUi


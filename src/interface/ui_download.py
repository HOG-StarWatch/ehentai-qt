# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_download.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Download(object):
    def setupUi(self, Download):
        if not Download.objectName():
            Download.setObjectName(u"Download")
        Download.resize(1156, 372)
        self.gridLayout_2 = QGridLayout(Download)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.redownloadRadio = QCheckBox(Download)
        self.redownloadRadio.setObjectName(u"redownloadRadio")

        self.horizontalLayout.addWidget(self.redownloadRadio)

        self.label = QLabel(Download)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.downloadNumBox = QComboBox(Download)
        self.downloadNumBox.addItem("")
        self.downloadNumBox.addItem("")
        self.downloadNumBox.addItem("")
        self.downloadNumBox.addItem("")
        self.downloadNumBox.addItem("")
        self.downloadNumBox.setObjectName(u"downloadNumBox")

        self.horizontalLayout.addWidget(self.downloadNumBox)

        self.pushButton = QPushButton(Download)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(Download)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(Download)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(Download)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.radioButton = QRadioButton(Download)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.tableWidget = QTableWidget(Download)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Download)
        self.pushButton.clicked.connect(Download.StartAll)
        self.pushButton_3.clicked.connect(Download.StopAll)
        self.pushButton_2.clicked.connect(Download.StartConvertAll)
        self.pushButton_4.clicked.connect(Download.StopConvertAll)
        self.radioButton.clicked.connect(Download.SetAutoConvert)

        QMetaObject.connectSlotsByName(Download)
    # setupUi

    def retranslateUi(self, Download):
        Download.setWindowTitle(QCoreApplication.translate("Download", u"\u4e0b\u8f7d", None))
        self.redownloadRadio.setText(QCoreApplication.translate("Download", u"\u4e0b\u8f7d\u5931\u8d25\u540e1\u5206\u949f\u81ea\u52a8\u91cd\u8bd5", None))
        self.label.setText(QCoreApplication.translate("Download", u"\u540c\u65f6\u4e0b\u8f7d\u6570", None))
        self.downloadNumBox.setItemText(0, QCoreApplication.translate("Download", u"1", None))
        self.downloadNumBox.setItemText(1, QCoreApplication.translate("Download", u"2", None))
        self.downloadNumBox.setItemText(2, QCoreApplication.translate("Download", u"3", None))
        self.downloadNumBox.setItemText(3, QCoreApplication.translate("Download", u"4", None))
        self.downloadNumBox.setItemText(4, QCoreApplication.translate("Download", u"5", None))

        self.pushButton.setText(QCoreApplication.translate("Download", u"\u5168\u90e8\u5f00\u59cb", None))
        self.pushButton_3.setText(QCoreApplication.translate("Download", u"\u5168\u90e8\u6682\u505c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Download", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.pushButton_4.setText(QCoreApplication.translate("Download", u"\u6682\u505c\u8f6c\u6362", None))
        self.radioButton.setText(QCoreApplication.translate("Download", u"\u4e0b\u8f7d\u5b8c\u81ea\u52a8\u8f6c\u6362", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Download", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Download", u"\u6807\u9898", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Download", u"\u7ad9\u70b9", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Download", u"\u4e0b\u8f7d\u8fdb\u5ea6", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Download", u"\u4e0b\u8f7d\u5927\u5c0f", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Download", u"\u4e0b\u8f7d\u901f\u5ea6", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Download", u"\u4e0b\u8f7d\u72b6\u6001", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Download", u"\u8f6c\u6362\u8fdb\u5ea6", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Download", u"\u8f6c\u6362\u8017\u65f6", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Download", u"\u8f6c\u6362\u72b6\u6001", None));
    # retranslateUi


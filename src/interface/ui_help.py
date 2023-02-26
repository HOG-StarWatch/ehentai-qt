# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_help.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from component.scroll_area.smooth_scroll_area import SmoothScrollArea
import images_rc
import images_rc

class Ui_Help(object):
    def setupUi(self, Help):
        if not Help.objectName():
            Help.setObjectName(u"Help")
        Help.resize(545, 586)
        Help.setStyleSheet(u"QListWidget {background-color:transparent;}\n"
"QScrollArea {background-color:transparent;}")
        self.verticalLayout = QVBoxLayout(Help)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = SmoothScrollArea(Help)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 508, 632))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/png/icon/icon_comment.png"))

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 50))
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.waifu2x = QLabel(self.widget_2)
        self.waifu2x.setObjectName(u"waifu2x")
        self.waifu2x.setFont(font)

        self.gridLayout.addWidget(self.waifu2x, 2, 1, 1, 1)

        self.openCmd = QPushButton(self.widget_2)
        self.openCmd.setObjectName(u"openCmd")

        self.gridLayout.addWidget(self.openCmd, 5, 1, 1, 1)

        self.logButton = QPushButton(self.widget_2)
        self.logButton.setObjectName(u"logButton")

        self.gridLayout.addWidget(self.logButton, 3, 2, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 50))
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.verCheck = QPushButton(self.widget_2)
        self.verCheck.setObjectName(u"verCheck")

        self.gridLayout.addWidget(self.verCheck, 1, 2, 1, 1)

        self.version = QLabel(self.widget_2)
        self.version.setObjectName(u"version")
        self.version.setFont(font)

        self.gridLayout.addWidget(self.version, 0, 1, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 50))
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.upTimeLabel = QLabel(self.widget_2)
        self.upTimeLabel.setObjectName(u"upTimeLabel")
        self.upTimeLabel.setFont(font)

        self.gridLayout.addWidget(self.upTimeLabel, 1, 1, 1, 1)

        self.preCheckBox = QCheckBox(self.widget_2)
        self.preCheckBox.setObjectName(u"preCheckBox")

        self.gridLayout.addWidget(self.preCheckBox, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.updateWidget = QWidget(self.widget)
        self.updateWidget.setObjectName(u"updateWidget")
        self.verticalLayout_5 = QVBoxLayout(self.updateWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.updateWidget)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_10.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_10)

        self.updateLabel = QLabel(self.updateWidget)
        self.updateLabel.setObjectName(u"updateLabel")

        self.verticalLayout_5.addWidget(self.updateLabel)

        self.updateButton = QPushButton(self.updateWidget)
        self.updateButton.setObjectName(u"updateButton")
        icon = QIcon()
        icon.addFile(u":/png/icon/new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.updateButton.setIcon(icon)

        self.verticalLayout_5.addWidget(self.updateButton)


        self.verticalLayout_2.addWidget(self.updateWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Help)

        QMetaObject.connectSlotsByName(Help)
    # setupUi

    def retranslateUi(self, Help):
        Help.setWindowTitle(QCoreApplication.translate("Help", u"\u5e2e\u52a9", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Help", u"\u9700\u8981\u53cd\u9988\u4f7f\u7528\u8fc7\u7a0b\u4e2d\u7684\u95ee\u9898\uff1f", None))
        self.label_3.setText(QCoreApplication.translate("Help", u"\u60f3\u63d0\u4f9b\u4e00\u4e9b\u5efa\u8bae\uff1f", None))
        self.pushButton.setText(QCoreApplication.translate("Help", u"Github Issue", None))
        self.label_4.setText(QCoreApplication.translate("Help", u"\u7248\u672c\u53f7:", None))
        self.waifu2x.setText(QCoreApplication.translate("Help", u"v1.0.8", None))
        self.openCmd.setText(QCoreApplication.translate("Help", u"\u6253\u5f00\u63a7\u5236\u53f0", None))
        self.logButton.setText(QCoreApplication.translate("Help", u"\u6253\u5f00\u65e5\u5fd7\u76ee\u5f55", None))
        self.label_6.setText(QCoreApplication.translate("Help", u"waifu2x\u7248\u672c:", None))
        self.verCheck.setText(QCoreApplication.translate("Help", u"\u68c0\u6d4b\u66f4\u65b0", None))
        self.version.setText(QCoreApplication.translate("Help", u"v1.2.8", None))
        self.label_7.setText(QCoreApplication.translate("Help", u"\u65e5\u5fd7:", None))
        self.label_9.setText(QCoreApplication.translate("Help", u"\u4e0a\u6b21\u66f4\u65b0\u65f6\u95f4\uff1a", None))
        self.upTimeLabel.setText(QCoreApplication.translate("Help", u"2021-11-27", None))
        self.preCheckBox.setText(QCoreApplication.translate("Help", u"\u63a5\u53d7Beta\u7248\u672c\u66f4\u65b0", None))
        self.label_10.setText(QCoreApplication.translate("Help", u"\u65b0\u7248\u672c\uff1a", None))
        self.updateLabel.setText("")
        self.updateButton.setText(QCoreApplication.translate("Help", u"\u524d\u5f80\u66f4\u65b0", None))
    # retranslateUi


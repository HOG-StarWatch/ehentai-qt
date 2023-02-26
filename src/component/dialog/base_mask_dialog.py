# coding:utf-8
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, Signal
from PySide6.QtWidgets import (QDialog, QGraphicsDropShadowEffect,
                               QGraphicsOpacityEffect, QWidget, QSpacerItem, QSizePolicy, QVBoxLayout)


class BaseMaskDialog(QDialog):
    """ 带遮罩的对话框抽象基类 """
    closed = Signal()

    def __init__(self, parent):
        QDialog.__init__(self, parent=parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.windowMask = QWidget(self)
        # 蒙版中间的对话框，所有小部件以他为父级窗口
        self.widget = QWidget(self, objectName='centerWidget')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint| Qt.WindowType.Window)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(self.parent().geometry())
        self.windowMask.resize(self.size())

        self.windowMask.setStyleSheet('background:rgba(255, 255, 255, 0.6)')
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.vBoxLayout.addItem(self.verticalSpacer)
        self.vBoxLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter)
        self.verticalSpacer2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.vBoxLayout.addItem(self.verticalSpacer2)

        self.__setShadowEffect()

    def reject(self):
        self.close()

    def closeEvent(self, arg__1) -> None:
        self.closed.emit()
        arg__1.accept()

    def __setShadowEffect(self):
        """ 添加阴影 """
        shadowEffect = QGraphicsDropShadowEffect(self.widget)
        shadowEffect.setBlurRadius(50)
        shadowEffect.setOffset(0, 5)
        self.widget.setGraphicsEffect(shadowEffect)

    def showEvent(self, e):
        """ 淡入 """
        opacityEffect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacityEffect)
        opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
        opacityAni.setStartValue(0)
        opacityAni.setEndValue(1)
        opacityAni.setDuration(200)
        opacityAni.setEasingCurve(QEasingCurve.InSine)
        opacityAni.finished.connect(opacityEffect.deleteLater)
        opacityAni.start()
        super().showEvent(e)

    # def closeEvent(self, e):
    #     """ 淡出 """
    #     self.widget.setGraphicsEffect(None)
    #     opacityEffect = QGraphicsOpacityEffect(self)
    #     self.setGraphicsEffect(opacityEffect)
    #     opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
    #     opacityAni.setStartValue(1)
    #     opacityAni.setEndValue(0)
    #     opacityAni.setDuration(100)
    #     opacityAni.setEasingCurve(QEasingCurve.OutCubic)
    #     opacityAni.finished.connect(self.deleteLater)
    #     opacityAni.start()
    #     e.ignore()

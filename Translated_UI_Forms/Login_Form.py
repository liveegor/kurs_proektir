# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Form.ui'
#
# Created: Sun Nov 30 05:33:58 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Login_Form(object):
    def setupUi(self, Login_Form):
        Login_Form.setObjectName(_fromUtf8("Login_Form"))
        Login_Form.resize(356, 193)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/1403590507_van.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login_Form.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Login_Form)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.postsComboBox = QtGui.QComboBox(self.centralwidget)
        self.postsComboBox.setObjectName(_fromUtf8("postsComboBox"))
        self.postsComboBox.addItem(_fromUtf8(""))
        self.postsComboBox.addItem(_fromUtf8(""))
        self.postsComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.postsComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.workersComboBox = QtGui.QComboBox(self.centralwidget)
        self.workersComboBox.setObjectName(_fromUtf8("workersComboBox"))
        self.horizontalLayout_2.addWidget(self.workersComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.exitPushButton = QtGui.QPushButton(self.centralwidget)
        self.exitPushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/1403292146_Log Out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitPushButton.setIcon(icon1)
        self.exitPushButton.setObjectName(_fromUtf8("exitPushButton"))
        self.horizontalLayout_3.addWidget(self.exitPushButton)
        self.refreshPushButton = QtGui.QPushButton(self.centralwidget)
        self.refreshPushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/1403548171_Synchronize.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshPushButton.setIcon(icon2)
        self.refreshPushButton.setObjectName(_fromUtf8("refreshPushButton"))
        self.horizontalLayout_3.addWidget(self.refreshPushButton)
        self.loginPushButton = QtGui.QPushButton(self.centralwidget)
        self.loginPushButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/1403297645_User.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginPushButton.setIcon(icon3)
        self.loginPushButton.setObjectName(_fromUtf8("loginPushButton"))
        self.horizontalLayout_3.addWidget(self.loginPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        Login_Form.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Login_Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        Login_Form.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Login_Form)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Login_Form.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(Login_Form)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(Login_Form)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(Login_Form)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Login_Form)
        QtCore.QMetaObject.connectSlotsByName(Login_Form)

    def retranslateUi(self, Login_Form):
        Login_Form.setWindowTitle(QtGui.QApplication.translate("Login_Form", "Вход в систему", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Login_Form", "Должность:", None, QtGui.QApplication.UnicodeUTF8))
        self.postsComboBox.setItemText(0, QtGui.QApplication.translate("Login_Form", "Директор", None, QtGui.QApplication.UnicodeUTF8))
        self.postsComboBox.setItemText(1, QtGui.QApplication.translate("Login_Form", "Зав. гаражом", None, QtGui.QApplication.UnicodeUTF8))
        self.postsComboBox.setItemText(2, QtGui.QApplication.translate("Login_Form", "Диспетчер", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Login_Form", "Сотрудник:", None, QtGui.QApplication.UnicodeUTF8))
        self.exitPushButton.setToolTip(QtGui.QApplication.translate("Login_Form", "<html><head/><body><p>Выход</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshPushButton.setToolTip(QtGui.QApplication.translate("Login_Form", "<html><head/><body><p>Заново установить соединение</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.loginPushButton.setToolTip(QtGui.QApplication.translate("Login_Form", "<html><head/><body><p>Войти</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("Login_Form", "Файл", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_2.setTitle(QtGui.QApplication.translate("Login_Form", "Действия", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("Login_Form", "Выход", None, QtGui.QApplication.UnicodeUTF8))
        self.action_2.setText(QtGui.QApplication.translate("Login_Form", "Вход в систему", None, QtGui.QApplication.UnicodeUTF8))
        self.action_3.setText(QtGui.QApplication.translate("Login_Form", "Обновить информацию", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditRun_Form.ui'
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

class Ui_EditRun_Form(object):
    def setupUi(self, EditRun_Form):
        EditRun_Form.setObjectName(_fromUtf8("EditRun_Form"))
        EditRun_Form.resize(400, 224)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/1403292157_Edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditRun_Form.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(EditRun_Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(EditRun_Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.idSpinBox = QtGui.QSpinBox(EditRun_Form)
        self.idSpinBox.setObjectName(_fromUtf8("idSpinBox"))
        self.horizontalLayout.addWidget(self.idSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(EditRun_Form)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        spacerItem1 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.busComboBox = QtGui.QComboBox(EditRun_Form)
        self.busComboBox.setObjectName(_fromUtf8("busComboBox"))
        self.horizontalLayout_5.addWidget(self.busComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_9 = QtGui.QLabel(EditRun_Form)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        spacerItem2 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.routeComboBox = QtGui.QComboBox(EditRun_Form)
        self.routeComboBox.setObjectName(_fromUtf8("routeComboBox"))
        self.horizontalLayout_6.addWidget(self.routeComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_10 = QtGui.QLabel(EditRun_Form)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        spacerItem3 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.driverComboBox = QtGui.QComboBox(EditRun_Form)
        self.driverComboBox.setObjectName(_fromUtf8("driverComboBox"))
        self.horizontalLayout_7.addWidget(self.driverComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(EditRun_Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem4 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.dateEdit = QtGui.QDateEdit(EditRun_Form)
        self.dateEdit.setDate(QtCore.QDate(2014, 6, 13))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.cancelPushButton = QtGui.QPushButton(EditRun_Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/1403362143_Cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelPushButton.setIcon(icon1)
        self.cancelPushButton.setObjectName(_fromUtf8("cancelPushButton"))
        self.horizontalLayout_4.addWidget(self.cancelPushButton)
        self.okPushButton = QtGui.QPushButton(EditRun_Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/1403362089_Check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.okPushButton.setIcon(icon2)
        self.okPushButton.setObjectName(_fromUtf8("okPushButton"))
        self.horizontalLayout_4.addWidget(self.okPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(EditRun_Form)
        QtCore.QMetaObject.connectSlotsByName(EditRun_Form)

    def retranslateUi(self, EditRun_Form):
        EditRun_Form.setWindowTitle(QtGui.QApplication.translate("EditRun_Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditRun_Form", "ID выезда: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("EditRun_Form", "Автобус:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("EditRun_Form", "Маршрут:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("EditRun_Form", "Водитель:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditRun_Form", "Дата выезда:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelPushButton.setText(QtGui.QApplication.translate("EditRun_Form", "Отмена", None, QtGui.QApplication.UnicodeUTF8))
        self.okPushButton.setText(QtGui.QApplication.translate("EditRun_Form", "OK", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Designs\to_do_list_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 721, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_search_in_to_do_list = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_search_in_to_do_list.setFont(font)
        self.lineEdit_search_in_to_do_list.setObjectName("lineEdit_search_in_to_do_list")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_search_in_to_do_list)
        self.label_search = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_search.setFont(font)
        self.label_search.setObjectName("label_search")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_search)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 89, 721, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_to_do_list = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget_to_do_list.setObjectName("tableWidget_to_do_list")
        self.tableWidget_to_do_list.setColumnCount(0)
        self.tableWidget_to_do_list.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_to_do_list)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 480, 721, 76))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add_to_do_item = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_add_to_do_item.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_add_to_do_item.setFont(font)
        self.btn_add_to_do_item.setObjectName("btn_add_to_do_item")
        self.horizontalLayout.addWidget(self.btn_add_to_do_item)
        self.btn_edit_to_do_item = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_edit_to_do_item.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_edit_to_do_item.setFont(font)
        self.btn_edit_to_do_item.setObjectName("btn_edit_to_do_item")
        self.horizontalLayout.addWidget(self.btn_edit_to_do_item)
        self.btn_to_or_do = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_to_or_do.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_to_or_do.setFont(font)
        self.btn_to_or_do.setObjectName("btn_to_or_do")
        self.horizontalLayout.addWidget(self.btn_to_or_do)
        self.btn_show_info_to_do_item = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_show_info_to_do_item.setFont(font)
        self.btn_show_info_to_do_item.setObjectName("btn_show_info_to_do_item")
        self.horizontalLayout.addWidget(self.btn_show_info_to_do_item)
        self.btn_delete_to_do_item = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_delete_to_do_item.setFont(font)
        self.btn_delete_to_do_item.setObjectName("btn_delete_to_do_item")
        self.horizontalLayout.addWidget(self.btn_delete_to_do_item)
        self.btn_refresh_to_do_item = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_refresh_to_do_item.setFont(font)
        self.btn_refresh_to_do_item.setObjectName("btn_refresh_to_do_item")
        self.horizontalLayout.addWidget(self.btn_refresh_to_do_item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.label_search.setText(_translate("MainWindow", "Search In To Do List"))
        self.btn_add_to_do_item.setText(_translate("MainWindow", "Add To Do Item"))
        self.btn_edit_to_do_item.setText(_translate("MainWindow", "Edit To Do Item"))
        self.btn_to_or_do.setText(_translate("MainWindow", "To Or Do"))
        self.btn_show_info_to_do_item.setText(_translate("MainWindow", "Show Info To Do List"))
        self.btn_delete_to_do_item.setText(_translate("MainWindow", "Delete To Do List"))
        self.btn_refresh_to_do_item.setText(_translate("MainWindow", "Refresh To Do List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
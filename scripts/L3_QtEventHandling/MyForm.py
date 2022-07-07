# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(1024, 768))
        icon = QIcon(QIcon.fromTheme(u"1"))
        MainWindow.setWindowIcon(icon)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_Qt = QAction(MainWindow)
        self.action_Qt.setObjectName(u"action_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter = QSplitter(self.tab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_3.addWidget(self.checkBox_3)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.splitter.addWidget(self.widget)
        self.toolBox = QToolBox(self.splitter)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 671, 539))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit_9 = QLineEdit(self.page)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_4.addWidget(self.lineEdit_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineEdit_8 = QLineEdit(self.page)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_5.addWidget(self.lineEdit_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lineEdit_7 = QLineEdit(self.page)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_6.addWidget(self.lineEdit_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_7.addWidget(self.label_8)

        self.lineEdit_10 = QLineEdit(self.page)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_7.addWidget(self.lineEdit_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 386, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"QLineEdit")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 671, 539))
        self.horizontalLayout_8 = QHBoxLayout(self.page_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit.setCursorWidth(1)

        self.horizontalLayout_8.addWidget(self.textEdit)

        self.toolBox.addItem(self.page_2, u"QTextEdit")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 671, 539))
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.plainTextEdit = QPlainTextEdit(self.page_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_6.addWidget(self.plainTextEdit)

        self.toolBox.addItem(self.page_4, u"QPlainTextEdit")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 616, 496))
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.calendarWidget = QCalendarWidget(self.page_3)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_8.addWidget(self.calendarWidget)

        self.toolBox.addItem(self.page_3, u"QCalendarWidget")
        self.splitter.addWidget(self.toolBox)

        self.verticalLayout_7.addWidget(self.splitter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_31 = QVBoxLayout(self.tab_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(256, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.groupBox_3.setFont(font1)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(105, 0))
        self.label_2.setSizeIncrement(QSize(0, 0))
        self.label_2.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setBaseSize(QSize(0, 0))
        self.lineEdit.setFont(font1)
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.lineEdit)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(105, 0))
        self.label_3.setSizeIncrement(QSize(0, 0))
        self.label_3.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setBaseSize(QSize(0, 0))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.lineEdit_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(105, 0))
        self.label_4.setSizeIncrement(QSize(0, 0))
        self.label_4.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setBaseSize(QSize(0, 0))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(105, 0))
        self.label_5.setSizeIncrement(QSize(0, 0))
        self.label_5.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.groupBox_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setBaseSize(QSize(0, 0))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.lineEdit_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(105, 0))
        self.label_9.setSizeIncrement(QSize(0, 0))
        self.label_9.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_9)

        self.lineEdit_5 = QLineEdit(self.groupBox_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setBaseSize(QSize(0, 0))
        self.lineEdit_5.setFont(font1)
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.lineEdit_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_41.addWidget(self.groupBox_3)

        self.groupBox_7 = QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(292, 16777215))
        self.groupBox_7.setFont(font1)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(140, 0))
        self.label_19.setSizeIncrement(QSize(0, 0))
        self.label_19.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_19)

        self.lineEdit_19 = QLineEdit(self.groupBox_7)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setFont(font1)
        self.lineEdit_19.setStyleSheet(u"color: rgb(255, 170, 0);")
        self.lineEdit_19.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.lineEdit_19)


        self.verticalLayout_18.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_20 = QLabel(self.groupBox_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(140, 0))
        self.label_20.setSizeIncrement(QSize(0, 0))
        self.label_20.setFont(font1)

        self.horizontalLayout_27.addWidget(self.label_20)

        self.lineEdit_20 = QLineEdit(self.groupBox_7)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setFont(font1)
        self.lineEdit_20.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.lineEdit_20.setReadOnly(True)

        self.horizontalLayout_27.addWidget(self.lineEdit_20)


        self.verticalLayout_18.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_21 = QLabel(self.groupBox_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(140, 0))
        self.label_21.setSizeIncrement(QSize(0, 0))
        self.label_21.setFont(font1)

        self.horizontalLayout_28.addWidget(self.label_21)

        self.lineEdit_21 = QLineEdit(self.groupBox_7)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setFont(font1)
        self.lineEdit_21.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.lineEdit_21.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.lineEdit_21)


        self.verticalLayout_18.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_22 = QLabel(self.groupBox_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(140, 0))
        self.label_22.setSizeIncrement(QSize(0, 0))
        self.label_22.setFont(font1)

        self.horizontalLayout_29.addWidget(self.label_22)

        self.lineEdit_22 = QLineEdit(self.groupBox_7)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setFont(font1)
        self.lineEdit_22.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.lineEdit_22.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.lineEdit_22)


        self.verticalLayout_18.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_23 = QLabel(self.groupBox_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(140, 0))
        self.label_23.setSizeIncrement(QSize(0, 0))
        self.label_23.setFont(font1)

        self.horizontalLayout_30.addWidget(self.label_23)

        self.lineEdit_23 = QLineEdit(self.groupBox_7)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setFont(font1)
        self.lineEdit_23.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.lineEdit_23.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.lineEdit_23)


        self.verticalLayout_18.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_41.addWidget(self.groupBox_7)

        self.groupBox_9 = QGroupBox(self.tab_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font1)
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tableWidget = QTableWidget(self.groupBox_9)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        brush = QBrush(QColor(85, 255, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setBackground(brush);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setBackground(brush);
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setBackground(brush);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_20.addWidget(self.tableWidget)


        self.horizontalLayout_41.addWidget(self.groupBox_9)


        self.verticalLayout_31.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setFont(font1)
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_24 = QLabel(self.groupBox_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(105, 0))
        self.label_24.setSizeIncrement(QSize(0, 0))
        self.label_24.setFont(font1)

        self.horizontalLayout_31.addWidget(self.label_24)

        self.lineEdit_24 = QLineEdit(self.groupBox_8)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setFont(font1)
        self.lineEdit_24.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.lineEdit_24.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.lineEdit_24)


        self.verticalLayout_19.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_25 = QLabel(self.groupBox_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(105, 0))
        self.label_25.setSizeIncrement(QSize(0, 0))
        self.label_25.setFont(font1)

        self.horizontalLayout_32.addWidget(self.label_25)

        self.lineEdit_25 = QLineEdit(self.groupBox_8)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setFont(font1)
        self.lineEdit_25.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.lineEdit_25.setReadOnly(True)

        self.horizontalLayout_32.addWidget(self.lineEdit_25)


        self.verticalLayout_19.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_26 = QLabel(self.groupBox_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(105, 0))
        self.label_26.setSizeIncrement(QSize(0, 0))
        self.label_26.setFont(font1)

        self.horizontalLayout_33.addWidget(self.label_26)

        self.lineEdit_26 = QLineEdit(self.groupBox_8)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setFont(font1)
        self.lineEdit_26.setStyleSheet(u"color: rgb(255, 170, 0);")
        self.lineEdit_26.setReadOnly(True)

        self.horizontalLayout_33.addWidget(self.lineEdit_26)


        self.verticalLayout_19.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_27 = QLabel(self.groupBox_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(105, 0))
        self.label_27.setSizeIncrement(QSize(0, 0))
        self.label_27.setFont(font1)

        self.horizontalLayout_34.addWidget(self.label_27)

        self.lineEdit_27 = QLineEdit(self.groupBox_8)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setFont(font1)
        self.lineEdit_27.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.lineEdit_27.setReadOnly(True)

        self.horizontalLayout_34.addWidget(self.lineEdit_27)


        self.verticalLayout_19.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_38.addWidget(self.groupBox_8)

        self.groupBox_10 = QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFont(font1)
        self.horizontalLayout_35 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.progressBar = QProgressBar(self.groupBox_10)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Vertical)

        self.verticalLayout_21.addWidget(self.progressBar)

        self.label_28 = QLabel(self.groupBox_10)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_21.addWidget(self.label_28)


        self.horizontalLayout_35.addLayout(self.verticalLayout_21)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.progressBar_3 = QProgressBar(self.groupBox_10)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy1.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy1)
        self.progressBar_3.setValue(75)
        self.progressBar_3.setOrientation(Qt.Vertical)

        self.verticalLayout_23.addWidget(self.progressBar_3)

        self.label_30 = QLabel(self.groupBox_10)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_23.addWidget(self.label_30)


        self.horizontalLayout_35.addLayout(self.verticalLayout_23)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.progressBar_4 = QProgressBar(self.groupBox_10)
        self.progressBar_4.setObjectName(u"progressBar_4")
        sizePolicy1.setHeightForWidth(self.progressBar_4.sizePolicy().hasHeightForWidth())
        self.progressBar_4.setSizePolicy(sizePolicy1)
        self.progressBar_4.setValue(100)
        self.progressBar_4.setOrientation(Qt.Vertical)

        self.verticalLayout_30.addWidget(self.progressBar_4)

        self.label_36 = QLabel(self.groupBox_10)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_30.addWidget(self.label_36)


        self.horizontalLayout_35.addLayout(self.verticalLayout_30)


        self.horizontalLayout_38.addWidget(self.groupBox_10)


        self.verticalLayout_31.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.groupBox_11 = QGroupBox(self.tab_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font1)
        self.groupBox_11.setFlat(False)
        self.horizontalLayout_36 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_36.setSpacing(6)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSlider = QSlider(self.groupBox_11)
        self.verticalSlider.setObjectName(u"verticalSlider")
        sizePolicy1.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy1)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_24.addWidget(self.verticalSlider)

        self.label_31 = QLabel(self.groupBox_11)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.verticalLayout_24.addWidget(self.label_31)


        self.horizontalLayout_36.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSlider_2 = QSlider(self.groupBox_11)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        sizePolicy1.setHeightForWidth(self.verticalSlider_2.sizePolicy().hasHeightForWidth())
        self.verticalSlider_2.setSizePolicy(sizePolicy1)
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.verticalLayout_25.addWidget(self.verticalSlider_2)

        self.label_32 = QLabel(self.groupBox_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)

        self.verticalLayout_25.addWidget(self.label_32)


        self.horizontalLayout_36.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSlider_3 = QSlider(self.groupBox_11)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        sizePolicy1.setHeightForWidth(self.verticalSlider_3.sizePolicy().hasHeightForWidth())
        self.verticalSlider_3.setSizePolicy(sizePolicy1)
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.verticalLayout_26.addWidget(self.verticalSlider_3)

        self.label_33 = QLabel(self.groupBox_11)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)

        self.verticalLayout_26.addWidget(self.label_33)


        self.horizontalLayout_36.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSlider_4 = QSlider(self.groupBox_11)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        sizePolicy1.setHeightForWidth(self.verticalSlider_4.sizePolicy().hasHeightForWidth())
        self.verticalSlider_4.setSizePolicy(sizePolicy1)
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.verticalLayout_27.addWidget(self.verticalSlider_4)

        self.label_34 = QLabel(self.groupBox_11)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)

        self.verticalLayout_27.addWidget(self.label_34)


        self.horizontalLayout_36.addLayout(self.verticalLayout_27)

        self.horizontalSpacer_5 = QSpacerItem(230, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_5)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalSlider_5 = QSlider(self.groupBox_11)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        sizePolicy1.setHeightForWidth(self.verticalSlider_5.sizePolicy().hasHeightForWidth())
        self.verticalSlider_5.setSizePolicy(sizePolicy1)
        self.verticalSlider_5.setOrientation(Qt.Vertical)

        self.verticalLayout_28.addWidget(self.verticalSlider_5)

        self.label_35 = QLabel(self.groupBox_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)

        self.verticalLayout_28.addWidget(self.label_35)


        self.horizontalLayout_36.addLayout(self.verticalLayout_28)


        self.horizontalLayout_37.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.tab_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFont(font1)
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.pushButton_5 = QPushButton(self.groupBox_12)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_40.addWidget(self.pushButton_5)


        self.verticalLayout_29.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.pushButton_6 = QPushButton(self.groupBox_12)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)

        self.horizontalLayout_39.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.groupBox_12)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)

        self.horizontalLayout_39.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.groupBox_12)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy2)

        self.horizontalLayout_39.addWidget(self.pushButton_8)


        self.verticalLayout_29.addLayout(self.horizontalLayout_39)


        self.horizontalLayout_37.addWidget(self.groupBox_12)


        self.verticalLayout_31.addLayout(self.horizontalLayout_37)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_Qt)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"My Design", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_Qt.setText(QCoreApplication.translate("MainWindow", u"\u041e Qt", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"QRadioButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton 1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton 2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton 3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"QCheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox 1", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox 2", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox 3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0412\u0430\u0448\u0443 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0412\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0412\u0430\u0448\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0412\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"QLineEdit", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"QTextEdit", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"QPlainTextEdit", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"QCalendarWidget", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043e\u0440\u0431\u0438\u0442\u044b", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"10256 \u043a\u043c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043e\u0440\u0431\u0438\u0442\u044b", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"0,2 \u043c/\u0441", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u041a\u0410", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"364 \u043a\u043c/\u0447", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"60,00000", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"30,00000", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.lineEdit_19.setText(QCoreApplication.translate("MainWindow", u"22 C", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.lineEdit_20.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u2116 1", None))
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u2116 2", None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u2116 3", None))
        self.lineEdit_23.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u043e\u0432", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0435\u0441\u0441", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"36,4", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"140/70", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"36,5", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"120/60", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"36,3", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"130/70", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 1", None))
        self.lineEdit_24.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 2", None))
        self.lineEdit_25.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 3", None))
        self.lineEdit_26.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435!", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 4", None))
        self.lineEdit_27.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043f\u043b\u0438\u0432\u043e", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0430\u043d\u0435\u0432\u0440\u043e\u0432\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0435\u0432\u043e", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0440\u0430\u0432\u043e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi


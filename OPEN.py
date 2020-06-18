from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
data=sqlite3.connect("Fan_Cricket.db")
curdata=data.cursor()


class Ui_OPEN(object):
    def setupUi(self, OPEN):
        OPEN.setObjectName("OPEN")
        OPEN.resize(382, 128)
        self.verticalLayout = QtWidgets.QVBoxLayout(OPEN)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.combo1 = QtWidgets.QComboBox(OPEN)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo1.sizePolicy().hasHeightForWidth())
        self.combo1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.combo1.setFont(font)
        self.combo1.setObjectName("combo1")
        self.horizontalLayout_2.addWidget(self.combo1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.b1 = QtWidgets.QPushButton(OPEN)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.horizontalLayout_2.addWidget(self.b1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.team_list=[]

        curdata.execute("SELECT Name FROM Teams")
        data1=curdata.fetchall()
        print(data1)
        for row in data1:
            self.combo1.addItem(row[0])

        self.b1.clicked.connect(self.addteam)


        self.retranslateUi(OPEN)
        QtCore.QMetaObject.connectSlotsByName(OPEN)

    def retranslateUi(self, OPEN):
        _translate = QtCore.QCoreApplication.translate
        OPEN.setWindowTitle(_translate("OPEN", "Select a Team"))
        self.b1.setText(_translate("OPEN", "OPEN"))

    
    def addteam(self):
        team=self.combo1.currentText()
        return team
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OPEN = QtWidgets.QWidget()
    ui = Ui_OPEN()
    ui.setupUi(OPEN)
    OPEN.show()
    sys.exit(app.exec_())

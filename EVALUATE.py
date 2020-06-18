#Evaluation
from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
con = sqlite3.connect('Fan_Cricket.db')
conn=con.cursor()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Evaluation")
        Dialog.resize(500, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(25, -1, 25, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cb0 = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.cb0.setFont(font)
        self.cb0.setObjectName("cb0")
        self.horizontalLayout.addWidget(self.cb0)

        sql="SELECT Name FROM Teams"
        conn.execute(sql)
        data=conn.fetchall()
        teams=[]
        for row in data:
            self.cb0.addItem(row[0])        
        
        
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cb1 = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.cb1.setFont(font)
        self.cb1.setObjectName("cb1")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.horizontalLayout.addWidget(self.cb1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lw1 = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lw1.setFont(font)
        self.lw1.setObjectName("lw1")
        self.horizontalLayout_2.addWidget(self.lw1)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lw2 = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lw2.setFont(font)
        self.lw2.setObjectName("lw2")
        self.horizontalLayout_2.addWidget(self.lw2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_3 = QtWidgets.QFrame(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.scorelabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scorelabel.setFont(font)
        self.scorelabel.setObjectName("scorelabel")
        self.horizontalLayout_3.addWidget(self.scorelabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def calculate(self):
        
        team=self.cb0.currentText()
        self.lw1.clear()
        self.lw2.clear()

        sql1="SELECT Players,Value FROM Teams WHERE Name='"+team+"'"
        conn.execute(sql1)
        data1=conn.fetchone()
        selected=data1[0].split(',')
        self.lw1.addItems(selected)

        team_total=0
        match=self.cb1.currentText()
        
        c=self.lw1.count()
        for i in range(c):
            total=0
            bat=0
            bowl=0
            field=0
            nm=self.lw1.item(i).text()
            cursor=conn.execute("SELECT * FROM Matchs WHERE Players='"+nm+"'")
            row=conn.fetchone()
            #print (row)

            bat=int(row[1]/2)
            if bat>=50:
                bat+=5
            if bat>=100:
                bat+=10
            if row[1]>0:
                sr=row[1]/row[2]
                if sr>=80 and sr<100:
                    bat+=2
                if sr>=100:
                    bat+=4
            bat=bat+row[3]
            bat=bat+2*row[4]

            bowl=row[8]*10
            if row[8]>=3:
                bowl+=5
            if row[8]>=5:
                bowl+=10
            if row[7]>0:
                er=6*row[7]/row[5]
                #print ("eco:",er)
                if er<=2:
                    bowl+=10
                if er>2 and er<=3.5:
                    bowl+=7
                if er>3.5 and er<=4.5:
                    bowl+=4

            field=(row[9]+row[10]+row[11])*10            

            total=bat+bowl+field
            self.lw2.addItem(str(total))
            team_total+=total
        self.scorelabel.setText(str(team_total))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Evaluation"))
        self.label_2.setText(_translate("Dialog", "Choose Team"))
        self.label.setText(_translate("Dialog", "Choose Match"))
        self.cb1.setItemText(0, _translate("Dialog", "Matchs"))
        self.cb1.setItemText(1, _translate("Dialog", "Match2"))
        self.cb1.setItemText(2, _translate("Dialog", "Match3"))
        self.cb1.setItemText(3, _translate("Dialog", "Match4"))
        self.cb1.setItemText(4, _translate("Dialog", "Match5"))
        self.label_5.setText(_translate("Dialog", "Players"))
        self.label_4.setText(_translate("Dialog", "Score"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))
        self.scorelabel.setText(_translate("Dialog", "00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


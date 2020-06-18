#main code for fantasy cricket

from PyQt5 import QtCore, QtGui, QtWidgets
from NEW import Ui_NEW_Team
from EVALUATE import Ui_Dialog
from OPEN import Ui_OPEN

from PyQt5.QtWidgets import QMessageBox

import sqlite3 
data=sqlite3.connect('Fan_Cricket.db')
datacur= data.cursor()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(750, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 693, 58))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BAT = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BAT.setFont(font)
        self.BAT.setObjectName("BAT")
        self.horizontalLayout.addWidget(self.BAT)
        self.BOW = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BOW.setFont(font)
        self.BOW.setObjectName("BOW")
        self.horizontalLayout.addWidget(self.BOW)
        self.AR = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AR.setFont(font)
        self.AR.setObjectName("AR")
        self.horizontalLayout.addWidget(self.AR)
        self.WK = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.WK.setFont(font)
        self.WK.setObjectName("WK")
        self.horizontalLayout.addWidget(self.WK)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 160, 641, 401))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.horizontalLayout_2.addWidget(self.l1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.l2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.l2.setObjectName("l2")
        self.horizontalLayout_2.addWidget(self.l2)
        self.pointsA = QtWidgets.QLabel(self.centralwidget)
        self.pointsA.setGeometry(QtCore.QRect(70, 110, 220, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pointsA.setFont(font)
        self.pointsA.setObjectName("pointsA")
        self.pointsU = QtWidgets.QLabel(self.centralwidget)
        self.pointsU.setGeometry(QtCore.QRect(420, 110, 220, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pointsU.setFont(font)
        self.pointsU.setObjectName("pointsU")
        self.RBAT = QtWidgets.QRadioButton(self.centralwidget)
        self.RBAT.setGeometry(QtCore.QRect(40, 140, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setBold(True)
        font.setWeight(75)
        self.RBAT.setFont(font)
        self.RBAT.setObjectName("RBAT")
        self.RBOW = QtWidgets.QRadioButton(self.centralwidget)
        self.RBOW.setGeometry(QtCore.QRect(110, 140, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setBold(True)
        font.setWeight(75)
        self.RBOW.setFont(font)
        self.RBOW.setObjectName("RBOW")
        self.RAR = QtWidgets.QRadioButton(self.centralwidget)
        self.RAR.setGeometry(QtCore.QRect(180, 140, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setBold(True)
        font.setWeight(75)
        self.RAR.setFont(font)
        self.RAR.setObjectName("RAR")
        self.RWK = QtWidgets.QRadioButton(self.centralwidget)
        self.RWK.setGeometry(QtCore.QRect(240, 140, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setBold(True)
        font.setWeight(75)
        self.RWK.setFont(font)
        self.RWK.setObjectName("RWK")
        self.teamname = QtWidgets.QLabel(self.centralwidget)
        self.teamname.setGeometry(QtCore.QRect(420, 140, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setBold(True)
        font.setWeight(75)
        self.teamname.setFont(font)
        self.teamname.setObjectName("teamname")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 18))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.actionNEW_Team.triggered.connect(self.NEWTeam)
        self.actionSAVE_Team.triggered.connect(self.SAVETeam)
        self.actionEVALUATE_Team.triggered.connect(self.EVALUATETeam)
        self.actionOPEN_Team.triggered.connect(self.OPENTeam)
        self.RBAT.setEnabled(False)
        self.RBOW.setEnabled(False)
        self.RWK.setEnabled(False)
        self.RAR.setEnabled(False)

        self.l1.itemDoubleClicked.connect(self.rm_l1)
        self.l2.itemDoubleClicked.connect(self.rm_l2)
        self.RBAT.toggled.connect(self.List)
        self.RBOW.toggled.connect(self.List)
        self.RAR.toggled.connect(self.List)
        self.RWK.toggled.connect(self.List)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.BAT.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.BOW.setText(_translate("MainWindow", "Bowler(BOW)"))
        self.AR.setText(_translate("MainWindow", "AllRounder(AR)"))
        self.WK.setText(_translate("MainWindow", "WktKeeper(WK)"))
        self.pointsA.setText(_translate("MainWindow", "Points Available "))
        self.pointsU.setText(_translate("MainWindow", "Points Used"))
        self.RBAT.setText(_translate("MainWindow", "BAT"))
        self.RBOW.setText(_translate("MainWindow", "BOW"))
        self.RAR.setText(_translate("MainWindow", "AR"))
        self.RWK.setText(_translate("MainWindow", "WK"))
        self.teamname.setText(_translate("MainWindow", "Team NAME"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team "))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))


#the list formation code    
    def rm_l1(self,item):
        if self.RBAT.isChecked()==True:
            self.bat-=1
            self.BAT.setText("Batsmen(BAT):"+str(self.bat))
            self.status(item)

        if self.RBOW.isChecked()==True:
            self.bwl-=1
            self.BOW.setText("Bowler(BOW):"+str(self.bwl))
            self.status(item)

        if self.RAR.isChecked()==True:
            self.ar-=1
            self.AR.setText("AllRounder(AR):"+str(self.ar))
            self.status(item)

        if self.RWK.isChecked()==True:
            if self.wk<2:
                msg="Wicketkeepers not more than 1"
                self.showmsg(msg)
            else:
                self.wk-=1
                self.BAT.setText("WktKeeper(WK):"+str(self.wk))
                self.status(item)



    def status(self,item):
        datacur.execute("SELECT value FROM stats WHERE players='"+item.text()+"'")
        row=datacur.fetchall()
        self.avl=self.avl-int(row[0][0])
        self.used=self.used+int(row[0][0])

        if self.avl<=0:
            msg = 'Exhausted Points'
            self.showmsg(msg)
        else:
            self.pointsA.setText("Points Available:"+str(self.avl))
            self.pointsU.setText("Points Used:"+str(self.used))
            self.l1.takeItem(self.l1.row(item))
            self.l2.addItem(item.text())


    def rm_l2(self,item):
        if self.RBAT.isChecked()==True:
            self.bat+=1
            self.BAT.setText("Batsmen(BAT):"+str(self.bat))

        if self.RBOW.isChecked()==True:
            self.bwl+=1
            self.BOW.setText("Bowler(BOW):"+str(self.bwl))

        if self.RAR.isChecked()==True:
            self.ar+=1
            self.AR.setText("AllRounder(AR):"+str(self.ar))

        if self.RWK.isChecked()==True:
            self.wk+=1
            self.WK.setText("WktKeeper(WK):"+str(self.wk))

        datacur.execute("SELECT value FROM stats WHERE players='"+item.text()+"'")
        row=datacur.fetchall()
        self.avl=self.avl+int(row[0][0])
        self.used=self.used-int(row[0][0])

        self.pointsA.setText("Points Available:"+str(self.avl))
        self.pointsU.setText("Points Used:"+str(self.used))
        
        self.l2.takeItem(self.l2.row(item))
        self.l1.addItem(item.text())

    def showmsg(self,msg):
        Dialog = QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Alert")
        Dialog.exec()
        



  #list manupulation
    def List(self):
        if self.RBAT.isChecked():
            
            self.l1.clear()
            datacur.execute('SELECT Players FROM stats WHERE ctg=="BAT";')
            fdata= datacur.fetchall()
            

            for data in fdata:
                self.l1.addItem(data[0])
                

        if self.RBOW.isChecked()==True:
            
            self.l1.clear()
            datacur.execute('SELECT Players FROM stats WHERE ctg=="BWL";')
            fdata=datacur.fetchall()
           
            

            for data in fdata:
                self.l1.addItem(data[0])

        if self.RAR.isChecked()==True:

            self.l1.clear()
            datacur.execute('SELECT Players FROM stats WHERE ctg=="AR";')
            fdata=datacur.fetchall()
            

            for data in fdata:
                self.l1.addItem(data[0])

        if self.RWK.isChecked()==True:

            self.l1.clear()
            datacur.execute('SELECT Players FROM stats WHERE ctg=="WK";')
            fdata=datacur.fetchall()
            

            for data in fdata:
                self.l1.addItem(data[0])

        
 #Menu function 
    
        
    def NEWTeam(self):
        
        self.nil()
    
        self.NEW_Team = QtWidgets.QDialog()
        self.ui = Ui_NEW_Team()
        self.ui.setupUi(self.NEW_Team)
        self.NEW_Team.show()
        self.NEW_Team.exec_()
        self.name=self.ui.accept()#assign the returned value of NEW accept method to name
        self.show_team()

        self.teamname.setText('Team NAME : ' + str(self.name))

    def SAVETeam(self):
        c=self.l2.count()
        player_names=''
        for i in range(c):
            player_names=player_names+self.l2.item(i).text()
            if i<c-1:
                player_names=player_names+','


        sql="INSERT INTO Teams (Name, Players, Value) VALUES ('"+self.name+"','"+player_names+"','"+str(self.used)+"');"
        try:
            datacur.execute(sql)
            data.commit()
            self.showmsg("Team Saved successfully")
        except:
            self.showmsg("Error")
            data.rollback()

    def OPENTeam(self):
        self.nil()

        self.OPEN = QtWidgets.QWidget()
        self.ui = Ui_OPEN()
        self.ui.setupUi(self.OPEN)
        self.OPEN.show()
    
        self.name=self.ui.addteam()
        self.teamname.setText('Team NAME : ' + str(self.name))

        sql1="SELECT Players,Value FROM Teams WHERE Name='"+self.name+"';"
        cur=datacur.execute(sql1)
        ROW=cur.fetchone()
        #selected=[]
        selected=ROW[0].split(',')
        #print(selected)

        self.l2.addItems(selected)
        self.used=int(ROW[1])
        self.avl=1000-int(ROW[1])
        c=self.l2.count()

        for i in range(c):
            player=self.l2.item(i).text()
            print(player)
            sql="SELECT ctg FROM stats WHERE Players='"+player+"'"
            datacur.execute(sql)
            row=datacur.fetchone()
            ct=row[0]
            if ct=="BAT":
                self.bat+=1
            if ct=="BWL":
                self.bwl+=1
            if ct=="AR":
                self.ar+=1
            if ct=="WK":
                self.wk+=1

        self.BAT.setText("Batsmen(BAT):"+str(self.bat))
        self.BOW.setText("Bowler(BOW):"+str(self.bwl))
        self.AR.setText("AllRounder(AR):"+str(self.ar))
        self.WK.setText("WktKeeper(WK):"+str(self.wk))

        self.pointsA.setText("Points Available:"+str(self.avl))
        self.pointsU.setText("Points Used:"+str(self.used))

        
    def EVALUATETeam(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        self.Dialog.exec_()

    def nil(self):
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0
        self.name=''
        self.l1.clear()
        self.l2.clear()
        self.BAT.setText("Batsmen(BAT)")
        self.BOW.setText("Bowler(BOW)")
        self.AR.setText("AllRounder(AR)")
        self.WK.setText("WktKeeper(WK)")
        self.pointsA.setText("Points Available:"+str(self.avl))
        self.pointsU.setText("Points Used:"+str(self.used))

        
  #points and information on dashboard        
    def show_team(self):
        self.RBAT.setEnabled(True)
        self.RBOW.setEnabled(True)
        self.RWK.setEnabled(True)
        self.RAR.setEnabled(True)

        datacur.execute('SELECT Players FROM stats WHERE ctg=="BAT";')
        fdata= datacur.fetchall()
        self.bat=len(fdata)
        self.BAT.setText("Batsmen(BAT):"+str(self.bat))

        datacur.execute('SELECT Players FROM stats WHERE ctg=="BWL";')
        fdata= datacur.fetchall()
        self.bwl=len(fdata)
        self.BOW.setText("Bowler(BOW):"+str(self.bwl))

        datacur.execute('SELECT Players FROM stats WHERE ctg=="AR";')
        fdata=datacur.fetchall()
        self.ar=len(fdata)
        self.AR.setText("AllRounder(AR):"+str(self.ar))

        datacur.execute('SELECT Players FROM stats WHERE ctg=="WK";')
        fdata=datacur.fetchall()
        self.wk=len(fdata)
        self.WK.setText("WktKeeper(WK):"+str(self.wk))

        self.pointsA.setText("Points Available:"+str(self.avl))
        self.pointsU.setText("Points Used:"+str(self.used))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

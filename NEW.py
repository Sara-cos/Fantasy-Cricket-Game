
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NEW_Team(object):
    def setupUi(self, NEW_Team):
        NEW_Team.setObjectName("NEW_Team")
        NEW_Team.resize(497, 133)
        NEW_Team.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.buttonBox = QtWidgets.QDialogButtonBox(NEW_Team)
        self.buttonBox.setGeometry(QtCore.QRect(20, 70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(NEW_Team)
        self.label.setGeometry(QtCore.QRect(20, 30, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(NEW_Team)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 261, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(NEW_Team)

        self.buttonBox.accepted.connect(self.accept)#changed NEW_Team to self 
        self.buttonBox.rejected.connect(NEW_Team.reject)#handler remain same

        QtCore.QMetaObject.connectSlotsByName(NEW_Team)

    def retranslateUi(self, NEW_Team):
        _translate = QtCore.QCoreApplication.translate
        NEW_Team.setWindowTitle(_translate("NEW_Team", "New Team"))
        self.label.setText(_translate("NEW_Team", "ENTER THE NAME :"))

    def accept(self):
        txt=self.lineEdit.text()
        return txt 
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NEW_Team = QtWidgets.QDialog()
    ui = Ui_NEW_Team()
    ui.setupUi(NEW_Team)
    NEW_Team.show()
    sys.exit(app.exec_())

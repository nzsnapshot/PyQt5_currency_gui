from PyQt5 import QtCore, QtGui, QtWidgets
from api_converter import Api
import json
import sys
import webbrowser



class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.api = Api()
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(239, 270)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 231, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(80, 160, 81, 23))
        self.convertButton.setObjectName("convertButton")
        self.convertButton.clicked.connect(self._on_click)

        self.entryBox = QtWidgets.QLineEdit(self.centralwidget)
        self.entryBox.setGeometry(QtCore.QRect(70, 130, 101, 20))
        self.entryBox.setObjectName("entryBox")
        self.entryBoxValue = self.entryBox.text()

        self.combo1 = QtWidgets.QComboBox(self.centralwidget)
        self.combo1.setGeometry(QtCore.QRect(20, 70, 71, 22))
        self.combo1.setObjectName("combo1")
        self.combo1.addItems(self.api.curr)
        # self.combo1.currentTextChanged.connect(self._on_combobox_change)
      
        self.combo2 = QtWidgets.QComboBox(self.centralwidget)
        self.combo2.setGeometry(QtCore.QRect(148, 70, 71, 22))
        self.combo2.setObjectName("combo2")
        self.combo2.addItems(self.api.curr2)
        # self.combo2.currentTextChanged.connect(self._on_combobox_change1)


        # self.currencyLabel1 = QtWidgets.QLabel(self.centralwidget)
        # self.currencyLabel1.setGeometry(QtCore.QRect(20, 100, 71, 20))
        # font = QtGui.QFont()
        # font.setFamily("MS Shell Dlg 2")
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setWeight(50)
        # self.currencyLabel1.setFont(font)
        # self.currencyLabel1.setAlignment(QtCore.Qt.AlignCenter)
        # self.currencyLabel1.setObjectName("currencyLabel1")

        self.arrowLabel = QtWidgets.QLabel(self.centralwidget)
        self.arrowLabel.setGeometry(QtCore.QRect(100, 70, 41, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.arrowLabel.setFont(font)
        self.arrowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.arrowLabel.setObjectName("arrowLabel")

        self.dollarSign = QtWidgets.QLabel(self.centralwidget)
        self.dollarSign.setGeometry(QtCore.QRect(50, 130, 20, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.dollarSign.setFont(font)
        self.dollarSign.setAlignment(QtCore.Qt.AlignCenter)
        self.dollarSign.setObjectName("dollarSign")

        # self.currencyLabel = QtWidgets.QLabel(self.centralwidget)
        # self.currencyLabel.setGeometry(QtCore.QRect(150, 100, 71, 20))
        # font = QtGui.QFont()
        # font.setFamily("MS Shell Dlg 2")
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setWeight(50)
        # self.currencyLabel.setFont(font)
        # self.currencyLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.currencyLabel.setObjectName("currencyLabel")

        # self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        # self.totalLabel.setGeometry(QtCore.QRect(80, 190, 81, 20))
        # font = QtGui.QFont()
        # font.setFamily("MS Shell Dlg 2")
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setWeight(50)
        # self.totalLabel.setFont(font)
        # self.totalLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.totalLabel.setObjectName("totalLabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 239, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Snap\'s Currency Converter"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.combo1.setItemText(0, _translate("MainWindow", "Currency"))
        self.combo2.setItemText(0, _translate("MainWindow", "Currency"))
        # self.currencyLabel1.setText(_translate("MainWindow", "0.0"))
        self.arrowLabel.setText(_translate("MainWindow", "--->"))
        self.dollarSign.setText(_translate("MainWindow", "$"))
        # self.currencyLabel.setText(_translate("MainWindow", "0.0"))
        # self.totalLabel.setText(_translate("MainWindow", "0.0"))

    # def _on_combobox_change(self, value):
    #     self.my_list = []
    #     self.country_curr = []
    #     self.currencyRate = []
    #     self.values = self.api.values
    #     self.my_list.append(self.values[4][1])
    #     for self.k, self.v in self.my_list[0].items():
    #         self.country_curr.append(self.k)
    #         self.currencyRate.append(self.v)
        
    #     for self.x in self.country_curr:
    #         if self.x in value:
    #             self.indexNumber = self.country_curr.index(value)
    #             self.currencyUpdate = self.currencyRate[self.indexNumber]
    #             self.to_str = str(self.currencyUpdate)
    #             self.currencyLabel1.setText(f"${self.to_str}")

    # def _on_combobox_change1(self, text):
    #     for self.x in self.country_curr:
    #         if self.x in text:
    #             self.indexNumber = self.country_curr.index(text)
    #             self.currencyUpdate1 = self.currencyRate[self.indexNumber]
    #             self.to_str = str(self.currencyUpdate1)
    #             self.currencyLabel.setText(f"${self.to_str}")

    def _on_click(self, value):
        self.text = str(self.combo1.currentText())
        self.text1 = str(self.combo2.currentText())
        self.amount = self.entryBox.text()
        print(self.text, self.text1, self.amount)  
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={self.amount}&From={self.text}&To={self.text1}"
        webbrowser.open(url)

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

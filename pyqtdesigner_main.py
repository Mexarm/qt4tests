#!/usr/bin/python
from PyQt4 import QtGui
import sys

import pyqtdesigner_ui
              

class ExampleApp(QtGui.QMainWindow, pyqtdesigner_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.btn_action)

    def btn_action(self):
        if self.radioButton.isChecked():
            self.radioButton.setChecked(False)
        else:    
            self.radioButton.setChecked(True)
        
def main():
    app = QtGui.QApplication(sys.argv) 
    form = ExampleApp()                
    form.show()                        
    sys.exit(app.exec_())              


if __name__ == '__main__':             
    main()                             

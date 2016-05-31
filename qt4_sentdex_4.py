import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("TiendaBip")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)

        #btn.resize(100,100)
        btn.resize(btn.sizeHint())
        #btn.resize(btn.minimumSizeHint())
        btn.move (100,100)
        
        
        self.show()

    def close_application(self):
        print ("Saliendo de tiendaBip")
        sys.exit()

def run():

    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

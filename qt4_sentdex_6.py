import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        #Window
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("TiendaBip")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        #Menu
        quitAction= QtGui.QAction("&Quit",self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setStatusTip("Salir de TiendaBip")
        quitAction.triggered.connect(self.close_application)

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu=mainMenu.addMenu("&File")
        fileMenu.addAction(quitAction)
        
        self.home()

    def home(self):
        #boton
        btn = QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)

        #btn.resize(100,100)
        btn.resize(btn.sizeHint())
        #btn.resize(btn.minimumSizeHint())
        btn.move (100,100)

        #toolbar
                                               #QAction(QIcon(icon), hover text, self)
        quitAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'),'Salir de TiendaBip',self)
        quitAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar('TiendabipToolbar')
        self.toolbar.addAction(quitAction)
        
        
        self.show()
    #Action 
    def close_application(self):
        print ("Saliendo de tiendaBip")
        sys.exit()

def run():

    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

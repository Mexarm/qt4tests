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
         
        #font choice          
        fontChoice = QtGui.QAction('Font',self)
        fontChoice.triggered.connect(self.font_choice)

        #self.toolbar = self.addToolBar('Font')
        self.toolbar.addAction(fontChoice)

        #color picker 
        color = QtGui.QColor(0, 0, 0)
        fontColor = QtGui.QAction('Font bg Color', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolbar.addAction(fontColor)


        #checkbox
        checkBox = QtGui.QCheckBox('Shrink Window',self)
        checkBox.move(100,150)
        checkBox.adjustSize()
        #checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)

        #progressbar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)
        btn2= QtGui.QPushButton("Download",self)
        btn2.move(200,120)
        btn2.clicked.connect(self.download)

        #dropdown
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("___",self)
        comboBox=QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("gtk+")
        comboBox.move(50,250)
        self.styleChoice.move(50,200)
        comboBox.activated[str].connect(self.style_choice)
        
        #, Calendar
        cal = QtGui.QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)
        
        
        self.show()

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
        
    def download(self):
        self.completed=0

        while self.completed < 100:
            self.completed +=0.001
            self.progress.setValue(self.completed)
            
        

    def enlarge_window(self,state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)
            

        
    #Action 
    def close_application(self):
        #7 messagebox
        choice = QtGui.QMessageBox.question(self, 'Salir de TiendaBip',
                                            'Seguro Desea Salir?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print('saliendo...')
                    
            sys.exit()
        else:
            pass
        

def run():

    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

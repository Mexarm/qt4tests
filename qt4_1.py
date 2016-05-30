import sys
from PyQt4.QtGui import *

from PyQt4.QtCore import QT_VERSION_STR
from PyQt4.Qt import PYQT_VERSION_STR
from sip import SIP_VERSION_STR

a = QApplication(sys.argv)       

w = QWidget()
w.resize(320, 240)
w.setWindowTitle("Hello World!") 

label = QLabel()
info = "Qt version:" + QT_VERSION_STR + \
       "\nSIP version:" + SIP_VERSION_STR + \
       "\nPyQt version:" + PYQT_VERSION_STR
label.setText(info)

hbox = QHBoxLayout()
hbox.addWidget(label)
w.setLayout(hbox)

w.show() 
 
sys.exit(a.exec_())

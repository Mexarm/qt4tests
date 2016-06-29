import sys
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
table = QtGui.QTableWidget(2,2)
combobox = QtGui.QComboBox()
combobox.addItem("")
combobox.addItem("Extra")
combobox.addItem("Combobox item 1")
combobox.addItem("Combobox item 2")
combobox.addItem("Combobox item 3")
label=QtGui.QLabel("Campo 1")
table.setCellWidget(0,0, label)
table.setCellWidget(0,1, combobox)
table.setHorizontalHeaderLabels( [ "Campo Original", "Nuevo Campo"] )
header = table.horizontalHeader()
header.setResizeMode(QtGui.QHeaderView.Stretch)

table.show()
app.exec_()

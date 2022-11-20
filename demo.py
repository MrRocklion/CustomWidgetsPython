import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from CustomLine import PyLineEdit
from CustomButton import PyPushButton
from CustomListButton import  CustomListButton


class MyCustomWidget(QWidget):
    def __init__(self, name, parent=None):
        super(MyCustomWidget, self).__init__(parent)

        self.row = QHBoxLayout()

        self.row.addWidget(QLabel(name))
        self.row.addWidget(QPushButton("view"))
        self.row.addWidget(QPushButton("select"))

        self.setLayout(self.row)



class MainWindow(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(400, 350)
        self.container = QFrame() #contenedor principal
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container {background-color: #222}")
        self.layout = QGridLayout()
        #agreamos widgets
        self.titulo = QLabel("Widgets Personalizados \n  V0.1 By David Diaz")
        self.titulo.setStyleSheet('QLabel{color:white;font:30px}')
        self.lista = CustomListButton(data=["Juan","Miguel","Andres","Ernesto"])
        #TEXTFIELDS
        self.textfield = PyLineEdit(place_holder_text="Ingresa Tu Nombre",width=200)
        #creamos los botones
        self.button = PyPushButton(width=200,text="Agregar",radius=3,color='#58D68D' ,bg_color_pressed='#28B463',bg_color_hover='#82E0AA')
        #agregamos los widgets al grid
        self.layout.addWidget(self.titulo,0,1,Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.textfield, 1,1, Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.button, 2, 1, Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.lista, 3, 1, Qt.AlignmentFlag.AlignCenter)
        #centramos
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

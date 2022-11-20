from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

style = '''
QListWidget {{
	background-color: {_bg_color};
	color: "#fff";
	border-radius:10px;
	radius: 3px solid #fff;

	
}}

'''


class CustomListButton(QListWidget):
    def __init__(
            self,
            bg_color="#333",
            data = ["opcion 1","opcion 2"]
    ):
        super().__init__()
        self.set_Style(
            bg_color,
        )
        self.addData(data)
        self.setMinimumWidth(300)

    def set_Style(
        self,
        bg_color,
    ):
        style_format = style.format(
            _bg_color = bg_color,
        )
        self.setStyleSheet(style_format)
    def addData(self,data):
        for i in data:
            item = QListWidgetItem(self)
            self.addItem(item)
            row = MyCustomWidget(i)
            item.setSizeHint(row.minimumSizeHint())
            self.setItemWidget(item,row)

class MyCustomWidget(QWidget):
    def __init__(self, title, parent=None):
        super(MyCustomWidget, self).__init__(parent)
        self.title = QLabel(title)
        self.title.setStyleSheet('''
        QLabel{
            color:#fff;
        }
        ''')
        self.editar =  QPushButton("EDITAR")
        self.editar.setStyleSheet('''
        QPushButton{
            color: #283747 ;
            width:80px;
            background-color: #F4D03F ;
            border-radius: 5px;
            height:30px;
            radius: 1px solid #fff;
        }
        QPushButton:pressed{
            background-color: #D4AC0D;
            color: white;
        }
        ''')
        self.eliminar = QPushButton("ELIMINAR")
        self.eliminar.setStyleSheet('''
        QPushButton{
            color:#283747 ;
            width:80px;
            background-color: #EC7063;
            border-radius: 5px;
            height:30px;
            radius: 1px solid #fff;
            margin-right:20px
        }
        QPushButton:pressed{
            background-color: #A93226;
            color: white;
        }
        ''')
        self.row = QHBoxLayout()
        self.row.addWidget(self.title)
        self.row.addWidget(self.editar)
        self.row.addWidget(self.eliminar)
        self.setLayout(self.row)



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from spider import THREAD

class graphic_interface(QWidget):
    def __init__(self,parent=None) -> None:
        super().__init__(parent)
        self.layout_main = QFormLayout()

        font = QFont()
        self.resize(500,100)
        font.setPointSize(20)   #括号里的数字可以设置成自己想要的字体大小
        self.setWindowTitle('微信公众号文章转换')  

        self.url = QLineEdit()
        self.url.setPlaceholderText("输入网址")

        self.doc_name = QLineEdit()
        self.doc_name.setText("1.docx")

        self.button = QPushButton()
        self.button.clicked.connect(self.run)
        self.button.setText("运行")
        self.status = "FREE"

        
    
        self.layout_main.addRow("网址",self.url)
        self.layout_main.addRow("文档名",self.doc_name)
        self.layout_main.addWidget(self.button)
        self.setLayout(self.layout_main)

    def run(self):
        url = self.url.text()
        doc_name = self.doc_name.text()
        self.THREAD = THREAD(url,doc_name)
        self.THREAD._signal.connect(self.call_backlog)
        self.change_button_status()
   
        self.THREAD.start()
        #self.change_button_status()
    
    def call_backlog(self,msg):
        self.change_button_status()
        QMessageBox.about(self, "提示", '已成功生成文件')

    def change_button_status(self):

        if self.status == 'FREE':
            self.button.setEnabled(False)
            self.button.setText("正在运行")
            self.status = 'RUNNING'
            #self.setLayout(self.layout_main)
        else:
            self.button.setEnabled(True)
            self.button.setText("运行")
            self.status = 'FREE'
            #self.setLayout(self.layout_main)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = graphic_interface()
    tool.show()
    sys.exit(app.exec_())
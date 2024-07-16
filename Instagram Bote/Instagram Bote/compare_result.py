from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QTextCharFormat, QColor

class CompareWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.initUI(data)

    def initUI(self, data):
        self.setWindowTitle("Comparison Results")
        
        layout = QVBoxLayout()
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        
        # Renkli metin formatı oluşturma
        format_not_following_back = QTextCharFormat()
        format_not_following_back.setForeground(QColor("red"))
        
        format_not_followed_back = QTextCharFormat()
        format_not_followed_back.setForeground(QColor("red"))
        
        # Metin içeriğini ayarlama
        cursor = self.result_text.textCursor()
        cursor.movePosition(cursor.End)
        
        cursor.insertText("Not Following Back:\n", format_not_following_back)
        cursor.insertText(data.split("\n\n")[0] + "\n\n", QTextCharFormat())
        
        cursor.insertText("Not Followed Back:\n", format_not_followed_back)
        cursor.insertText(data.split("\n\n")[1], QTextCharFormat())
        
        layout.addWidget(self.result_text)
        
        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 300)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = CompareWindow("Results")
    window.show()
    sys.exit(app.exec_())

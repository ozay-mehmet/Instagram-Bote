from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QApplication
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
        format_not_followed_back.setForeground(QColor("blue"))
        
        # Metin içeriğini ayarlama
        cursor = self.result_text.textCursor()
        cursor.movePosition(cursor.End)
        
        # Veriyi satır satır okuyarak renkli olarak ekleme
        lines = data.splitlines()
        current_format = None
        for line in lines:
            if line.startswith("Not Following Back:") or line.startswith("Not Followed Back:"):
                if line.startswith("Not Following Back:"):
                    current_format = format_not_following_back
                elif line.startswith("Not Followed Back:"):
                    current_format = format_not_followed_back
                cursor.insertText(line + "\n", current_format)
            else:
                cursor.insertText(line + "\n")
        
        layout.addWidget(self.result_text)
        
        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 300)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = CompareWindow("Not Following Back:\nUser1\nUser2\n\nNot Followed Back:\nUser3\nUser4")
    window.show()
    sys.exit(app.exec_())

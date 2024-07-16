from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from insta import Insta
from compare_result import CompareWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Instagram Login')
        
        layout = QVBoxLayout()

        self.label_username = QLabel('Username:')
        layout.addWidget(self.label_username)
        self.entry_username = QLineEdit(self)
        layout.addWidget(self.entry_username)
        
        self.label_password = QLabel('Password:')
        layout.addWidget(self.label_password)
        self.entry_password = QLineEdit(self)
        self.entry_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.entry_password)
        
        self.button_login = QPushButton('Login', self)
        self.button_login.clicked.connect(self.on_login_click)
        layout.addWidget(self.button_login)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 150)

    def on_login_click(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if username and password:
            try:
                insta = Insta(username, password)
                insta.login()
                insta.get_follow()
                insta.get_followers()
                insta.compare_follows_and_followers()
                insta.close_insta()
                self.show_compare_result()
                self.hide() 
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Warning", "Please enter your username and password!")

    def show_compare_result(self):
        try:
            with open("compare.txt", "r", encoding='utf-8') as file:
                data = file.read()
            
            self.result_window = CompareWindow(data)
            self.result_window.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while reading the results: {e}")

if __name__ == '__main__':
    app = QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec_()

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtWidgets import QPlainTextEdit, QLabel,QMessageBox,QRadioButton
from PySide2.QtWidgets import QLineEdit
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtWidgets
import student_login, teacher_login, admin_login
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        #super().__init__()
        self.ui = QUiLoader().load('login.ui')
        self.ui.login.clicked.connect(self.login_function)
        self.admin_acc_paswrd = {}
        self.stu_acc_paswrd = {}
        self.tea_acc_paswrd = {}
        self.tem = QLineEdit()
        self.tem.text()
    def login_function(self):
        if self.ui.admin.isChecked():
            print("admin login")
            self.admin_login()
            return
        elif self.ui.student.isChecked():
            print("student login")
            self.student_login()
            return
        elif self.ui.teacher.isChecked():
            print("teacher login")
            self.teacher_login()
            return
        else:
            return False

    def admin_login(self):
        print(self.ui.account_input.text())
        self.admin = admin_login.Admin_Login()
        self.admin.ui.show()
        #self.ui.close()

    def student_login(self):
        self.student = student_login.Student_Login()
        self.student.ui.show()
        #self.ui.close()

    def teacher_login(self):
        self.teacher = teacher_login.Teacher_Login()
        self.teacher.ui.show()
        #self.ui.close()

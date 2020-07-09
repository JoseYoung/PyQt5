from PySide2.QtUiTools import QUiLoader
import student_choose_class
class Student_Login():
    def __init__(self):
        self.ui = QUiLoader().load('student.ui')
        self.ui.exit.clicked.connect(self.close_window)
        self.ui.choose.clicked.connect(self.choose_class)
    def close_window(self):
        self.ui.close()
    def choose_class(self):
        self.choose_window = student_choose_class.Student_Choose()
        self.choose_window.ui.show()


from PySide2.QtUiTools import QUiLoader
import teacher_modify
class Teacher_Login():
    def __init__(self):
        self.ui = QUiLoader().load('teacher.ui')
        self.ui.exit.clicked.connect(self.close_window)
        self.ui.modify.clicked.connect(self.modify_score)
    def close_window(self):
        self.ui.close()

    def modify_score(self):
        self.modify_window = teacher_modify.Teacher_Modify()
        self.modify_window.ui.show()

from PySide2.QtUiTools import QUiLoader

class Student_Choose():
    def __init__(self):
        self.ui = QUiLoader().load('student_choose_class.ui')
        self.ui.exit.clicked.connect(self.close_window)
        self.ui.add.clicked.connect(self.add)
    def close_window(self):
        self.ui.close()
    def add(self):
        self.courseID = self.ui.courseID.text()
        print("adding "+self.courseID)
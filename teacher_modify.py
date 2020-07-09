from PySide2.QtUiTools import QUiLoader

class Teacher_Modify():
    def __init__(self):
        self.ui = QUiLoader().load('teacher_modify_score.ui')
        self.ui.ok.clicked.connect(self.close_window)

    def close_window(self):
        self.studentID = self.ui.studentID_line.text()
        self.courseID  = self.ui.courseID_line.text()
        self.score     = self.ui.score_line.text()
        print(self.studentID)
        print(self.courseID)
        print(self.score)
        self.ui.close()

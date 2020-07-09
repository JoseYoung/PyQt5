from PySide2.QtUiTools import QUiLoader
import admin_modify, admin_add, admin_delete, admin_query_choose_score, admin_score_data
class Admin_Login():
    def __init__(self):
        self.ui = QUiLoader().load('admin.ui')

        self.ui.modify.clicked.connect(self.modify)
        self.ui.add.clicked.connect(self.add)
        self.ui.remove.clicked.connect(self.remove)
        self.ui.exit.clicked.connect(self.close_window)
        self.ui.query_choose_score.clicked.connect(self.query_choose_score)
        self.ui.avg_score.clicked.connect(self.avg_score)

        self.ui.query_student.clicked.connect(self.query_student)
        self.ui.query_teacher.clicked.connect(self.query_teacher)
        self.ui.query_course.clicked.connect(self.query_course)



    def modify(self):
        self.modify_window = admin_modify.Admin_Modify()
        self.modify_window.ui.show()
    def add(self):
        self.add_window = admin_add.Admin_Add()
        self.add_window.ui.show()

    def remove(self):
        self.delete_window = admin_delete.Admin_Delete()
        self.delete_window.ui.show()

    def close_window(self):
        self.ui.close()

    def query_choose_score(self):
        self.query_choose_score_window = admin_query_choose_score.Admin_Choose_Score()
        self.query_choose_score_window.ui.show()

    def avg_score(self):
        self.score_data_window = admin_score_data.Admin_Score_Data()
        self.score_data_window.ui.show()

    def query_student(self):
        pass

    def query_teacher(self):
        pass

    def query_course(self):
        pass
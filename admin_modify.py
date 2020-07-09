from PySide2.QtUiTools import QUiLoader

class Admin_Modify():
    def __init__(self):
        self.ui = QUiLoader().load('admin_modify.ui')
        self.ui.exit.clicked.connect(self.close_window)
        self.ui.ok.clicked.connect(self.make_change)


    def close_window(self):
        self.ui.close()


    def make_change(self):
        self.column = self.ui.column_input.text()
        self.ID     = self.ui.id_input.text()
        self.value  = self.ui.value_input.text()

        if self.ui.radio_student.isChecked():
            self.modify_student(self.column, self.ID, self.value)

        elif self.ui.radio_teacher.isChecked():
            self.modify_teacher(self.column, self.ID, self.value)

        elif self.ui.radio_course.isChecked():
            self.modify_course(self.column, self.ID, self.value)

        elif self.ui.radio_choose.isChecked():
            self.modify_choose(self.column, self.ID, self.value)
    def modify_teacher(self, column, ID, value):
        pass

    def modify_student(self, column, ID, value):
        pass

    def modify_course(self, column, ID, value):
        pass

    def modify_choose(self, column, ID, value):
        pass
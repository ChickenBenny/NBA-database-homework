import sys
import backend
import pandas as pd
from PyQt5 import QtWidgets, QtGui, QtCore, QTableWidgetItem
from frontend.view import Ui_MainWindow



class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.pushButton.clicked.connect(self.branch_operation)

    def branch_operation(self):
        index, column, table, info, limit = self.get_info()
        if index == 0 and column and table and limit:
            rows = backend.select_from_where(column, table, limit)
            self.ui.tableView.setRowCount(len(rows))

    
    def get_info(self):
        index = self.ui.menu.currentIndex()
        column = self.ui.lineEdit_column.text()
        table = self.ui.lineEdit_table.text()
        info = self.ui.lineEdit_information.text()
        limit = self.ui.lineEdit_limit.text()
        return index, column, table, info, limit


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
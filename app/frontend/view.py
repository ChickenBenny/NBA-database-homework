import psycopg2

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self):
        self.database = "postgres"
        self.user = "postgres"
        self.password = "postgres"
        self.host = "127.0.0.1"
        self.port = "5432"        
    
    def setupUi(self, MainWindow):

        font = QtGui.QFont('Helvetica')
        font.setBold(True)
        font.setPixelSize(20)

        self.conn = psycopg2.connect(
            database = self.database,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port            
        )

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('background-color: rgba(29, 82, 171, 10%)')

        self.buttonbox_info = QtWidgets.QGroupBox(self.centralwidget)
        self.buttonbox_info.setGeometry(QtCore.QRect(10, 30, 241, 111))
        self.buttonbox_info.setObjectName("groupBox")
        self.buttonbox_info.setFont(font)

        self.buttonbox = QtWidgets.QGroupBox(self.centralwidget)
        self.buttonbox.setGeometry(QtCore.QRect(250, 30, 950, 111))
        self.buttonbox.setObjectName("groupBox_2")
        self.buttonbox.setFont(font)

        self.querybox_info = QtWidgets.QGroupBox(self.centralwidget)
        self.querybox_info.setGeometry(QtCore.QRect(10, 140, 241, 111))
        self.querybox_info.setObjectName("groupBox_3")
        self.querybox_info.setFont(font)
        font.setBold(True)
        font.setPixelSize(14)
        self.comboBox = QtWidgets.QComboBox(self.buttonbox)
        self.comboBox.setFont(font)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 211, 41))
        self.comboBox.setStyleSheet("""QComboBox {background-color: rgba(255, 255, 255, 100%); selection-background-color: rgba(255, 255, 255, 100%); selection-color: black}""")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('SELECT-FROM-WHERE')
        self.comboBox.addItem('DELETE')
        self.comboBox.addItem('INSERT')
        self.comboBox.addItem('UPDATE')
        self.comboBox.addItem('IN')
        self.comboBox.addItem('NOT IN')
        self.comboBox.addItem('EXISTS')
        self.comboBox.addItem('NOT EXISTS')
        self.comboBox.addItem('COUNT')
        self.comboBox.addItem('SUM')
        self.comboBox.addItem('MAX')
        self.comboBox.addItem('MIN')
        self.comboBox.addItem('AVG')
        self.comboBox.addItem('HAVING')
        self.comboBox.activated.connect(self.showInfo)

        font.setPixelSize(18)
        font.setBold(False)
        self.showbutton_result = QtWidgets.QPushButton(self.buttonbox)
        self.showbutton_result.setGeometry(QtCore.QRect(70, 70, 81, 31))
        self.showbutton_result.setStyleSheet('background-color: rgba(255, 255, 255, 80%)')
        self.showbutton_result.clicked.connect(lambda: self.kernel(None))
        self.showbutton_result.setFont(font)

        self.clearbutton_result = QtWidgets.QPushButton(self.buttonbox)
        self.clearbutton_result.setGeometry(QtCore.QRect(160, 70, 75, 31))
        self.clearbutton_result.setStyleSheet('background-color: rgba(255, 255, 255, 80%)')
        self.clearbutton_result.clicked.connect(lambda: self.clearOutput(self.infoBrowser))
        self.clearbutton_result.setFont(font)

        self.showquery_result = QtWidgets.QPushButton(self.centralwidget)
        self.showquery_result.setGeometry(QtCore.QRect(1000, 220, 81, 31))
        self.showquery_result.setStyleSheet('background-color: rgba(255, 255, 255, 80%)')
        self.showquery_result.clicked.connect(lambda: self.getInput(self.queryBrowser))
        self.showquery_result.setFont(font)

        self.clearquery_result = QtWidgets.QPushButton(self.centralwidget)
        self.clearquery_result.setGeometry(QtCore.QRect(1105, 220, 71, 31))
        self.clearquery_result.setStyleSheet('background-color: rgba(255, 255, 255, 80%)')
        self.clearquery_result.clicked.connect(lambda: self.clearOutput(self.queryBrowser))
        self.clearquery_result.setFont(font)

        self.clear_result = QtWidgets.QPushButton(self.centralwidget)
        self.clear_result.setGeometry(QtCore.QRect(1105, 740, 71, 30))
        self.clear_result.setStyleSheet('background-color: rgba(255, 255, 255, 80%)')
        self.clear_result.setText('Clear')
        self.clear_result.clicked.connect(lambda: self.clearOutput(self.resultBrowser))
        self.clear_result.setFont(font)

        self.clear_all = QtWidgets.QPushButton(self.centralwidget)
        self.clear_all.setGeometry(QtCore.QRect(10, 740, 81, 30))
        self.clear_all.setStyleSheet('background-color: rgba(255, 255, 255, 80%)')
        self.clear_all.setText('Clear ALL')
        self.clear_all.clicked.connect(lambda: self.clearOutput(None))
        self.clear_all.setFont(font)

        self.queryBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.queryBrowser.setGeometry(QtCore.QRect(260, 150, 930, 61))
        self.queryBrowser.setStyleSheet('background-color: rgba(255, 255, 255, 80%)')
        self.queryBrowser.setFont(font)

        font.setPixelSize(20)
        font.setBold(True)
        
        self.query_label = QtWidgets.QLabel(self.centralwidget)
        self.query_label.setGeometry(QtCore.QRect(260, 220, 400,20))
        self.query_label.setText("Type some POSTGRES query up here ↑")
        self.query_label.setFont(font)
        self.query_label.setStyleSheet('background-color: transparent')
        
        self.resultBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.resultBrowser.setGeometry(QtCore.QRect(10, 260, 1181, 471))
        self.resultBrowser.setStyleSheet('background-color: rgba(255, 255, 255, 80%)')
        self.resultBrowser.setFont(font)

        self.infoBrowser = QtWidgets.QTextBrowser(self.buttonbox)
        self.infoBrowser.setGeometry(QtCore.QRect(240, 20, 700, 81))
        self.infoBrowser.setStyleSheet('background-color: rgba(255, 255, 255, 100%)')
        font.setPixelSize(20)
        self.infoBrowser.setFont(font)
        self.infoBrowser.append('選取目前在洋基球隊打球的 MLB 球員')
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        # Variable
        # to store the query
        self.current_text = ["SELECT player_ssn, first_name, last_name FROM player AS P, team AS T WHERE T.team_name='New York Yankees' AND P.current_team=T.team_id;"]
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        # window trivials design
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def kernel(self,object):
        if object != None:
            # query
            # SQL is already on textEdit
            pass
        else:
            # button
            # append default scenario on textEdit
            for query in self.current_text:
                self.queryBrowser.append(query)
        try:
            for query in self.current_text:
                temp = ""
                format_config = "\t\t"
                cursor = self.conn.cursor()
                print(query)
                cursor.execute(query)
                rows = cursor.fetchall()
                if cursor.description:
                    for title in cursor.description:
                        temp = temp + str(title[0])
                        temp = temp + "\t"
                    self.resultBrowser.append(temp)
                    for row in rows:
                        text = ""
                        for item in row:
                            text = text + str(item)
                            text = text + format_config
                        self.resultBrowser.append(str(text))
                    self.resultBrowser.append('\n')
                self.conn.commit()            
            cursor.close()

        except Exception as ex: # catch exception 
            self.resultBrowser.append("There is something wrong!") # warning message
            self.resultBrowser.append(str(ex)) # exception message

    def getInput(self, object): # function to get user input sql
        text = object.toPlainText()
        self.current_text = text
        self.kernel(self.queryBrowser) # execute query

    def clearOutput(self, object): # function to clear the text of passed object
        if object != None:
            object.clear() # target object
        else:
            self.infoBrowser.clear() # clear all browser
            self.queryBrowser.clear() #
            self.resultBrowser.clear() #

    def showInfo(self): # default scenario establishment
        text = self.comboBox.currentText()
        output = None
        if text == 'SELECT-FROM-WHERE':
            output = '選取目前在洋基球隊打球的 MLB 球員'
            self.current_text = ["SELECT player_ssn, first_name, last_name FROM player AS P, team AS T WHERE T.team_name='New York Yankees' AND P.current_team=T.team_id;"]
        elif text == 'DELETE':
            output = '因為太空人隊作弊事件，目前球團解散，刪除所有在太空人隊打球的球員資料'
            self.current_text = [
                "SELECT player_ssn, first_name, last_name FROM player AS P, team AS T WHERE T.team_name='Houston Astros' AND P.current_team=T.team_id;",
                "DELETE FROM player WHERE player_ssn IN(SELECT P.player_ssn FROM player AS P, team AS T WHERE T.team_name='Houston Astros' AND P.current_team=T.team_id);",
                "SELECT player_ssn, first_name, last_name FROM player AS P, team AS T WHERE T.team_name='Houston Astros' AND P.current_team=T.team_id"
            ]
        elif text == 'INSERT':
            output = '插入新咖啡師佑恩的經驗'
            self.current_text = 'SELECT e_user_id, user_name ,e_dscrp FROM exp, user_info WHERE e_user_id=user_id AND e_user_id=5;INSERT INTO exp (e_user_id, e_bean_id, e_proc_id, e_dscrp, e_temp, e_time, e_weight) VALUES (5, 9, 3, \'避免過萃取，水柱力道分散在圓錐每個半徑軌道上\', 90, 72, 20); SELECT e_user_id, user_name ,e_dscrp FROM exp, user_info WHERE e_user_id=user_id AND e_user_id=5;'
        elif text == 'UPDATE':
            output = '將小萬升級為傳說級達人咖啡師'
            self.current_text = "SELECT user_name, user_dscrp FROM user_info WHERE user_name=\'小萬\';UPDATE user_info SET user_dscrp=\'傳說級達人咖啡師\' WHERE user_name=\'小萬\'; SELECT user_name, user_dscrp FROM user_info WHERE user_name=\'小萬\';"
        elif text == 'IN':
            output = '找出資歷不到一年、一到五年的咖啡師'
            self.current_text = "SELECT user_name, user_tenure, user_dscrp FROM user_info WHERE user_tenure IN (0, 1, 2, 3, 4, 5);"
        elif text == 'NOT IN':
            output = '找出敘述不為達人以下的咖啡師'
            self.current_text = "SELECT user_name, user_tenure, user_dscrp FROM user_info WHERE user_dscrp NOT IN (\'準達人咖啡師\', \'達人咖啡師\', \'特A達人咖啡師\');"
        elif text == 'EXISTS':
            output = '找出使用過手沖法沖泡咖啡的人'
            self.current_text = 'SELECT user_id, user_name FROM user_info WHERE EXISTS (SELECT e_user_id FROM exp WHERE user_id = e_user_id AND e_proc_id IN (SELECT process_id FROM process WHERE method IN (\'手沖濾掛\', \'手沖梯形濾杯\', \'手沖圓錐濾杯\')));'
        elif text == 'NOT EXISTS':
            output = '找出沒有使用過深焙咖啡豆的人'
            self.current_text = 'SELECT user_id, user_name FROM user_info WHERE NOT EXISTS (SELECT e_user_id FROM exp WHERE user_id = e_user_id AND e_bean_id IN (SELECT bean_id FROM bean_info WHERE category_id IN (SELECT roast_id FROM roast WHERE roast_name IN (\'深焙\', \'直火深焙\'))));'
        elif text == 'COUNT':
            output = '找出資料庫有幾種咖啡豆'
            self.current_text = 'SELECT COUNT(bean_id) FROM bean_info'
        elif text == 'SUM':
            output = '找出小萬全部經驗的總花費'
            self.current_text = 'SELECT SUM(cost) FROM device WHERE device_id IN (SELECT device_device_id FROM method_need_device WHERE process_process_id IN (SELECT process_id FROM process, exp, user_info WHERE process_id = e_proc_id AND e_user_id = user_id AND user_name=\'小萬\'))'
        elif text == 'MAX':
            output = '找出使用者中年資最大的'
            self.current_text = 'SELECT user_name, user_tenure FROM user_info WHERE user_tenure IN (SELECT MAX(user_tenure) FROM user_info)'
        elif text == 'MIN':
            output = '找出使用者中年資最小的'
            self.current_text = 'SELECT user_name, user_tenure FROM user_info WHERE user_tenure IN (SELECT MIN(user_tenure) FROM user_info)'
        elif text == 'AVG':
            output = '找出國佑平均沖泡咖啡使用的溫度'
            self.current_text = 'SELECT AVG(e_temp) FROM exp WHERE e_user_id IN (SELECT user_id FROM user_info WHERE user_name = \'國佑\')'
        elif text == 'HAVING':
            output = '找出使用者經驗平均使用豆重大於15克的使用者'
            self.current_text = 'SELECT user_id, user_name, AVG(e_weight) FROM user_info, exp WHERE user_id = e_user_id GROUP BY user_id HAVING AVG(e_weight) > 15;'
        self.infoBrowser.append(output) # Print scenairo

    def retranslateUi(self, MainWindow): # Format, set Style of UI
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple DBMS User Interface"))
        self.buttonbox_info.setStyleSheet('background-color: rgba(29, 82, 171, 50%)')
        self.buttonbox_info.setTitle(_translate("MainWindow", "Button"))
        self.buttonbox.setTitle(_translate("MainWindow", "information"))
        self.buttonbox.setStyleSheet('background-color: rgba(29, 82, 171, 30%)')
        self.showbutton_result.setText(_translate("MainWindow", "Show"))
        self.clearbutton_result.setText(_translate("MainWindow", "Clear"))
        self.querybox_info.setTitle(_translate("MainWindow", "Query"))
        self.querybox_info.setStyleSheet('background-color: rgba(29, 82, 171, 50%)')
        self.showquery_result.setText(_translate("MainWindow", "Show"))
        self.clearquery_result.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__": # main
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

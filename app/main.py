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
            pass
        else:
            for query in self.current_text:
                self.queryBrowser.append(query)
        text = self.comboBox.currentText()
        if text == 'SELECT-FROM-WHERE':
            self._select_from_where()
        elif text == 'DELETE':
            self._delete()
        elif text == 'INSERT':
            self._insert()
        elif text == 'UPDATE':
            self._update()
        elif text == 'IN':
            self._in()
        elif text == 'NOT IN':
            self._not_in()
        elif text == 'EXISTS':
            self._exists()
        

    def _show_result(self, cursor, rows, space):
        temp = ""
        format_config = "\t\t"
        if cursor.description:
            for title in cursor.description:
                temp = temp + str(title[0])
                if space == 1:
                    temp = temp + "\t"
                else:
                    temp = temp + "\t\t"
            self.resultBrowser.append(temp)
            for row in rows:
                text = ""
                for item in row:
                    text = text + str(item)
                    text = text + format_config
                self.resultBrowser.append(str(text))
            self.resultBrowser.append('\n')

    def _select_from_where(self):
        query = "SELECT player_ssn, first_name, last_name FROM player AS P, team AS T WHERE T.team_name='New York Yankees' AND P.current_team=T.team_id;"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 1)
        cursor.close()

    def _delete(self):
        query = "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)

        query = "DELETE FROM game WHERE game_id IN(SELECT G.game_id FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros');"
        cursor.execute(query)
        self.conn.commit()

        query = "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)    

    def _insert(self):
        query = "INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-29', '16', '29', '18', '1');"
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()         

        query = "INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-23', '17', '29', '18', '1');"
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()   

        query = "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)    

    def _update(self):
        query = "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros' AND G.dt='2022-10-29';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2) 

        query = "UPDATE game SET dt='2022-11-02' WHERE game_id IN(SELECT G.game_id FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros' AND G.dt='2022-10-29');"                 
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()     

        query = "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros' AND G.dt='2022-11-2';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)  

    def _in(self):
        query = "SELECT H.player_id AS id, H.position, P.first_name AS fName, P.last_name AS lName FROM hitter_stats AS H, player AS P WHERE H.player_ssn IN (SELECT H.player_ssn WHERE H.player_ssn=P.player_ssn AND H.position IN ('3B'));"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)        

    def _not_in(self):
        query = "SELECT P.player_id AS id, PY.first_name AS fname, PY.last_name AS lname, P.era, P.win FROM pitcher_stats AS P, player AS PY WHERE P.player_ssn NOT IN (SELECT player_ssn FROM pitcher_stats WHERE era >= '0' AND era < '2') AND PY.player_ssn=P.player_ssn;"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)     

    def _exists(self):
        query = "SELECT G.game_id, R.ref_id, R.ref_name FROM game AS G, referee AS R WHERE EXISTS (SELECT 1 WHERE G.dt='2022-10-15' AND R.ref_id=G.ref_id);"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)                       

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
            output = '因為太空人隊作弊事件，目前球對遭禁賽，取消10/20後在太空人主場的比賽'
            self.current_text = [
                "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros';",
                "DELETE FROM game WHERE game_id IN(SELECT G.game_id FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros');",
                "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros';",
            ]
        elif text == 'INSERT':
            output = '由於現在是世界大賽，太空人球團極力抗議，因此聯盟將主場球賽重新加回一場至賽事表'
            self.current_text = [
                "INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-29', '16', '29', '18', '1');",
                "INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-23', '17', '29', '18', '1');",
                "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros';",
            ]
        elif text == 'UPDATE':
            output = '太空人對決費城人在10/29的比賽因為遇到暴雨，因此延期到11/2號'
            self.current_text = [
                "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros' AND G.dt='2022-10-29';",
                "UPDATE game SET dt='2022-11-02' WHERE game_id IN(SELECT G.game_id FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros' AND G.dt='2022-10-29');"
                "SELECT G.dt, G.game_id, G.home_team, T.team_name FROM game as G, team as T WHERE G.home_team=T.team_id AND T.team_name='Houston Astros' AND G.dt='2022-11-2';",
            ]
        elif text == 'IN':
            output = '找出防守位置是3B的打者'
            self.current_text = ["SELECT H.player_id AS id, H.position, P.first_name AS fName, P.last_name AS lName FROM hitter_stats AS H, player AS P WHERE H.player_ssn IN (SELECT H.player_ssn WHERE H.player_ssn=P.player_ssn AND H.position IN ('3B'));"]
        elif text == 'NOT IN':
            output = '找出防禦率不再2以內的投手'
            self.current_text = ["SELECT P.player_id AS id, PY.first_name AS fname, PY.last_name AS lname, P.era, P.win FROM pitcher_stats AS P, player AS PY WHERE P.player_ssn NOT IN (SELECT player_ssn FROM pitcher_stats WHERE era >= '0' AND era < '2') AND PY.player_ssn=P.player_ssn;"]
        elif text == 'EXISTS':
            output = '找出 2022-10-15 有出場判決的裁判'
            self.current_text = ["SELECT G.game_id, R.ref_id, R.ref_name FROM game AS G, referee AS R WHERE EXISTS (SELECT 1 WHERE G.dt='2022-10-15' AND R.ref_id=G.ref_id);"]
        elif text == 'NOT EXISTS':
            output = '找出全壘打不足兩隻的打者'
            self.current_text = ["SELECT H.player_id AS id, H.position, P.first_name AS fname, P.last_name AS lname from"]
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

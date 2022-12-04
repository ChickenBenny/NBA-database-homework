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
        self.infoBrowser.append('列出主隊球場在 California 的球隊')
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
        elif text == "NOT EXISTS":
            self._not_exists()
        elif text == "COUNT":
            self._count()
        elif text == "SUM":
            self._sum()
        elif text == "MAX":
            self._max()
        elif text == 'MIN':
            self._min()
        elif text == "AVG":
            self._avg()
        elif text == "HAVING":
            self._having()
        

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
        query = "SELECT T.team_name AS Full_name_of_team, S.stadium_name AS Stadium_name, S.stadium_state AS Stadium_state FROM team AS T, stadium AS S WHERE T.stadium=S.stadium_id AND S.stadium_state='California';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)
        cursor.close()

    def _delete(self):
        query = "SELECT G.dt AS Date_of_the_game, G.game_id, S.stadium_name, S.stadium_state FROM game AS G, stadium AS S WHERE G.stadium=S.stadium_id AND S.stadium_state='Illinois';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)

        query = "DELETE FROM game WHERE game_id IN(SELECT G.game_id FROM game AS G, stadium AS S WHERE G.stadium=S.stadium_id AND S.stadium_state='Illinois');"
        cursor.execute(query)
        self.conn.commit()

        query = "SELECT G.dt AS Date_of_the_game, G.game_id, S.stadium_name, S.stadium_state FROM game AS G, stadium AS S WHERE G.stadium=S.stadium_id AND S.stadium_state='Illinois';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)    

    def _insert(self):
        query = "INSERT INTO game(game_id, dt, score, stadium, home, away) VALUES(21, '2022-11-2', '108-99', '6', '6', '16');"
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()         

        query = "SELECT G.dt AS Date_of_the_game, S.stadium_name, S.stadium_state AS state, G.score FROM game AS G, stadium as S WHERE G.stadium=S.stadium_id AND game_id=21 AND dt='2022-11-2';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)    

    def _update(self):
        query = "SELECT N.first_name AS Fname, N.last_name AS Lname, T.team_name FROM nba_player AS N, team AS T WHERE N.current_team=T.team_id AND N.first_name='Jayson' AND N.last_name='Tatum';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2) 

        query = "UPDATE nba_player SET current_team=7 WHERE player_id IN(SELECT player_id FROM nba_player WHERE first_name='Jayson' AND last_name='Tatum');"                 
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()     

        query = "SELECT N.first_name AS Fname, N.last_name AS Lname, T.team_name FROM nba_player AS N, team AS T WHERE N.current_team=T.team_id AND N.first_name='Jayson' AND N.last_name='Tatum';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)  

    def _in(self):
        query = "SELECT first_name AS Fname, last_name AS Lname FROM nba_player WHERE player_id IN (SELECT N.player_id FROM nba_player AS N, team AS T WHERE N.position='G' AND N.current_team=T.team_id AND T.team_id=27);"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)        

    def _not_in(self):
        query = "SELECT first_name AS Fname, last_name AS Lname, height FROM nba_player WHERE player_id NOT IN(SELECT player_id FROM nba_player WHERE height>=7.0) AND position='C';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)     

    def _exists(self):
        query = "SELECT G.dt AS Date_of_the_game, S.stadium_name FROM stadium AS S, game AS G WHERE EXISTS (SELECT 1 WHERE G.dt='2022-11-2' AND G.stadium=S.stadium_id);"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)          

    def _not_exists(self):
        query = "SELECT team_name FROM team WHERE NOT EXISTS (SELECT 1 WHERE champ!=0);" 
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)    

    def _count(self):
        query = "SELECT COUNT(team_id) FROM team;"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)

    def _sum(self):
        query = "SELECT SUM(champ) FROM team WHERE team_name='Boston Celtics' OR team_name='Los Angeles Lakers';"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)

    def _max(self):
        query = "SELECT first_name AS Fname, last_name AS Lname, MAX(height) FROM nba_player GROUP BY player_id ORDER BY MAX(height) DESC LIMIT 1;"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2)        

    def _min(self):
        query = "SELECT first_name AS Fname, last_name AS Lname, MIN(height) FROM nba_player GROUP BY player_id ORDER BY MIN(height) ASC LIMIT 1;"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2) 

    def _avg(self):
        query = "SELECT AVG(champ) FROM coach;"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self._show_result(cursor, rows, 2) 

    def _having(self):
        query = "SELECT first_name AS Fname, last_name AS Lname, MAX(height) FROM nba_player GROUP BY player_id HAVING MAX(height)>6.7;"
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
            output = '列出主隊球場在 California 的球隊'
            self.current_text = ["SELECT T.team_name AS Full_name_of_team, S.stadium_name AS Stadium_name, S.stadium_state AS Stadium_state FROM team AS T, stadium AS S WHERE T.stadium=S.stadium_id AND S.stadium_state='California';"]
        elif text == 'DELETE':
            output = '11月1日因為伊利諾伊州的芝加哥發生暴動，所以當天在芝加哥球館取消所有比賽'
            self.current_text = [
                "SELECT G.dt AS Date_of_the_game, G.game_id, S.stadium_name, S.stadium_state FROM game AS G, stadium AS S WHERE G.stadium=S.stadium_id AND S.stadium_state='Illinois';",
                "DELETE FROM game WHERE game_id IN(SELECT G.game_id FROM game AS G, stadium AS S WHERE G.stadium=S.stadium_id AND S.stadium_state='Illinois');",
                "SELECT G.dt AS Date_of_the_game, G.game_id, S.stadium_name, S.stadium_state FROM game AS G, stadium AS S WHERE G.stadium=S.stadium_id AND S.stadium_state='Illinois';",
            ]
        elif text == 'INSERT':
            output = '由於暴動被警察適當的鎮壓，因此11月1日芝加哥球館的比賽在11月2日中重新舉行，並且該比賽最終比數為108-99。'
            self.current_text = [
                "INSERT INTO game(game_id, dt, score, stadium, home, away) VALUES(21, '2022-11-2', '108-99', '6', '6', '16');",
                "SELECT G.dt AS Date_of_the_game, S.stadium_name, S.stadium_state AS state, G.score FROM game AS G, stadium as S WHERE G.stadium=S.stadium_id AND game_id=21 AND dt='2022-11-2';",
            ]
        elif text == 'UPDATE':
            output = '賽爾提克的 Jason Tatum 因為季中交易案，被塞爾提克交易至騎士隊'
            self.current_text = [
                "SELECT N.first_name AS Fname, N.last_name AS Lname, T.team_name FROM nba_player AS N, team AS T WHERE N.current_team=T.team_id AND N.first_name='Jayson' AND N.last_name='Tatum';",
                "UPDATE nba_player SET current_team=7 WHERE player_id IN(SELECT player_id FROM nba_player WHERE first_name='Jayson' AND last_name='Tatum');"
                "SELECT N.first_name AS Fname, N.last_name AS Lname, T.team_name FROM nba_player AS N, team AS T WHERE N.current_team=T.team_id AND N.first_name='Jayson' AND N.last_name='Tatum';",
            ]
        elif text == 'IN':
            output = '找出在 Rocket 打後衛 (G) 的所有球員'
            self.current_text = ["SELECT first_name AS Fname, last_name AS Lname FROM nba_player WHERE player_id IN (SELECT N.player_id FROM nba_player AS N, team AS T WHERE N.position='G' AND N.current_team=T.team_id AND T.team_id=27);"]
        elif text == 'NOT IN':
            output = '找出身高不再7尺以上的中鋒 (C) 的球員'
            self.current_text = ["SELECT first_name AS Fname, last_name AS Lname, height FROM nba_player WHERE player_id NOT IN(SELECT player_id FROM nba_player WHERE height>=7.0) AND position='C';"]
        elif text == 'EXISTS':
            output = '找出 2022-11-2 有進行比賽的球場'
            self.current_text = ["SELECT G.dt AS Date_of_the_game, S.stadium_name FROM stadium AS S, game AS G WHERE EXISTS (SELECT 1 WHERE G.dt='2022-11-2' AND G.stadium=S.stadium_id);"]
        elif text == 'NOT EXISTS':
            output = '找出從來沒有奪冠過的球隊'
            self.current_text = ["SELECT team_name FRON team WHERE NOT EXISTS (SELECT 1 WHERE champ!=0);"]
        elif text == 'COUNT':
            output = '找出 NBA 總共有幾支球隊'
            self.current_text = ["SELECT COUNT(team_id) FROM team;"]
        elif text == 'SUM':
            output = '找出 Lakers 和 Celtics 獲得的總冠軍數'
            self.current_text = ["SELECT SUM(champ) FROM team WHERE team_name='Boston Celtics' OR team_name='Los Angeles Lakers';"]
        elif text == 'MAX':
            output = '找出身高最高的球員'
            self.current_text = ["SELECT first_name AS Fname, last_name AS Lname, MAX(height) FROM nba_player GROUP BY player_id ORDER BY MAX(height) DESC LIMIT 1;"]
        elif text == 'MIN':
            output = '找出身高最矮的球員'
            self.current_text = ["SELECT first_name AS Fname, last_name AS Lname, MIN(height) FROM nba_player GROUP BY player_id ORDER BY MIN(height) ASC LIMIT 1;"]
        elif text == 'AVG':
            output = '找出教頭平均奪冠次數'
            self.current_text = ["SELECT AVG(champ) FROM coach;"]
        elif text == 'HAVING':
            output = '找出身高超過6.7尺的球員'
            self.current_text = ["SELECT first_name AS Fname, last_name AS Lname, MAX(height) FROM nba_player GROUP BY player_id HAVING MAX(height)>6.7;"]
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

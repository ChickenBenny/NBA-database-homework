# RDBMS homework - NBA Database

## Quick start
1. clone the repository and enter the folder
```
$ git clone https://github.com/ChickenBenny/NBA-database-homework
$ cd NBA-database-homework
```
2. Use docker to build the database
```
$ docker-compose up
```
3. Install the requirement and run the GUI app 
```
$ pip install -r requirements.txt
$ python ./app/main.py
```
## 系統架構與環境
### 系統架構

![](https://i.imgur.com/LVsNkTD.png)
### 系統環境 
* 系統 : Ubuntu 20.04
* 容器 : Docker 20.10.17
* 資料庫 : PostgresSQL 13
* 前端 : PyQT5
* 使用說明
    1. 使用 `docker-compose up` 架設 Postgres。
    ![](https://i.imgur.com/ZQYS67N.png)
    2. 確認 Postgres 是否成功架設。
    ![](https://i.imgur.com/2FbQUg3.png)
    3. 使用 `python ./app/main.py`開啟前端 UI 頁面。
    ![](https://i.imgur.com/azYMCke.png)
    4. 下拉選擇你要的 query，然後點選 show 便能觸發該 query。(點選 Clear 刪除頁面上的結果)
    ![](https://i.imgur.com/UGHMOpJ.png)


## ER Diagrams
![](https://i.imgur.com/T3kgJQ7.png)

## Relation schema
![](https://i.imgur.com/o8EQIOh.png)

## 資料庫基本需求

### Entity (5個)
* **nba_player** (共43筆資料) : 
    1. player_id (**primary key**) : 球員的 id，為 key attribute。
    2. first_name : 球員的 first_name。
    3. last_name : 球員的 last_name。
    4. position : 球員在球隊中的打的位置。
    5. height : 球員的身高。
    6. current_team (**foreign key**) : 目前球員所屬的球隊。
* **team** (共30筆資料) : 
    1. team_id (**primary key**) : 球隊的 id。
    2. name : 球隊的名稱。
    3. team_state : 球隊所屬的州 。
    4. coach (**foreign key**) : 球隊的總教練 id。
    5. stadium (**forign key**) : 球隊得主隊球場 id。
* **coach** (共30筆資料) : 
    1. coach_id (**primary key**) : 教練的 id。
    2. name : 教練的名稱。
    3. champ : 奪冠總數量。
* **stadium** (共30筆資料) : 
    1. stadium_id (**primary key**) : 球場的 id。
    2. name : 球場的名稱。
    3. staduyn)state : 球場所在的州。
    4. seating : 球場的觀眾席次。
* **game** (共20筆資料) :
    1. game_id (**primary key**) : 比賽的 id。
    2. dt : 比賽的日期。
    3. score : 比賽結束的比分。
    4. stadium (**foreign key**) : 比賽的球場 id。
    5. home (**foreign key**) : 比賽的主隊 id。
    6. away (**foreign key**) : 比賽的客隊 id。

### Relationship (需包含二元及三元)
* 二元關係
    1. current_on => nba_player and team
        每一支球隊有 N 個球員目前為他效力，但並不是每個球隊都有所屬球隊，有些球員可能是自由球員。
    2. coach_by => coach and team
        每一支球隊必有一個總教練執教，但並不是每個總教練都有球隊可以執教。
    3. plays_in => team and stadium
        每一支球隊都必有一個球隊主場。
* 三元關係
    1. play_as_home => game, stadium and team
        每一場比賽都必定有主隊球隊、比賽的球場。
    3. play_as_away => game, stadium and team
        每一場比賽都必定有客隊球隊、比賽的球場。    

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
$ python main.py
```

## ER Diagrams
![](https://i.imgur.com/7MdSdTy.png)

## Relation schema
![](https://i.imgur.com/o8EQIOh.png)

## 資料庫基本需求

### Entity (5個)
* **nba_player** : 
    1. player_id (**primary key**) : 球員的 id，為 key attribute。
    2. first_name : 球員的 first_name。
    3. last_name : 球員的 last_name。
    4. position : 球員在球隊中的打的位置。
    5. height : 球員的身高。
    6. current_team (**foreign key**) : 目前球員所屬的球隊。
* **team** : 
    1. team_id (**primary key**) : 球隊的 id。
    2. name : 球隊的名稱。
    3. team_state : 球隊所屬的州 。
    4. coach (**foreign key**) : 球隊的總教練 id。
    5. stadium (**forign key**) : 球隊得主隊球場 id。
* **coach** : 
    1. coach_id (**primary key**) : 教練的 id。
    2. name : 教練的名稱。
    3. champ : 奪冠總數量。
* **stadium** : 
    1. stadium_id (**primary key**) : 球場的 id。
    2. name : 球場的名稱。
    3. staduyn)state : 球場所在的州。
    4. seating : 球場的觀眾席次。
* **game**
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
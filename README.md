# RDBMS homework - NBA Database

## ER Diagrams
![](https://i.imgur.com/aG3ZJLV.png)

## Relation schema
![](https://i.imgur.com/UA4430o.png)

## 資料庫基本需求

### Entity (5個)
1. nba_player
2. team
3. coach
4. stadium
5. game

### Relationship (需包含二元及三元)
* 二元關係
    1. current_on => nba_player and team
    2. coach_by => coach and team
    3. plays_in => team and stadium
* 三元關係
    1. play_as_home => game, stadium and team
    2. play_as_away => game, stadium and team
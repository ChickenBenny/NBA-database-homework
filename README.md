# MLB database homework
## ER Diagrams
![](https://i.imgur.com/Rg6vH0z.png)

## Relation schema
![](https://i.imgur.com/858b8CR.png)

## 符合規定的數量
### Entity
* **player(5個 attribute, 1個 key attirbute, 30筆不同的資料)**
    player 中包含球員的 ssn、球員的名字、目前所屬球隊和選秀球隊，其中球員的名字是由 first_name 和 last_name所組成，球員的 ssn 不可重複。
    1. player_ssn : 球員的身分證。
    2. name : 球員的名字，由 first_name 和 last_name 組成。
    3. current_team : 球員目前所屬球隊。
    4. draft_team : 球員選秀的球隊。
* **hitter_stats(5個 attribute, 1個 key attribute, 15筆不同的資料)**
    hitter_stats 中包含野手的 id、球員的ssn、守備位置、全壘打數和打擊率，野手的 id 不可重複。
    1. player_id : 野手在資料庫的 id。
    2. player_ssn : 野手的身分證。
    3. position : 野手的守備位置。
    4. hr : 野手的全壘打次數。
    5. ops : 野手的打擊率。
* **pitcher_stats(5個 attribute, 1個 key attribute, 15筆不同的資料)**
    pitcher_stats 中包含投手的 id、球員的ssn、贏球場數和防禦率，投手的 id 不可重複。
    1. player_id : 投手在資料庫的 id。
    2. player_ssn : 投手的身分證。
    3. win : 投手的勝投場次。
    4. era : 投手的防禦率。
* **team(3個 attribute, 2個 key attribute, 30筆不同的資料)**
    team 中包含 team_name、team_id 和 stadium，team_id 和 team_name 不可重複。
    1. team_id : 球隊在資料庫的 id。
    2. team_name : 球隊的名稱。
    3. stadium : 球隊的所屬球場。
* **game(5個 attribute, 1個 key attribute, 15筆不同的資料)**
    game 中包含 dt、game_id、home_team、guest_team 和 ref_id，其中 game_id 不可重複。
    1. dt : 球賽的比賽日期。
    2. game_id : 球賽在資料庫的 id。
    3. home_team : 主隊的對應球隊 id。
    4. guest_team : 客隊的對應球隊 id。
    5. ref_id : 對應的裁判 id。

* **referee(3個 attribute, 1個key attribute, 15筆不同的資料)**
    referee 中包含 ref_id、ref_name 和 sex，其中 ref_id 不可重複。
    1. ref_id : 裁判在資料庫中的 id。
    2. ref_name : 裁判的名稱。
    3. sex : 裁判的性別

### Relationship
* 二元關係
    * **play_as_hitter**
        1. 若球員是野手，他將有對應的 hitter_stats。
        2. player 的 player_ssn 為primary key ，hitter_stats 的 player_ssn 為 froegin key。
        4. 非所有的球員皆為野手，因此 player 非完全參與，但 hitter_stats 中的野手必定都有對應的 player。
    * **play_as_pitcher**
        1. 若球員為投手，他將有對應的 pitcher_stats。
        2. player 的 player_ssn 為primary key ，pitcher_stats 的 player_ssn 為 froegin key。
        3. 非所有的球員皆為野手，因此 player 非完全參與，但 pitcher_stats 中的野手必定都有對應的 player。
    * **draft_by** 
        1. 球員若是選秀的方式登上大聯盟，會有對應的選擇球隊，但非所有球員都是以選秀的方式進入大聯盟。
        2. team 的 team_id 為 primary key，player 的 draft_team 為 foreign key。
    * **currently_on** 
        1. 球員若非自由球員，則有所屬的球隊，但非所有球員都有所屬球隊。(team 的 team_id 為 primary_key)。

* 三元關係
    * **participate** 
        1. 每場的球賽都必須有兩支隊伍參加。
        2. 賽季中每支隊伍都必須參加球賽。
        3. 每場球賽都會有一個主審裁判，但不是所有裁判都有比賽能夠參與。
        4. referee 的 ref_id 為 primary_key，game 的 ref_id 為 foreign key。
        5. team 的 team_id 為 primary_key，game 的 home_team 為 foreign key。
        6. team 的 team_id 為 primary_key，game 的 guest_team 為 foreign key。

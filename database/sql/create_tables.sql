CREATE TABLE IF NOT EXISTS team (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(25) UNIQUE,
    stadium VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS player (
    player_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    current_team SERIAL ,
    draft_team SERIAL,

    CONSTRAINT FK_current_on
        FOREIGN KEY(current_team)
            REFERENCES team(team_id),  

    CONSTRAINT FK_draft_by
        FOREIGN KEY(draft_team)
            REFERENCES team(team_id)    
);

CREATE TABLE IF NOT EXISTS game_role (
    player_id SERIAL,
    position VARCHAR(2),
    job_type VARCHAR(8),

    CONSTRAINT FK_play_rol
        FOREIGN KEY(player_id)
            REFERENCES player(player_id)
);

CREATE TABLE IF NOT EXISTS referee (
    ref_id SERIAL PRIMARY KEY,
    seniority INTEGER,
    SEX VARCHAR(6)
);

CREATE TABLE IF NOT EXISTS game (
    game_id SERIAL PRIMARY KEY,
    home_team SERIAL,
    guest_team SERIAL,
    ref_id SERIAL,

    CONSTRAINT FK_participate_home_team
        FOREIGN KEY(home_team)
            REFERENCES team(team_id),   

    CONSTRAINT FK_participate_guest_team
        FOREIGN KEY(guest_team)
            REFERENCES team(team_id),     

    CONSTRAINT FK_participate_referee
        FOREIGN KEY(ref_id)
            REFERENCES referee(ref_id)     
);

-- init team table
INSERT INTO team(team_id,team_name,stadium) VALUES('1','Chicago White Sox','Guaranteed Rate Field');
INSERT INTO team(team_id,team_name,stadium) VALUES('2','Cleveland Guardians','Progressive Field');
INSERT INTO team(team_id,team_name,stadium) VALUES('3','Detroit Tigers','Comerica Park');
INSERT INTO team(team_id,team_name,stadium) VALUES('4','Kansas City Royals','Kauffman Stadium');
INSERT INTO team(team_id,team_name,stadium) VALUES('5','Minnesota Twins','Target Field');
INSERT INTO team(team_id,team_name,stadium) VALUES('6','Chicago Cubs','Wrigley Field');
INSERT INTO team(team_id,team_name,stadium) VALUES('7','Cincinnati Reds','Great American Ball Park');
INSERT INTO team(team_id,team_name,stadium) VALUES('8','Milwaukee Brewers','American Family Fielddouble-dagger');
INSERT INTO team(team_id,team_name,stadium) VALUES('9','Pittsburgh Pirates','PNC Park');
INSERT INTO team(team_id,team_name,stadium) VALUES('10','St. Louis Cardinals','Busch Stadium');
INSERT INTO team(team_id,team_name,stadium) VALUES('11','Baltimore Orioles','Oriole Park at Camden Yards');
INSERT INTO team(team_id,team_name,stadium) VALUES('12','Boston Red Sox','Fenway Park');
INSERT INTO team(team_id,team_name,stadium) VALUES('13','New York Yankees','Yankee Stadium');
INSERT INTO team(team_id,team_name,stadium) VALUES('14','Tampa Bay Rays','Tropicana Fielddagger');
INSERT INTO team(team_id,team_name,stadium) VALUES('15','Toronto Blue Jays','Rogers Centredouble-dagger');
INSERT INTO team(team_id,team_name,stadium) VALUES('16','Atlanta Braves','Truist Park');
INSERT INTO team(team_id,team_name,stadium) VALUES('17','New York Mets','LoanDepot Parkdouble-dagger');
INSERT INTO team(team_id,team_name,stadium) VALUES('18','Philadelphia Phillies','Citi Field');
INSERT INTO team(team_id,team_name,stadium) VALUES('19','Washington Nationals','Citizens Bank Park');
INSERT INTO team(team_id,team_name,stadium) VALUES('20','Los Angeles Angels','Nationals Park');
INSERT INTO team(team_id,team_name,stadium) VALUES('21','Oakland Athletics','Angel Stadium');
INSERT INTO team(team_id,team_name,stadium) VALUES('22','Seattle Mariners','T-Mobile Parkdouble-dagger');
INSERT INTO team(team_id,team_name,stadium) VALUES('23','Texas Rangers','Globe Life Fielddouble-dagger');
INSERT INTO team(team_id,team_name,stadium) VALUES('24','Arizona Diamondbacks','Chase Fielddouble-dagger');
INSERT INTO team(team_id,team_name,stadium) VALUES('25','Colorado Rockies','Coors Field');
INSERT INTO team(team_id,team_name,stadium) VALUES('26','Los Angeles Dodgers','Dodger Stadium');
INSERT INTO team(team_id,team_name,stadium) VALUES('27','San Diego Padres','Petco Park');
INSERT INTO team(team_id,team_name,stadium) VALUES('28','San Francisco Giants','Oracle Park');
INSERT INTO team(team_id,team_name,stadium) VALUES('29','Houston Astros','Minute Maid Parkdouble-dagger');
INSERT INTO team(team_id,team_name,stadium) VALUES('30','Miami Marlins','LoanDepot Parkdouble-dagger');

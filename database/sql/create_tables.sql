CREATE TABLE IF NOT EXISTS team (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(25) UNIQUE,
    stadium VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS player (
    player_ssn SERIAL PRIMARY KEY,
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

CREATE TABLE IF NOT EXISTS hitter_stats (
    player_id SERIAL PRIMARY KEY,
    player_ssn SERIAL,
    position VARCHAR(2),
    hr INTEGER,
    ops REAL,

    CONSTRAINT FK_play_as_hitter
        FOREIGN KEY(player_ssn)
            REFERENCES player(player_ssn)
);

CREATE TABLE IF NOT EXISTS pitcher_stats (
    player_id SERIAL PRIMARY KEY,
    player_ssn SERIAL,
    era REAL,
    win INTEGER,

    CONSTRAINT FK_play_as_pitcher
        FOREIGN KEY(player_ssn)
            REFERENCES player(player_ssn)
);

CREATE TABLE IF NOT EXISTS referee (
    ref_id SERIAL PRIMARY KEY,
    ref_name VARCHAR(20),
    sex VARCHAR(6)
);

CREATE TABLE IF NOT EXISTS game (
    dt DATE NOT NULL,
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

-- init player table
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('1', 'Matt', 'Olson', '16', '21');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('2', 'Teoscar', 'Hernandez', '15', '29');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('3', 'Travis', 'Arnaud', '16', '17');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('4', 'Freddie', 'Freeman', '26', '16');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('5', 'Harrison', 'Bader', '13', '10');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('6', 'Bryce', 'Harper', '18', '19');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('7', 'Eduardo', 'Escobar', '17', '1');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('8', 'Trea', 'Turner', '26', '27');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('9', 'Pete', 'Alonso', '17', '17');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('10', 'Orlando', 'Arcia', '16', '8');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('11', 'Matt', 'Chapman', '15', '21');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('12', 'Jeremy', 'Pena', '29', '29');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('13', 'Lars', 'Nootbaar', '21', '10');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('14', 'Anthony', 'Rizzo', '13', '12');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('15', 'Eugenio', 'Suarez', '22', '3');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('16', 'Jason', 'Adam', '14', '4');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('17', 'Tyler', 'Anderson', '26', '25');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('18', 'Garrent', 'Cleavinger', '14', '11');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('19', 'Giovanny', 'Gallegos', '10', '13');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('20', 'Tyler', 'Glasnow', '14', '9');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('21', 'Gerrit', 'Cole', '13', '9');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('22', 'Yu', 'Darvish', '27', '27');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('23', 'Seranthony', 'Dominguez', '18', '18');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('24', 'Brad', 'Hand', '18', '30');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('25', 'Cristian', 'Javier', '29', '29');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('26', 'Hector', 'Neris', '29', '18');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('27', 'Aaron', 'Nola', '18', '18');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('28', 'Blake', 'Snell', '27', '14');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('29', 'Ranger', 'Suarez', '18', '18');
INSERT INTO player(player_ssn, first_name, last_name, current_team, draft_team) VALUES('30', 'Framber', 'Valdez', '29', '29');


-- init hitter_stats table
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('1', '1', '1B', '2', '1.362');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('2', '2', 'RF', '2', '1.333');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('3', '3', 'C', '2', '1.313');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('4', '4', '1B', '1', '1.286');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('5', '5', 'CF', '5', '1.262');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('6', '6', 'DH', '6', '1.178');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('7', '7', '3B', '1', '1.233');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('8', '8', 'SS', '2', '1.111');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('9', '9', '1B', '1', '1.017');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('10', '10', '2B', '1', '1.017');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('11', '11', '3B', '0', '1.015');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('12', '12', 'SS', '4', '1.022');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('13', '13', 'LF', '0', '1.000');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('14', '14', '1B', '2', '0.984');
INSERT INTO hitter_stats(player_id, player_ssn, position, hr, ops) VALUES('15', '15', '3B', '1', '0.981');

-- init pitcher_stats table
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('1', '16', '0.', '0');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('2', '17', '0.', '0');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('3', '18', '0.', '0');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('4', '19', '0.', '0');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('5', '20', '0.', '0');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('6', '21', '2.95', '2');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('7', '22', '2.88', '2');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('8', '23', '1.69', '2');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('9', '24', '4.76', '2');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('10', '25', '0.71', '2');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('11', '26', '1.5', '2');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('12', '27', '4.91', '2');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('13', '28', '4.61', '2');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('14', '29', '1.23', '2');
INSERT INTO pitcher_stats(player_id, player_ssn, era, win) VALUES('15', '30', '1.44', '2');

-- init referee table
INSERT INTO referee(ref_id, ref_name, sex) VALUES('1', 'Pat Hoberg', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('2', 'Quinn Wolcott', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('3', 'Adrian Johnson', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('4', 'Alfonso Marquez', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('5', 'Adam Hamari', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('6', 'Lance Barrett', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('7', 'Stu Scheurwater', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('8', 'Marvin Hudson', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('9', 'Dan Iassogna', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('10', 'Jeremie Rehak', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('11', 'Bill Miller', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('12', 'Mark Carlson', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('13', 'Nic Lentz', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('14', 'Chris Segal', 'male');
INSERT INTO referee(ref_id, ref_name, sex) VALUES('15', 'David Rackley', 'male');

-- init game table
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-29', '1', '29', '18', '1');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-23', '2', '29', '27', '2');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-23', '3', '13', '29', '3');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-22', '4', '13', '29', '4');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-22', '5', '18', '27', '5');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-19', '6', '27', '18', '6');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-15', '7', '18', '16', '7');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-15', '8', '22', '29', '8');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-15', '9', '2', '13', '9');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-14', '10', '13', '2', '10');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-14', '11', '18', '16', '11');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-14', '12', '27', '26', '12');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-12', '13', '16', '18', '13');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-12', '14', '26', '27', '14');
INSERT INTO game(dt, game_id, home_team, guest_team, ref_id) VALUES('2022-10-11', '15', '16', '18', '15');

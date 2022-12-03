CREATE TABLE IF NOT EXISTS stadium (
    stadium_id SERIAL PRIMARY KEY,
    stadium_name VARCHAR(30),
    stadium_state VARCHAR(20),
    seating INTEGER
);

CREATE TABLE IF NOT EXISTS coach (
    coach_id SERIAL PRIMARY KEY,
    coach_name VARCHAR(20),
    champ INTEGER
);

CREATE TABLE IF NOT EXISTS team (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(25),
    champ INTEGER,
    stadium SERIAL,
    coach SERIAL,

    CONSTRAINT FK_play_in
        FOREIGN KEY(stadium)
            REFERENCES stadium(stadium_id),

    CONSTRAINT FK_coach_by
        FOREIGN KEY(coach)
            REFERENCES coach(coach_id)
);

CREATE TABLE IF NOT EXISTS nba_player (
    player_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    position VARCHAR(5),
    height REAL,
    current_team SERIAL,

    CONSTRAINT FK_current_on
        FOREIGN KEY(current_team)
            REFERENCES team(team_id)
);

CREATE TABLE IF NOT EXISTS game(
    game_id SERIAL PRIMARY KEY,
    dt DATE NOT NULL,
    score VARCHAR(10),
    stadium SERIAL,
    home SERIAL,
    away SERIAL,

    CONSTRAINT FK_play_as_home
        FOREIGN KEY(home)
            REFERENCES team(team_id),

    CONSTRAINT FK_play_as_away
        FOREIGN KEY(away)
            REFERENCES team(team_id),

    CONSTRAINT FK_play_in
        FOREIGN KEY(stadium)
            REFERENCES stadium(stadium_id)
);

--init stadium table
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(1, 'TD Garden', 'Massachusetts', 19156);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(2, 'Barclays Center', 'New York', 17732);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(3, 'Madison Square Garden', 'New York', 19812);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(4, 'Wells Fargo Center', 'Pennsylvania,', 20478);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(5, 'Scotiabank Arena', 'Ontario', 19800);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(6, 'United Center', 'Illinois', 20917);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(7, 'Rocket Mortgage FieldHouse', 'Ohio', 19432);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(8, 'Little Caesars Arena', 'Michigan', 20332);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(9, 'Gainbridge Fieldhouse', 'Indiana', 17923);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(10, 'Fiserv Forum', 'Wisconsin', 17341);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(11, 'State Farm Arena', 'Georgia', 16600);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(12, 'Spectrum Center', 'North Carolina', 19077);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(13, 'FTX Arena', 'Florida', 19600);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(14, 'Amway Center', 'Florida', 18846);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(15, 'Capital One Arena', 'D.C.', 20356);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(16, 'Ball Arena', 'Colorado', 19520);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(17, 'Target Center', 'Minnesota', 18798);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(18, 'Paycom Center', 'Oklahoma', 18203);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(19, 'Moda Center', 'Oregon', 19393);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(20, 'Vivint Arena', 'Utah', 16600);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(21, 'Chase Center', 'California', 18064);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(22, 'Crypto.com Arena', 'California', 19079);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(23, 'Intuit Dome', 'California', 18000);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(24, 'Footprint Center', 'Arizona', 16645);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(25, 'Golden 1 Center', 'California', 17608);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(26, 'American Airlines Center', 'Texas', 19200);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(27, 'Toyota Center', 'Texas', 18055);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(28, 'FedExForum', 'Tennessee', 18119);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(29, 'Smoothie King Center', 'Louisiana', 16867);
INSERT INTO stadium(stadium_id,stadium_name,stadium_state,seating) VALUES(30, 'AT&T Center', 'Texas', 18418);

--init coach
INSERT INTO coach(coach_id,coach_name, champ) VALUES(1, 'Nate McMillan', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(2, 'Joe Mazzulla', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(3, 'Jacque Vaughn', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(4, 'Steve Clifford', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(5, 'Billy Donovan', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(6, 'J. Bickerstaff', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(7, 'Dwane Casey', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(8, 'Rick Carlisle', 1);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(9, 'Erik Spoelstra', 2);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(10, 'M. Budenholzer', 1);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(11, 'Tom Thibodeau', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(12, 'Jamahl Mosley', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(13, 'Doc Rivers', 1);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(14, 'Nick Nurse', 1);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(15, 'Wes Unseld Jr.', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(16, 'Jason Kidd', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(17, 'Michael Malone', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(18, 'Steve Kerr', 4);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(19, 'Stephen Silas', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(20, 'Tyronn Lue', 1);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(21, 'Darvin Ham', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(22, 'Taylor Jenkins', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(23, 'Chris Finch', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(24, 'Willie Green', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(25, 'Mark Daigneault', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(26, 'Monty Williams', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(27, 'C. Billups', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(28, 'Mike Brown', 0);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(29, 'Gregg Popovich', 5);
INSERT INTO coach(coach_id,coach_name, champ) VALUES(30, 'Will Hardy', 0);

--init team
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(1, 'Boston Celtics', 17, 1, 2);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(2, 'Brooklyn Nets', 0, 2, 3);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(3, 'New York Knicks', 2, 3, 11);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(4, 'Philadelphia 76ers', 3, 4, 13);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(5, 'Toronto Raptors', 1, 5, 14);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(6, 'Chicago Bulls', 6, 6, 5);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(7, 'Cleveland Cavaliers', 1, 7, 6);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(8, 'Detroit Pistons', 3, 8, 7);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(9, 'Indiana Pacers', 0, 9, 8);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(10, 'Milwaukee Bucks', 2, 10, 10);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(11, 'Atlanta Hawks', 1, 11, 1);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(12, 'Charlotte Hornets', 0, 12, 4);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(13, 'Miami Heat', 3, 13, 9);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(14, 'Orlando Magic', 0, 14, 12);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(15, 'Washington Wizards', 1, 15, 15);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(16, 'Denver Nuggets', 0, 16, 17);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(17, 'Minnesota Timberwolves', 0, 17, 23);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(18, 'Oklahoma City Thunder', 1, 18, 25);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(19, 'Portland Trail Blazers', 0, 19, 27);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(20, 'Utah Jazz', 0, 20, 30);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(21, 'Golden State Warriors', 7, 21, 18);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(22, 'Los Angeles Clippers', 0, 22, 20);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(23, 'Los Angeles Lakers', 17, 23, 21);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(24, 'Phoenix Suns', 0, 24, 26);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(25, 'Sacramento Kings', 1, 25, 28);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(26, 'Dallas Mavericks', 1, 26, 16);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(27, 'Houston Rockets', 0, 27, 19);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(28, 'Memphis Grizzlies', 0, 28, 22);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(29, 'New Orleans Pelicans', 0, 29, 24);
INSERT INTO team(team_id,team_name,champ,stadium,coach) VALUES(30, 'San Antonio Spurs', 5, 30, 29);

--init player
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(1, 'Precious', 'Achiuwa', 'F', 6.8, 5);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(2, 'Steven', 'Adams', 'C', 6.11, 28);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(3, 'Ban', 'Adebayo', 'C', 6.9, 13);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(4, 'Ochai', 'Agbaji', 'G', 6.5, 20);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(5, 'Santi', 'Aldama', 'F', 7.0, 28);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(6, 'Grayson', 'Allen', 'G', 6.4, 10);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(7, 'Jarrent', 'Allen', 'C', 6.9, 7);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(8, 'Jose', 'Alvardo', 'G', 6.0, 29);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(9, 'Kyle', 'Anderson', 'F', 6.9, 17);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(10, 'Giannis', 'Antetokounmpo', 'F', 7.0, 10);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(11, 'Cole', 'Anthony', 'G', 6.3, 14);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(12, 'O.G.', 'Anunoby', 'F', 6.7, 5);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(13, 'Ryan', 'Arcidiacono', 'G', 6.3, 3);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(14, 'Deni', 'Avdija', 'F', 6.9, 15);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(15, 'Deandore', 'Ayton', 'C', 7.0, 24);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(16, 'Ibou', 'Badji', 'C', 7.1, 19);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(17, 'Marvin', 'Bagley', 'F', 6.10, 8);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(18, 'Patrick', 'Baldwin Jr.', 'F', 7.0, 21);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(19, 'LaMelo', 'Ball', 'G', 6.7, 12);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(20, 'Paolo', 'Banchero', 'F', 6.10, 14);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(21, 'Dominick', 'Barlow', 'F', 6.9, 30);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(22, 'Harrison', 'Barnes', 'F', 6.8, 25);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(23, 'Nicolas', 'Batum', 'G', 6.8, 22);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(24, 'Darius', 'Bazley', 'F', 6.9, 18);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(25, 'Patrick', 'Beverley', 'G', 6.2, 23);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(26, 'Goga', 'Bitadze', 'F', 6.11, 9);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(27, 'Bismack', 'Biyombo', 'C', 6.8, 24);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(28, 'Jalen', 'Brown', 'F', 6.6, 1);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(29, 'Jayson', 'Tatum', 'F', 6.8, 1);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(30, 'Nic', 'Claxton', 'C', 6.11, 2);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(31, 'Seth', 'Curry', 'G', 6.1, 2);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(32, 'Lonzo', 'Ball', 'F', 6.6, 6);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(33, 'Alex', 'Caruso', 'G', 6.5, 6);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(34, 'Tyrese', 'Haliburton', 'G', 6.5, 9);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(35, 'Buddy', 'Hield', 'G', 6.4, 9);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(36, 'Bogdan', 'Bogdanovic', 'G', 6.5, 11);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(37, 'John', 'Collins', 'F', 6.9, 11);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(38, 'Nikola', 'Jokic', 'C', 6.11, 16);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(39, 'Aron', 'Gordon', 'F', 6.8, 16);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(40, 'Luka', 'Doncic', 'F', 6.7, 26);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(41, 'Tim', 'Hardaway Jr.', 'G', 6.5, 26);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(42, 'Eric', 'Gordon', 'G', 6.3, 27);
INSERT INTO nba_player(player_id,first_name,last_name,position,height, current_team) VALUES(43, 'Jalen', 'Green', 'G', 6.4, 27);

--init game
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(1, '2022-12-2', '116-117', 15, 15, 12);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(2, '2022-12-2', '109-117', 16, 16, 11);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(3, '2022-12-2', '120-116', 13, 13, 1);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(4, '2022-11-1', '108-99', 6, 6, 16);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(5, '2022-11-1', '109-116', 21, 21, 13);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(6, '2022-11-2', '121-111', 15, 15, 4);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(7, '2022-11-2', '113-114', 1, 1, 7);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(8, '2022-11-3', '129-130', 21, 21, 14);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(9, '2022-11-5', '126-123', 25, 25, 14);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(10, '2022-11-6', '114-100', 7, 7, 23);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(11, '2022-11-7', '108-100', 15, 15, 12);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(12, '2022-11-9', '87-94', 26, 26, 14);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(13, '2022-11-10', '105-113', 26, 26, 15);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(14, '2022-11-11', '112-131', 16, 16, 1);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(15, '2022-11-11', '112-121', 8, 8, 3);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(16, '2022-11-12', '110-95', 2, 2, 22);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(17, '2022-11-13', '145-135', 18, 18, 3);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(18, '2022-11-14', '115-111', 5, 5, 8);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(19, '2022-11-15', '102-113', 17, 17, 29);
INSERT INTO game(game_id,dt,score,stadium,home,away) VALUES(20, '2022-11-18', '106-107', 13, 13, 15);

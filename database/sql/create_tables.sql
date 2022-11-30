CREATE TABLE IF NOT EXISTS stadium (
    stadium_id SERIAL PRIMARY KEY,
    stadium_name VARCHAR(20),
    stadium_state VARCHAR(20),
    seating INTEGER
)

CREATE TABLE IF NOT EXISTS coach (
    coach_id SERIAL PRIMARY KEY,
    coach_name VARCHAR(20),
    champ INTEGER
)

CREATE TABLE IF NOT EXISTS team (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(25),
    team_state VARCHAR(20),
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
)


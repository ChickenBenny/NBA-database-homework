CREATE TABLE IF NOT EXISTS player (
    player_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    current_team SERIAL ,
    draft_team SERIAL

    CONSTRAINT FK_current_on
        FOREIGN KEY(current_team)
            REFERENCES team(team_id)    

    CONSTRAINT FK_draft_by
        FOREIGN KEY(draft_team)
            REFERENCES team(team_id)    
);

CREATE TABLE IF NOT EXISTS game_role (
    player_id SERIAL,
    position VARCHAR(2),
    job_type VARCHAR(8)

    CONSTRAINT FK_play_rol
        FOREIGN KEY(player_id)
            REFERENCES player(player_id)
);

CREATE TABLE IF NOT EXISTS team (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(20) UNIQUE,
    stadium VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS game (
    game_id SERIAL PRIMARY KEY,
    home_team VARCHAR(20),
    stadium VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS reference (
    game_id SERIAL,
    ref_id VARCHAR(20),
    stadium VARCHAR(20)
);
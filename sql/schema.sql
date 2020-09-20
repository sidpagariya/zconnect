PRAGMA foreign_keys = ON;

CREATE TABLE questions (
    questionid INTEGER PRIMARY KEY AUTOINCREMENT,
    question CHAR(500) NOT NULL
)
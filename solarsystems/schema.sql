DROP TABLE IF EXISTS systems;
CREATE TABLE systems (
    id integer PRIMARY KEY autoincrement,
    name text,
    manufacturer text,
    model text,
    avg_performance real,
    system_size real,
    latitude real,
    longitude real
)
import sqlalchemy
import psycopg2

engine = sqlalchemy.create_engine('postgresql://PY_41:123456@localhost:5432/Music_db')

connection = engine.connect()

sel_album = connection.execute('''SELECT album_name, year_of_release FROM album
WHERE year_of_release = 2018;
''').fetchall()
print(sel_album)

sel_track = connection.execute('''SELECT track_name, track_time FROM track
ORDER BY track_time DESC;
''').fetchone()
print(sel_track)

sel_track_time = connection.execute('''SELECT track_name FROM track
WHERE track_time >= 210;
''').fetchall()
print(sel_track_time)

sel_collection = connection.execute('''SELECT collection_name FROM collection_of_music
WHERE year_of_release BETWEEN 2018 AND 2020;
''').fetchall()
print(sel_collection)

sel_track_time = connection.execute('''SELECT nickname FROM singer
WHERE nickname not like '%% %%';
''').fetchall()
print(sel_track_time)

sel_track_time = connection.execute('''SELECT track_name FROM track
WHERE track_name ilike '%%my%%';
''').fetchall()
print(sel_track_time)

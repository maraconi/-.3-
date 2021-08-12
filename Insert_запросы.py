import sqlalchemy
import psycopg2

engine = sqlalchemy.create_engine('postgresql://PY_41:123456@localhost:5432/Music_db')

connection = engine.connect()

connection.execute('''INSERT INTO genres_of_songs
VALUES(1, 'Рок'),
(2, 'Поп'),
(3, 'Кантри',),
(4, 'Рэп'),
(5, 'Альтернатива');
''')

connection.execute('''INSERT INTO singer
VALUES(1, 'Полина Гагарина'),
(2, 'Сергей Лазарев'),
(3, 'LP'),
(4, 'Дана Соколова'),
(5, 'Savage Garden'),
(6, 'Taylor Swift'),
(7, 'Диана Арбенина'),
(8, 'Баста');
''')

connection.execute('''INSERT INTO album
VALUES(1, 'О себе', 2010),
(2, 'THE ONE', 2018),
(3, 'Lost on You', 2016),
(4, 'Heart to Mouth', 2018),
(5, 'Мыслепад', 2018),
(6, 'Фонари', 2019),
(7, 'To the Moon and Back', 2017),
(8, 'Truly Madly Completely', 2016),
(9, '1989', 2014),
(10, 'Выживут только влюбленные', 2016),
(11, 'О2', 2020),
(12, 'Баста 3', 2010);
''')

connection.execute('''INSERT INTO track
VALUES(1, 'Любовь под солнцем', 209, 1),
(2, 'Ой', 205, 1),
(3, 'Мелочи жизни', 227, 1),
(4, 'You Put Out the Fire', 180, 2),
(5, 'Eat You Up', 183, 2),
(6, 'Going Under', 184, 2),
(7, 'Muddy Waters', 270, 3),
(8, 'No Witness', 208, 3),
(9, 'Lost on You', 267, 3),
(10, 'One Night in the Sun', 264, 4),
(11, 'Girls Go Wild', 221, 4),
(12, 'Recovery', 234, 4),
(13, 'Остров грехов', 206, 5),
(14, 'Только вперёд', 207, 5),
(15, 'Фонари', 156, 6),
(16, 'Z Поколение', 228, 6),
(17, 'To the Moon and Back', 286, 7),
(18, 'I Want You', 231, 8),
(19, 'Welcome To my New York', 210, 9),
(20, 'Blank Space', 272, 9),
(21, 'Шагай', 154, 10),
(22, 'Помолчим', 282, 10),
(23, 'Авиарежим', 195, 11),
(24, 'Самый красивый гопник', 229, 11),
(25, 'Ходим по краю', 207, 12),
(26, 'Хэндз Ап!', 243, 12);
''')

connection.execute('''INSERT INTO collection_of_music
VALUES(1, 'Collection_1', 2010),
(2, 'Collection_2', 2015),
(3, 'Collection_3', 2016),
(4, 'Collection_4', 2016),
(5, 'Collection_5', 2017),
(6, 'Collection_6', 2018),
(7, 'Collection_7', 2019),
(8, 'Collection_8', 2020);
''')

connection.execute('''INSERT INTO album_of_singer
VALUES(1, 1),
(2, 2),
(3, 3),
(3, 4),
(4, 5),
(4, 6),
(5, 7),
(5, 8),
(6, 9),
(7, 10),
(7, 11),
(8, 12);
''')

connection.execute('''INSERT INTO genres_of_singer
VALUES(1, 2),
(2, 2),
(3, 5),
(4, 1),
(5, 2),
(6, 3),
(7, 1),
(8, 4);
''')

connection.execute('''INSERT INTO tracks_of_collection
VALUES(1, 1),
(2, 1),
(3, 1),
(25, 1),
(26, 1),
(1, 2),
(2, 2),
(3, 2),
(19, 2),
(20, 2),
(7, 3),
(8, 3),
(9, 3),
(18, 3),
(21, 4),
(22, 4),
(25, 4),
(26, 4),
(17, 5),
(18, 5),
(5, 6),
(6, 6),
(10, 6),
(11, 6),
(13, 7),
(14, 7),
(15, 7),
(16, 7),
(15, 8),
(16, 8),
(23, 8),
(24, 8);
''')

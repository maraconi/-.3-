create table if not exists genres_of_songs (
	id_genres SERIAL primary KEY,
	name_genres VARCHAR(40) not null UNIQUE
);

create table if not exists singer (
	id_singer SERIAL primary KEY,
	nickname VARCHAR(60) not null
);

create table if not exists album (
	id_album SERIAL primary KEY,
	album_name VARCHAR(60) not null,
	year_of_release integer not null
);

create table if not exists track (
	id_track SERIAL primary KEY,
	track_name VARCHAR(60) not null,
	track_time integer not null, 
	id_album integer references album (id_album) not null
);

create table if not exists collection_of_music (
	id_collection SERIAL primary KEY,
	collection_name VARCHAR(60) not null,
	year_of_release integer not null
);

create table if not exists album_of_singer (
	id_singer integer references singer (id_singer) not null,
	id_album integer references album (id_album) not null,
	constraint pk primary key (id_singer, id_album)
);

create table if not exists genres_of_singer (
	id_singer integer references singer (id_singer) not null,
	id_genres integer references genres_of_songs (id_genres) not null,
	constraint pk_2 primary key (id_singer, id_genres)
);

create table if not exists tracks_of_collection (
	id_track integer references track (id_track) not null,
	id_collection integer references collection_of_music (id_collection) not null,
	constraint pk_3 primary key (id_track, id_collection)
);


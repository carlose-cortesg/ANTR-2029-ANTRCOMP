from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import json
import os
from datetime import datetime

Base = declarative_base()

# Association table for the many-to-many relationship between Playlists and Songs
playlist_songs = Table('playlist_songs', Base.metadata,
    Column('playlist_id', Integer, ForeignKey('playlists.pid')),
    Column('song_id', Integer, ForeignKey('songs.id'))
)

class Playlist(Base):
    __tablename__ = 'playlists'
    pid = Column(Integer, primary_key=True)
    name = Column(String)
    collaborative = Column(String)
    modified_at = Column(DateTime)  # Changed to DateTime type
    num_tracks = Column(Integer)
    num_albums = Column(Integer)
    num_followers = Column(Integer)
    num_edits = Column(Integer)
    duration_ms = Column(Integer)
    num_artists = Column(Integer)
    songs = relationship('Song', secondary=playlist_songs, back_populates='playlists')

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    track_uri = Column(String)
    artist_name = Column(String)
    artist_uri = Column(String)
    track_name = Column(String)
    album_uri = Column(String)
    duration_ms = Column(Integer)
    album_name = Column(String)
    playlists = relationship('Playlist', secondary=playlist_songs, back_populates='songs')

def load_data(session, json_path):
    print(f"Processing {json_path}...")  
    with open(json_path, 'r') as file:
        data = json.load(file)
        for plist in data['playlists']:
            modified_datetime = datetime.utcfromtimestamp(plist['modified_at'])  # Convert Unix time to datetime
            playlist = Playlist(
                pid=plist['pid'],
                name=plist['name'],
                collaborative=plist['collaborative'],
                modified_at=modified_datetime,
                num_tracks=plist['num_tracks'],
                num_albums=plist['num_albums'],
                num_followers=plist['num_followers'],
                num_edits=plist['num_edits'],
                duration_ms=plist['duration_ms'],
                num_artists=plist['num_artists']
            )
            session.add(playlist)
            session.commit()
            
            for track in plist['tracks']:
                song = session.query(Song).filter_by(track_uri=track['track_uri']).first()
                if not song:
                    song = Song(
                        track_uri=track['track_uri'],
                        artist_name=track['artist_name'],
                        artist_uri=track['artist_uri'],
                        track_name=track['track_name'],
                        album_uri=track['album_uri'],
                        duration_ms=track['duration_ms'],
                        album_name=track['album_name']
                    )
                    session.add(song)
                    session.commit()
                playlist.songs.append(song)
            session.commit()

def main():
    engine = create_engine('sqlite:///playlists.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    json_folder = 'Semana6/Datos/JSON'
    for json_file in os.listdir(json_folder):
        load_data(session, os.path.join(json_folder, json_file))

if __name__ == '__main__':
    main()

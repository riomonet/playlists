"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
        db.init_app(app)



class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    description =  db.Column(db.String(200), nullable = True)
    

    
class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable = False)
    artist =  db.Column(db.String(100), nullable = False)

    playlist = db.relationship('Playlist', secondary='playlist_songs', backref = 'songs')



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlist_songs'
    
    playlist_id =  db.Column(db.Integer, db.ForeignKey('playlists.id'), primary_key = True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), primary_key = True)

    

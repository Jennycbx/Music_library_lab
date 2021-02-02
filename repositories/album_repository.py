from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def update(album):
    sql = "UPDATE albums SET (title, genre, artist) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist, album.id]
    run_sql(sql, values)


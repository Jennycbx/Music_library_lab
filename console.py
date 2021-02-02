import pdb
from models.album import Album 
from models.artist import Artist 
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_1 = Album("Black", "Pop", "Beyonce")
album_repository.save(album_1)

album_1.title = "White"
album_1.genre = "Rock_Pop"
album_1.artist = "Beatles"
album_repository.update(album_1)

artist_1 = Artist("Michael", "Jackson")
artist_repository.save(artist_1)

pdb.set_trace()
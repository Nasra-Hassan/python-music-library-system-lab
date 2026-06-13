class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        if artist not in Song.artists:
            Song.artists.append(artist)

        if genre not in Song.genres:
            Song.genres.append(genre)

        Song.genre_count.setdefault(genre, 0)
        Song.genre_count[genre] += 1

        Song.artist_count.setdefault(artist, 0)
        Song.artist_count[artist] += 1

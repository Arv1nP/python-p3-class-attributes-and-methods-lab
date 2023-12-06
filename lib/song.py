class Song:
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.genre = genre
        self.artist = artist
        Song.count += 1
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_to_genres(cls):
        cls.genres.append(cls.genre)
        cls.genres = list(set(cls.genres))

    @classmethod
    def add_to_artists(cls):
        cls.artists.append(cls.artist)
        cls.artists = list(set(cls.artists))

    @classmethod
    def add_to_genre_count(cls):
        if cls.genre in cls.genre_count:
            cls.genre_count[cls.genre] += 1
        else:
            cls.genre_count[cls.genre] = 1

    @classmethod
    def add_to_artist_count(cls):
        if cls.artist in cls.artist_count:
            cls.artist_count[cls.artist] += 1
        else:
            cls.artist_count[cls.artist] = 1

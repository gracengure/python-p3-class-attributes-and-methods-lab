class Song:
    count = 0  # Class attribute to store the count of songs
    genres = []  # Class attribute to store unique genres
    artists = []  # Class attribute to store unique artists
    genre_count = {}  # Class attribute to store genre counts
    artist_count = {}  # Class attribute to store artist counts

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()  # Call class method to increment count
        Song.add_to_genres(genre)  # Call class method to add genre
        Song.add_to_artists(artist)  # Call class method to add artist
        if genre in self.genre_count:
            self.genre_count[genre] += 1
        else:
            self.genre_count[genre] = 1

        # Update artist count
        if artist in self.artist_count:
            self.artist_count[artist] += 1
        else:
            self.artist_count[artist] = 1

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1  # Increment the count of songs by one whenever a new song is created

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {genre: cls.genres.count(genre) for genre in cls.genres}

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {artist: cls.artists.count(artist) for artist in cls.artists}

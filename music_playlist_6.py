class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.title} by {self.artist}"


class Playlist:
    def __init__(self):
        self.current_song = None

    def add_song(self, song):
        if self.current_song is None:
            self.current_song = song
        else:
            last_song = self.current_song
            while last_song.next:
                last_song = last_song.next
            last_song.next = song
            song.prev = last_song

    def remove_song(self, song):
        if self.current_song == song:
            self.current_song = song.next
        elif song.prev:
            song.prev.next = song.next
        if song.next:
            song.next.prev = song.prev

    def next_song(self):
        if self.current_song and self.current_song.next:
            self.current_song = self.current_song.next
        else:
            raise Exception("No next song")

    def previous_song(self):
        if self.current_song and self.current_song.prev:
            self.current_song = self.current_song.prev
        else:
            raise Exception("No previous song")


if __name__ == "__main__":
    playlist = Playlist()

    song1 = Song("Song 1", "Artist 1")
    song2 = Song("Song 2", "Artist 2")
    song3 = Song("Song 3", "Artist 3")

    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)

    print("Currently playing:", playlist.current_song)
    playlist.next_song()
    print("Next song:", playlist.current_song)
    playlist.previous_song()
    print("Previous song:", playlist.current_song)
import unittest
from music_playlist_6 import Playlist, Song


class TestMusicPlaylist(unittest.TestCase):

    def test_add_remove_song(self):
        playlist = Playlist()

        song1 = Song("Song 1", "Artist 1")
        song2 = Song("Song 2", "Artist 2")

        playlist.add_song(song1)
        playlist.add_song(song2)

        self.assertEqual(playlist.current_song.title, "Song 1")

        playlist.remove_song(song1)
        self.assertEqual(playlist.current_song.title, "Song 2")

    def test_navigation(self):
        playlist = Playlist()

        song1 = Song("Song 1", "Artist 1")
        song2 = Song("Song 2", "Artist 2")

        playlist.add_song(song1)
        playlist.add_song(song2)

        playlist.next_song()
        self.assertEqual(playlist.current_song.title, "Song 2")

        playlist.previous_song()
        self.assertEqual(playlist.current_song.title, "Song 1")


if __name__ == "__main__":
    unittest.main()
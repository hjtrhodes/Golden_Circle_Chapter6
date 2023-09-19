import pytest
from lib.track_music import *

"""
Given new object created
creates empty list
"""
def test_init_creates_empty_tracklist():
    music = MusicTracker()
    result = music.tracklist
    assert result == []

"""
Given a music track (string)
adds track to the list of tracks
"""
def test_add_and_list_track():
    music = MusicTracker()
    music.add_tracks("Millenium")
    music.add_tracks("Happy Days")
    music.add_tracks("Dance!")
    result = music.list_tracks()
    assert result == ["Millenium", "Happy Days", "Dance!"]

"""
Given an empty string
gives an exception "Track input empty."
"""
def test_add_tracks_exception_error():
    music = MusicTracker()
    with pytest.raises(Exception) as e:
        music.add_tracks("")
    error_message = str(e.value)
    assert error_message == "Track input empty."
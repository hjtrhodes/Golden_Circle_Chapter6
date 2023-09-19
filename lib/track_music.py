"""
As a user so that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them
"""

class MusicTracker():
    def __init__(self):
        # Parameters: None
        # Side Effects: creation of empty list
        self.tracklist = []
        pass
    
    def add_tracks(self, track):
        # Parameters: track: string
        # Returns: None
        # Side Effects: add track to list of tracks
        if track == "":
            raise Exception("Track input empty.")
        self.tracklist.append(track)
        pass
    
    def list_tracks(self):
        # Parameters: None
        # Returns: list of tracks
        # Side Effects: None
        return self.tracklist
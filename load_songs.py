import json

# load songs from songs.json
def load_songs():
    with open('songs.json', 'r') as f:
        songs = json.load(f)
    return songs

from count_min_sketch import CountMinSketch
import hashlib

class SpotifyCMS(CountMinSketch):
    def __init__(self, p, error_rate, failure_probability):
        super().__init__(p, error_rate, failure_probability)

    # function to encode the song uri into an integer
    def song_id(self, song_uri):
        s = song_uri.strip("spotify:track:")
        h = int(hashlib.md5(s.encode()).hexdigest(), 16) % self.p
        return h
    

from spotify_cms import SpotifyCMS
from load_songs import load_songs
from count_min_sketch import CountMinSketch
from benchmark import benchmark_cms_vs_dict
import random
import pandas as pd
import sys

# ----- Spotify Implementation -----
# load songs
songs = load_songs()

# initialize SpotifyCMS
cms = SpotifyCMS(p=2**31 - 1, error_rate=0.001, failure_probability=0.001)
actual_counts = {}
estimated_counts = {}

# add songs to CMS
for song in songs:
    uri = song[3]
    play_count = random.randint(1, 10)
    song_hash = cms.song_id(uri)
    for _ in range(play_count):
        cms.update(song_hash)
    actual_counts[song[0]] = play_count
    

# query songs
for song in songs:
    uri = song[3]
    song_hash = cms.song_id(uri)
    estimated_count = cms.query(song_hash)
    estimated_counts[song[0]] = int(estimated_count)

df_actual = pd.DataFrame.from_dict(actual_counts, orient='index', columns=['actual_count'])
df_estimated = pd.DataFrame.from_dict(estimated_counts, orient='index', columns=['estimated_count'])
df = pd.concat([df_actual, df_estimated], axis=1)
print(df)

table = pd.DataFrame(cms.table)
print(table)
 


# -----Benchmarking-----
n = [10, 100, 1000, 5000, 10000, 100000, 1000000]
df_benchmark = benchmark_cms_vs_dict(n)
print(df_benchmark)


    

    
    



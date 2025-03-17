import random
import sys
import pandas as pd
from count_min_sketch import CountMinSketch

def benchmark_cms_vs_dict(n):
    # dictionary to store memory usage of CMS and dictionary for each value of n, where n is the number of data points we want to store
    memory_usage = {"n": [], "CMS (bytes)": [], "Dictionary (bytes)": []}

    # initialize CMS
    cms_benchmark = CountMinSketch(p=2**31 - 1, error_rate=0.001, failure_probability=0.001)

    print("Benchmarking CMS against dictionary")
    for i in n:
        # dictionary to store the frequency of each item
        dict_benchmark = {}
        # update CMS and dictionary with random values
        for j in range(i+1):
            frequency = random.randint(1, 10)
            for _ in range(frequency):
                cms_benchmark.update(j)
            dict_benchmark[j] = frequency
        
        memory_usage["n"].append(i)
        memory_usage["CMS (bytes)"].append(sys.getsizeof(cms_benchmark.table))  
        memory_usage["Dictionary (bytes)"].append(sys.getsizeof(dict_benchmark))

    df = pd.DataFrame(memory_usage)
    return df

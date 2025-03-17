import random
import sys
import pandas as pd
from count_min_sketch import CountMinSketch

def benchmark_cms_vs_dict(n):
    memory_usage = {"n": [], "CMS (bytes)": [], "Dictionary (bytes)": []}

    print("Benchmarking CMS against dictionary")
    for i in n:
        cms_benchmark = CountMinSketch(p=2**31 - 1, error_rate=0.001, failure_probability=0.001)
        dict_benchmark = {}
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
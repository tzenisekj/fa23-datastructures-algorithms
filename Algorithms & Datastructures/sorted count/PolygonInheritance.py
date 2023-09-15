my_name = "Tyler Zenisek"

import time
import numpy as np
import random
import matplotlib.pyplot as plt


if __name__ == "__main__":
    list_max_size = 5000
    how_many_times = 5000

    n_values = np.linspace(2, list_max_size, how_many_times, dtype=int)
    sort_times = []

    min_val = 1
    max_val = 1000
    print("n_values", n_values)
    for n in n_values:
        init_list = [random.randint(min_val, max_val) for _ in range(n)]
        start_time = time.time_ns()
        sorted(init_list)
        end_time = time.time_ns()
        sort_times.append((end_time - start_time) / 1000000)
        print("Sorted Time", n, ((end_time - start_time) / 1000000), end_time==start_time)

    plt.figure(figsize=(20,10))
    plt.ylim(-.00005, 2)

    plt.plot(n_values, sort_times, label="Sorted Times")

    plt.xlabel("List Size")
    plt.ylabel("Time (ms)")

    plt.legend
    plt.show()


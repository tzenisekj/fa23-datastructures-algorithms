my_name = "Tyler Zenisek"

import time
import numpy as np
import random
from matplotlib import pyplot as plt
from heap_sort import heap_sort


def sorted_method(l):
    start_time = time.time_ns()
    temp_array = sorted(l)
    end_time = time.time_ns()
    print("Sorted Time", n, ((end_time - start_time) / 1000000), end_time == start_time)
    return (end_time - start_time) / 1000000

def insertion_sort(l):
    start_time = time.time_ns()
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j+1] = key
    end_time = time.time_ns()
    print("Insertion Sort Time", n, ((end_time - start_time) / 1000000), end_time == start_time)
    return (end_time - start_time) / 1000000

def heap_sort_algorithm(l):
    start_time = time.time_ns()
    temp_array = heap_sort(l)
    end_time = time.time_ns()
    print("Heap Sort Time", n, ((end_time - start_time) / 1000000), end_time == start_time)
    return (end_time - start_time) / 1000000



if __name__ == "__main__":
    list_max_size = 3000
    how_many_times = 250

    n_values = np.linspace(3, list_max_size, how_many_times, dtype=int)

    # arrays for sort times
    sort_times = []
    heap_times = []
    insertion_times = []

    min_val = 0
    max_val = 10000
    print("n_values", n_values)
    for n in n_values:
        init_list = [random.randint(min_val, max_val) for _ in range(n)]
        list_two = init_list.copy()
        list_three = init_list.copy()
        sort_times.append(sorted_method(init_list))
        heap_times.append(heap_sort_algorithm(list_two))
        insertion_times.append(insertion_sort(list_three))

    plt.figure(figsize=(20,10))
    plt.ylim(-.00005, 200)

    print("sorted_times: ", sort_times)
    print("heap-sort_times: ", heap_times)
    print("Insertion sorted_times: ", insertion_times)

    plt.plot(n_values, sort_times, label="Sorted Times")
    plt.plot(n_values, heap_times, label="Heap Times")
    plt.plot(n_values, insertion_times, label="Insertion Times")

    plt.xlabel("List Size")
    plt.ylabel("Time (ms)")

    plt.legend
    plt.show()
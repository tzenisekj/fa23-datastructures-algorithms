# bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - 1 - i):  # gets next in line to i index
            if arr[j] > arr[j + 1]:  # swap if left number is greater than right number in index
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # array swap
                swapped = True
        if not swapped: break
    return arr

if __name__ == "__main__":
    init_array = [5,7,8,4,23,56,98,481,151,0,2165,26]
    print("Init-Array: ", init_array)
    sorted_array = bubble_sort(init_array)
    print("Sorted-Array: ", sorted_array)
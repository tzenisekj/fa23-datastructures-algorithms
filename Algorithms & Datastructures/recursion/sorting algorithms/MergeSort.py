# merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2                   #digit division
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i=0
        j=0
        k=0

        while i < (len(left_half)) and j < len(right_half):
            if left_half[i]<right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            k += 1
            i += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            k += 1
            j += 1

    return arr

if __name__ == "__main__":
    init_array = [45,6498,1515,31,5155,0,65,788,15]
    print("Init-Array: ", init_array)
    new_array = merge_sort(init_array)
    print("Sorted-Array: ", new_array)
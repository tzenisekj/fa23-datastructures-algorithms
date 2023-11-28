def inversions(input_List: list) -> int:
    inv_count = 0
    # implement the function Here to count inversions
    for i in range(len(input_List)):
        for j in range(i+1, len(input_List)):
            if input_List[i] > input_List[j]:
                inv_count += 1

    return inv_count


# code that would be executed first (Dont change)
if __name__ == "__main__":
    # Driver Code
    arr = [1, 2, 3, 5, 4]
    n = len(arr)
    print("Number of inversions: ", inversions(arr))  # 1

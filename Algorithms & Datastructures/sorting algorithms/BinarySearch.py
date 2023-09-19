def binary_search(data, target, low, high):
    if low > high:
        return False

    mid = (low+high)//2
    print("Mid-Value: ", data[mid], "Low-Value: ", data[low], "high-value: ", data[high])

    if target == data[mid]:
        return True
    elif target < data[mid]:
        print(data[low:mid])
        return binary_search(data, target, low, mid-1)
    else:
        print(data[mid:high+1])
        return binary_search(data, target, mid+1, high)


if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9, 20,30,40,50,60,70,80,90]
    target = 8
    print(data, "target", target)
    print(binary_search(data, target, 0, len(data)-1))
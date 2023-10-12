import sys

if __name__ == "__main__":
    data = []
    for i in range(20):
        data.append(None)

    past_size = sys.getsizeof(data)
    while len(data) != 0:
        a = len(data)
        b = sys.getsizeof(data)
        print("Length: {0:3d}: Size in bytes: {1:4d}".format(a, b))
        data.pop()
        if sys.getsizeof(data) < past_size:
            print("Size Deducted")
def rec_sum(data, n):
    if n == 1:
        return data[0]

    return data[n-1] + rec_sum(data, n-1)

if __name__ == "__main__":
    data = [1,2,3,4,5]
    print(rec_sum(data, 5))
def reverse_array(data, i, j):
    if i < j:
        data[i],data[j] = data[j],data[i]
        print("Swapped", data)
        reverse_array(data, i+1,j-1)



if __name__ == "__main__":
    data = ["A", "B", "C", "D", "E", "F", "W"]
    reverse_array(data, 0, len(data)-1)
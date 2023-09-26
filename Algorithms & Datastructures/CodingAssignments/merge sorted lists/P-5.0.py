my_name = "Tyler Zenisek"


# Assignment: Programming Project 3
def merge_sorted_lists(list1, list2):
    """
    This function merges two sorted lists into one sorted list.

    Parameters:
    list1 (list): The first sorted list.
    list2 (list): The second sorted list.

    Returns:
    list: A sorted list that contains all elements from list1 and list2.
    """
    merged_list = []
    # WRITE YOUR CODE HERE
    i = 0
    j = 0

    while len(merged_list) != len(list1) + len(list2):
        if i > len(list1) - 1:
            merged_list.append(list2[j])
            j += 1
        elif j > len(list2) - 1:
            merged_list.append(list1[i])
            i += 1
        else:
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            elif list2[j] < list1[i]:
                merged_list.append(list2[j])
                j += 1
            else:
                merged_list.append(list1[i])
                merged_list.append(list2[j])
                i += 1
                j += 1

    # Hint:
    # 1. Keep two pointers, each initially pointing to the start of list1 and list2.
    # 2. Compare the elements pointed by the pointers and choose the smaller one to append to the 'merged_list'.
    # 3. Increment the pointer of the list from which an element is chosen.
    # 4. If one list gets exhausted, append all remaining elements from the other list to 'merged_list'.

    return merged_list


if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]
    print(merge_sorted_lists(list1, list2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


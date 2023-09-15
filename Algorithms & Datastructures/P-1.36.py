my_name = "Tyler Zenisek"


# Assignment: Programming Project 1, P1.36
def count_words(words):
    word_count = {}
    # WRITE YOUR CODE HERE
    # Note: Output order does not matter because it is a dictionary
    current_word = ""
    for i in words:
        if i == " ":
            if current_word in word_count:
                store = word_count.get(current_word)
                word_count[current_word] = store + 1
            else:
                word_count[current_word] = 1
            current_word = ""
        else:
            current_word += i

    if current_word != "":
        if current_word in word_count:
            store = word_count[current_word]
            word_count[current_word] = store + 1
        else:
            word_count[current_word] = 1

    return word_count


if __name__ == '__main__':
    words = "abc ab mno abc a vwx vwx stu mno abc"
    words2 = "abc abc abc"
    print(count_words(words))  # {'abc': 3, 'vwx': 2, 'a': 1, 'mno': 2, 'ab': 1, 'stu': 1}
    print(count_words(words2))  # {'abc': 3}

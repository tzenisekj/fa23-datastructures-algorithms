# function converts a single character to its numerical value
# character must be a number from 0-9
def char_to_num(num):
    if num == "0":
        return 48
    elif num == "1":
        return 49
    elif num == "2":
        return 50
    elif num == "3":
        return 51
    elif num == "4":
        return 52
    elif num == "5":
        return 53
    elif num == "6":
        return 54
    elif num == "7":
        return 55
    elif num == "8":
        return 56
    elif num == "9":
        return 57
    else:
        return 0


# function converts a single number to a character value
# number must be a single digit from 0-9
def int_to_char(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    elif num == 2:
        return "2"
    elif num == 3:
        return "3"
    elif num == 4:
        return "4"
    elif num == 5:
        return "5"
    elif num == 6:
        return "6"
    elif num == 7:
        return "7"
    elif num == 8:
        return "8"
    elif num == 9:
        return "9"
    else:
        return ""


# function converrts a number to a string
# works with both negative and positive numbers
def convert_to_str(result):
    isNeg = False
    numbers = []

    if result < 0:
        isNeg = True
        result = result * -1

    while result > 0:
        num = result % 10
        numbers.append(int_to_char(num))
        result //= 10

    numbers.reverse()

    if isNeg:
        numbers.insert(0, "-")

    return "".join(numbers)

def str_num_multiply(num1: str, num2: str) -> str:
    result_str = ""

    # Write your code there you are NOT allowed to use any of the inbuilt function such as str() or int() functions
    first = 0
    second = 0

    # iterates to convert num1 to an int
    for c in num1:
        if c != "-":
            first = first * 10 + char_to_num(c) - 48

    # iterates to convert num2 to an int
    for c in num2:
        if c != "-":
            second = second * 10 + char_to_num(c) - 48

    # checking and handling negatives
    if num1[0] == "-":
        first = first * -1

    if num2[0] == "-":
        second = second * -1

    result = first * second

    # convert back to str
    result_str = convert_to_str(result)

    return result_str


if __name__ == '__main__':
    # this is an example of how the function should be called and what example values it would take
    print("result 9*3: ", str_num_multiply("9", "3"))
    print("result 100*200: ", str_num_multiply("100", "200"))
    print("result 16*128: ", str_num_multiply("16", "128"))
    print("result -5*10: ", str_num_multiply("-5", "10"))
    print("result -64*-64: ", str_num_multiply("-64", "-64"))
    print("result 16*-64: ", str_num_multiply("16", "-64"))
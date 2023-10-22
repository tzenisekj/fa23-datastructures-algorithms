from stack_list import Stack, Empty
my_name = "TTyler Zenisek"
 

# Assignment: Programming Project
def eval_expr(expression):
    """
    This function evaluates an arithmetic expression using a stack. The expression can contain digits and the operators '+' and '-'.
    The '+' and '-' operators have the same precedence and the expression is evaluated from left to right.
 
    Parameters:
    expression (str): The arithmetic expression to evaluate. The expression can contain digits (0-9) and the operators '+' and '-'.
 
    Returns:
    int: The result of the arithmetic expression.
    """
    # WRITE YOUR CODE HERE
    init_numbers = Stack()                                                  #first stack (numbers)
    init_operators = Stack()                                                #first stack (operators)
    numbers = Stack()                                                       #correct stack order (numbers)
    operators = Stack()                                                     #correct stack order (operators)
    current_number = ""   
    result = 0                                                  #holds number value to keep track of numbers in str

    for i in expression:                                                    #loops through expression to set up stacks
        if i == "+" or i == "-":
            init_numbers.push(int(current_number))
            current_number = ""
            init_operators.push(i)
        else:
            current_number += i

    if current_number != "":                                                #if extra number held, push to stack
        init_numbers.push(int(current_number))  

    
    while not init_numbers.is_empty() and not init_operators.is_empty():    #sorts stacks in correct order
        if not init_numbers.is_empty():
            value = init_numbers.top()
            init_numbers.pop()
            numbers.push(value)

        if not init_operators.is_empty():
            o = init_operators.top()
            init_operators.pop()
            operators.push(o)

    # while not numbers.is_empty() and not operators.is_empty():              #evaluate the expression from stacks
    #     pass
            
    
    # Step 1: Initialize stacks for numbers and operators.
    # Hint: Use Stack class to create two stacks, one for numbers and one for operators.
    
    # Step 2: Parse the expression.
    # Hint: Loop through each character in the expression.
    # If the character is a digit, accumulate it in a string for multi-digit numbers.
    # If the character is an operator, push the accumulated number to the number stack, and push the operator to the operator stack.
    
    # Step 3: Push the last accumulated number onto the number stack.
    # Hint: After the loop, there might be a number that you haven't pushed onto the number stack yet.
 
    # Step 4: Reverse the stacks
    # Hint: Create two new temporary stacks and pop from the original stacks to push into these, thereby reversing the order.
    
    # Step 5: Initialize the result with the first number from the reversed number stack.
    # Hint: Pop the first number off the reversed number stack and store it as your initial result.
    
    # Step 6: Perform the operations.
    # Hint: Loop through the reversed operator stack, pop one operator and one number each time from their respective reversed stacks,
    # and update the result accordingly.
    
    # Step 7: Return the final result.
    # Hint: The final result is the value you get after applying all operators to the numbers.
    
    return result  # replace this line with the correct return


 
if __name__ == '__main__':
    expression = "1+2-3+4-5"
    print(eval_expr(expression))  # -1
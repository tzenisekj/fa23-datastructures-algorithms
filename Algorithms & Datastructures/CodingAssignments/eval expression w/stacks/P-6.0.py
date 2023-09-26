from stack_list import Stack, Empty
my_name = ""
 
 
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
    
    return 0  # replace this line with the correct return
 
 
 
 
if __name__ == '__main__':
    expression = "1+2-3+4-5"
    print(eval_expr(expression))  # -1
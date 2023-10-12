import os
my_name = "Tyler Zenisek"
# Assignment: Programming Project 2, P-4.23
def find(path, filename):
     """
     This function searches for a specific filename in a given path using recursion.
     Parameters:
     path (str): The root path from which the search should begin.
     filename (str): The filename to search for. A partial match is sufficient.
     Returns:
     None. The function should print the full path of each matching file.
     """
     # WRITE YOUR CODE HERE
     list = os.listdir(path)
     for i in list:
         path += i
         if os.path.isdir(path):
            find(path, filename)
         else:
             if i.endswith(filename):
                print(path)
     # Hint: You can use os.listdir(path) to get a list of all files and directories in 'path'.
     # For each entry in this list, use os.path.join(path, entry) to get the full path.
     # Check if this path ends with 'filename'. If it does, print the path.
     # If the entry is a directory, call the 'find' function recursively with the new path.

if __name__ == '__main__':
 path = "./TDir/" # from current directory check inside TDir folder
 filename = ".docx" # All word ducuments
 find(path, filename)


"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.
"""


if __name__ == '__main__':
    N = int(input())

    
    lst = []
    for m in range(N):
        x = input().split()
        command = str(x[0])
        if command == 'append':
            lst.append(int(x[1]))
        elif command == 'print':
            print(lst)
        elif command == 'insert':
            lst.insert(int(x[1]), int(x[2]))
        elif command == 'reverse':
            lst.reverse()
        elif command == 'pop':
            lst.pop()
        elif command == 'sort':
            lst.sort()
        elif command == 'remove':
            lst.remove(int(x[1]))


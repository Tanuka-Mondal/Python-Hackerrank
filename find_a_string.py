#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.


def count_substring(string, sub_string):
    counter,sum = 0,0
    for _ in range(0, len(string)):
        if matcher(string[counter:(len(sub_string)+counter)], sub_string):
            sum = sum + 1
        counter=counter + 1
    return sum

def matcher(sliced_str, sub_string):
    return sliced_str == sub_string



if __name__ == '__main__':

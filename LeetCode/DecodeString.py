"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""

# Understand - repeat letters in square brackets by the number outside the square brackets
#       There are 4 characters in the string. We can make an edge case for each one while we loop thru
#       It makes sense to create a stack for letters and a stack for numbers
#       Once you hit a "]" you pop off the characters and pop off the number. Then repeat the characters number times and store in result string


def decodeString(self, str1: str) -> str:
    stack_letters = []  # letters stack
    stack_nums = []  # num stack
    num = ""  # to keep track of digits
    result_str = ""  # result string
    for i in str1:
        if i.isdigit():
            num += i
        elif i == "[":
            stack_letters.append(result_str)
            stack_nums.append(int(num))
            # reset so that we don't push what we have already pushed again
            num, result_str = "", ""
        elif i == "]":
            n = stack_nums.pop()  # get the last number we pushed
            t = stack_letters.pop()  # get the last letter(s) we pushed
            # multiply letters inside brackets by n, then add to previous string
            result_str = t + result_str * n

        else:  # it's a letter
            result_str += i
    return result_str

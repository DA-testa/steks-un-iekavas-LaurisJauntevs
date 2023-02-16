# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))
            pass

        if next in ")]}":
            opening_brackets_stack.append(Bracket(next,i+2))
            if are_matching==(opening_brackets_stack(next, i+1),opening_brackets_stack[-1]):
                opening_brackets_stack.pop()
            else:
                return i+1
            # Process closing bracket, write your code here
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if text ==
        print("Sucess")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()


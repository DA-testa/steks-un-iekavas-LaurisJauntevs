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
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            if opening_brackets_stack.pop():
                return opening_brackets_stack[-1].position
            return "Sucess"
            # Process closing bracket, write your code here
            pass


def main():
    x = input("input I or F:")
    if "F" in x:
        path = input("Input file path:")
        with open(path, "r") as file:
            a = file.read()
            mismatch = find_mismatch(a)
            if mismatch == 0:
                print("Sucess")
            else:
                print(mismatch)
    if "I" in x:
        a = input()
        mismatch = find_mismatch(a)
        if mismatch == 0:
                print("Sucess")
        else:
                print(mismatch)
    else:
         print("Wrong input")
    # Printing answer, write your code here

if __name__ == "__main__":
    main()

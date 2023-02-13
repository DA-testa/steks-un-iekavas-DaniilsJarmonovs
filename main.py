#Programmas autors: Daniils Jarmonovs ; 221RDC003 ; 18. grupa
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        #print(opening_brackets_stack)
        #print("i = ", i)
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if (len(opening_brackets_stack)==0):
                  return i+1
            elif(not are_matching(opening_brackets_stack[-1].char, next)):
                  return i+1
            opening_brackets_stack.pop()
            pass
      
    if len(opening_brackets_stack) == 0:
        return 0
    else:
        return i+1


def main():
    inputMode = input()
    if("I" in inputMode):
        text = input()    
    elif("F" in inputMode):
        #Do something...
        print()
    else:
        return
    mismatch = find_mismatch(text)
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()



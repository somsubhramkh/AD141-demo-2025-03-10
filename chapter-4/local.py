#!/usr/bin/env python3
def demo():
    global count
    count = 0
    print("Inside Function:", count)


count = 5
print("Before Function:", count)
demo()
print("After Function: ", count)
#!/usr/bin/env python3
# separator = "----------------------------"
# name = "First: {} \tLast Name: {} \tMiddle Initial: {}"
# print(name.format("John","Smith","C."))
# print(name.format("Melony", "Jones", "A."))

# name = "{1},  {0}"

# print(name.format("First", "Last"))
# print(name.format("John", "Smith"))
# print(name.format("Melony", "Jones"))

dimensions = "Type: {type}\nHeight:{height}, Width:{width}"
print(dimensions.format(height=50,width=20,type="Package"))

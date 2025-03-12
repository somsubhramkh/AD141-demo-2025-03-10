#!/usr/bin/env python3
def volume(length=10, width=5, height=2):
    """Returns the volume of a box for given dimensions"""
    return length * (width + height)


# dim1 = float(input("Enter length of the box: "))
# dim2 = float(input("Enter width of the box: "))
# dim3 = float(input("Enter height of the box: "))
# result = volume(height=dim3, width=dim2, length=dim1)
# print("The volume is:", result)

print(volume())
#!/usr/bin/env python3
# The following String has 3 sets of 2 spaces in it
data = "\t  \nabc  def\t  \n"
print(data)
result = data.strip()
print(len(data),len(result),len(data.rstrip()),len(data.lstrip()))
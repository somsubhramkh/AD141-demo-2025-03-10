#!/usr/bin/env python3

counter = 5
total = 0

while True:
    total += counter
    counter += 1
    if counter == 11:
        break
    print("Running Total =", total, "Counter =", counter)

print()
print("Final Total =", total)
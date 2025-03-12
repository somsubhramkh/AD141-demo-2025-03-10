#!/usr/bin/env python3
def main():
    total = 0
    msg = "Please enter a number, or 'end' to quit: "
    while True:
        try:
            value = input(msg)
            if value == "end":
                break
        except EOFError:
            print("Unexected End of Stream")
            continue
        try:
            total += int(value)
        except ValueError as ve:
            print("Invalid - Enter a number",ve)
        finally:
            print("Finally: This line will always execute")

    print("Total is", total)


if __name__ == "__main__":
    main()
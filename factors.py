#!/usr/bin/env python3
import sys


def factorize(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return i, number // i
    return None, None


def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                if number > 1:
                    factor1, factor2 = factorize(number)
                    if factor1 is not None and factor2 is not None:
                        print(f"{number}={factor1}*{factor2}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    else:
        main(sys.argv[1])

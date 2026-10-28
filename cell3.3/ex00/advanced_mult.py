#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) > 1:
        print("none")
        return
    table = 0
    while table <= 10:
        line = "Table de " + str(table) + ":"
        value = 0
        while value <= 10:
            line += " " + str(table * value)
            value += 1
        print(line)
        table += 1
if __name__ == "__main__":
    main()
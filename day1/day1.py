#!/usr/bin/python3

def main():
    """ solves aoc 2021 day1
    """
    with open("day_input.txt", encoding="utf-8") as day1_text:
        current_high = 0
        inc_counter = 0
        for line in day1_text:
            if int((line.strip())) > current_high:
                inc_counter += 1
            current_high = int((line.strip()))
    print(inc_counter-1)

if __name__ == '__main__':
    main()

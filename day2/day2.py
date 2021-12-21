#!/usr/bin/python3

def main():
    """ provides solution for aoc 2021 day 2
    """
    horizontal = 0
    depth = 0
    with open("day_input.txt", encoding="utf-8") as day_input:
        for line in day_input:
            direction_steps = line.strip().split(" ")
            if "forward" in direction_steps[0]:
                horizontal = horizontal + int(direction_steps[1])
            elif "down" in direction_steps[0]:
                depth = depth + int(direction_steps[1])
            else:
                depth = depth - int(direction_steps[1])
    result = horizontal * depth
    print(result)

if __name__ == '__main__':
    main()

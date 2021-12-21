#!/usr/bin/python3

def get_signifcant(h):
    """ helper function to get the most and least
    significant bit
    """
    zeros = h.count(0)
    ones = h.count(1)
    if zeros > ones:
        return 0, 1
    else:
        return 1, 0

def main():
    """ solves aoc 2021 day3-1
    """
    gamma = ""
    epislon = ""
    horizontal = []
    first_run = True
    with open("day_input.txt", encoding="utf-8") as day_input:
        count_lines = 0
        for line in day_input:
            if first_run:
                for x in range(len(line)-1):
                    horizontal.append([int(line[x])])
            else:
                for x in range(len(line)-1):
                    horizontal[x].append(int(line[x]))
            first_run = False
            count_lines = count_lines +1 
    for h in horizontal:
        gamma_bit, epislon_bit = get_signifcant(h)
        gamma = gamma + str(gamma_bit)
        epislon = epislon + str(epislon_bit)
    gamma_dec = int(gamma, 2)
    epislon_dec = int(epislon, 2)
    result = gamma_dec * epislon_dec
    print(result)

if __name__ == '__main__':
    main()

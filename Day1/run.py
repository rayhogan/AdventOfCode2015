

def solution():
    with open('input.txt') as f:
        lines = f.readlines()

    floor = 0
    basement = 0
    for index, character in enumerate(lines[0]):
        if floor == -1 and basement == 0:
            basement = index

        if character == '(':
            floor += 1
        else:
            floor -= 1

    print(floor)
    print(basement)


if __name__ == '__main__':
    solution()



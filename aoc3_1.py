import numpy as np


def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    out1 = out[0].split(",")
    out2 = out[1].split(",")
    f.close()
    return [out1, out2]

def get_size(input):

    x = 0
    y = 0
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    for i in input:
        direction = i[0]
        dist = int(i[1:])

        if direction == "R":
            x = x + dist
            if x > x_max:
                x_max = x
        elif direction == "L":
            x = x - dist
            if x < x_min:
                x_min = x
        elif direction == "U":
            y = y + dist
            if y > y_max:
                y_max = y
        elif direction == "D":
            y = y - dist
            if y < y_min:
                y_min = y
        #print("Direction and distance is: ", i)
        #print("x and y are: ", x, " ", y)

    return [x_min, x_max, y_min, y_max]

def move(input, matrix, value):

    x = 5000
    y = 5000

    for i in input:
        direction = i[0]
        dist = int(i[1:])

        if direction == "R":
            matrix[y, x:x + dist] += value
            x = x + dist
        elif direction == "L":
            matrix[y, x - dist:x] += value
            x = x - dist
        elif direction == "U":
            matrix[y:y+dist, x] += value
            y = y + dist
        elif direction == "D":
            matrix[y - dist:y, x] += value
            y = y - dist
        #print("Direction and distance is: ", i)
        #print("x and y are: ", x, " ", y)

    return matrix


def main():
    input = read_input("aoc3_input.txt")
    print(input[0])
    print(get_size(input[0]))
    print(get_size(input[1]))

    board = np.zeros((10000,10000))

    board_1 = move(input[0], board, 1)
    print(board_1)

if __name__ == "__main__":
    main()
# given: coordinates of a sq in random order
# return: area of the sq

# we just need the length of one side so check the first x-coord and the first y-coord,
# if the second x-coord is the same as the first x-coord, then we get the vertical side and return the square of the side
# same if second y-coord is the same as the first y-coord

def sqArea(coords):
    # Loop through the coordinates
    x_coord = coords[0][0]
    y_coord = coords[0][1]

    for i in range(1, len(coords)):
        if coords[i][0] == x_coord:
            return (coords[i][1] - y_coord) ** 2
        elif coords[i][1] == y_coord:
            return (coords[i][0] - x_coord) ** 2

if __name__ == "__main__":
    for _ in range(int(input())):
        coords = []
        for _ in range(4):
            coords.append(list(map(int, input().split())))
        print(sqArea(coords))

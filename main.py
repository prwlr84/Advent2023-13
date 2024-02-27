from input import input_string


def parse_input(string):
    img_strs = [s.split('\n') for s in string.split('\n\n')]
    img_grids = []
    for i in img_strs:
        img_grids.append([list(s) for s in i])

    return img_grids


def calc_mirror_score(grid, vertical=False):
    for i, e in enumerate(grid):
        while len(grid) - 4 > i > 3:
            if all([e == grid[i + 1], grid[i - 1] == grid[i + 2], grid[i - 2] == grid[i + 3], grid[i - 3] == grid[i + 4]]):
                return i + 1 if vertical else (i + 1) * 100
            else:
                break

    return 0


# def mirrors(grids):
#     count = 0
#     for grid in grids:
#         score = calc_mirror_score(grid)
#         if score == 0:
#             score = calc_mirror_score([list(row) for row in zip(*grid[::-1])], vertical=True)
#         count += score
#
#     print(count)


def mirrors(grids):
    count = 0
    for grid in grids:
        max = 0
        current = None
        for i,line in enumerate(grid):
            for j in range(len(grid), 1):
                while j < i - 1:


        score = calc_mirror_score(grid)
        if score == 0:
            score = calc_mirror_score([list(row) for row in zip(*grid[::-1])], vertical=True)
        count += score

    print(count)


if __name__ == '__main__':
    mirrors(parse_input(input_string))

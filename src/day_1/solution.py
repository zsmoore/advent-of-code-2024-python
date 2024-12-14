def solve_it(col_1, col_2):
    col = make_columns(col_1, col_2)
    summarized = summarize(col)
    return summarized


def make_columns(col_1, col_2):
    col_1.sort()
    col_2.sort()

    col_3 = []

    for i in range(0, len(col_1)):
        item_1 = col_1[i]
        item_2 = col_2[i]

        value = abs(item_1 - item_2)
        col_3.append(value)

    return col_3


# [1, 2, 3]
def summarize(col):
    total = 0
    for num in col:
        total = total + num

    return total

def read_file(name):
    col_1 = []
    col_2 = []
    with open(name, 'r') as f:
        for line in f.readlines():
            spl = line.split()
            col_1.append(int(spl[0]))
            col_2.append(int(spl[1]))

    return col_1, col_2


def solve_day_1():
    col_1, col_2 = read_file('input.txt')

    sor = make_columns(col_1, col_2)
    tot = summarize(sor)

    return tot


if __name__ == "__main__":
    print(solve_day_1())
from input import input_string


def parse_input(string):
    reports = []
    for line in string.split('\n'):
        key, values = line.split()

        values = list(map(int, values.split(',')))
        reports.append((key, values))
    return reports





def get_variation_sum(line, pattern):


if __name__ == '__main__':

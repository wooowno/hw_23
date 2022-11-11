def file_data(filename):
    with open('data/' + filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def filter_lines(lines, value):
    return filter(lambda line: value in line, lines)


def map_lines(lines, column):
    column = int(column)
    return map(lambda line: line.split()[column], lines)


def unique_lines(lines, value):
    return set(lines)


def sort_lines(lines, reverse):
    return sorted(lines, reverse=True if reverse == 'desc' else False)


def limit_lines(lines, value):
    value = int(value)
    return list(lines)[:value]

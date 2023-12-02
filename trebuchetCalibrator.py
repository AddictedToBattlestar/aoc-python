def get_value(line):
    left = None
    right = None
    for c in line:
        if c.isdigit():
            if not left:
                left = int(c)
            right = int(c)
    return (left * 10) + right


def calculate(lines):
    calibration_value = 0
    for line in lines:
        calibration_value += get_value(line=line)
    return calibration_value


def calculate_from_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.readlines()
    return calculate(lines=lines)


if __name__ == '__main__':
    result = calculate_from_file(file_name="day1-part1-data.txt")
    print(f'The solution for Day 1, part 1 is: {result}')
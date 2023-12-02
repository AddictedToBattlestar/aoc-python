numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_calibration_value(line):
    left = get_left_calibration_value(line)
    right = get_right_calibration_value(line)
    return (left * 10) + right


def get_left_calibration_value(line):
    buffer = ""
    for c in line:
        value = get_value_from_right(c, buffer)
        if value:
            return value
        else:
            buffer = buffer + c
    return None


def get_right_calibration_value(line):
    buffer = ""
    for c in reversed(line):
        value = get_value_from_left(c, buffer)
        if value:
            return value
        else:
            buffer = c + buffer
    return None


def get_value_from_right(character_value, buffer):
    if character_value.isdigit():
        return int(character_value)
    new_buffer = buffer + character_value
    for number_string, value in numbers.items():
        if number_string == new_buffer[-len(number_string):]:
            return value
    return None


def get_value_from_left(character_value, buffer):
    if character_value.isdigit():
        return int(character_value)
    new_buffer = character_value + buffer
    for number_string, value in numbers.items():
        if number_string == new_buffer[:len(number_string)]:
            return value
    return None


def calculate(lines):
    calibration_value = 0
    line_number = 1
    for line in lines:
        line_value = get_calibration_value(line=line)
        calibration_value += line_value
        print(f'line_number {str(line_number)}, line_value = {line_value}, calibration_value = {calibration_value}, value = {line}')
        line_number += 1
    return calibration_value


def calculate_from_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.readlines()
    return calculate(lines=lines)


if __name__ == '__main__':
    result = calculate_from_file(file_name="day1-data.txt")
    print(f'The solution for Day 1 is: {result}')
    # part 1: 54159
    # part 2: 53900, too high

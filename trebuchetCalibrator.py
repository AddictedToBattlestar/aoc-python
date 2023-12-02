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
    left = None
    right = None
    buffer = ""
    for c in line:
        value = get_value(c, buffer)
        if value:
            if not left:
                left = value
            right = value
            buffer = ""
        else:
            buffer = buffer + c
    return (left * 10) + right


def get_value(current_character, buffer):
    if current_character.isdigit():
        return int(current_character)
    new_buffer = buffer + current_character
    for number_string, value in numbers.items():
        if number_string == new_buffer[-len(number_string):]:
            return value
    return None


def calculate(lines):
    calibration_value = 0
    for line in lines:
        calibration_value += get_calibration_value(line=line)
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

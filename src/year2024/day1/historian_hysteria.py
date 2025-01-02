from src.utilities.file_reader import read_lines_from_file

def get_total_distance(input_data):
    list1 = []
    list2 = []
    for input_line in input_data:
        left, right = input_line.split("   ")
        list1.append(int(left))
        list2.append(int(right))
    list1.sort()
    list2.sort()
    running_difference = 0
    for i in range(len(list1)):
        running_difference = running_difference + abs(list1[i] - list2[i])
    return running_difference

def get_similarity_score(input_data):
    left_numbers = []
    right_number_map = {}
    for input_line in input_data:
        left, right = input_line.split("   ")
        left_numbers.append(int(left))
        right_value = int(right)
        if right_value in right_number_map:
            right_number_map[right_value] += 1
        else:
            right_number_map[right_value] = 1
    get_similarity_score = 0
    for value in left_numbers:
        if value in right_number_map:
            get_similarity_score += value * right_number_map[value]
    return get_similarity_score

def get_total_distance_from_file(input_file):
    input_data = read_lines_from_file(input_file)
    return get_total_distance(input_data)

def get_similarity_score_from_file(input_file):
    input_data = read_lines_from_file(input_file)
    return get_similarity_score(input_data)

if __name__ == "__main__":
    part1_result = get_total_distance_from_file("data.txt")
    print(f"part 1 result {part1_result}")

    part2_result = get_similarity_score_from_file("data.txt")
    print(f"part 2 result {part2_result}")


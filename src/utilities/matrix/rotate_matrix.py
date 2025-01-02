def rotate_matrix_clockwise_90_degrees(input_data: list[str]) -> list[str]:
    rotated = []
    for character in input_data[0]:
        rotated.append(character)
    for row in input_data[1:]:
        for index, character in enumerate(row):
            rotated[index] = character + rotated[index]
    return rotated
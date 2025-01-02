from src.utilities.matrix.rotate_matrix import rotate_matrix_clockwise_90_degrees

def test_rotate_input_data_2x2():
    result = rotate_matrix_clockwise_90_degrees(
        [
            "10",
            "01"
        ]
    )

    assert result == [
            "01",
            "10"
    ]

def test_rotate_input_data_4x4():
    result = rotate_matrix_clockwise_90_degrees(
        [
            "1234",
            "4123",
            "3412",
            "2341"
        ]
    )

    assert result == [
            "2341",
            "3412",
            "4123",
            "1234"
    ]

def test_rotate_input_data_1x4():
    result = rotate_matrix_clockwise_90_degrees(
        [
            "1234"
        ]
    )

    assert result == [
            "1",
            "2",
            "3",
            "4"
    ]

def test_rotate_input_data_4x1():
    result = rotate_matrix_clockwise_90_degrees([
        "1",
        "2",
        "3",
        "4"
    ])

    assert result == ["4321"]

def test_rotate_input_data_2x4():
    result = rotate_matrix_clockwise_90_degrees([
        "15",
        "26",
        "37",
        "48"
    ])

    assert result == [
        "4321",
        "8765"
    ]
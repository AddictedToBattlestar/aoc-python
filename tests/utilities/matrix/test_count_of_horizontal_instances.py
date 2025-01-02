from src.utilities.matrix.count_of_horizontal_instances import count_of_horizontal_instances

def test_exact_match():
    result = count_of_horizontal_instances([
        "test"
    ], "test")

    assert result == 1

def test_single_character_match():
    result = count_of_horizontal_instances(["x"], "x")
    assert result == 1

def test_no_match():
    result = count_of_horizontal_instances([""], "test")
    assert result == 0

def test_match_with_spaces():
    result = count_of_horizontal_instances([".test."], "test")
    assert result == 1

def test_backwards_match():
    result = count_of_horizontal_instances(["tset"], "test")
    assert result == 1

def test_backwards_match_with_spaces():
    result = count_of_horizontal_instances([".tset."], "test")
    assert result == 1

def test_multiples():
    result = count_of_horizontal_instances(["test.test"], "test")
    assert result == 2

def test_multiples_with_backwards_match():
    result = count_of_horizontal_instances(
    [
        "test.tset",
        "test.tset",
        "test.tset",
        "test.tset",
    ],
    "test"
    )
    assert result == 8
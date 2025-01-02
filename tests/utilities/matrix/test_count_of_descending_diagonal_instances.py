from src.utilities.matrix.count_of_descending_diagonal_instances import count_of_descending_diagonal_instances


def test_exact_match():
    result = count_of_descending_diagonal_instances([
        "t...",#    "3210", current_diagonal_row_being_scanned
        ".e..",#    "4321",
        "..s.",#    "5432",
        "...t",#    "6543",
    ], "test")
    assert result == 1

def test_single_character_match():
    result = count_of_descending_diagonal_instances(["x"], "x")
    assert result == 1

def test_no_match():
    result = count_of_descending_diagonal_instances([""], "test")
    assert result == 0

def test_match_with_spaces():
    result = count_of_descending_diagonal_instances([
        "......",
        ".t....",
        "..e...",
        "...s..",
        "....t.",
        "......"
    ], "test")
    assert result == 1

def test_backwards_match():
    result = count_of_descending_diagonal_instances([
        "t...",
        ".e..",
        "..s.",
        "...t",
    ], "test")
    assert result == 1

def test_backwards_match_with_spaces():
    result = count_of_descending_diagonal_instances([
        "......",
        ".t....",
        "..s...",
        "...e..",
        "....t.",
        "......"
    ], "test")
    assert result == 1

def test_multiples():
    result = count_of_descending_diagonal_instances([
        "t........",
        ".e.......",
        "..s......",
        "...t.....",
        ".........",
        ".....t...",
        "......e..",
        ".......s.",
        "........t",
    ], "test")
    assert result == 2

def test_multiples_with_backwards_match():
    result = count_of_descending_diagonal_instances([
        "t........",
        ".s.......",
        "..e......",
        "...t.....",
        ".........",
        ".....t...",
        "......s..",
        ".......e.",
        "........t",
    ], "test")
    assert result == 2
from src.utilities.split_strip import split_strip


def split_strip_to_int(source_text, split_character):
    if split_character == " ":
        split_text = split_strip(source_text, " ")
        filtered_text = list(filter(lambda n: n != "", split_text))
        return list(map(lambda n: int(n), filtered_text))
    else:
        return [int(x.strip()) for x in source_text.split(split_character)]

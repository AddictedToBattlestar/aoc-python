def read_lines_from_file(file_name: str):
    with open(file_name, "r") as text_file:
        return [x.strip() for x in text_file.readlines()]

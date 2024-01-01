from src.day8_haunted_wasteland.network_mapper import NetworkMapper


def read_file(file_name: str):
    with open(file_name, "r") as text_file:
        line_number = 1
        instructions = None
        lines = text_file.readlines()
        network_mapper = NetworkMapper()
        for line in lines:
            if line_number == 1:
                instructions = line.strip()
            else:
                if line_number > 2:
                    network_mapper.add_node(line)
            line_number += 1
        return instructions, network_mapper

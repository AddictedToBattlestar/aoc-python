from utilities.split_strip import split_strip


class NetworkMapper:
    def __init__(self):
        self.starting_node_ids = []
        self.network = {}

    def add_node(self, raw_node):
        location, paths_to_take = split_strip(raw_node, "=")
        if location[-1] == "A":
            self.starting_node_ids.append(location)
        paths_to_take = paths_to_take.replace(")", "").replace("(", "")
        left_path, right_path = split_strip(paths_to_take, ",")
        self.network[location] = (left_path, right_path)

    def add_nodes(self, raw_nodes):
        for raw_node in raw_nodes:
            self.add_node(raw_node)
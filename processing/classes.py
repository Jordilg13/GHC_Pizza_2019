class Rules:
    def __init__(self, line):
        line = line.split(" ")
        self.rows = int(line[0])
        self.cols = int(line[1])
        self.min_ingredients = int(line[2])
        self.max_cells = int(line[3].replace("\n", ""))


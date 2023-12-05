#Objects that help with file management

class FileWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data, mode="a"):
        with open(self.file_path, mode) as f:
            f.write(data)

    def write_lines(self, lines, mode="a"):
        with open(self.file_path, mode) as f:
            f.writelines(lines)

    def append(self, data):
        self.write(data, mode="a")

#Objects that help with time management 
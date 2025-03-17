import sys
import os

class FileParser:
    
    def __init__(self, filename=None):
        self.filename = filename or os.path.abspath(sys.argv[0])
        self.lines = self._read_file()

    def _read_file(self):
        with open(self.filename, "r") as f:
            return f.readlines()

    def extract_labels(self, prefix="#:"):
        labels = {}
        for i, line in enumerate(self.lines):
            if line.strip().startswith(prefix):
                label_name = line.strip()[len(prefix):].strip()
                labels[label_name] = i + 1
        return labels

    def extract_commands(self, prefix="#!"):
        commands = []
        for line in self.lines:
            if line.strip().startswith(prefix):
                commands.append(line.strip()[len(prefix):].strip())
        return commands

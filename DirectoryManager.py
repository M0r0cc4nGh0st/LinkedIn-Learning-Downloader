import os


class DirectoryManager:
    def __init__(self):
        self.directory = None

    def get_directory(self):
        if self.directory is not None:
            return self.directory
        else:
            # Default path or raise an error
            return os.path.join(os.path.expanduser('~'), 'Desktop', 'LinkedIn Learning Courses')

    def set_directory(self, path):
        self.directory = path

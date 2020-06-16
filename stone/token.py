

class Token:
    EOF = -1
    def __init__(self, line):
        self._line_number = line

    def get_line_number(self):
        return self._line_number

    def is_identifier(self):
        return False

    def is_number(self):
        return False

    def is_string(self):
        return False

    def get_number(self):
        raise ValueError("Stone Exception")

    def get_text(self):
        return ""

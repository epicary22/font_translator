import json

SPACING_LENGTH = 1

with open("charsets.json", "r") as file:
    data = file.read()
    charsets = json.loads(data)


class BigChar:
    def __init__(self, char, char_type, charset=None, transform_char=True):
        self.char = char
        self.charset = charset
        self.char_type = char_type
        if transform_char and charset:
            self.char = charsets[charset][char_type][self.char]
        self.row_count = self.char.count("\n") + 1

    def __repr__(self):
        return self.char

    def append_(self, big_char):
        if big_char.charset == self.charset:
            old_char = self.char.split("\n")
            input_char = big_char.char.split("\n")
            new_char = "\n".join(
                [old_char[row] + " "*SPACING_LENGTH + input_char[row]
                for row in range(self.row_count)]
            )
            return BigChar(new_char, "text", self.charset, False)
        else:
            raise TypeError(f"Cannot concatenate different charsets: {self.charset}, {big_char.charset}")

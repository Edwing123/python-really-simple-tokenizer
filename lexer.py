import enum
import string
from typing import List


class Tokens(int, enum.Enum):
    NUMBER = 0
    STRING = 1
    ASSIGNMENT = 2
    NEWLINE = 3


class UnexpectedCharacterException(Exception):
    pass


tokensToString = ["NUMBER", "STRING", "ASSIGNMENT", "NEWLINE"]

digits = string.digits

letters = string.ascii_letters


def getTokenString(type: Tokens):
    return tokensToString[type.value]


class Token:
    def __init__(self, type: Tokens, value: str) -> None:
        self.type = getTokenString(type)
        self.value = value

    def __str__(self) -> str:
        return f"Token({self.type}, {self.value})"

    def to_dict(self):
        return {"type": self.type, "value": self.value}


class Lexer:
    def __init__(self) -> None:
        self.tokens: list[Token] = []
        self.position = 0

    def feed(self, data: str):
        self.data = data

    def add_token(self, type: Tokens, value: str):
        self.tokens.append(Token(type, value))

    def is_eof(self):
        return self.position == len(self.data)

    def consumeNumber(self) -> None:
        number = ""

        while (c := self.data[self.position]) in digits:
            number += c

            self.position += 1

            if self.is_eof():
                break

            c = self.data[self.position]

        self.add_token(Tokens.NUMBER, number)
        return None

    def consumeString(self) -> None:
        string = ""

        while (c := self.data[self.position]) in letters:
            string += c

            self.position += 1

            if self.is_eof():
                break

        self.add_token(Tokens.STRING, string)
        return None

    def start(self):
        while not self.is_eof():
            c: str = self.data[self.position]

            # whitespace
            # skip whitespace
            if c in [" "]:
                self.position += 1
                continue

            # number
            if c in digits:
                self.consumeNumber()
                continue

            # string
            # ? I'm just handling letters in range [a-zA-Z]
            if c in letters:
                self.consumeString()
                continue

            # assingment/equal sign
            if c == "=":
                self.add_token(Tokens.ASSIGNMENT, c)
                self.position += 1
                continue

            # newline
            if c in ["\n", "\r\n"]:
                self.add_token(Tokens.NEWLINE, c)
                self.position += 1
                continue

            # if c is not identified throw an error
            raise UnexpectedCharacterException(f'Unexpected character "{c}"')

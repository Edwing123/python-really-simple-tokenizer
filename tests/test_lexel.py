import unittest
import context


class LexerTest(unittest.TestCase):
    def test_number_token(self):
        data = ["1", "12", "123"]

        for d in data:
            lexer = context.Lexer()
            lexer.feed(d)
            lexer.start()

            tokens = lexer.tokens
            count = len(tokens)

            self.assertEqual(count, 1)
            self.assertEqual(str(tokens[0]), f"Token(NUMBER, {d})")

    def test_string_token(self):
        data = "Edwin Garcia"
        lexer = context.Lexer()

        lexer.feed(data)
        lexer.start()

        tokens = lexer.tokens
        count = len(tokens)

        self.assertEqual(count, 2)
        self.assertEqual(tokens[0].to_dict()["type"], "STRING")
        self.assertEqual(tokens[0].to_dict()["value"], "Edwin")

    def test_assignment_token(self):
        data = "Var=Value"
        lexer = context.Lexer()

        lexer.feed(data)
        lexer.start()

        tokens = lexer.tokens
        count = len(tokens)

        self.assertEqual(count, 3)
        self.assertEqual(tokens[1].to_dict()["type"], "ASSIGNMENT")

    def test_newline_token(self):
        data = "Hello World\n"
        lexer = context.Lexer()

        lexer.feed(data)
        lexer.start()

        tokens = lexer.tokens
        count = len(tokens)

        self.assertEqual(count, 3)
        self.assertEqual(tokens[2].to_dict()["type"], "NEWLINE")

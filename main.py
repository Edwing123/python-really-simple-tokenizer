from typing import List
import json
import sys

import lexer


def tokens_to_json(tokens: List[lexer.Token]):
    return json.dumps([t.to_dict() for t in tokens], indent=2)


def main(src: str, dest: str):
    l = lexer.Lexer()

    with open(src, encoding="utf-8") as f:
        l.feed(f.read())
        l.start()

    with open(dest, "w", encoding="utf-8") as f:
        tokens = tokens_to_json(l.tokens)
        f.write(tokens)


if __name__ == "__main__":
    try:
        src, dest = sys.argv[1:3]
        main(src, dest)
    except ValueError as _:
        print("Please provide all the value")

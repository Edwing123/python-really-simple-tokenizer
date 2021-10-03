import sys
import os

dirname = os.path.dirname(__file__)

sys.path.append(c := os.path.abspath(os.path.join(dirname, "..")))

from lexer import Lexer

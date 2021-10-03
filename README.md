# Python implementation of a simple lexer/tokenizer

it identifies tokens of type:

- STRING - sequense of ascii letters
- NUMBER - positive integers (+ not supported)
- NEWLINE - "\n"
- ASSIGNMENT - equals sign

## Requirements

- Python 3 (I used Python 3.9)

## Usage

- Clone the repository
- Execute the main python file with the required arguments

```
python main.py <src-data-file> <dest-data-file>
# <src-data-file> - file with plain text data
# <dest-data-file> - file where the tokens list (json array) will be saved
```

Go to [examples](./examples) directory to see some examples of the output.

## Run tests

- Move to directory `tests`
- Execute command

```
python -m unittest
```

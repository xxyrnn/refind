# ReFind

Search for the given pattern in all the files within the given path and its subdirectories

---

## Installation

Clone the repository:

```bash
git clone https://github.com/xxyrnn/refind.git
```

## Usage

The script takes two required parameters:
- `path`: where to look for files, using `/` or `\` makes no difference as it is
parsed through the `pathlib` module
- `pattern`: what to search in the files, it is a regex

And two optional parameters:
- `-c`: maximum number of files to find
- `-r`: if used, the script will search for files recursively in all subdirectories

**N.B.:** `pattern` is parsed as a raw string, so characters like
parenthesis, brackets and `.*?` must be escaped (e.g. `\)`, `\.`) if you want them
to be read as normal symbols, otherwise they will be parsed as special flags

## Examples

- Search in the Desktop folder for files containing a word of at least one lowercase
letter

	```bash
	python3 refind.py "~/Desktop" "[a-z]+"
	```

- Search recursively in `./folder` for all the files containing the word "word"

	```bash
	python3 refind.py -r "./folder" "word"
	```
 
- Search recursively in `/` for maximum 10 files containing a three-digit number

	```bash
	python3 refind.py -r -c 10 "/" "\b[0-9]{3}\b"
	```

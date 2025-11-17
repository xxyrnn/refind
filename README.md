# ReFind

Search for the given pattern in all the files within the given path and its subdirectories

---

## Download

Clone the repository:

```bash
git clone https://github.com/xxyrnn/refind.git
```

## Usage

The script takes two positional parameters: `path` and `pattern`.

`path`: where to look for files, using "/" and "\\" makes no difference since it is
then parsed through the pathlib module
`pattern`: what to search in the files, it is read as a raw string and used as a regex
pattern, so it can contain all the regex special flags without backslashes

## Examples

- Search for words containing at least one lower letter in the desktop folder recursively

```bash
python3 refind.py ~/Desktop "[a-z]+"
```

- Search for the word "word" in all the files in `./folder` recursively

```bash
python3 refind.py ./folder "word"
```

---

## TODO

- Add logic to choose between searching only in the given directory or recursively
- Add logic to only find the pattern `count` (or less if `count` is not reached) times and then exit

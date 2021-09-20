# Source Delimiter

A tool to generate nice-looking comment to separate parts of your source code files. For example, if you want to generate a `Serial communication` part in your file, Source Delimiter will generate the following.
```C
/* -------------------------- Serial communication -------------------------- */
```

## User manual

```
usage: source_delimiter.py [-h] -l LANGUAGE -c COMMENT [-s SIZE]

Source Delimiter is a tool to generate pretty comment meant to be used as
delimiters in source file.

optional arguments:
  -h, --help            show this help message and exit
  -l LANGUAGE, --language LANGUAGE
                        The name of the programming language the comment will
                        be made in. The supported languages are c, lua, and
                        python.
  -c COMMENT, --comment COMMENT
                        The comment you want to produce.
  -s SIZE, --size SIZE  The total length of the output result.
```


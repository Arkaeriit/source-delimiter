#!/usr/bin/env python3

import argparse
import sys

# For some programming languages, present the start and stop
# comment delimiters
comment_delimiters = {
        "c"        : {"start": "/* " , "stop": " */"},
        "lua"      : {"start": "--"  , "stop": ""   },
        "python"   : {"start": "# "  , "stop": " #" },
        "apl"      : {"start": "⍝ "  , "stop": " ⍝" },
        "fortranIV": {"start": "C"   , "stop": "Ͻ"  }, 
        "fortran90": {"start": "!-"  , "stop": "-!" }, 
        "latex"    : {"start": "% "  , "stop": " %" }, 
        "forth"    : {"start": "( "  , "stop": " )" }, 
        "ocaml"    : {"start": "(* " , "stop": " *)"}, 
        "html"     : {"start": "<!--", "stop": "-->"},
        "assembly" : {"start": ";"   , "stop": ";"  },
}

# For all supported languages, corelate their name
# to a language in the comment_delimitersdictionary
all_languages = {
        "c"        : ["C", "C++", "C#", "Java", "Javascript", "Verilog", "Go", "PHP", "Swift", "Rust"],
        "lua"      : ["Lua", "VHDL", "Ada", "AppleScript", "Haskell", "SQL", ],
        "python"   : ["Python", "Shell", "Nim", "Perl", "R", "Ruby", ],
        "apl"      : ["APL", ],
        "fortranIV": ["FortranIV", ],
        "fortran90": ["Fortran90", ],
        "latex"    : ["LaTeX", "Matlab"],
        "forth"    : ["FORTH", ],
        "ocaml"    : ["OCaml", "Pascal", ],
        "html"     : ["HTML", "XML", ],
        "assembly" : ["Assembly", "Lisp", ],
}


def list_available_languages():
    ret = ""
    language_lst = list(all_languages.values())
    for i in range(len(language_lst)-1):
        for lang in language_lst[i]:
            ret += lang + ", "
    for i in range(len(language_lst[-1])-1):
        ret += language_lst[-1][i] + ", "
    ret += "and " + language_lst[-1][-1] + "."
    return ret

def center_txt_in_line(txt, size):
    ret = ""
    used_txt = " " + txt + " "
    start_write = size // 2 - ( len(used_txt) // 2)
    for i in range(start_write):
        ret += "-"
    for i in range(len(used_txt)):
        ret += used_txt[i]
    for i in range(size - start_write - len(used_txt)):
        ret += "-"
    return ret

def get_delimiter(language):
    lang_types = list(all_languages.keys())
    for t in lang_types:
        for lang in all_languages[t]:
            if lang.lower() == language.lower():
                return comment_delimiters[t]
    print("Error, '"+language+"' is not a supported language.\n"
            "The supported languages are "+list_available_languages()+".", file = sys.stderr)
    sys.exit(1)

def add_comment_delimiters(txt, language):
    delimiters = get_delimiter(language)
    return delimiters["start"] + txt + delimiters["stop"]

def get_usable_size(size, language):
    delimiters = get_delimiter(language)
    return size - len(delimiters["start"]) - len(delimiters["stop"])

def make_comment(txt, size, language):
    size_used = get_usable_size(size, language)
    txt_line = center_txt_in_line(txt, size_used)
    return add_comment_delimiters(txt_line, language)

def main():
    parser = argparse.ArgumentParser(description="Source Delimiter is a tool to generate pretty comment meant to be used as delimiters in source file.")
    parser.add_argument("-l", "--language", type=str, help="The name of the programming language the comment will be made in. The supported languages are "+list_available_languages(), required=True)
    parser.add_argument("-c", "--comment", type=str, help="The comment you want to produce.", required=True)
    parser.add_argument("-s", "--size", type=int, help="The total length of the output result.", required=False, default=80)
    args = parser.parse_args()
    print(make_comment(args.comment, args.size, args.language))

if __name__ == "__main__":
    main()


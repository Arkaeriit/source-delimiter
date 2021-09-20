#!/usr/bin/env python3

import argparse

comment_delimiters = {
        "c": ["/* ", " */"],
        "lua": ["", ""],
        "python": ["# ", " #"],
}

def list_available_languages():
    ret = ""
    arg_lst = list(comment_delimiters.keys())
    for i in range(len(arg_lst)-1):
        ret += arg_lst[i] + ", "
    ret += "and " + arg_lst[len(arg_lst)-1] + "."
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

def add_comment_delimiters(txt, language):
    key = language.lower()
    delimiters = comment_delimiters[key]
    return delimiters[0] + txt + delimiters[1]

def get_usable_size(size, language):
    key = language.lower()
    delimiters = comment_delimiters[key]
    return size - len(delimiters[0]) - len(delimiters[1])

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


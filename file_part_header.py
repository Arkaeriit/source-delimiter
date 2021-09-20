#!/usr/bin/env python3

comment_delimiters = {
        "c": ["/* ", " */"],
        "lua": ["", ""],
        "python": ["# ", " #"],
}

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


print(center_txt_in_line("Coucou", 80))
print(make_comment("Coucou", 80, "C"))


#!/usr/bin/env python3

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

print(center_txt_in_line("Coucou", 80))


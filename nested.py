#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Swaav (with help from instructor)"

import sys


def bracket_checker(string):
    # openers = ["[", "{", "(", "<", "(*"]
    # closers = ["]", "}", ")", ">", "*)"]
    bracket_dictionary = {')': '(', '}': '{', ']': '[', '>': '<', '*)': '(*'}
    stack = []
    token_count = 0

    while string:
        token = string[0]
        if string.startswith('(*'):
            token = '(*'
        elif string.startswith('*)'):
            token = '*)'
        string = string[len(token):]
        token_count += 1
        if token in bracket_dictionary.values():
            stack.append(token)
        elif token in bracket_dictionary.keys():
            if not stack or stack.pop() != bracket_dictionary[token]:
                return ('NO '+ str(token_count))
    if stack:
        return ('NO ' + str(token_count))

    else:
        return 'YES'


def main():
    with open('input.txt') as f:
        with open('output.txt', 'w') as Ganon:
            for line in f:
                result = bracket_checker(line)
                print(result) 
                Ganon.write(result + '\n')


if __name__ == '__main__':
    main()

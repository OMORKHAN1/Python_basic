// Regex, short for Regular Expression, is a powerful tool used for searching, matching, and manipulating text based on specific patterns.

import re // re is Python's built-in module for working with regular expressions (regex). It provides functions and tools to search, match, split, replace, and manipulate text based on patterns.

T = int(raw_input()) // old version input which does not complie input 
for i in range(T):
    try:
        re.compile(raw_input())
        print True
    except:
        print False


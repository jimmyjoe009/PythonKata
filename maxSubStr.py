# Find the Length of the Longest Substring Without Repeating Characters

# Given a string s, return the length of the longest substring that has no repeating characters.

def maxstr(longstr):
    biggest=""
    current=""
    mymap=set()
    str_len=0
    for c in longstr:
        if c not in mymap:
            mymap.add(c)
            current+=c
            if len(current) > len(biggest):
                biggest=current
        else:
            current=c
            mymap=set()
            mymap.add(c)
    return(biggest)

print(maxstr("abcabcbbholygrail"))

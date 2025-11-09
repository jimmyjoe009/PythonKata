def is_isogram(string):
    mystr=string.casefold()
    for char in mystr:
        if (mystr.count(char)>1):
            return False
    return True

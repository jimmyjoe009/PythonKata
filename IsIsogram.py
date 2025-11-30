#An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
#Implement a function that determines whether a string that contains only letters is an isogram. 
#Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    mystr=string.casefold()
    for char in mystr:
        if (mystr.count(char)>1):
            return False
    return True

# More efficient version with reduced complexity
def is_isogram2(string):
    the_set=set(string)
    return(len(string)==len(the_set))

test_string="abcdeff"
print(is_isogram(test_string))
print(is_isogram2(test_string))

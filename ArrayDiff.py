#Implement a function that computes the difference between two lists. 
#The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). 
#The order of elements in the first list should be preserved in the result.

def array_diff(a, b):
    new_list=a
    for i in b:
        while (new_list.count(i) > 0):
            new_list.remove(i)
    return(new_list)

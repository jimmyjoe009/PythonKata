#Implement a function that computes the difference between two lists. 
#The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). 
#The order of elements in the first list should be preserved in the result.

def array_diff(a, b):
    new_list=a
    for i in b:
        while (new_list.count(i) > 0):
            new_list.remove(i)
    return(new_list)


# Improved version. Lower complexity
def array_diff2(a,b):
    the_set=set(b)
    return[i for i in a if (i not in the_set)]

list1=[1,2,3,4,5,6,7]
list2=[5,6,7,8,9,10]
print(array_diff(list1,list2))
print(array_diff2(list1,list2))

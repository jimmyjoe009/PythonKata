# You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
# Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    pair=0
    impair=0
    for i in integers:
        if (i%2==0):
            pair+=1
            my_pair=i
        else:
            impair+=1
            my_impair=i
        if (pair>1 and impair==1):
            return(my_impair)
        if (pair==1 and impair>1):
            return(my_pair) 
    return None


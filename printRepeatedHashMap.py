# Prints the repeated numbers in a set using HashMap method

a=[2, 5, 1, 2, 3, 5]
x={}
for n in a:
    if (x.get(n,0)>0):
        print(n)
    x[n]=x.get(n,0)+1

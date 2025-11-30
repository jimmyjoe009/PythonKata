# Prints the repeated numbers in a set using HashMap method

a=[2, 5, 1, 2, 3, 5]
x={}
for n in a:
    x[n]=x.get(n,0)+1
    if (x.get(n,0)>1):
        print(n)

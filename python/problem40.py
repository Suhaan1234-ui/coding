def patter(n):
    if n==0:
        return  #returning nothing to stop recursion
    print("*"*n)
    patter(n-1)
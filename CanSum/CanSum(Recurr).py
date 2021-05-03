def RemainderSum(n, arr):
    if n==0:
        return True
    if(n<0):
        return False
    for i in arr:
        rem=n-i
        if(RemainderSum(rem,arr)==True):
            return True
    return False
print(RemainderSum(9,[2,3,5]))

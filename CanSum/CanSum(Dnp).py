def RemainderSum(n, arr,memo={}):
    if(n in memo):
        return memo[n]
    if n==0:
        return True
    if(n<0):
        return False
    for i in arr:
        rem=n-i
        if(RemainderSum(rem,arr,memo)==True):
            memo[n]=True
            return True
    memo[n]=False
    return False
print(RemainderSum(300,[7,14]))

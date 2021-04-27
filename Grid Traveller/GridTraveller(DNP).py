def grid(m,n,dic={}):
    key=str(m) + ','+ str(n)
    if key in dic:
        return dic[key]
    if m==1 and n==1:
        return 1
    if(m==0 or n==0):
        return 0
    dic[key]= grid(m-1,n,dic)+grid(m,n-1,dic)
    return dic[key]
print(grid(18,18))

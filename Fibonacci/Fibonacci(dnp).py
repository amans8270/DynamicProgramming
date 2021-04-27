def fibo(n,dic={}):#Creating a dictionary to store previous calculated result, thus to avoid calculating same result again and again
    if n in dic:
        return dic[n]#if the present fibo(n) is  already  calculated it return the stored result.
    if n<=2:
        return 1
    dic[n]=fibo(n-1,dic)+fibo(n-2,dic) #cacluting and storing result in dictionary
    return dic[n] #returning the require fibo(n)
print(fibo(50)) #You can change this part or can ask for input from the user

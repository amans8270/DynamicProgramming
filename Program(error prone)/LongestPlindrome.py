def longestPalindrome(s):
    res=""
    max=0
    def helper(arr,start,end):
        while(arr[start]==arr[end] and start>=0 and end<=len(arr)-1):
            start-+1
            end+=1
        return arr[start+1,end]
    sarr=s.split(" ");
    for i in range(0,len(sarr)):
        oddstring=helper(sarr,i,i)
        if len(oddstring)>len(res):
            res=oddstring
        evenstring=helper(sarr,i,i+1)
        if len(evenstring)>len(res):
            res=evenstring
    return res.join(" ")
longestPalindrome("babad")

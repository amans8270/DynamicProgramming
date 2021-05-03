"""On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0"""
def solve(N,K):
    if N==1 and K==1:
        return False
    mid=(2**(N-1))//2
    if K<=mid:
        return solve(N-1,K)
    return not solve(N-1,K-mid)
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if(solve(N,K)):
            return 1
        return 0
        

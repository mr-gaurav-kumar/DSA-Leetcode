class Solution:
    def countCommas(self, n: int) -> int:

#         comma = 0

#         for i in range(1,n+1):
#             digits = len(str(i))
#             comma = comma + (digits - 1)//3

#         return comma


# #Time Complexity = O(n log n)
# #Spcae Complexity = O(log n) 

        ans = 0
        start = 1000
        commas = 1

        while start <= n:
            end = min(n,start*1000-1)

            count = end - start + 1
            ans = ans + (count * commas)

            start = start * 1000
            commas = commas + 1
        return ans

#Time Complexity = O(log n)
#Space Complexity = O(1)
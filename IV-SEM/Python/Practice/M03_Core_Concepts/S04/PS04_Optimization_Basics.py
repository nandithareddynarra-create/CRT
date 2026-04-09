'''1.
2. Usinh hastags
3. '''

'''input = [1,2,3,4,5,1]
output = True'''

'''input = [1,2,3]
output = False'''
'''Traditional Way'''
# def check_duplicates(nums):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]==nums[j]:
#                 return(True)
#     return(False)

# nums = list(map(int,input().split()))
# print(check_duplicates(nums))

'''Optimized solution'''
# def check_duplicates(nums):
#     return len(nums) != len(set(nums))
# nums = list(map(int,input().split()))
# print(check_duplicates(nums))
'''BruteForce'''
# def check_duplicates(nums):
#     s = set()
#     for ele in nums:
#         if ele in s:
#             return True
#         s.add(ele)
#     return False
# nums = list(map(int,input().split()))
# print(check_duplicates(nums))

# #Find the sum of array elements
# def Array_sum(nums):
#     s = 0
#     for i in range(len(nums)-1,-1,-1):
#         s += nums[i]
#     return s
# nums = list(map(int,input().split()))
# print(Array_sum(nums))

# def Array_sum_recursion(nums,i):
#     if i == -1:
#         return 0
#     return nums[i]+Array_sum_recursion(nums,i-1)
# print(Array_sum_recursion([10,20,30,40],3))

# def Array_sum(nums):
#     if len(nums) == 0:
#         return 0
#     return nums[-1] + Array_sum(nums[:-1])
# print(Array_sum([10,20,30,40,50]))

'''Reverse array'''

# def reverse_array(nums):
#     arr = []
#     for i in range(len(nums)):
#         arr.insert(0,nums[i])
    
#     return arr
# print(reverse_array([1,2,3,4]))

# def reverse_arr(nums,i,j):
#     if i>=j:
#         return nums
#     nums[i],nums[j] = nums[j],nums[i]
#     return(reverse_arr(nums,i+1,j-1))
# print(reverse_arr([1,2,3,4],0,3))

# def Reverse_string(st):
#     s = ""
#     for i in st:
#         s = i + s
#     return s
# print(Reverse_string("abc"))

def reverse_str_recursion(s):
    if s == "":
        return ""
    return s[-1] + reverse_str_recursion(s[:-1])
print(reverse_str_recursion("abc"))

def is_palindrome(s):
    return s == reverse_str_recursion(s)
print(is_palindrome("abc"))
print(is_palindrome("mam"))
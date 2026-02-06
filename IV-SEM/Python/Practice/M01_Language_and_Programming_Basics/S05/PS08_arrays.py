# import numpy as np
# arr = np.array([10,20,30])
# print(arr)

# print(np.max(arr))
# print(np.min(arr))
# print(np.sum(arr))
# print(np.mean(arr))
# print("Even numbers list is:", np.arange(2,10,2))
# print("Odd numbers list is :", np.arange(1,10,2))

# n = int(input("Enter the size:"))
# ele = list(map(int,input("enter ele:").split()))
# print("Array Ele are: ",np.array(ele))
# print("sum of elements:",np.sum(ele))

''''Third maximum number'''
# nums = list(map(int,input().split()))
# if len(set(nums)) >= 3:
#     print(sorted(set(nums))[-3])
# else:
#     print(max(nums))
'''Monotomic number'''
nums = list(map(int,input().split()))
increasing = True
decreasing = True
for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        increasing = False
    if nums[i]<nums[i+1]:
        decreasing = False
if increasing or decreasing:
    print("Monotomic Array")
else:
    print("not monotomic Array")
'''
1)Linear search(sequential)
2)Binary search(Interval)'''

# def Linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i]== target:
#             return i
#     return -1
# arr = list(map(int,input().split()))
# target = int(input())
# print(Linear_search(arr,target))
# print(Linear_search([1,2,3,4,5],1))

def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid-1
        else:
            low = mid+1
# print(binary_search([2,5,7,8,10,20,36,45],7))
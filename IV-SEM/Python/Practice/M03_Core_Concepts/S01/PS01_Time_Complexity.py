'''Time Complexity:
Definition : Time Complexity can be measured based pon on the input


O(1) ---> Constant Time
O(n) ---> Single Loop
O()'''
'''Linear Search'''
# print("Time Complexity:")
# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
# print(linear_search([10,20,30,50,46],10))
# print(linear_search([10,20,30,50,46],46))
# print(linear_search([10,20,30,50,46],30))

'''Binary Search'''
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



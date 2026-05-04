'''Merge sort'''

# def Merge(left,right):
#     i = j = 0
#     res = []
#     while i < len(left) and j< len(right):
#         if left[i] < right[j]:
#             res.append(left[i])
#             i+=1
#         else:
#             res.append(right[j])
#             j+=1
#     res.extend(left[i:])
#     res.extend(right[j:])
#     return res
#     # return res + left[i:] + right[j:]
# print(Merge([7,14],[3,12]))

# def Merge_sort(arr):
#     if len(arr)<= 1:
#         return arr
#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]
#     left_sorted = Merge_sort(left)
#     right_sorted = Merge_sort(right)

#     return Merge(left_sorted,right_sorted)
# print(Merge_sort([7,14,3,12]))

'''Quick sort'''
def partition(arr,low,high):
    i = low+1
    j = high
    pivot = arr[low]
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    arr[low],arr[j] = arr[j],arr[low]
    return j
print(partition([54,26,93,17,77,31,44,55,20],0,8))

def Quick_sort(arr,low,high):
    if low <= high:
        p = partition(arr,low,high)
        Quick_sort(arr,low,p-1)
        Quick_sort(arr,p+1,high)
    return arr
print(Quick_sort([54,26,93,17,77,31,44,55,20],0,8))
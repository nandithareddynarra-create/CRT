# def Reverse_list(li):
#     '''solution 1
#     res = []
#     s = -1*(len(li)+ 1)
#     for i in range(-1,s,-1):
#         res.append(li[i])
#     return res
#     '''

#     '''solution- 2
#     res = []
#     stop = -1*(len(li)+1)
#     res = [li[i] for i in range(-1,stop,-1)]
#     return res
#     '''

#     '''Solution - 3
#     res = []
#     n = len(li)
#     for i in range(0,n//2):
#       li[i],li[n-1-i] = li[n-1-i],li[i]
#     return li
#     '''

#     '''Solution - 4
#     res = []
#     for ele in li:
#         res.insert(0,ele)
#     return res
#     '''

# print(Reverse_list([1,2,3,4]))

# def is_sorted(nums):
#     for i in range(len(nums)-1):
#         if nums[i]> nums[i+1]:
#             return False
#     return True
# print(is_sorted([12,33,45,56,78]))
# print(is_sorted([45,20,36,78,1]))

'''
input : [1,2,3,2,4,3,1,5]
output : [1:2,2:2,3:2,4:1,5:1]'''
# li = [1,2,3,4,3,1,4]
# d = {}
'''Solution - 1
# for i in li:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)
# print(d.get(1))
# print(d.get(10,0))
# '''

'''Solution - 2
for i in li:
    d[i] = d.get(i,0)+1
print(d)
'''

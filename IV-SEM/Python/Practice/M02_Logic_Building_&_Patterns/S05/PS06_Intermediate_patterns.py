# li = list(map(int,input().split()))
# l =[]
# for i in li:
#     i = i**2
#     l.append(i)
# print(l)
#Comprehension 
# ans = [i**2 for i in li]
# print(ans)

'''Even numbers of list'''
# li = list(map(int,input().split()))
# l = []
# for i in li:
#     if i%2==0:
#         l.append(i)
# print(l)
# Comprehension
# ans = [i for i in li if i%2==0]
# print(ans)
'''Joining multiple strings into single string'''
# li = ['rri','vgh','tyu']
# res =""
# for i in li:
#     res = res + i+" "
# print(res)
# print(" ".join(li))
# print(*li)    Takes space as seperating element

#Intermediate patterns
'''
    *
   * *
  * * *
 * * * * 
 '''
'''
li = [1,2,3,4,5]
output:[1,4,9,16,25]'''
'''Pyramid pattern'''
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)

'''Inverted pattern'''
n= int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
    print(" "*(i-1)+"* "*((n+1)-i))
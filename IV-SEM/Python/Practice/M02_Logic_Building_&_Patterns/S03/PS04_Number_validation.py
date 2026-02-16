'''Print Armstrong number or not'''
# n = int(input())
# r = len(str(n))
# temp = n
# total = 0
# for i in range(1,n+1):
#     digit = n%10
#     total += digit**r
#     n = n//10
# if (total == temp):
#     print("Armstrong")
# else:
#     print("Not Armstrong")
'''Ma'am solution'''
# n = int(input())
# r = len(str(n))
# res = 0
# for i in str(n):
#     res += int(i)**r
# if n == res:
#     print("Yes")
# else:
#     print("No")

'''perfect Number'''
# n = int(input())
# r = 0
# for i in range(1,n//2+1):
#     if (n%i==0):
#         r += i
# if (r == n):
#     print("perfect")
# else:
#     print("Not perfect")

'''Strong Number'''
# n = int(input())
# r = 0
# o = n
# while n>0:
#     digit = n%10
#     fact = 1
#     for i in range(1,digit+1):
#         fact *= i
#     r += fact
#     n = n//10
# if r == o:
#     print("Strong")
# else:
#     print("no")
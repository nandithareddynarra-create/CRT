'''1)Write a python code to count the digits of number?'''
# n = int(input())
# count = 0
# while n>0:
#     count += 1
#     n = n//10
#     print(count)
'''Sum of the digits of a number?'''
# n = int(input())
# sum = 0
# while n>0:
#     sum+=n%10
#     n = n//10
# print(sum)

'''Product of a number'''
# n = int(input())
# prod = 1
# while n > 0:
#     prod *= n%10
#     n = n//10
# print(prod) 
'''Reverse of a number'''
# n = int(input())
# r = 0
# while n>0:
#     r = r*10 + n%10
#     n = n//10
# print(r)
'''Count the even and odd digits'''
# n = int(input())
# even = 0
# odd = 0
# while n>0:
#     d = n%10
#     if d%2 == 0:
#         even += 1
#     else:
#         odd +=1
#     n = n//10
# print(even,odd)
'''print the largest digit of a number?'''
n = int(input())
lar = 0
while n > 0:
    d = n%10
    if d>lar:
        lar = d
    n = n//10
print(lar)
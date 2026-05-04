'''Fibonacci series'''
# def fibo(n):
#     if n == 1:
#         return 0 
#     if n == 2:
#         return 1
#     return fibo(n-1)+fibo(n-2)
# n = int(input())
# print(fibo(n))

'''Gcd'''
# import math
# print(math.gcd(3,4))
# a = int(input())
# b = int(input())
# while b!= 0:
#     a,b = b,a%b
# print(a)
'''Recursive GCD'''
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
print(gcd(3,4))
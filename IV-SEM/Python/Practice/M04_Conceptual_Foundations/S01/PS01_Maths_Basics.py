'''
# import math
# print(math.factorial(5))    
# print(math.floor(12.45))    ----> nearest smallest integer == 12
# print(math.ceil(12.45))     -----> nearest largest integer == 13
# print(math.pi)
# print(math.gcd(2,4))
'''
# GCD solution -1
# a = int(input())
# b = int(input())
# min_num = min(a,b)
# for i in range(1,min_num):
#     if a% i == 0 and b%i == 0:
#         gcd = i
        
# print(gcd)

# GCD Solution - 2
# a = int(input())
# b = int(input())
# while b!= 0:
#     a,b = b,a%b
# print(a)

'''LCM with GCD
==>LCM = a*b = GCD*LCM'''
# import math
# a = int(input())
# b = int(input())
# GCD = math.gcd(a,b)
# LCM = (a*b)//GCD
# print(LCM)

'''perfect Number'''
def check_perfect_number(n):
    r = 0
    for i in range(1,n//2+1):
        if (n%i==0):
            r += i
    if (r == n):
        return("perfect")
    else:
        return("Not perfect")
print(check_perfect_number(6))
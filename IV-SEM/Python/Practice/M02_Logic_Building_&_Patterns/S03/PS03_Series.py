'''Display Arithmetic Progression values upto 10'''
# a = int(input())
# d =int(input())
# for i in range(1,10):
#     print(a+(i-1)*d,end=" ")


'''Display Fibonacci series upto 5 recursive function'''
# n = int(input())
# a = 0
# b = 1
# for i in range(1,n+1):
#     print(a,end=" ")
#     a,b = b,a+b


'''Fibonacci series upto 5 using list'''
# n = int(input())
# List = [0,1]
# for i in range(2,n):
#     List.append(List[i-2]+List[i-1])
# print(*List)


'''Power of a number'''
n = int(input())
for i in range(1,n+1):
    print(n**i , end=" ")
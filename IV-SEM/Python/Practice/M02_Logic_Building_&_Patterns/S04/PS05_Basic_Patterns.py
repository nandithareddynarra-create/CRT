'''Basic * pattern
n = 4
ouput:
* * * *
* * * *
* * * *
* * * *
Solution'''
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print(" ")

'''Basic triangle pattern
output
*
* *
* * *
* * * *
* * * * *
Solution'''
# n = int(input())
# for i in range(n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

'''Inverted triangle
output:
* * * *
* * *
* *
*
Solution'''
# n = int(input())
# for i in range(n+1):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

'''printing number patterns
Output
1
2 3
4 5 6
7 8 9 10
Solution'''
# n = int(input())
# k=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(k,end=" ")
#         k+=1
#     print()

'''Printing Alphabets
n =4
A
A B
A B C
A B C D
Solution'''
# n = int(input())
# for i in range(n+1):
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()
'''Alphabet sequence
n = 4
A
B C
D E F
G H I J'''
# n = int(input())
# k = 65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()

'''Print Square
* * * *
*     *
*     *
* * * *
Solution'''
n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
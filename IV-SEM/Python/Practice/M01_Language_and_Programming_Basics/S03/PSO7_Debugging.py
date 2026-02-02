'''bug --> Errors
Degugging  --> Finding and fixing errors


Types of errors:
1)Syntax Errors : Missing of colon , missing of indentation
2)Runtime Errors : Division by Zero
3)Logical Errors : Missing of Logics


pdb Commands :
1)n :- To execute the output in a next line
2)p variable :- To get the value of a variable
3)l :- List nearby code
4)c :- Continue the execution
5)s :- To start the function
6)r :- To return from the function
7)h :- Help
8)q :- Quit the execution

'''
# try:
#     a= int(input())
#     print(10/a)
# except ZeroDivisionError:
#     print("Can not divisible by Zero. ")
# except ValueError:
#     print("Invalid input") 

import pdb
def add(a,b):
    pdb.set_trace() #set the breakpoint
    return a+b
a = int(input())
b = int(input())
print(add(a,b))
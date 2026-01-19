#Bitwise operators
x = 7
y = 13
print(x&y)
print(x/y)
print(x^y)
print(~x) #--------->{Unary operator(~,logical not)}    {trinary(if else)}   {remaining are binary}
print(x<<3)
print(y>>1)


#Membership operators ==> in and not in
print(100 in[10,20,30,40])      #False
print("on" in "python")         #True
print("on" not in "pythON")     #True
print("P" not in "Python")      #False



#Identity operators ==> is and is not
x =10    #integer is immutable
y = 20
z = 10
print(x is y) #False
print(x is z) #True

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)    #False beacause it is mutable

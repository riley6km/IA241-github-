'''
lec 5 if statement
'''

import this

print(  1+
        2)

print([1,2,3,

        4,5,6])
        # print (1+2)
        




a = [1,2,3]
b = [1,2,3]


print(id([1,2,3]))
print(id(a))
print(id(b))

print(a is b)

print(a == b)

x = None

print(id(x))
print(id(None))

print(x == None)
print(x is None)

y= []

print(y == None)
print(y is None)

print(True and False)
print(True or False)

print(not True)
print(not False)

print(not None)
print(not "0")

if 2>1 :
        print('2>1')
        if 3>1:
                print('3>1')
        if 2<=1:
                print('2<=1')
                
print('not in the if block')

if 2>=1:
        print('2>=1')
else:
        print('2<1')
        
if 2<1:
        print('2<1')
        
elif 2<=2:
        print('2<=2')

else:
        print('2>1')
'''num1=input("Enter the first number \n")
num2=input("Enter the second number \n")
try:
    print("the sum of twoi numbers is", int(num1) + int(num2))
except Exception as e:
    print(e)
print("This line is very important")'''


#Will never come in except block
'''a=[1,2,3]
try:
    print("second element",a[1])
except Exception as e:
    print("Fourth element")
    print(" An Error occured")  '''


'''a=[1,2,3]
try:
    print("Second element is",a[1])
    print("Fourth element is",a[3])
except Exception as e:
    print(e)'''


'''a=[1,2,3]
try:
    print("Second element",a[1])
    print("Fourth element is",a[3])
except IndexError:
    print("An Error occured")'''

'''try:
    a=3
    if a<4:
        b=a/(a-3)
        print(b)
except Exception as e:
    print(e)'''

'''try:
    a=eval(input("Enter  anumber between 3 and 4,inclusive"))
    if a<4:
        b=a/(a-3)
        print("Value of b:",b)
    print("Value of b",b)
except (ZeroDivisionError):
    print("ZeroDivsionError occured")
except (NameError):
    print("NameError occured")'''


'''def func(a,b):
    try:
        c=(a+b)/(a-b)
    except (ZeroDivisionError):
        print("Result is 0")
    else:
        print(c)
func(3,2)
func(2,2)'''


#Raise statement
#force a specific exception to occur.

# try:
#     raise NameError("Hi there")  #raise
# except NameError:
#     print("An exception")
#     raise




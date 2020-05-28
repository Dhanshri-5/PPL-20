#exception handling using try except in python

# ZeroDivisionError Exception

p = int(input("Enter dividend to be divided by zero): "))
try:
    ans = p/0

# Catches the exception executesfollowing code in case of an exception.
except ZeroDivisionError:           
    print("ZeroDivisonError: Handled !\n")

# Gets executed if no exceptions occured and program block ran successfully.
else:
    print("No Exception Occured\n.")
    print("Result = {}\n".format(ans))
 
# KeyboardInterrupt Exception

try:
    inp = input("Press Ctrl+C or Interrupt the Kernel: ")  
except KeyboardInterrupt:
    print ('KeyboardInterrupt exception : Handled!\n')
else:
    print ('No exception occurred')

#TypeError

a = "Dhanshri"
try:
    print(5 + a) #concatenating string and int
except TypeError as t:
    print("Type Error : (Convert int to string first) ,Handled!\n")
else:
    print('No exception occured.\n')

#name error
try:
    a = b
except NameError:
    print("The given variable does not exist!\n")   
else:
    print('No name error occured\n')

# Key Error

try:
    dic = {'a':"apple" , 'b':"bat" , 'c': "cat"}
    print(dic,"\n")
    x = input('Enter the key to display.    \n')
    print(dic[x],"\n")

except LookupError:
    print("LookupError: (because the key is not present in the dictionary) , Handled!\n")
else:
    print("No exception occured to access the value of the key.\n")

# Assertion Error
try:  
    a = int(input("Enter your age.\n"))
    b = input("Enter your name\n")
    assert a == b
except AssertionError:  
    print ("AssertionError: Eqauting a integer value with String ,Handled!\n")
else:
    print ("Success, no error!\n")

# Index error
list = [num**2 for num in range(1,6)]
print("List of squres upto 5 : " , list)
try:
    n = int(input("Enter index to check.\n"))
    print("That element of the list is:{}".format(list[10]))
except IndexError:
    print("Index Error : (Array index out of bounds),Exception Handled!\n")     
else:
    print ("No exception occured!\n")

#Import module exception
print('Importing AAAA modules\n')
try:
    import AAAA
except ImportError:
    print("Import Exception:(Module does not exist), Handled !\n")
    
#file handling 

file = input("Enter filename: \n")
try:  
    fl = open(file, 'r')
    content = fl.read()
    open = True
except IOError:						 							
    print("\nFileNotFoundError: File is not found.\n")
    open = False

else:								 									
    print(", '{}'\n".format(file))
    print("Succesfully read the file . File content:\n {}\n".format(content))
#finally will be excuted in both the cases.
finally:
    print("THE END\n")
    if(open):
        fl.close()
   
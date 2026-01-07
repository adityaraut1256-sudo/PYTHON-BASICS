# Let's store a string (string = any kind of text) in a variable. In the following example, 'dummy' is a variable which holds some text data (string) 
# Use print() to print something (it's not necessary in google colab, but tag along with us here for now)

dummy = "Hello world!"
print(dummy)# Let's explore other data type quickly before focusing our attention to strings

num = 7
another_num = 4.0
print(type(num))
print(type(another_num))

num1 = 9
num2 = 11
print(num1, num2)
print(type(num1), type(num2))

# Let's accept input from user
# input is a special function that allows user to type (and pass) user's own input

name = input('raju')   # once this is run, type anything in the box
print(name)
print(type(name))

# You can carry out basic + - * /

#part2

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num2 / num1)   # division sometimes may result in float
# You can carry out basic + - * /

# Other arithmatic operators - // % **


print(num2 // num1)  # this is called floor division i.e. the output is quotient without reminder i.e. discarding the numbers after decimal point
print(num2 % num1)   # this is called modulus i.e. the reminder after division
print(3 ** 5)        # exponent (^) ---> 3^2

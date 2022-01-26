# Question 1
inp_str = str(input('Enter the string:'))
# inp_str is a variable used for the user to enter a string

print('length of string is:', len(inp_str))
print('Reverse of string is:', inp_str[::-1])

slice_str = inp_str[9:26]
# slice_str is a variable used to slice the inp_str(string entered by the user)

print(slice_str)
new_str = inp_str.replace('a case sensitive', 'object oriented')
# new_str is a variable used for replacing replacing existing part of the string with a new part

print('index of substring a', inp_str.index('a'))
print(inp_str.replace(' ', ''))




# Question 2

name = str(input('Enter your name:'))
# name variable is used for the user to enter his name

sid = int(input('Enter you sid:'))
# sid variable is used for the user to enter his SID

dept = str(input('Enter your department:'))
# dept variable is used for the user to enter his department

cgpa = float(input('Enter your CGPA:'))
# cgpa variable is used for the user to enter his CGPA

print('Hey,', name, 'Here!\n' 
      'My SID is ', sid, '\n'
      'I am from', dept, 'and my CGPA is:', cgpa)



# Question 3

a = 56
# a is a variable which is assigned a value of 56

b = 10
# b is a variable which is assigned a value of 10

print('a&b:', a & b)
print('a|b:', a | b)
print('a^b:', a ^ b)
print('Left shift "a" with 2 bits (a<<2): ', a << 2, ',and Left shift "b" with 4 bits (b<<4): ', b << 4)
print('Right shift "a" with 2 bits (a>>2):', a >> 2, ',and Right shift "b" with 4 bits (b>>4):', b >> 4)



# Question 4

list = []
for i in range(3):
    num = float(input("Enter number : "))
    list.append(num)

list.sort(reverse=True)
print("The greatest value is:", list[0])



# Question 5

inp_string = str(input('Enter a string:'))
#inp_string is a variable used for the user to enter a string

if 'name' in inp_string:
    print('Yes')
else:
    print('No')



# Question 6

a1 = float(input('Enter side 1 of a triangle:'))
# a1 is the variable used for the user to enter the first side of a triangle

a2 = float(input('Enter side 2 of a triangle:'))
# a2 is the variable used for the user to enter the second side of a triangle

a3 = float(input('Enter side 3 of a triangle:'))
# a3 is the variable used for the user to enter the third side of a triangle

if a1 > (a2 + a3):
    print('No')
elif a3 > (a2 + a1):
    print('No')
elif a2 > (a1 + a3):
    print('No')
else:
    print('Yes')




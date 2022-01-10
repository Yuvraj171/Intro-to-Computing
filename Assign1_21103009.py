# Question 1

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
num3 = int(input('Enter third number:'))
avg = (num1 + num2 + num3)/(3)
print(avg)

# Question 2

GrossInc = int(input('Enter your Gross Income :'))
Std_Deducts = 10000
Dep_Deducts = 3000
Dependts = int(input('Enter the number of Dependents :'))
Taxable_Inc = GrossInc - Std_Deducts - (Dep_Deducts * Dependts)
Tax = Taxable_Inc * 0.2
print(Tax)

# Question 3
sid = int(input('Enter your SID:'))
Name = str(input('Enter your name:'))
Gender = str(input('Enter your Gender:'))
CourseName = str(input('Enter your Course:'))
CGPA = float(input('Enter your CGPA:'))
Student = [sid, Name, Gender, CourseName, CGPA]
print(Student)

# Question 4
List = []
for i in range(5):
    Marks = float(input('Enter your Marks:'))
    List.append(Marks)

List.sort()
print(List)


# Question 5(a)

colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour.pop(3)
print(colour)

# Question 5(b)

colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour[3] = 'Purple'
colour.pop(4)
print(colour)

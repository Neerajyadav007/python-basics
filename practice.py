## Question 1:- Take input of name + branch + roll no -> print a fromatted ID card
# name = input("Enter Your name : ")
# branch = input("Enter Your branch : ")
# roll_no = int(input("Enter your roll number: "))

# print(f"Name = {name}")
# print(f"Branch = {branch}")
# print(f"Roll No. = {roll_no}")

##Question 2:- Check if user age >= 18 -> print Eligible for vote

# age = int(input("Enter your age : "))

# if age>=18:
#     print("You Eligible for vote ")
# else:
#     print("You are not Eligible for vote")

## Question 3:- Given 2 numbers -> print maximum

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))


# if num1>num2 :
#     print(f"{num1} is maximum")
# else:
#     print(f"{num2} is the maximum")

## Question 4:- create a list of 5 fruits -> print each one using loop

# fruits = ("Apple","Banana","Orange", "Mango", "Grapes")
                               

# for item in fruits:
#     print(item)
    
## Question 5:- Write a function are_circle(r) -> calculate and return area

pi = 3.14
def AreaOfCircle(r):
    area = pi*r*r
    return area

r = int(input("Enter the redius of circle : "))

print(AreaOfCircle(12))

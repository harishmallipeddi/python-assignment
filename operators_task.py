# # 1. Arithmetic Operators
# # Accept two numbers and display the results of +, -, , /, //, %, and *.
# # Assignment Operators
# a=5
# b=8
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# # Assignment Operators
# # 2. Initialize a variable with 50 and perform +=, -=, =, /=, //=, %=, and *= operations, displaying the value after each operation.
# # Initialize variable
# num = 50
# print("Initial value:", num)
# num += 10
# print("After += 10:", num)
# num -= 5
# print("After -= 5:", num)
# num *= 2
# print("After *= 2:", num)
# num /= 4
# print("After /= 4:", num)
# num //= 3
# print("After //= 3:", num)
# num %= 7
# print("After %= 7:", num)

# 3. Comparison Operators
# Accept two numbers and display the results of ==, !=, >, <, >=, and <=.
# a=50
# b=60
# print("a == b:", a == b)
# print("a != b:", a != b)
# print("a > b:", a > b)
# print("a < b:", a < b)
# print("a >= b:", a >= b)
# print("a <= b:", a <= b)

# Logical Operators
# Accept a number and display the results of the following expressions:
# num > 10 and num < 100
# num % 2 == 0 or num % 5 == 0
# not(num > 50)
# num=50
# print("num > 10 and num < 100:", num > 10 and num < 100)
# print("num % 2 == 0 or num % 5 == 0:", num % 2 == 0 or num % 5 == 0)
# print("not(num > 50):", not(num > 50))

# Identity Operators
# Create two lists with the same elements and another variable that references the first list. Compare them using ==, is, and is not.

# list1=[1,2,3,4,5]
# list2=[1,2,3,4,5]
# list3=list1
# # Comparisons
# print("list1 == list2:", list1 == list2)   
# print("list1 is list2:", list1 is list2)  
# print("list1 is list3:", list1 is list3)  
# print("list1 is not list2:", list1 is not list2)  

# Membership Operators
# take a character and check whether it is present in the string "PYTHON" using in and not in.
# cha=input("enter a string:")
# text="python"
# print(cha in text)
# print(cha not in text)

# Student Marks Calculator
# Accept marks of five subjects and calculate the total, average, and percentage using arithmetic operators.
# Accept marks of five subjects
# sub1 = int(input("Enter marks of Subject 1: "))
# sub2 = int(input("Enter marks of Subject 2: "))
# sub3 = int(input("Enter marks of Subject 3: "))
# sub4 = int(input("Enter marks of Subject 4: "))
# sub5 = int(input("Enter marks of Subject 5: "))

# total = sub1 + sub2 + sub3 + sub4 + sub5
# average = total / 5
# percentage = (total / 500) * 100   
# print("Total Marks:", total)
# print("Average Marks:", average)
# print("Percentage:", percentage, "%")




# Shopping Bill Calculator
# Accept the price and quantity of three products, calculate the total bill, and then use comparison operators to compare the totals of any two products.
# Shopping Bill Calculator
# price1 = float(input("Enter price of product 1: "))
# qty1 = int(input("Enter quantity of product 1: "))

# price2 = float(input("Enter price of product 2: "))
# qty2 = int(input("Enter quantity of product 2: "))

# price3 = float(input("Enter price of product 3: "))
# qty3 = int(input("Enter quantity of product 3: "))


# total1 = price1 * qty1
# total2 = price2 * qty2
# total3 = price3 * qty3


# total_bill = total1 + total2 + total3


# print("\n--- Shopping Bill Summary ---")
# print(f"Product 1 Total: ₹{total1}")
# print(f"Product 2 Total: ₹{total2}")
# print(f"Product 3 Total: ₹{total3}")
# print(f"Overall Bill: ₹{total_bill}")


# print("\n--- Comparison Results ---")
# print("Product 1 > Product 2:", total1 > total2)
# print("Product 2 < Product 3:", total2 < total3)
# print("Product 1 == Product 3:", total1 == total3)




# Temperature Converter
# Accept temperature in Celsius, convert it to Fahrenheit, and compare whether the Fahrenheit value is greater than 100 using comparison operators.
# Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"\nTemperature in Fahrenheit: {fahrenheit}")
print("Is Fahrenheit greater than 100?", fahrenheit > 100)

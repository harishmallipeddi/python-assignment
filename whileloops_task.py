# Task :
# Write a Python program to print each digit of a number separately.
# num = input("Enter a number: ")

# for digit in num:
#     print(digit)




# Write a Python program to find the sum of digits of a given number.
# num=int(input("enter a number:"))
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
# print("sum of all digits",sum)
    




# Write a Python program to find the smallest digit in a number.
# num=int(input("enter a number"))
# smallest=9
# while num>0:
#     digit=num%10
#     if digit<smallest:
#         smallest=digit
#     num//=10
# print("smallest digit is :",smallest)



# # Write a program to check whether a number is an Armstrong number using a while loop.
# num=int(input("enter a number:"))
# original=num
# count=0
# temp=num
# while temp>0:
#     count+=1
#     temp//10
# sum=0
# temp=num



# Write a Python program to reverse a given number.
#reverse a number not using slice
n=1234
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n//=10
print(rev)
# TASK :
# Write a Python program to print all even numbers from 1 to 20 using a while loop.
# i = 0
# while i <= 20:
#     if i%2==0:
#         print("even",i)
#     i+=1


# Write a Python program to print all odd numbers from 1 to 20 using a while loop.

# i = 0
# while i <= 20:
#     if i%2!=0:
#         print("odd",i)
#     i+=1
    
# Write a Python program to print the first 10 natural numbers using a while loop
# i = 1
# while i<=10:
#     print(i)           
#     i+=1

# Write a Python program to print the first 10 multiples of 5 using a while loop.
# i=1
# while i<=10:
#     print("5 x",i,"=",5*i)
#     i+=1



# Write a Python program to find the sum of numbers from 1 to N using a while loop. (Take N as input.)
# n=int(input("enter a number:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)



# Write a Python program to print the multiplication table of a given number using a while loop.
# n=int(input("enter a number:"))
# i=1
# while i<=10:
#     print(n ,"x",i,"=",n*i)
#     i+=1

# Write a Python program using a while loop to display the battery percentage after each charge until it reaches 100%.
# battery=int(input("enter your battery:"))
# while battery<=100:
#     print("battery",battery,"%")
#     battery+=1
# Write a Python program using a while loop that keeps asking the user to enter the PIN until the correct PIN is entered. 
# Once the correct PIN is entered, display "Access Granted".
correct_pin=123
attemps=1
while attemps<=3:
    pin=int(input("enter your pin:"))
    if pin==correct_pin:
        print("access granted")
        break 
    else:
        print("wrong pin")
        attemps+=1
if attemps>3:
    print("next 1hour u can retry")

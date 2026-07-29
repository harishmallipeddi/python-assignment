# 1. Print each digit of a number separately
num = int(input("Enter a number: "))
temp = num
while temp > 0:
    digit = temp % 10
    print(digit)
    temp //= 10

# 2. Find the sum of digits of a given number
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10
print("Sum of digits:", sum)

# 3. Find the smallest digit in a number
num = int(input("Enter a number: "))
temp = num
smallest = 9
while temp > 0:
    digit = temp % 10
    if digit < smallest:
        smallest = digit
    temp //= 10
print("Smallest digit:", smallest)

# 4. Check whether a number is an Armstrong number
num = int(input("Enter a number: "))
temp = num
order = len(str(num))
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# 5. Reverse a given number
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print("Reversed number:", rev)
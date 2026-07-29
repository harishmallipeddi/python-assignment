# 1. Find the average of numbers from 1 to N
N = int(input("Enter a number N: "))
i = 1
sum = 0
while i <= N:
    sum += i
    i += 1
average = sum / N
print("Average of numbers from 1 to", N, "is", average)

# 2. Find the sum of squares from 1 to N
N = int(input("Enter a number N: "))
i = 1
sum_squares = 0
while i <= N:
    sum_squares += i * i
    i += 1
print("Sum of squares from 1 to", N, "is", sum_squares)

# 3. Find the sum of cubes from 1 to N
N = int(input("Enter a number N: "))
i = 1
sum_cubes = 0
while i <= N:
    sum_cubes += i * i * i
    i += 1
print("Sum of cubes from 1 to", N, "is", sum_cubes)

# 4. Find the sum of numbers divisible by 3
N = int(input("Enter a number N: "))
i = 1
sum_div3 = 0
while i <= N:
    if i % 3 == 0:
        sum_div3 += i
    i += 1
print("Sum of numbers divisible by 3 up to", N, "is", sum_div3)

# 5. Find the sum of numbers divisible by both 2 and 5
N = int(input("Enter a number N: "))
i = 1
sum_div2and5 = 0
while i <= N:
    if i % 2 == 0 and i % 5 == 0:
        sum_div2and5 += i
    i += 1
print("Sum of numbers divisible by both 2 and 5 up to", N, "is", sum_div2and5)




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
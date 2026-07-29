# ==========================================
# TASK 1: Check Armstrong Number
# ==========================================

num = int(input("Enter a number: "))

original = num
temp = num
count = 0

while temp > 0:
    count += 1
    temp = temp // 10

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# ==========================================
# TASK 2: Separate Even and Odd Elements
# ==========================================

numbers = [10, 15, 22, 37, 40, 51, 68]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even Numbers:", even)
print("Odd Numbers:", odd)


# ==========================================
# TASK 3: Merge Two Lists
# ==========================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2

print("Merged List:", merged)


# ==========================================
# TASK 4: Print Missing Number in a Sequence
# ==========================================

numbers = [1, 2, 3, 5, 6]

for i in range(numbers[0], numbers[-1] + 1):
    if i not in numbers:
        print("Missing Number:", i)


# ==========================================
# TASK 5: Print Duplicate Elements from a List
# ==========================================

numbers = [10, 20, 30, 20, 40, 10, 50]

duplicates = []

for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate Elements:", duplicates)


# ==========================================
# TASK 6: Print Duplicate Characters from a String
# ==========================================

text = "programming"

duplicates = []

for ch in text:
    if text.count(ch) > 1 and ch not in duplicates:
        duplicates.append(ch)

print("Duplicate Characters:", duplicates)


# ==========================================
# TASK 7: Check Last Digit (Even or Odd)
# ==========================================

num = int(input("Enter a number: "))

last_digit = num % 10

if last_digit % 2 == 0:
    print("Even Last Digit")
else:
    print("Odd Last Digit")


# ==========================================
# TASK 8: Check Divisibility of Last Digit by 3
# ==========================================

num = int(input("Enter a number: "))

last_digit = num % 10

if last_digit % 3 == 0:
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3")


# ==========================================
# TASK 9: Check Character Type
# ==========================================

ch = input("Enter a character: ")

if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print("Alphabet")
else:
    print("Not an Alphabet")


# ==========================================
# TASK 10: Check Uppercase or Lowercase
# ==========================================

ch = input("Enter an alphabet: ")

if 'A' <= ch <= 'Z':
    print("Uppercase")
else:
    print("Lowercase")


# ==========================================
# TASK 11: Check Vowel or Consonant
# ==========================================

ch = input("Enter an alphabet: ")

if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")


# ==========================================
# TASK 12: Print Each Digit of a Number
# ==========================================

num = input("Enter a number: ")

for digit in num:
    print(digit)


# ==========================================
# TASK 13: Sum of Digits
# ==========================================

num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of Digits:", sum)
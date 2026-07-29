# 1. Check the number is Armstrong number or not
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

# 2. Separate even and odd elements from given list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = []
odd = []
i = 0
while i < len(lst):
    if lst[i] % 2 == 0:
        even.append(lst[i])
    else:
        odd.append(lst[i])
    i += 1
print("Even elements:", even)
print("Odd elements:", odd)

# 3. Merge 2 lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("Merged list:", merged)

# 4. Print missing number in a sequence (list)
lst = [1, 2, 3, 5, 6, 7]
i = 1
while i <= max(lst):
    if i not in lst:
        print("Missing number:", i)
    i += 1

# 5. Print duplicates from the list or string
lst = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = []
i = 0
while i < len(lst):
    if lst.count(lst[i]) > 1 and lst[i] not in duplicates:
        duplicates.append(lst[i])
    i += 1
print("Duplicates in list:", duplicates)

s = "programming"
duplicates_str = []
i = 0
while i < len(s):
    if s.count(s[i]) > 1 and s[i] not in duplicates_str:
        duplicates_str.append(s[i])
    i += 1
print("Duplicates in string:", duplicates_str)
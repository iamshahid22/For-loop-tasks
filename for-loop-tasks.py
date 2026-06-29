# For Loop Applications

# 1. Calculate the sum of squares of numbers
print("1. Sum of Squares")

numbers = [1, 2, 3, 4, 5]
sum_of_squares = 0

for num in numbers:
    sum_of_squares += num ** 2

print("Numbers:", numbers)
print("Sum of Squares:", sum_of_squares)

print("\n" + "=" * 40)

# 2. Print each character of a string on a new line
print("2. Print Characters of a String")

def print_characters(text):
    for ch in text:
        print(ch)

print_characters("Python")

print("\n" + "=" * 40)

# 3. Find the maximum number in a list
print("3. Find Maximum Number")

numbers = [12, 45, 7, 89, 23, 56]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Numbers:", numbers)
print("Maximum Number:", maximum)

print("\n" + "=" * 40)

# 4. Generate the first 10 Fibonacci numbers
print("4. First 10 Fibonacci Numbers")

a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

print()

print("\n" + "=" * 40)

# 5. Iterate over a dictionary and print key-value pairs
print("5. Dictionary Key-Value Pairs")

student = {
    "Name": "Shahid",
    "Age": 21,
    "Course": "B.Tech CSE",
    "College": "AITS"
}

for key, value in student.items():
    print(key, ":", value)
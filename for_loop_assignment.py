# For Loop Applications Assignment - Student Solution

# Task 1: Sum of squares of numbers in a list
def sum_of_squares(numbers):
    """Calculate sum of squares using for loop."""
    total = 0
    for num in numbers:
        total += num * num
    return total

# Test
print("=== Task 1: Sum of Squares ===")
nums = [1, 2, 3, 4, 5]
print(f"Numbers: {nums}")
print("Sum of squares:", sum_of_squares(nums))


# Task 2: Print each character of string on new line
def print_characters(s):
    """Print each character of string on new line using for loop."""
    print(f"Characters of '{s}':")
    for char in s:
        print(char)

# Test
print("\n=== Task 2: Print Characters ===")
print_characters("Python")


# Task 3: Find maximum number in a list
def find_maximum(numbers):
    """Find maximum in list using for loop."""
    if not numbers:
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test
print("\n=== Task 3: Find Maximum ===")
nums2 = [45, 12, 89, 33, 67, 91, 25]
print(f"List: {nums2}")
print("Maximum number:", find_maximum(nums2))


# Task 4: First 10 Fibonacci numbers
def print_fibonacci(n=10):
    """Generate and print first n Fibonacci numbers using for loop."""
    print(f"First {n} Fibonacci numbers:")
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # New line

# Test
print("\n=== Task 4: Fibonacci Series ===")
print_fibonacci(10)


# Task 5: Iterate over dictionary and print key-value pairs
def print_dictionary(d):
    """Print each key-value pair using for loop."""
    print("Dictionary contents:")
    for key, value in d.items():
        print(f"Key: {key}  -->  Value: {value}")

# Test
print("\n=== Task 5: Dictionary Iteration ===")
student = {
    "name": "Rahul Sharma",
    "age": 20,
    "course": "Computer Science",
    "grade": "A",
    "city": "Delhi"
}
print_dictionary(student)


# ==================== Additional Practice / Combined Demo ====================

def combined_demo():
    """Run all tasks together for easy testing."""
    print("\n" + "="*50)
    print("COMPLETE FOR LOOP ASSIGNMENT DEMO")
    print("="*50)
    
    # Task 1
    print("\n1. Sum of Squares:")
    print(sum_of_squares([2, 4, 6, 8]))
    
    # Task 2
    print("\n2. Characters:")
    print_characters("Hello")
    
    # Task 3
    print("\n3. Maximum:")
    print(find_maximum([10, 5, 99, 42, 78]))
    
    # Task 4
    print("\n4. Fibonacci:")
    print_fibonacci()
    
    # Task 5
    print("\n5. Dictionary:")
    print_dictionary({"apple": 3, "banana": 6, "cherry": 9})

# Run the complete demo
if __name__ == "__main__":
    combined_demo()

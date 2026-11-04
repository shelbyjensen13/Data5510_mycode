'''3. Write a function that takes an array of integers 
as input and returns the maximum difference between any 
two numbers in the array.

Analyze the time complexity of your solution using Big O 
notation, especially what is the Big O notation of the code 
you wrote, and include it in the comments of your program.
'''

def find_max_dif(numbers):
    if len(numbers) < 2:
        return None

    smallest = numbers[0]
    largest = numbers[0]

 # time complexity: O(n) . I loop through the array once, each comparison takes O(1) time.

    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    return largest - smallest

# space complexity: O(1), I only use two variables to store the smallest and largest numbers, regardless of array size.

shel_num = [3, 5, 6, 13, 23]

result = find_max_dif(shel_num)

if result is None:
    print("The array must contain at least two numbers.")
else: 
    print("Maximum difference:", result)


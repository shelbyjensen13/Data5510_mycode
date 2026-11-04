'''1. Given an array of integers, write a function to calculate the sum of all elements in the array.

Analyze the time complexity of your solution using Big O notation, 
especially what is the Big O notation of the code you wrote, 
and include it in the comments of your program.

 '''
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

shel_numbers = [3, 5, 6, 13, 23]
print("Sum:", calculate_sum(shel_numbers))

# Big O Time Complexity: O(n)
# The loop visits every element in the list once. If there are n elements, the
# function performs n additions. Therefore, the time complexity is O(n).
# Space Complexity: O(n)
# The function only uses one additional variable, total, regardless of how many numbers are in the list. 
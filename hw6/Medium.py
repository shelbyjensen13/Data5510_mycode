'''2. Given an array of integers, write a function that finds the second 
largest number in the array.

Analyze the time complexity of your solution using Big O notation, 
especially what is the Big O notation of the code you wrote, and include 
it in the comments of your program.
'''

def find_sec_lar(numbers):
    lar = None
    sec_lar = None
    
# Time complexity: O(n)
# I loop through the array once.
# Each comparison takes O(1) time.

    for number in numbers:

        if lar is None or number > lar:
            sec_lar = lar
            lar = number
        elif number != lar and (
            sec_lar is None or number > sec_lar
        ):
            sec_lar = number

    return sec_lar

# Space complexity: O(1)
# I only use tow variables to store the largest and second largest numbers, regardless of array size.

shel_num = [3, 5, 6, 13, 23]

result = find_sec_lar(shel_num)

if result is None:
    print("There is no second largest distinct number.")
else:
    print("Second largest number:", result)
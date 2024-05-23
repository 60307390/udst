##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 5

def median(numbers):
    'Returns the median of a given list \'numbers\'. Returns 0 if empty.'
    numbers.sort()
    num_length = len(numbers)
    
    if num_length == 0:
        return None
    if not num_length%2: # If even
        return 0.5*(numbers[num_length//2-1]+numbers[num_length//2])
    return numbers[num_length//2]

assert median([]) == None, "Empty list test failed!"
assert median([1, 2, 3]) == 2, "Test 2 failed." 
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5, "Test 3 failed."
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6, "Test 4 failed."
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6
print("All tests succesfull!")

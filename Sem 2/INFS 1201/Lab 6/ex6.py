##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 6

def closestAverage(numbers):
    'returns the number in the list \'numbers\' closest to the average of the list'
    if len(numbers) == 0:
        return None
    avg = sum(numbers)//len(numbers)
    distances = []
    for i in numbers:
        distances.append(abs(i-avg))
    return numbers[distances.index(min(distances))]



assert closestAverage([]) == None, "Empty list test failed!"
assert closestAverage([1, 2, 3]) == 2, "Test 2 failed." 
assert closestAverage([3, 7, 10, 4, 1, 9, 5, 6, 2, 8]) == 5, "Test 3 failed."
assert closestAverage([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6 or closestAverage([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 4, "Test 4 failed."
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert closestAverage(testData) == 6 or closestAverage(testData) == 4
print("All tests succesfull!")


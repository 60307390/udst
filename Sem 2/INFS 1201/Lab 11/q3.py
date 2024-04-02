##
#Gowshikrajan Senthilkumar - 60307390
# Lab 11
#Exercise 3

def input_scores(n):
    'asks user for score input `n` times'
    if n == 0:
        return []
    else:
        score = int(input("Enter score: "))
        return [score] + input_scores(n-1)

def count_passes(scores):
    'counts the number of passing grades within a given list'
    if len(scores) == 0:
        return 0
    else:
        if scores[0] >= 60:
            return 1 + count_passes(scores[1:])
        return count_passes(scores[1:])

print(count_passes(input_scores(6)))

##
# Gowshikrajan Senthilkumar - 60307390
# Week11 lab
# Exercise 9

from q4 import scoreMCQ

def curveMCQ(attempts):
    'curves the MCQ based on the given attempts to optimize average of grades'
    correct_avg = ""
    scores = []
    for i in range(len(attempts[0])):
        count_T, count_F = 0, 0
        for j in attempts:
            if j[i] == 'T':
                count_T += 1
            else:
                count_F += 1
        if count_T >= count_F:
            correct_avg += 'T'
        else:
            correct_avg += 'F'

    for i in attempts:
        scores.append(scoreMCQ(i, correct_avg))
    avg_score = sum(scores)/len(scores)

    print(f"Arranged 'correct' answers: {correct_avg}")
    print(f"Arranged scores: {scores}")
    print(f"Best average: {avg_score}")


attempts=['TTFTTFFTFT','FFFTTFFTFT','TTFFFFFTFT','TTFFFFFTFT','TTFTTTTTFT','TTTTTTTTTT']
curveMCQ(attempts)
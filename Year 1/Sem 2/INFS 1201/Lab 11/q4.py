##
#Gowshikrajan Senthilkumar - 60307390
# Lab 11
#Exercise 3

def replace_i(st, i, x):
    st = list(st)
    st[i] = x
    return ''.join(st)

def grade(lst, correct_str):
    scores = []
    for i in range(len(lst)):
        scores.append(0)
        for j in range(len(lst[i])):
            if lst[i][j] == correct_str[j]:
                scores[i] += 1
    return scores

def curveMCQ(attempts):
    'returns the adjusted answer key, optimized by the highest minimum score'
    correct = ''
    for i in range(len(attempts[0])):
        correct += 'T'
    for i in range(len(correct)):
        grade_T = grade(attempts, correct)
        grade_F = grade(attempts, replace_i(correct, i, 'F'))
        
        if (min(grade_T) == min(grade_F) and (sum(grade_T) < sum(grade_F))) or min(grade_T) < min(grade_F):
            correct = replace_i(correct, i, 'F')

    scores = grade(attempts, correct)
    print(f"Arranged 'correct' answers: {correct}")
    print(f"Arranged scores: {scores}")
    print(f"Best min grade: {min(scores)}")

'''
attempts=['TTFTTFFTFT','FFFTTFFTFT','TTFFFFFTFT','TTFFFFFTFT','TTFTTTTTFT','TTTTTTTTTT']
curveMCQ(attempts)
'''
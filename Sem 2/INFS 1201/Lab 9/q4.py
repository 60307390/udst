##
# Gowshikrajan Senthilkumar - 60307390
# Week11 lab
# Exercise 4

def scoreMCQ(attempt, correct):
    'checks if the attempted options is equal to the correct options'
    assert len(attempt) == len(correct)
    score = 0
    for i in range(len(attempt)):
        if attempt[i] == correct[i]:
            score += 1
    return score

'''
assert(scoreMCQ("","")==0), "First test failed"
assert(scoreMCQ("TFTF","TTTT")==2), "Second test failed"
assert(scoreMCQ("TTTT","TTTT")==4), "Third test failed"
assert(scoreMCQ("CCCC","ABCD")==1), "Fourth test failed"
print("All tests succesfull")
'''
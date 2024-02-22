# Gowshikrajan
# 60307390
# INFS1101 - 16
# PicnicDecisionGimmick

n_people = int(input("How many participants are there for games? "))

if n_people == 1:
    print("How about a nice book or some music for relaxation?")
elif n_people == 2:
    print("Let's play a card game!")
elif n_people >= 5:
    print("Team sports like soccer or volleyball could be fun!")
else:
    print("How about a board game?")

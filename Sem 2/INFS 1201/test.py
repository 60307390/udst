def sortThings(x):
    lst = []
    for i in sorted(x):
        lst.append(sorted(i))
    return lst

classList = []

with open('coolfile.txt','r') as f:
    for line in f:
        classList.append(line.rstrip())

indexes = []

for i in range(len(classList)):
    a = []
    for j in range(len(classList)):
        if i != j and (j != i+j-len(classList)+1):
            if i+j >= len(classList):
                a.append([classList[j],classList[i+j-len(classList)+1]])
            else:       
                a.append([classList[j],classList[i+j]])
    a.append(["Munir, Muhammad","Senthilkumar, Gowshikrajan"])
    a = sortThings(a)
    indexes.append(a.index(["Munir, Muhammad","Senthilkumar, Gowshikrajan"]))
    print(i,a)

print(min(indexes))
print(max(indexes))

print(indexes)
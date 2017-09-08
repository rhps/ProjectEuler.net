file = 'p022_names.txt'
dict = {'"':0, "A": 1, "B": 2,"C": 3,"D": 4, "E": 5,"F": 6,"G": 7,"H": 8,"I": 9,"J": 10,"K": 11,"L": 12,"M": 13,"N": 14,"O": 15,"P": 16,"Q": 17,"R": 18, "S": 19, "T": 20, "U": 21, "V": 22,"W": 23,"X": 24, "Y": 25, "Z": 26}

a = open(file)
for y in a:
    name = y.split(",")

name.sort()

sumscore = 0
for x in range(len(name)):
    tot = 0
    for y in name[x]:
        tot = tot + dict[y]
    score = tot*(x+1)
    sumscore = sumscore + score

print(sumscore)
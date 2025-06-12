def surSep(name):
    return(name.split()[-1])
def lstPrint(lst):
    for i in lst:
        print(i)
    if len(lst) == 0:
        print("None")
names = []
with open("names.txt" , "r") as file:
    names = (file.read()).split("\n")
for i in names:
    siblings = []
    for j in names:
        if j == i:
            continue
        elif surSep(i) == surSep(j):
            siblings.append(j)
    print(f"{i} has {len(siblings)} siblings : ")
    lstPrint(siblings)
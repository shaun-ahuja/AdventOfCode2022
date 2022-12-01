eachElf = 0
allElf = []

for i in range(2253):
    calories = input()
    if calories != "":
       eachElf += int(calories)
    else:
        allElf.append(eachElf)
        print(allElf)
        eachElf = 0

print(max(allElf))

#'''#eachElf = 0
#allElf = []

#for i in range(2253):
    #calories = input()
    #if calories != "":
     #   eachElf += int(calories)
    #else:
    #    allElf.append(eachElf)
    #    print(allElf)
    #    eachElf = 0

#print(max(allElf))'''

lines = 2251
temp = []
calories = []

for i in range(lines):
    n = input()
    if n != "":
        temp.append(int(n))
    else:
        calories.append(sum(temp))
        print("Hello")
        temp = []
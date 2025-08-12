numbers = [2, 2, 4, 1, 5, 6, 6, 4]
uniques = [] 

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(sorted(uniques))
        


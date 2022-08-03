numbers=[2,2,4,6,4,5,6]
uniques=[]
for i in numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)

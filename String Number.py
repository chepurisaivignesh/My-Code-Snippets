import re
inplisty=input()

numlisty=re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", inplisty)
print(numlisty)
sumval=0
for j in numlisty:
    sumval=sumval+int(j)
averageval=sumval/(len(numlisty))

print(sumval)
print(averageval)


from difflib import Differ
from pprint import pprint

#with open('Adventures2.txt') as file_1, open('Adventures3.txt') as file_2:
#    differ = Differ()

    #for line in differ.compare(file_1.readlines(), file_2.readlines()):
        #print(line)

file_1 = open('Adventures2.txt')
file_1 = file_1.readlines()
file_2 = open('Adventures3.txt')
file_2 = file_2.readlines()

differ = Differ()

result = list(differ.compare(file_1, file_2))

#pprint(result)

differences = []

for i in range(len(result)):
    if result[i][1] in "+-":
        differences.append(result[i])

if differences == []:
    print("No differences")
else:
    print("Differences:")
    pprint(differences)

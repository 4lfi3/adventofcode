import requests

contents = requests.get("https://adventofcode.com/2024/day/2/input", headers={"Cookie":"session=53616c7465645f5ff09934c3bbd383fede5539d7e3d0a6cf7a2f0a97c71afc9e1363c211ef3107a6ffdffefba6f442d99cc25ba501d803a1a36c6975ff26c826"})
input = contents.text
print(input)

lines = input.split("\n")
lines.pop()

safeCount = 0

for line in lines:
    report = line.split(" ")
    report = list(map(int, report))

    safe = True
    problemEncountered = False
    ascending = False
    ascendingSet = False
 
    length = len(report) - 1

    level = 0

    while level < length:

        if ascendingSet:
            if ascending:
                if report[level] >= report[level+1]:
                    if problemEncountered:
                        safe = False
                        break
                    else:
                        problemEncountered = True
                        del report[level+1]
                        #level -= 1
                        length -= 1
                    
            if not ascending:
                if report[level] <= report[level+1]:    
                    if problemEncountered:
                        safe = False
                        break
                    else:
                        problemEncountered = True
                        del report[level+1]
                        #level -= 1
                        length -= 1

        else:
            if report[level] < report[level+1]:
                ascendingSet = True
                ascending = True
            elif report[level] > report[level+1]:
                ascendingSet = True
                ascending = False
            elif report[level] == report[level+1]:
                if problemEncountered:
                    safe = False
                    break
                else:
                    problemEncountered = True
                    del report[level+1]
                    #level -= 1
                    length -= 1

        if abs(report[level] - report[level+1]) > 3:
            if problemEncountered:
                safe = False
                break
            else:
                problemEncountered = True
                del report[level+1]
                #level -= 1
                length -= 1

    if safe == True:
        safeCount += 1

print(str(safeCount))
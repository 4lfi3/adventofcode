import requests

contents = requests.get("https://adventofcode.com/2024/day/2/input", headers={"Cookie":"session=53616c7465645f5fdb1414f283e111d067203eb6d9bc975cf6d71e649d6253e9227b8e768f33d3aaf2ec3b05ea3bfd098e7666ee5ee7f51078b8470595e30bb6"})
input = contents.text
print(input)

reports = input.split("\n")
reports.pop()

safeCount = 0


#problems:
#what should i be?
#how is report being damaged?

def check(report):
    safe = True

    ascendingSet = False
    ascending = False

    for i in range(len(report)-1):
        if safe:
            if ascendingSet:
                if ascending:
                    if report[i] >= report[i+1]:
                            safe = False
                            break     
                if not ascending:
                    if report[i] <= report[i+1]:    
                        safe = False
                        break 
            else:
                if report[i] < report[i+1]:
                    ascendingSet = True
                    ascending = True
                elif report[i] > report[i+1]:
                    ascendingSet = True
                    ascending = False
                elif report[i] == report[i+1]:
                    safe = False
                    break

            if abs(report[i] - report[i+1]) > 3:
                safe = False
                break

    return safe

for report in reports:
    report = report.split(" ") #convert to array of strings
    report = list(map(int, report)) #convert array to ints

    result = check(report)

    if result:
        safeCount += 1
    else:  
        for i in range(len(report)):
            newReport = report.copy()
            del newReport[i]
            if check(newReport):
                safeCount += 1
                break
            
print(str(safeCount))
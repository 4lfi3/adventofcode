import requests

contents = requests.get("https://adventofcode.com/2024/day/2/input", headers={"Cookie":"session=53616c7465645f5ff09934c3bbd383fede5539d7e3d0a6cf7a2f0a97c71afc9e1363c211ef3107a6ffdffefba6f442d99cc25ba501d803a1a36c6975ff26c826"})
input = contents.text
print(input)

lines = input.split("\n")
lines.pop()

safeCount = 0
reportNumberDbg = 0

def problem():
    global safe, problemEncountered, currentLevel, report, done, report1, report2, report1Done
    if problemEncountered:
        if report1Done:
            done = True
            safe = False
        else:
            report1Done = True
    else:
        problemEncountered = True
        report1 = report
        report2 = report
        del report1[currentLevel]
        check(report1)
        if report1Done:
            del report2[currentLevel+1]
            check(report2)

def check(report):
    global done, currentLevel, ascending, ascendingSet
    currentLevel = 0
    while not done:
        if abs(report[currentLevel] - report[currentLevel+1]) > 3:
            problem()

        elif ascendingSet:
            if ascending:
                if report[currentLevel] >= report[currentLevel+1]:
                    problem()

            elif report[currentLevel] <= report[currentLevel+1]:
                problem()

        else:
            if report[currentLevel] < report[currentLevel+1]:
                ascendingSet = True
                ascending = True

            elif report[currentLevel] > report[currentLevel+1]:
                ascendingSet = True

            elif report[currentLevel] == report[currentLevel+1]:
                problem()

        if currentLevel >= len(report)-2:
            done = True

        currentLevel += 1

for report in lines:
    report = report.split(" ")
    report = list(map(int, report))

    safe = True
    ascending = False
    ascendingSet = False
    currentLevel = 0
    problemEncountered = False
    done = False
    report1 = []
    report2 = []
    report1Done = False

    check(report)       
        
    if safe == True:
        safeCount += 1
        print("Safe " + str(lines[reportNumberDbg]))
    else:
        print("Nots " + str(lines[reportNumberDbg]))

    reportNumberDbg += 1

print(str(safeCount))
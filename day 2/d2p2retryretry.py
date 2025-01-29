import requests

contents = requests.get("https://adventofcode.com/2024/day/2/input", headers={"Cookie":"session=53616c7465645f5ff09934c3bbd383fede5539d7e3d0a6cf7a2f0a97c71afc9e1363c211ef3107a6ffdffefba6f442d99cc25ba501d803a1a36c6975ff26c826"})
input = contents.text
print(input)

lines = input.split("\n")
lines.pop()

safeCount = 0


#problems:
#what should i be?
#how is report being damaged?

def check(report):
    safe = True
    error = None

    ascendingSet = False
    ascending = False

    for i in range(len(report)-1):
        if safe:
            if ascendingSet:
                if ascending:
                    if report[i] >= report[i+1]:
                            safe = False
                            error = i
                            break     
                if not ascending:
                    if report[i] <= report[i+1]:    
                        safe = False
                        error = i
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
                    error = i
                    break

            if abs(report[i] - report[i+1]) > 3:
                safe = False
                error = i
                break

    if safe:
        return safe, error
    else:
        error -= 1
        return safe, error

for line in lines:
    report = line.split(" ")
    report = list(map(int, report))

    result = check(report)
    safe = False

    if result[0]:
        safe = True
    else:
        reportDampened1 = report
        reportDampened2 = report
        del(reportDampened1[result[1]])
        if check(reportDampened1)[0]:
            safe = True
        else:
            if result[1] < len(report):
                del(reportDampened2[result[1]+1])
                if check(reportDampened2)[0]:
                    safe = True

    if safe:
        safeCount += 1
        print("SAFE" + str(report))
    else:
        print("UNSA" + str(report))

print(str(safeCount))
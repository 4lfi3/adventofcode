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
    ascending = False

    if report[0] < report[1]:
        ascending = True

    elif report[0] == report[1]:
        safe = False
        continue
 
    for level in range(len(report)-1):
        if ascending:
            if report[level] >= report[level+1]:
                safe = False
                break
        else:
            if report[level] <= report[level+1]:
                safe = False
                break

        if abs(report[level] - report[level+1]) > 3:
            safe = False
            break

    if safe == True:
        safeCount += 1

print(str(safeCount))
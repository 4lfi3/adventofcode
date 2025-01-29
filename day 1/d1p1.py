import requests

contents = requests.get("https://adventofcode.com/2024/day/1/input", headers={"Cookie":"session=53616c7465645f5ff09934c3bbd383fede5539d7e3d0a6cf7a2f0a97c71afc9e1363c211ef3107a6ffdffefba6f442d99cc25ba501d803a1a36c6975ff26c826"})
input = contents.text
print(input)

lines = (input.split("\n"))
lines.pop()

totalDifference = 0
list1 = []
list2 = []

for i in lines:
    items = i.split("   ")
    list1.append(int(items[0]))
    list2.append(int(items[1]))

list1.sort()
list2.sort()

for i in range(1000):
    totalDifference += abs(list1[i] - list2[i])
    print(str(totalDifference))
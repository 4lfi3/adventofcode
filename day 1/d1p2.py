import requests

contents = requests.get("https://adventofcode.com/2024/day/1/input", headers={"Cookie":"session=53616c7465645f5ff09934c3bbd383fede5539d7e3d0a6cf7a2f0a97c71afc9e1363c211ef3107a6ffdffefba6f442d99cc25ba501d803a1a36c6975ff26c826"})
input = contents.text
print(input)

lines = (input.split("\n"))
lines.pop()

similarity = 0
list1 = []
list2 = []

for i in lines:
    items = i.split("   ")
    list1.append(int(items[0]))
    list2.append(int(items[1]))

for i in range(1000):
    matches = 0
    for y in range(1000):
        if list1[i] == list2[y]:
            matches += 1
    similarity += list1[i] * matches
    print(str(similarity))
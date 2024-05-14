# this uses a word list to test the input handler with a large number of continues inputs
# Amount = 3873 inputs tested in a row

from source.core.inputHandler import Input

with open("testword.txt", "r") as file:
    data = file.read().split("\n")
    file.close()

print("Testing ... ")
for i in data:
    print(f"input number: {data.index(i)}")
    if Input.check(i):
        continue
    break

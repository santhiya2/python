filename = "preproinsulin-clean.txt"  # replace with your file name

with open(filename, "r") as file:
    contents = file.read()

count = 0
for char in contents:
    if char.islower():
        count += 1

print("The number of lowercase letters in the file is:", count)
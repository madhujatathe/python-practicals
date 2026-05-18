with open("count.txt","a+") as file:
    file.write("\tone piece is \trevealing soon\n")
    file.seek(0)
    data = file.read()

tab = 0
space = 0
newline = 0

for ch in data:
    if ch =="\t":
        tab+=1
    elif ch ==" ":
        space+=1
    elif ch =="\n":
        newline+=1
file.close()
print("number of tab:",tab)
print("number of space:",space)
print("number of line:",newline)

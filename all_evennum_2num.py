start = int(input("starting number: "))
end = int(input("ending number: "))

print("even number between ",start,"and",end,"are: ")

for i in range(start,end+1):
    if i%2 == 0:
        print(i)

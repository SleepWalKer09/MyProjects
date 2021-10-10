# break
x = ["blue", 1,5,2,8,"yellow", "green", "black"]
print("string con Break")
for i in x:
    if i == "yellow":
        break
    
    print(i)

print("")
print("")

# continue
y = ["blue", 1,5,2,8,"yellow", "green", "black"]
print("string con continue")
for i in y:
    if i == 5:
        continue
    print(i)

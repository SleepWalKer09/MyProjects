x = ["big", "small", "bold", "light", "heavy"]
y = ["iron", "silver", "gold", "platinum", "diamond"]

a=0
b=0

for i in x:
    for j in y:
        print(x[a],y[b])
        b += 1
    a += 1   
    b = 0
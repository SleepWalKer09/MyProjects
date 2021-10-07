def temp(c):
    f = (9/5)*c + 32
    return print(int(f))

c = input("Ingresa temperatura en celsius")
c= int(c)

def leng(m,s):
    h = int(m)/60 + int(s)/3600
    return print(int(h))


m = input("minutos")
m = int(m)
s = input("segundos")
s = int(s)
leng(m,s)

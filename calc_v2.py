import math
import matplotlib.pyplot as plt

start = 0
rectangles = 1000
aux = rectangles/10
end = 3*aux
f = lambda x: math.sin(x**2)
diff = 1/aux
dx = diff/rectangles

def integral(a, b, i):
    suma = 0
    j = 1
    while j <= rectangles*i:
        x_i = a + j*dx
        if x_i >= b: break
        suma += f(x_i)*dx
        j+=1
    return suma


i=start
x = []
y = []
while i < end:
    a=i/aux
    i+=1
    b=i/aux
    #suma = integral(0, b, i)
    suma = integral(a, b, i)
    x.append(a)
    y.append(suma)

#for p in lista: print(p)

plt.plot(x,y)
plt.savefig('quiz/a.png', dpi = 200)
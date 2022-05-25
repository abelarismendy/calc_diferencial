import math
import matplotlib.pyplot as plt

start = 0
rectangles = 1000
aux = rectangles/10
end = 3*aux
f = lambda x: math.sin(x**2)
diff = 1/aux
dx = diff/rectangles
g_x = r'$G(x)=\int_{0}^{x} sin(t^2) \cdot dt$'
delta = r'$\Delta{x}$'
title = f'{g_x}\nn={rectangles}, {delta}={dx}'

sum_txt =r'$\sum_{i=1}^{n}f(x_{i})\Delta{x}$'

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
    # a=i/aux
    b=i/aux
    i+=1
    suma = integral(0, b, i)
    x.append(b)
    y.append(suma)

#for p in lista: print(p)

plt.plot(x,y)
texto = plt.annotate(sum_txt, xy = (2.0,0.8), xytext = (1.3, 0.3), fontsize=15,
        arrowprops=dict(arrowstyle="<-", connectionstyle="arc3,rad=0"))

plt.grid()
plt.title(title)
plt.savefig('quiz/0.png', dpi = 200)
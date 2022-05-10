from math import *
from numpy import *
from matplotlib import pyplot as plt
from matplotlib import patches
n = 10
incremento = 10
inicio = 0
fin = 3
f = r'$y=x^2+2$'


def graficar_funcion():
    t = arange(0.01, 3, 0.01)
    y = (t**2)+2
    fig, ax = plt.subplots()
    ax.plot(t, y)
    texto = plt.annotate(f, xy = (2,6), xytext = (1.2, 7), fontsize=15,
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
    plt.grid()
    return ax
    # plt.show()

while n <= 100:
    diferencia = fin - inicio
    fragmento = diferencia/n
    i = 1
    x = inicio
    suma = 0
    ax = graficar_funcion()
    while i <= n:
        x += fragmento
        f_de_x = ((x**2)+2)
        suma += f_de_x*fragmento
        ax.add_patch(patches.Rectangle(
            (x-fragmento, 0),
            fragmento,
            f_de_x,
            edgecolor = 'red',
            # facecolor = 'red',
            fill=False
        ))
        i += 1
    plt.title(f'Función: {f}\nn = {n}, área = {suma}')
    plt.show()
    # print(fragmento, n, suma)
    n += incremento



# graficar_funcion(10, 15)
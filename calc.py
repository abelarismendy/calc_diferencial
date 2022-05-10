from numpy import arange
from matplotlib import pyplot as plt
from matplotlib import patches
n = 10
incremento = 10
inicio = 0
fin = 3
f = r'$y=x^2+2$'
delta = r'$\Delta{x}$'

def graficar_funcion():
    t = arange(0.01, 3, 0.01)
    y = (t**2)+2
    fig, ax = plt.subplots()
    ax.plot(t, y, label=f)
    texto = plt.annotate(f, xy = (2,6), xytext = (1.2, 7), fontsize=15,
        arrowprops=dict(arrowstyle="<-", connectionstyle="arc3,rad=0"))
    plt.grid()
    return ax

while n <= 100:
    diferencia = fin - inicio
    fragmento = diferencia/n
    i = 1
    x = inicio
    suma = 0
    sum_txt =r'$\sum_{i=0}^{3}x_{i}$'
    ax = graficar_funcion()
    red_patch = patches.Patch(edgecolor='red', fill=False,  label=sum_txt)
    sumatoria_leyenda = ax.legend(handles=[red_patch], loc='upper right', bbox_to_anchor= (0.2,0.89))
    ax.add_artist(sumatoria_leyenda)
    while i <= n:
        x += fragmento
        f_de_x = ((x**2)+2)
        suma += f_de_x*fragmento
        ax.add_patch(patches.Rectangle(
            (x-fragmento, 0),
            fragmento,
            f_de_x,
            edgecolor = 'red',
            fill=False
        ))
        i += 1
    plt.title(f'Función: {f}, n = {n}, {delta} = {fragmento}\nárea = {suma}')
    plt.legend()
    plt.show()
    n += incremento

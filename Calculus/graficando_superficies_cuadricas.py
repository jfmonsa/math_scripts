import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import projections
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
#Ignorar un warning
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 
# os para función de limpiar pantalla
import os
import time
import gc #garbage collector
#Hecho por: Juan Felipe Monsalve Vargas - 2160145-3743

#Validación de los parametros a,b y c de las funciones
def advertencia_parametros(w):
    if(w): print("Para que la grafica se vea bien a,b,c > 1 y a,b,c < 10, por favor ingrese los parametros siguiendo este criterio")
    else: "Para que la grafica se vea bien a,b > 1 y a,b < 10, por favor ingrese los parametros siguiendo este criterio"

def parametros_validos(a,b,c=2): #Para que la grafica este bien
    if(a<1 or b<1 or c<1 or a>10 or b>10 or c>10):
        print("Error: Los parametros a,b y c no cumple con el criterio: a,b,c > 1 y a,b,c < 10\nIntentelo de nuevo")
        time.sleep(3)
        return False
    else: return True

#Funciones para cada superficie
#para graficar todas las funciones las despejé en función de z de modo que z=F(x,y)
#Las ultimas tres quedan en función de y=f(x) ya que z dezaparece por su coeficiente 0: 0z=0
def elipsoide(x,y,a,b,c):
    z = (-(c**2)*((x/a)**2 + (y/b)**2 -1))**0.5
    return z
def paraboloide_eliptico(x,y,a,b):
    z = (x/a)**2+(y/b)**2
    return z
def hyperboloide_prabolico(x,y,a,b):
    z = (x/a)**2-(y/b)**2
    return z
def hyperboloide_una_hoja(x,y,a,b,c):
    z = (c**2 * ((x/a)**2+(y/b)**2-1))**0.5
    return z
def hyperboloide_dos_hojas(x,y,a,b,c):
    z = (c**2 * ((x/a)**2+(y/b)**2+1))**0.5
    return z
def cono_eliptico(x,y,a,b,c):
    z = c*((x/a)**2+(y/b)**2)**0.5
    return z
def cilindro_eliptico(x,a,b):
    y = b*(-1*((x/a)**2 -1))**0.5
    return y
def cilindro_hyperbolico(x,a,b):
    y = b*((x/a)**2 -1)**0.5
    return y
def cilindro_parabolico(x,a):
    y = x**2 /(-2*a)
    return y

menu_text="""
        [0] finalizar el programa
        ********* Superficies cuádricas reales no degeneradas *********
        [1] graficar un elipsoide
        [2] graficar paraboloide eliptico
        [3] graficar Hyperboloide parabolico
        [4] graficar Hyperboloide de una sola hoja (Hyperboloide hyperbolico)
        [5] graficar Hyperboloide de dos hojas (Hyperboloide eliptico)

        ********* Superficies cuádricas reales degeneradas *********
        [6] graficar Cono eliptico (Cono cuadrico)
        [7] graficar Cilindro Eliptico
        [8] graficar Cilindro hyperbolico
        [9] graficar Cilindro parabolico
        \nSeleccione una opción (escriba el número de opción):"""

# plt.rcParams['text.usetex'] = True #Para mostrar ecuaciones en LATEX, me genera error :(
while(True):
    #Projectamos los ejes 3d
    ax = plt.axes(projection='3d') #ax = plt.gca(projection='3d') sintaxis desactualizada
    ax.set_xlabel("eje x")
    ax.set_ylabel("eje y")
    ax.set_zlabel("eje z")
    #---------------------------------------------------------------------------------
    print(menu_text)
    opc=int(input())
    if(opc==0): break


    ##########################################################################
    if(not (opc==7 or opc==8 or opc ==9)): #Para 3 variables z=f(x,y)
        # --------------------------------------------------------------------
        #Configuraciones del sistema de coordenadas
        n=2250  #n numero de valores para generar
        # generamos un rango de de n puntos entre -10 y 10 en cada eje
        # Con estos puntos evaluaremos la función correpondiente para graficarla
        x_values=np.linspace(-10,10,n)
        y_values=np.linspace(-10,10,n)
        #Creamos una un grilla de puntos (x,y) para reemplazar en la función Z=F(x,y)
        X,Y=np.meshgrid(x_values,y_values)
        # --------------------------------------------------------------------
        if(opc==1):
            print("para graficar la ecuación del elipsoide (x/a)^2 + (y/b)^2 + (z/c)^2 = 1")
            advertencia_parametros(True)
            a=input("Ingrese parametro a:")
            b=input("Ingrese parametro b:")
            c=input("Ingrese parametro c:")
            eq=r"$\frac{x^2}{"+a+r"^2}+\frac{y^2}{"+b+r"^2}+\frac{z^2}{"+c+r"^2}=1$"
            plt.title('Elipsoide: '+eq)
            a=int(a);b=int(b);c=int(c)
            if(parametros_validos(a,b,c)):
                Z=elipsoide(X,Y,a,b,c)
                ax.plot_surface(X, Y, Z, cmap=cm.gist_heat)
                ax.plot_surface(X, Y, -Z, cmap=cm.gist_heat_r)
                plt.show()
        elif(opc==2):
            print("para graficar la ecuación del Paraboloide eliptico (x/a)^2 + (y/b)^2 - z = 0")
            advertencia_parametros(False)
            a=input("Ingrese parametro a:")
            b=input("Ingrese parametro b:")
            eq=r'$\frac{x^2}{'+a+r'^2}+\frac{y^2}{'+b+r'^2}-z=0$'
            plt.title('Paraboloide eliptico: '+eq)
            a=int(a);b=int(b)
            if(parametros_validos(a,b)):
                Z=paraboloide_eliptico(X,Y,a,b)
                ax.plot_surface(X, Y, Z, cmap=cm.gist_heat)
                plt.show()
        elif(opc==3):
            print("para graficar la ecuación del Hyperboloide parabolico (x/a)^2 - (y/b)^2 - z = 0")
            advertencia_parametros(False)
            a=input("Ingrese parametro a:")
            b=input("Ingrese parametro b:")
            eq=r'$\frac{x^2}{'+a+r'^2}-\frac{y^2}{'+b+r'^2}-z=0$'
            plt.title('Hyperboloide parabolico: '+eq)
            a=int(a);b=int(b)
            if(parametros_validos(a,b)):
                Z=hyperboloide_prabolico(X,Y,a,b)
                ax.plot_surface(X, Y, Z, cmap=cm.gist_heat)
                plt.show()
        elif(opc==4):
            print("para graficar la ecuación del Hyperboloide de una sola hoja (x/a)^2 + (y/b)^2 - (z/c)^2 = 1")
            advertencia_parametros(True)
            a=input("Ingrese parametro a:")
            b=input("Ingrese parametro b:")
            c=input("Ingrese parametro c:")
            eq=r'$\frac{x^2}{'+a+r'^2}+\frac{y^2}{'+b+r'^2}-\frac{z^2}{'+c+r'^2}=1$'
            plt.title('Hyperboloide de una sola hoja: '+eq)
            a=int(a);b=int(b);c=int(c)
            if(parametros_validos(a,b,c)):
                Z=hyperboloide_una_hoja(X,Y,a,b,c)
                ax.plot_surface(X, Y, Z, cmap=cm.gist_heat)
                ax.plot_surface(X, Y, -Z, cmap=cm.gist_heat_r)
                plt.show()
        elif(opc==5):
            print("para graficar la ecuación del Hyperboloide de dos hojas (x/a)^2 + (y/b)^2 - (z/c)^2 = -1")
            advertencia_parametros(True)
            a=input("Ingrese parametro a:")
            b=input("Ingrese parametro b:")
            c=input("Ingrese parametro c:")
            eq=r'$\frac{x^2}{'+a+r'^2}+\frac{y^2}{'+b+r'^2}-\frac{z^2}{'+c+r'^2}=-1$'
            plt.title('Hyperboloide de dos hojas: '+eq)
            a=int(a);b=int(b);c=int(c)
            if(parametros_validos(a,b,c)):
                Z=hyperboloide_dos_hojas(X,Y,a,b,c)
                ax.plot_surface(X, Y, Z, cmap=cm.gist_heat)
                ax.plot_surface(X, Y, -Z, cmap=cm.gist_heat_r)
                plt.show()
        elif(opc==6):
            print("para graficar la ecuación del Cono eliptico (x/a)^2 + (y/b)^2 - (z/c)^2 = 0")
            advertencia_parametros(True)
            a=input("Ingrese parametro a:")
            b=input("Ingrese parametro b:")
            c=input("Ingrese parametro c:")
            eq=r'$\frac{x^2}{'+a+r'^2}+\frac{y^2}{'+b+r'^2}-\frac{z^2}{'+c+r'^2}=0$'
            plt.title('Cono eliptico: '+eq)
            a=int(a);b=int(b);c=int(c)
            if(parametros_validos(a,b,c)):
                Z=cono_eliptico(X,Y,a,b,c)
                ax.plot_surface(X, Y, Z, cmap=cm.gist_heat)
                ax.plot_surface(X, Y, -Z, cmap=cm.gist_heat)
                plt.show()
    ##########################################################################





    

    ##########################################################################
    else: #Para 2 variables y=f(x)
        # --------------------------------------------------------------------
        #Configuraciones del sistema de coordenadas
        n=2250  #n numero de valores para generar
        # generamos un rango de de n puntos entre -10 y 10 en cada eje
        # Con estos puntos evaluaremos la función correpondiente para graficarla
        # generamos un rango de de n puntos entre -10 y 10 en cada eje
        # Con estos puntos evaluaremos la función correpondiente para graficarla
        x_values=np.linspace(-10,10,n)
        z_values=np.linspace(-10,10,n)
        #Creamos una un grilla de puntos
        X,Z=np.meshgrid(x_values, z_values)
        # --------------------------------------------------------------------


        if(opc==7):     
            print("para graficar la ecuación del Cilindro eliptico (x/a)^2 + (y/b)^2 = 1")
            advertencia_parametros(False)
            a=input("Ingrese parametro a:")
            b=input("Ingrese parametro b:")
            eq=r'$\frac{x^2}{'+a+r'^2}+\frac{y^2}{'+b+r'^2}=1$'
            plt.title('Cilindro eliptico: '+eq)
            a=int(a);b=int(b)
            if(parametros_validos(a,b)):
            #Como tenemos para este caso y=f(x) vamos a seguir utilizando la variable Z
            #pero a la hora de graficar vamos a intercambiar X y Z
                Y = cilindro_eliptico(X,a,b) #En realidad es Y = f(X,11,1) pero la renombramos como Z
                ax.plot_surface(X, Y, Z, cmap=cm.gist_heat)
                ax.plot_surface(X, -Y, Z, cmap=cm.gist_heat_r)
                plt.show()
        elif(opc==8):
            print("para graficar la ecuación del Cilindro hyperbolico (x/a)^2 - (y/b)^2 = 1")
            advertencia_parametros(False)
            a=input("Ingrese parametro a:")
            b=input("Ingrese parametro b:")
            eq=r'$\frac{x^2}{'+a+r'^2}-\frac{y^2}{'+b+r'^2}=1$'
            plt.title('Cilindro hyperbolico: '+eq)
            a=int(a);b=int(b)
            if(parametros_validos(a,b)):
            #Como tenemos para este caso y=f(x) vamos a seguir utilizando la variable Z
            #pero a la hora de graficar vamos a intercambiar X y Z
                Y = cilindro_hyperbolico(X,a,b) #En realidad es Y = f(X,11,1) pero la renombramos como Z
                ax.plot_surface(X, Y, Z, cmap=cm.gist_heat)
                ax.plot_surface(X, -Y, Z, cmap=cm.gist_heat_r)
                plt.show()
        elif(opc==9):
            print("para graficar la ecuación del Cilindro parabolico x^2 + 2ay = 0")
            advertencia_parametros(False)
            a=input("Ingrese parametro a:")
            eq=r'$x^2+2('+a+r')y=0$'
            plt.title('Cilindro parabolico: '+eq)
            a=int(a)
            if(parametros_validos(a,b=2)):
            #Como tenemos para este caso y=f(x) vamos a seguir utilizando la variable Z
            #pero a la hora de graficar vamos a intercambiar X y Z
                Y = cilindro_parabolico(X,a) #En realidad es Y = f(X,11,1) pero la renombramos como Z
                ax.plot_surface(X, Y, Z, cmap=cm.gist_heat)
                plt.show()
    #Borrando el objeto ax, para volver a graficar
    os.system('cls')
    del ax; #del X;del Y;del Z
    gc.collect()    
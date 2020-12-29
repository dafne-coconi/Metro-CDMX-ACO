from skimage import data,color,io,filters,segmentation,morphology
from mpl_toolkits import mplot3d
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

Ima=io.imread('NODOS.jpeg')  #Cambiamos de placa a conveniencia
#gris=np.uint8(color.rgb2gray(Ima)*255)
plt.figure()
plt.imshow(Ima)


matriz_distancia=np.load('Distancias_todos.npy')
k=1
while (k>0):
    print('Seleccione los dos nodos')
    punto=np.int32(plt.ginput(-1))
    distancia=np.sqrt((punto[0,0]-punto[1,0])**2+(punto[0,1]-punto[1,1])**2)
    n=int(input("Ingrese punto n: "))
    m=int(input("Ingrese punto m: "))
    if (n==0):
        break
    matriz_distancia[n,m]=distancia

#np.save('Distancias_todos2',matriz_distancia) 
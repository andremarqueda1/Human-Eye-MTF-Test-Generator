"""
@author: Narváez Marqueda Ricardo André Sebastián
PRACTICA 1 MANIPULACIÓN BÁSICA DE IMÁGENES EN PYTHON
"""

import cv2 
import napari
import numpy as np

f=np.full((512,1),0,dtype=np.double) #Declaramos el arreglo F
g=np.full((1,512),0,dtype=np.double) #Declaramos el arreglo G

k1=0.009012078823#Rep
k2=3.4859
k3=0.0255   #Para la función de atenuación

for i in range (512):
    f[i][0]=np.sin(k2*np.exp(k1*i))
    g[0][i]=np.exp(-k3*i)

h=np.multiply(f,g)
h=cv2.rotate(h,cv2.ROTATE_90_COUNTERCLOCKWISE)
viewer=napari.view_image(h,colormap="gray") #Utilizamos napari para visualizar en tiempo real
napari.run() #ejecutamos el visualizador


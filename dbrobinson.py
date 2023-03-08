import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('omero.jpg', 0)
img2 = img.copy()

(row, col) = img.shape

for i in range(row):
    for j in range(col):
        if (img[i][j] < 10):
            img2[i][j] = 10
        if (img[i][j] > 240):
            img2[i][j] = 240

f_max = img2.max()
f_min = img2.min()
img3 = img2.copy()
for i in range(row):
    for j in range(col):
        img3[i][j] = ((img2[i][j] - f_min) / (f_max - f_min)) * 256

norte = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
imagen_norte = cv2.filter2D(img3,-1,norte)

sur = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
imagen_sur = cv2.filter2D(img3,-1,sur)

este = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
imagen_este = cv2.filter2D(img3,-1,este)

oeste = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
imagen_oeste = cv2.filter2D(img3,-1,oeste)

noreste = np.array([[-2,-1,0],[-1,0,1],[0,1,2]])
imagen_noreste = cv2.filter2D(img3,-1,noreste)

noroeste = np.array([[0,1,2],[-1,0,1],[-2,-1,0]])
imagen_noroeste = cv2.filter2D(img3,-1,noroeste)

sureste = np.array([[0,-1,-2],[1,0,-1],[2,1,0]])
imagen_sureste = cv2.filter2D(img3,-1,sureste)

suroeste = np.array([[2,1,0],[1,0,-1],[0,-1,-2]])
imagen_suroeste = cv2.filter2D(img3,-1,suroeste)

fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(8, 8))

axs[0][0].imshow(imagen_norte, cmap="gray")
axs[0][0].axis("off")
axs[0][0].set_title('Norte')

axs[0][1].imshow(imagen_noreste, cmap="gray")
axs[0][1].axis("off")
axs[0][1].set_title('Noreste')

axs[1][0].imshow(imagen_sur, cmap="gray")
axs[1][0].axis("off")
axs[1][0].set_title('Sur')

axs[1][1].imshow(imagen_noroeste, cmap="gray")
axs[1][1].axis("off")
axs[1][1].set_title('Noroeste')

axs[2][0].imshow(imagen_este, cmap="gray")
axs[2][0].axis("off")
axs[2][0].set_title('Este')

axs[2][1].imshow(imagen_sureste, cmap="gray")
axs[2][1].axis("off")
axs[2][1].set_title('Sureste')

axs[3][0].imshow(imagen_oeste, cmap="gray")
axs[3][0].axis("off")
axs[3][0].set_title('Oeste')

axs[3][1].imshow(imagen_suroeste, cmap="gray")
axs[3][1].axis("off")
axs[3][1].set_title('Suroeste')

plt.show()
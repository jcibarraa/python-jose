import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('omero.jpg')
img2 = cv2.imread('omero.jpg')
img3 = cv2.imread('omero.jpg')
img4 = cv2.imread('omero.jpg')

cv2.imshow('Visualizar',img) #nombre de la ventana donde va a visualizar la imagen

color = ('b','g','r')

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))#cmbiar los canales de los colores para matplotlib 
plt.show()

for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.show()

fig, axs = plt.subplots(nrows = 2, ncols = 2, figsize =(8,8))
axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0, 0].axis("off")

axs[0, 1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
axs[0, 1].axis("off")

axs[1, 0].imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
axs[1, 0].axis("off")

axs[1, 1].imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))
axs[1, 1].axis("off")

plt.show()

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.destroyAllWindows()
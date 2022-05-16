import numpy as np
import cv2

img = cv2.imread('Cartas.jpg')

imag = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2. imshow('Original' , img)
cv2.waitKey()
cv2.destroyAllWindows()


"------------------ Laplaciano ----------------------------- "
lap = cv2.Laplacian(imag, cv2.CV_64F) #Deteccion  de bordes de Laplacian
lap = np.uint8(np.absolute(lap)) # Ir al valor absoluto de vueltas

cv2.imshow('Laplacian', lap)
cv2.waitKey()
cv2.destroyAllWindows()


"------------------ Sobel -----------------"

#variable = codigo( imagen,Profundidad de la imagen,orden de la derivada, orden de la derivada mientras calculamos Sobel, el tamaño de kernel Sobel(1,3,5,7)
sobelx = cv2.Sobel(imag,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(imag,cv2.CV_64F,0,1,ksize=5)

cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)

cv2.waitKey()
cv2.destroyAllWindows()


"----------------- Canny -------------------"

bordes = cv2.Canny(imag, 100, 200)#Los numeros son los lumbrales

cv2.imshow('Canny',bordes)
cv2.waitKey()
cv2.destroyAllWindows()

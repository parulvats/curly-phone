'''
Created on Aug 8, 2021

@author: Parul Vats
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'E:\cognizant\Computer-Vision-with-Python\Computer-Vision-with-Python\DATA\internal_external.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.show()
#cv2.RETR_CCOMP-->COMPLETE CONTOUR(INTERNAL+EXTERNAL)
contours,hierarchy= cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
plt.imshow(img,cmap='gray')
plt.show()

blank_img = np.zeros(img.shape)
#EXTERNAL COUNTORS
#Boundary is actually touching the background of image
for i in range(len(contours)):
    #external contours
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(blank_img,contours,i,255,-1)
    #internal contours
    #if hierarchy[0][i][3] != -1:
plt.imshow(blank_img,cmap='gray')
plt.show()
    
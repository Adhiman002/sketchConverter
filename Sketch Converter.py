# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:51:38 2023

@author: Abhishek
"""

import cv2
i=cv2.imread('a.png')
g_img=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
In=cv2.bitwise_not(g_img)
blur=cv2.GaussianBlur(In,(21,21),0)
inBlur=cv2.bitwise_not(blur)
sketch=cv2.divide(g_img,inBlur,scale=256.0)
cv2.imwrite('sketch.png',sketch)

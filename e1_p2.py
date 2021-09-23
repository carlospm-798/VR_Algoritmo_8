#Carlos Paredes Márquez
#algoritmo 8, parte 2
#09 23 2021

import cv2

im = cv2.imread('e2_p2.png')
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask0 = cv2.inRange(hsv, (62, 0, 0), (62, 255, 255))

mask = cv2.bitwise_not(mask0)
im2 = cv2.bitwise_and(im, im, mask=mask)

cv2.imshow('Image0', im)
cv2.imshow('Image1', im2)
cv2.waitKey(0)
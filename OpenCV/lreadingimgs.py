import cv2

"""img = cv2.imread("pikachu.png",1)
#-1 is unchanged, 0 is greyscale/black and white, 1 is specify the loaded image and color
img = cv2.imread("pikachu.png",-1)

#showing img
cv2.imshow("Pikachu",img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

img = cv2.imread("pikachu.png",1)

B, G, R = cv2.split(img)

cv2.imshow("Pikachu",img)
cv2.imshow("Pickachu_green",B)
"""cv2.imwrite("Pikachu_gray.png",img)"""
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

smile = cv2.imread("smile.png",1)



cv2.imshow("smile",smile)
cv2.waitKey(0)
B, G, R = cv2.split(smile)
cv2.imshow("smile_green",G)
cv2.waitKey(0)
cv2.imshow("smile_blue",B)
cv2.waitKey(0)
cv2.imshow("smile_red",R)


gray = cv2.imread("smile.png",0)
cv2.imwrite("smile_greyscale.png",gray)
cv2.waitKey(0)
cv2.imshow("smile_greyscale",gray)


cv2.waitKey(0)
cv2.DestroyAllWindows()
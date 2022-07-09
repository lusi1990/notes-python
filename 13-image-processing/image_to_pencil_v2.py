import cv2

img=cv2.imread('263697.20.jpg')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_img, (25, 25), sigmaX=0)

finnal_img=cv2.divide(gray_img,blur_image,scale=255.0)
cv2.imshow('2',finnal_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
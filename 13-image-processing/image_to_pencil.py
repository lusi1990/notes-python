import cv2

img=cv2.imread('263697.20.jpg')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inverted_img = 255-gray_img
blur_image = cv2.GaussianBlur(inverted_img, (25, 25), sigmaX=0)

def dodge(front,back):
    front=front.astype('float32')
    back=back.astype('float32')
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

finnal_img=dodge(blur_image,gray_img)
cv2.imshow('2',finnal_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
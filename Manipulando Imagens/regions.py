import cv2 as cv

img = cv.imread(r'Manipulando Imagens\lenna.jpg', cv.IMREAD_COLOR)
if not img.data:
    print("An error ocurred while trying to get the image")

img[100:210, 150:300] = 255 - img[100:210, 150:300]

cv.imshow('Lenna', img)

cv.waitKey(0)
cv.destroyAllWindows()
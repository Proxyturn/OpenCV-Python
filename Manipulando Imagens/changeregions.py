import cv2 as cv

def change_diagonals(img):
    inverted_image = img
    h, w, img_channels = img.shape
    metade_h = h/2
    metade_w = w/2

    

   
    
    

    #return inverted_image

img = cv.imread('Manipulando Imagens\lenna.jpg', cv.IMREAD_COLOR)
if not img.data:
    print("An error ocurred while trying to get the image")
h, w, img_channels = img.shape

metade_h = h/2
metade_w = w/2
q1 = img[0:int(metade_h), 0:int(metade_w)]
q2 = img[0:int(metade_h), int(metade_w):w]
q4 = img[int(metade_h):h, int(metade_w):w]
q3 = img[int(metade_h):h, 0:int(metade_w)]
#cv.imshow('img1', q1)
#cv.imshow('img2', q2)
#cv.imshow('img3', q3)
#cv.imshow('img4', q4)

inverted_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

inverted_img[0:int(metade_h), 0:int(metade_w)] = q4
inverted_img[int(metade_h):h, int(metade_w):w] = q1
inverted_img[0:int(metade_h), int(metade_w):w] = q3
inverted_img[int(metade_h):h, 0:int(metade_w)] = q2

cv.imshow('nanLe', inverted_img)


cv.waitKey(0)
cv.destroyAllWindows()

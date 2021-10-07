import cv2 as cv
import numpy as np

def remove_bordas(img, pixel_ref=255):
    tamanho = img.shape
    borda = (tamanho[0] - 1, tamanho[1] - 1)
    img_ret = img.copy()

    for i in range(tamanho[0]):
        if img_ret[i, 0] == pixel_ref:
            cv.floodFill(img_ret, None, (0, i), 0)
        if img_ret[i, borda[1]] == pixel_ref:
            cv.floodFill(img_ret, None, (borda[1], i), 0)

    for j in range(tamanho[1]):
        if img_ret[0, j] == pixel_ref:
            cv.floodFill(img_ret, None, (j, 0), 0)
        if img_ret[borda[0], j] == pixel_ref:
            cv.floodFill(img_ret, None, (j, borda[0]), 0)

    return img_ret

def labeling_pos_ref(img, pixel_ref=255):
    tamanho = img.shape
    imagem_temp = remove_bordas(img)

    cv.floodFill(imagem_temp, None, (0, 0), 32)

    p_bolha = []
    p_bolha_de_bolha = []
    p_anterior = (0, 0)
    for i in range(tamanho[0]):
        for j in range(tamanho[1]):
            if imagem_temp[i, j] == pixel_ref:
                cv.floodFill(imagem_temp, None, (j, i), 64)
                p_bolha.append((j, i))
            if imagem_temp[i, j] == 0:
                cv.floodFill(imagem_temp, None, (j, i), 128)
                cv.floodFill(imagem_temp, None, p_anterior, 128)
                p_bolha_de_bolha.append((j, i))
            p_anterior = (j, i)

    return imagem_temp, p_bolha, p_bolha_de_bolha



img = cv.imread(r'Preenchimentos\labeling.png', cv.IMREAD_GRAYSCALE)
if not img.data:
    print("An error ocurred while trying to get the image")
th, img_threshold = cv.threshold(img, 220, 255, cv.THRESH_BINARY)




floodfill = img_threshold.copy()

h, w = img_threshold.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

cv.floodFill(floodfill, mask, (0,0), 255)

floodfill_inv = cv.bitwise_not(floodfill)

img_out = img_threshold | floodfill_inv

cv.imshow("Thresholded Image", img_threshold)
cv.imshow("Floodfilled Image", floodfill)
cv.imshow("Foreground", img_out)

img3, bolha, bolha_de_bolha = labeling_pos_ref(img)
print('\n\nExercicio 3.2 B:')
print(f'\nNumero de bolhas: {len(bolha)}\nPosições:\n{bolha}')
print(f'\nNumero de bolhas de bolha: {len(bolha_de_bolha)}\nPosições:\n{bolha_de_bolha}')
cv.imshow('Exercicio 3.2 B', img3)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
import numpy as np
from tqdm import tqdm

img_name = "376001"

img = cv.imread("inputs/" + img_name + ".jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

choquet_weights = np.array([1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 1])

dimensions = img.shape
height = dimensions[0]
width = dimensions[1]
cons = 1

newimg = np.zeros((height, width), np.uint8)
img = cv.GaussianBlur(img,(5,5),sigmaX=1)

def choquet(array):
    sum = 0
    for i in range(1,8):
        sum += (array[8-i] - array[7-i]) * ((1/i))
    sum += array[0] * ((1/7))
    return sum

for i in tqdm(range(1,width-1),
               desc="Loading…",
               ascii=False, ncols=75):
    for j in range(1,height-1):
        central = int(img[j,i])
        derivative = []
        # top
        derivative.append(abs(central - int(img[j-1][i])))
        # top right
        derivative.append(abs(central - int(img[j-1][i+1])))
        # right
        derivative.append(abs(central - int(img[j][i+1])))
        # bottom right
        derivative.append(abs(central - int(img[j+1][i+1])))
        # bottom
        derivative.append(abs(central - int(img[j+1][i])))
        # bottom left
        derivative.append(abs(central - int(img[j+1][i-1])))
        # left
        derivative.append(abs(central - int(img[j][i-1])))
        # top left
        derivative.append(abs(central - int(img[j-1][i-1])))

        derivative.sort()
        # if(choquet(derivative) * cons > 255):
        #     newimg[j,i] = 255
        # else:
        # newimg[j,i] = choquet(derivative) * cons
        if(choquet(derivative) > 7):
        #     if(choquet(derivative)*cons) > 255:
        #         newimg[j,i] = 255
        #     else:
            newimg[j,i] = choquet(derivative)
        #    newimg[j,i] = 255
        #newimg[j,i] = choquet(derivative, choquet_weights)
        # if(choquet(derivative, choquet_weights) > 127):
        #     newimg[j,i] = 0
        # else:
        #     newimg[j,i] = 255
cv.imshow('newimg',cv.equalizeHist(newimg))
# cv.imshow('newimg',newimg)

# cv.imwrite('inputs/' + img_name + '-choquet.png',newimg)
cv.waitKey(0)
 
# closing all open windows
cv.destroyAllWindows()

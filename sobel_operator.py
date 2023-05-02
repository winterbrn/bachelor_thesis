import cv2 as cv
import numpy as np
import math

def my_product(x1, x2):
    sum = 0
    for i in range(len(x1)):
        sum += x1[i]*x2[i]
    return sum

def edge_detector(image):
    x_kernel = [1,0,-1,2,0,-2,1,0,-1]
    y_kernel = [1,2,1,0,0,0,-1,-2,-1]
    try:
        img = cv.imread(image)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        print(img[0,0])
        #img = cv.GaussianBlur(img,(9,9),0)
        width = img.shape[1]
        height = img.shape[0]

        new_image = np.zeros((height,width,1), np.uint8)
        i = 0
        k = 0

        for k in range(1,width-1):
            for i in range(1,height-1):
                #for j in range(9):
                act_kernel = []
                act_kernel.append(img[i-1][k-1])
                act_kernel.append(img[i][k-1])
                act_kernel.append(img[i+1][k-1])
                act_kernel.append(img[i-1][k])
                act_kernel.append(img[i][k])
                act_kernel.append(img[i+1][k])
                act_kernel.append(img[i-1][k+1])
                act_kernel.append(img[i][k+1])
                act_kernel.append(img[i+1][k+1])
                if(math.sqrt((my_product(act_kernel, x_kernel))**2+(my_product(act_kernel, y_kernel))**2) > 80):
                    new_image[i][k] = math.sqrt((my_product(act_kernel, x_kernel))**2+(my_product(act_kernel, y_kernel))**2)
            print(k)

        cv.imshow("new_image", new_image)
        cv.waitKey(0)

    except IOError:
        print("Image not found.")
        pass

#edge_detector("images/castle.png")

import cv2 as cv
import numpy as np

def edge_detector(img, row_frame, col_frame, threshold):
    row_frame_half = (int) (row_frame/2)
    col_frame_half = (int) (col_frame/2)
    try:
        img = cv.imread(img)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        print(img[0][0])

        width = img.shape[1]
        height = img.shape[0]

        img_bw=[[]]
        new_image_x = np.zeros((height,width,1), np.uint8)
        i = 0
        k = 0

        for k in range(height):
            row = []
            img_bw.append(row)
            for i in range(width):
                row.append(img[k][i])
            j = 0
            while (j < width - row_frame):
                left_sum = 0
                right_sum = 0
                for i in range(row_frame_half):
                    left_sum = row[j + i] / row_frame_half
                for i in range(row_frame_half):
                    right_sum = row[j + i + row_frame_half] / row_frame_half
                new_image_x[k][j] = abs(left_sum - right_sum)
                j = j + 1
            if(k % 100 == 0):
                print(k)
        i = 0
        k = 0

        new_image_y = np.zeros((height,width,1), np.uint8)

        for k in range(width):
            col = []
            img_bw.append(col)
            for i in range(height):
                col.append(img[i][k])
            j = 0
            while (j < height - col_frame):
                top_sum = 0
                bottom_sum = 0
                for i in range(col_frame_half):
                    top_sum = col[j + i] / col_frame_half
                for i in range(col_frame_half):
                    bottom_sum = col[j + i + col_frame_half] / col_frame_half
                new_image_y[j][k] = abs(top_sum - bottom_sum)
                j = j + 1
            if(k % 100 == 0):
                print(k)
        new_image = np.zeros((height,width,1), np.uint8)

        for j in range(height):
            for i in range(width):
                if(new_image_x[j][i] + new_image_y[j][i] > threshold):
                    new_image[j][i] = 255
        cv.resize(new_image, (960, 960))
        cv.imshow("new_image", new_image)
        cv.waitKey(0)


    except IOError:
        print("Image not found.")
        pass
#edge_detector("images/castle.png", 4, 4, 40)

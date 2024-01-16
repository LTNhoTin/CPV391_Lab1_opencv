import cv2

import numpy as np

img_path = 'vinfast.jpeg'

ori_img = cv2.imread(img_path)

src = []  

#mouse callback handler

def mouse_handler(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONUP:  

        img = ori_img.copy()

        src.append([x, y])

        for xx, yy in src:

            cv2.circle(img, center=(xx, yy), radius=5, color=(0, 255, 0), thickness=-1)

        cv2.imshow('Original Image', img)

        #perspective transform

        if len(src) == 4:

            src_np = np.array(src, dtype=np.float32)

            print("original points : \n", src_np)

cv2.namedWindow('Original Image')

cv2.setMouseCallback('Original Image', mouse_handler)  

cv2.imshow('Original Image', ori_img)

if cv2.waitKey(0) == 32:

    cv2.destroyAllWindows()

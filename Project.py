folder_path = 'D:\\work\\my_work\\Second_year\\Second Semester\\Image Processing\\Photos'

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def FindCentroid(img):
    img_path = os.path.join(folder_path, img)
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    L,Y,B = cv2.split(img)

    Banana = cv2.inRange(B, 50, 140)
    Banana = cv2.medianBlur(Banana, 3)
    M = cv2.moments(Banana)

    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(img, (cX, cY), 20, (255, 0, 0), -1)
    cv2.putText(img, (f'Centroid = X : {cX}, Y :{cY}.'), (cX - 25, cY - 100),cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 10)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img)

    plt.subplot(1,2,2)
    plt.imshow(Banana, cmap="gray")
    plt.show()


def DetectingHouseArea(img):
    plt.figure(figsize=(10, 5))
    img_path = os.path.join(folder_path, img)
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.medianBlur(img, 3)
    Frame = cv2.inRange(img, 14, 25)

    lines = cv2.HoughLinesP(
    Frame,
    1,              #Distance resolution in pixels
    np.pi / 80,  #Angle resolution in radians
    61,      #Min. number of intersecting points to detect a line   #Vector to return start and end points of the lines indicated by [x1, y1, x2, y2] 
    0,   #Line segments shorter than this are rejected
    28       #Max gap allowed between points on the same line
    )

    left = 1000 #X axis 0 is on the left
    right = 0
    top = 1000 #Y axis 0 at the top
    bottom = 0

    for line in lines:
        if line[0][0] < left : #looking for left
            left = line[0][0]
        
        if line[0][1] < top: #looking for top
            top = line[0][1]

        if line[0][2] > right : #looking for right
            right = line[0][2]

        if line[0][3] > bottom : #looking for bottom
            bottom = line[0][3]

    cv2.line(img, (left, top), (right, top), (255,255,255), 3)
    cv2.line(img, (left, bottom), (right,bottom), (255,255,255), 3)
    cv2.line(img, (left, top), (left,bottom), (255,255,255), 3)     
    cv2.line(img, (right, top), (right,bottom), (255,255,255), 3)

    plt.subplot(2,3,5)
    plt.imshow(Frame, "gray")

    plt.subplot(2,3,4)
    plt.imshow(img)
    plt.show()


def LaneDetect(img):
    img_path = os.path.join(folder_path, img)
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
    H,S,V = cv2.split(img)
    img = cv2.cvtColor(img, cv2.COLOR_XYZ2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


    height, width = img.shape
    print(img.shape)
    black = np.zeros_like(img)
    triangle = np.array([[(width//2, 80), (0, height-20) , (width, height-20)]]) 
    triangle_img = cv2.fillPoly(black, triangle, 255) 
    ROI = cv2.bitwise_and(triangle_img, img)

    print(triangle)
    
    Lane = cv2.inRange(ROI, 160, 255)

    lines = cv2.HoughLinesP(
    Lane,
    1,              #Distance resolution in pixels
    np.pi / 180,  #Angle resolution in radians
    50,      #Min. number of intersecting points to detect a line   #Vector to return start and end points of the lines indicated by [x1, y1, x2, y2] 
    30,   #Line segments shorter than this are rejected
    10       #Max gap allowed between points on the same line
    )

    try:
        for line in lines:
            if line[0][1] > 78 or line[0][3] > 78 :
                cv2.line(img, (line[0][0], line[0][1]), (line[0][2],line[0][3]), (0,0,0), 10)

    except TypeError:
        print(TypeError)

    plt.figure(figsize=(10,5))
    plt.subplot(2,3,1)
    plt.imshow(ROI, "gray")

    plt.subplot(2,3,2)
    plt.imshow(img)

    plt.subplot(2,3,3)
    plt.imshow(Lane, "gray")

    plt.show()

def NoiseReduction(img):
    img_path = os.path.join(folder_path, img)
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    L,Y,B = cv2.split(img)

def ImageEnhancement(img):
    img_path = os.path.join(folder_path, img)
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    L,Y,B = cv2.split(img)

    Y = cv2.convertScaleAbs(Y, alpha=1, beta=-10)

    img = cv2.merge([L, Y, B])

    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)



    plt.figure(figsize=(10,25))
    plt.subplot(1,3,1)
    plt.imshow(L)

    plt.subplot(1,3,2)
    plt.imshow(img_rgb)


    plt.subplot(1,3,3)
    plt.imshow(img)

    plt.show()


# FindCentroid('Q1_Mas01.JPG')
# DetectingHouseArea("Question 2.jpg")
LaneDetect("Question 3.jpg")
# ImageEnhancement("Question 5.jpg")


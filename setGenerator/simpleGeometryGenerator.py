import cv2
import cv2.cv
import numpy as np
from random import randint

def showImage(image):
    cv2.imshow("simpleGeometryGenerator show", image)
    cv2.waitKey()

class simpleGeometryGenerator:

    def __init__(self):
        self.w = 0
        self.h = 0
        self.img = np.array([])

    def loadImg(self, image):
        self.w = image.shape[0]
        self.h = image.shape[1]
        self.img = np.array(np.copy(image), dtype=np.uint8)

    def whiteBoard(self, w, h):
        self.w = w
        self.h = h
        self.img = np.ones((w,h), dtype=np.uint8) * 255

    def getImage(self):
        return self.img

    def getImageCopy(self):
        return np.copy(self.img)

    def showImage(self):
        cv2.imshow("simpleGeometryGenerator",self.img)
        cv2.waitKey()

    def drawRandomlines(self, n, horizontal):
        if horizontal:
            for i in range(0,n):
                cv2.line(self.img, (0, randint(0,self.h)), (self.w, randint(0,self.h)), 0, randint(0,3))
        else:
            for i in range(0,n):
                cv2.line(self.img, (randint(0,self.w),0 ), (randint(0,self.w),self.h ), 0, randint(0,3))

    def drawRandomCircles(self, n, width):
        for i in range(0,n):
            c_x = randint(0,self.w)
            c_y = randint(0,self.h)
            if c_x < c_y:
                maxrad = self.w-c_x if c_x > self.w/2 else c_x
            else:
                maxrad = self.h-c_y if c_y > self.h/2 else c_y
            cv2.circle(self.img, (c_y, c_x), randint(0,maxrad), 0, randint(1,width))

    def detectCircles(self):
        self.showImage()
        circles = cv2.HoughCircles(self.img, cv2.cv.CV_HOUGH_GRADIENT, 1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=min(self.w,self.h)/2)
        if not circles == None:
            print circles
            image = cv2.cvtColor(self.img,cv2.COLOR_GRAY2BGR)
            for i in circles[0,:]:
                cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
                cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)
                cv2.imshow('detected circles',image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        else:
            print "no circles"


def genlineTest():

    img_size = (200,200)
    img = np.ones(img_size) * 255
    cv2.line(img, (0, randint(0,200)), (200, randint(0,200)), 0)
    cv2.imshow("line_test",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def genCircleTest():

    img_size = (200,200)
    img = np.ones(img_size) * 255
    cv2.circle(img, (100,100), 30, 0)
    cv2.imshow("circle_test",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

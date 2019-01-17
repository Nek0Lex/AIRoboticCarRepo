# USAGE
# python videostream_demo.py
# python videostream_demo.py --webcam 1

# import the necessary packages
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from imutils.video import VideoStream
import datetime
import argparse
import imutils
import time
import cv2
import numpy as np
import atexit

###################  START of Motor setting  ################

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

def turnOffMotors():
        print "Turn OFF ALL motors!  "
        FL.run(Raspi_MotorHAT.RELEASE)
	FR.run(Raspi_MotorHAT.RELEASE)
	BL.run(Raspi_MotorHAT.RELEASE)
	BR.run(Raspi_MotorHAT.RELEASE)

# recommended for auto-disabling motors on shutdown!
atexit.register(turnOffMotors)

# Objects for 4 wheels
#myMotor = mh.getMotor(3)
FL = mh.getMotor(4)
FR = mh.getMotor(3)
BL = mh.getMotor(2)
BR = mh.getMotor(1)

# set the speed to start, from 0 (off) to 255 (max speed)
#myMotor.setSpeed(150)
#myMotor.run(Raspi_MotorHAT.FORWARD);
speed_FL = 60
Speed_FR = 60
Speed_BL = 60
Speed_BR = 60

FL.setSpeed(speed_FL)
FR.setSpeed(Speed_FR)
BL.setSpeed(Speed_BL)
BR.setSpeed(Speed_BR)

FL.run(Raspi_MotorHAT.RELEASE)
FR.run(Raspi_MotorHAT.RELEASE)
BL.run(Raspi_MotorHAT.RELEASE)
BR.run(Raspi_MotorHAT.RELEASE)

###################  END of Motor setting  ################

#Difference Variable
minDiff = 3000
minSquareArea = 2000
match = -1

#Frame width & Height
w=320
h=240

#Reference Images Display name & Original Name

ReferenceImages = ["left.jpg","right.jpg","uturn.jpg", "start.jpg", "stop.jpg", "search.jpg"]
ReferenceTitles = ["Turn Left 90", "Turn Right 90", "Turn Around", "Start", "Stop", "AroundAbout"]

#define class for References Images
class Symbol:
    def __init__(self):
        self.img = 0
        self.name = 0

#define class instances (6 objects for 6 different images)
symbol= [Symbol() for i in range(6)]


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--webcam", type=int, default=-1,
	help="whether or not the Webcam should be used")
args = vars(ap.parse_args())

# initialize the video stream and allow the cammera sensor to warmup
vs = VideoStream(usePiCamera=args["webcam"] < 0).start()
time.sleep(2.0)


################################        END of Image Processing Setting ###############################

################################        Function Decaration             ###############################


def forward():
        print "Forward!  "
        FL.setSpeed(speed_FL)
        FR.setSpeed(Speed_FR)
        BL.setSpeed(Speed_BL)
        BR.setSpeed(Speed_BR)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)
    
def backward():
        print "Backward!  "
        FL.setSpeed(speed_FL)
        FR.setSpeed(Speed_FR)
        BL.setSpeed(Speed_BL)
        BR.setSpeed(Speed_BR)

        FL.run(Raspi_MotorHAT.BACKWARD)
        FR.run(Raspi_MotorHAT.BACKWARD)
        BL.run(Raspi_MotorHAT.BACKWARD)
        BR.run(Raspi_MotorHAT.BACKWARD)

def left():
        print "Turn Left!  "
        FL.setSpeed(speed_FL - 30)
        FR.setSpeed(Speed_FR + 30)
        BL.setSpeed(Speed_BL - 30)
        BR.setSpeed(Speed_BR + 30)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)


def right():
        print "Turn Right!  "
        FL.setSpeed(speed_FL + 30)
        FR.setSpeed(Speed_FR - 30)
        BL.setSpeed(Speed_BL + 30)
        BR.setSpeed(Speed_BR - 30)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)

def readRefImages():
        for count in range(6):
                imageRef = cv2.imread(ReferenceImages[count], cv2.COLOR_BGR2GRAY)
                imageRefResized = cv2.resize(imageRef,(w/2,h/2),interpolation = cv2.INTER_AREA) 

                symbol[count].img = resize_and_threshold_warped(imageRefResized)
                symbol[count].name = ReferenceTitles[count] 
                 
                #print symbol[count].img
                #print symbol[count].name
                #cv2.imshow(symbol[count].name,symbol[count].img);
                
def order_points(pts):
        #Ref. https://gist.github.com/nikgens/1a129d620978a4abc6a9a30f5f66e0d3
        # initialzie a list of coordinates that will be ordered
        # such that the first entry in the list is the top-left,
        # the second entry is the top-right, the third is the
        # bottom-right, and the fourth is the bottom-left
        rect = np.zeros((4, 2), dtype = "float32")

        # the top-left point will have the smallest sum, whereas
        # the bottom-right point will have the largest sum
        s = pts.sum(axis = 1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]

        # now, compute the difference between the points, the
        # top-right point will have the smallest difference,
        # whereas the bottom-left will have the largest difference
        diff = np.diff(pts, axis = 1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]

        # return the ordered coordinates
        return rect

def four_point_transform(image, pts):
        # obtain a consistent order of the points and unpack them
        # individually
        rect = order_points(pts)

        maxWidth = w/2
        maxHeight = h/2

        # construct our destination points which will be used to # map the screen to a top-down, "birds eye" view
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

        # calculate the perspective transform matrix and warp
        # # the perspective to grab the screen
        M = cv2.getPerspectiveTransform(rect, dst)

        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

        #warped = image

        # return the warped image
        return warped


def auto_canny(image, sigma=0.33):
        # compute the median of the single channel pixel intensities
        v = np.median(image)

        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(image, lower, upper)

        # return the edged image
        return edged


def resize_and_threshold_warped(image):
        #Resize the corrected image to proper size & convert it to grayscale
        #warped_new =  cv2.resize(image,(w/2, h/2))
        warped_new_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #Smoothing Out Image
        blur = cv2.GaussianBlur(warped_new_gray,(5,5),0)

        #Calculate the maximum pixel and minimum pixel value & compute threshold
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(blur)
        threshold = (min_val + max_val)/2

        #Threshold the image
        ret, warped_processed = cv2.threshold(warped_new_gray, threshold, 255, cv2.THRESH_BINARY)

        #return the thresholded image
        return warped_processed

def main():
        #Font Type
        font = cv2.FONT_HERSHEY_SIMPLEX

        #Windows to display frames
        cv2.namedWindow("Main Frame", cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow("Matching Operation", cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow("Corrected Perspective", cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow("Contours", cv2.WINDOW_AUTOSIZE)

        #Read all the reference images
        readRefImages()

        # loop over the frames from the video stream
        while True:
                try:
                        # grab the frame from the threaded video stream
                        OriginalFrame = vs.read()
                        
                        #frame = imutils.resize(frame, width=400)
                        gray = cv2.cvtColor(OriginalFrame, cv2.COLOR_BGR2GRAY)
                        blurred = cv2.GaussianBlur(gray,(3,3),0)

                        #Detecting Edges
                        edges = auto_canny(blurred)

                        #Contour Detection & checking for squares based on the square area
                        cntr_frame, contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

                        for cnt in contours:
                                #Approximates a polygonal curve(s) with the specified precision.
                                approxVertex = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

                                #If the detected objects have 4 vertex and larger than a minimal size
                                if len(approxVertex)==4:
                                        #Calculate the area of the square
                                        area = cv2.contourArea(approxVertex)

                                        if area > minSquareArea:
                                                try:
                                                        cv2.drawContours(OriginalFrame,[approxVertex],0,(0,0,255),3)
                                                        #Using reshape to skip the line in a 4 to 2 matrix
                                                        #approxVertexReshaped = approxVertex.reshape(4, 2)
                                                        warped = four_point_transform(OriginalFrame, approxVertex.reshape(4, 2))
                                                        #Histogram Equalization, converting image from grayscale to binary 
                                                        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
                                                        warpedDilated= cv2.dilate(warped,kernel,iterations = 1)
                                                        warped_eq = resize_and_threshold_warped(warpedDilated)
                                                        

                                                        for i in range(6):
                                                                diffImg = cv2.bitwise_xor(warped_eq, symbol[i].img)
                                                                diff = cv2.countNonZero(diffImg)
                                                                #print "Different between sampled image and database"
                                                                #print diff

                                                                if diff < minDiff:
                                                                        
                                                                        match = i
                                                                        
                                                                        #Accessing Values in Tuples, get the top left conner of the vertex
                                                                        cv2.putText(OriginalFrame,symbol[match].name, tuple(approxVertex.reshape(4,2)[0]), font, 1, (255,0,255), 2, cv2.LINE_AA)
                                                                       
                                                                        ####    Show Matched View       ####
                                                                        #cv2.imshow("Matching Operation", diffImg)

                                                                        #print tuple(approxVertex.reshape(4,2)[0])
                                                                        #print approxVertex.reshape(4,2)
                                                                        #["Turn Left 90", "Turn Right 90", "Turn Around", "Start", "Stop", "AroundAbout"]
                                                                        if match == 0:
                                                                                print "Turn left"
                                                                                left()
                                                                                time.sleep(1.0)
                                                                                #turnOffMotors()
                                                                                
                                                                        elif match == 1:
                                                                                print "Turn right"
                                                                                right()
                                                                                time.sleep(3)
                                                                                turnOffMotors()
                                                                                break
                                                                                
                                                                        elif match ==2:
                                                                                print "Case 2"
                                                                                turnOffMotors()
                                                                                

                                                                        elif match == 3:
                                                                                print "Forward"
                                                                                forward()
                                                                                
                                                                                #time.sleep(1.5)
                                                                                #turnOffMotors()
                                                                                
                                                                                break
                                                                                

                                                                        elif match == 4:
                                                                                print "STOP"
                                                                                turnOffMotors()
                                                                        elif match == 5:
                                                                                print "Case 5"
                                                                        else:
                                                                                print "NO Matched Image"

                                                                        
                                                                        break

                                                except:
                                                        print "Error inside the contours"
                                                        pass
                                                ####     Perspective view        ####
                                                #cv2.imshow("Corrected Perspective", warped_eq)
                                        



                        ####      show the frame ####
                        cv2.imshow("Main Frame", OriginalFrame)

                        ####    Show Contours   ####
                        #cv2.imshow("Contours", cntr_frame)

                        

                        key = cv2.waitKey(1) & 0xFF
                        # if the `q` key was pressed, break from the loop
                        if key == ord("q"):
                                break
                except:
                        print "Error inside the Main"
                        atexit.register(turnOffMotors)
                        pass

        # do a bit of cleanup
        cv2.destroyAllWindows()
        vs.stop()

#Run Main
if __name__ == "__main__" :
    main()
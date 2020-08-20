import cv2
import dlib
import os,shutil
import sys

classid=sys.argv[1]
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
directory=os.path.join(os.path.dirname(os.path.abspath(__file__)),'Cropped_faces\\'+classid+'\\')
print(directory)
if os.path.exists(directory):
    shutil.rmtree(directory)
os.makedirs(directory)

if(sys.argv) is not 1:
    ret, img = cap.read()                                                       # reading the camera input
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
    dets = detector(img, 1)
    #print(dets)
    cv2.imshow('frame', img)
    cv2.waitKey(4000)
    for i, d in enumerate(dets):                                                # loop will run for each face detected
        
        cv2.imwrite(directory+"\Cropped_faces." + str(i+1) + ".jpg",
                    img[d.top():d.bottom(), d.left():d.right()]) 
    print ("detected = "+str(len(dets)))
    #for i, d in enumerate(dets):
     #   cv2.imwrite('E:\Autoattendance-Cognitive-master-Copy\Cropped_faces' + str(i + 1) + '.jpg', img[d.top():d.bottom(), d.left():d.right()])
cap.release()
cv2.destroyAllWindows()
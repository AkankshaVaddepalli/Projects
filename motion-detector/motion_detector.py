import cv2
import pandas as pd
import time
from datetime import datetime

stillImage = None
motionImage = [ None, None ]
time = []


df = pd.DataFrame(columns = ["start", "end"])


video = cv2.VideoCapture(0)

while True:

   check, frame = video.read()
   motion = 0


   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   gray = cv2.GaussianBlur(gray, (21, 21), 0)
   if stillImage is None:
      stillImage = gray
      continue

   diff_frame = cv2.absdiff(stillImage, gray)


   thresh_frame = cv2.threshold(diff_frame, 25, 255, cv2.THRESH_BINARY)[1]
   thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

   contours,hierachy = cv2.findContours(thresh_frame.copy(),
      cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   for contour in contours:
      if cv2.contourArea(contour) < 10000:
         continue
      motion = 1
      (x, y, w, h) = cv2.boundingRect(contour)
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

   motionImage.append(motion)
   motionImage = motionImage[-2:]

   if motionImage[-1] == 1 and motionImage[-2] == 0:
      time.append(datetime.now())


   if motionImage[-1] == 0 and motionImage[-2] == 1:
      time.append(datetime.now())

   cv2.imshow("Gray_Frame", gray)

   cv2.imshow("Threshold Frame", thresh_frame)
   cv2.imshow("Colored_Frame", frame)

   key = cv2.waitKey(1)
   if key == ord('q'):
      if motion == 1:
         time.append(datetime.now())
      break


for i in range(0, len(time), 2):
   df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True)


df.to_csv("FrameInMotion_time.csv")

video.release()


cv2.destroyAllWindows()
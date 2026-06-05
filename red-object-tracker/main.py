import cv2
import numpy as np

camera = cv2.VideoCapture(0)
points = []
while True:
    ret,frame = camera.read()
    lower_red = np.array([160, 80, 130])
    upper_red = np.array([180, 255, 255])

    if not ret:
        print("unsyvess")

    csv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(csv, lower_red, upper_red)

    h, w = frame.shape[:2]

    # print(csv[h//2, w//2])

    contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if contours :
        largest = max(contours, key = cv2.contourArea)
        M = cv2.moments(largest)

        if M["m00"] != 0:
            if M["m00"] > 300:
                cx= int(M["m10"]// M["m00"])
                cy= int(M["m01"]// M["m00"])

                points.append((cx,cy))

                cv2.circle(frame,(cx,cy),5,(0,255,0),-1)
                cv2.putText(frame,f"{cx},{cy}",(cx+10,cy),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
        else:
            points.clear()
            print("CLEARED")
    if len(points) > 0:
        for i in range(1, len(points)):
            cv2.line(frame,points[i-1],points[i],(0,255,0), 2)

    cv2.drawContours( frame, contours, -1, (0,255,0),2)
    cv2.imshow("image", mask)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()    

import cv2
vid_capture = cv2.VideoCapture('C:/Users/OSLAB/Downloads/lab1.mov')
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('C:/Users/OSLAB/Downloads/lab2.mov',fourcc,20.0,(1920,1080))
while(True):
    ret, frame = vid_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid_capture.release()
out.release()
cv2.destroyAllWindows()
import cv2
cap =cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
framecount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

writer = cv2.VideoWriter('myVideo.avi',cv2.VideoWriter_fourcc(*'XVID'),20,(width,h))
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    writer.write(frame)
    
    cv2.imshow('video',frame)
    print("framecount:-",framecount)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()

    

import cv2
cap = cv2.VideoCapture()
cap.open('rtsp://admin:Hik12345@192.168.20.19:554/Streaming/channels/02/')

while(True):
     # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
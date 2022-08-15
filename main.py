from ModuloDetector import *

cap = cv2.VideoCapture()
cap.open('rtsp://admin:Hik12345@192.168.20.19:554/Streaming/channels/02/')
cap.set(3, 648)
cap.set(4, 488)
# cap.set(10,78)

while True:
    success, img = cap.read()
    result, Info = getobjects(img)
    cv2.imshow("Output", img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
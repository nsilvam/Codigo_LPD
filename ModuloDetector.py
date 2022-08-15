import cv2

thres = 0.45

classNames = ['placa', 'carro']

configPath = 'placas_labels.pbtxt'
weightsPath = 'placas_pesos.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(428, 640)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def getobjects(img):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=0.2)
    # print(classIds,bbox)
    objectInfo = []
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            objectInfo.append([box, className])
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv2.putText(img, className.upper, (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (0, 255, 0), 2)
    return img, objectInfo


if __name__ == "__main__":

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
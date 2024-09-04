import cv2
from pyzbar.pyzbar import decode
import numpy as np
from firebase import firebase

firebase = firebase.FirebaseApplication('REMOVED', None)

cam = cv2.VideoCapture(0)

while True:
    ok,frame = cam.read()
    for code in decode(frame):            #decode tung frame trong video
        print(code)
        pts = np.array([code.polygon], np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(frame, [pts], True, (193, 123, 36), 3)
        data = code.data.decode('utf-8')
        frame = cv2.putText(frame, data, (code.rect.left, code.rect.top + code.rect.height),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        
        state = firebase.get('/Mode','/State')
        if state == 1:
            firebase.put('/Python', '/QR-Data', data)
            firebase.put('/Mode','/State',11)

    cv2.imshow('QR Code', frame)
    key_pressed = cv2.waitKey(13)

    if key_pressed == 113:

        break

cam.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        HiddenData = barcode.data.decode('utf-8')
        print(HiddenData)
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape((-1, 1, 2)) #creating bounding box
        cv2.polylines(img, [points], True, (255, 0, 255), 5)
        points2 = barcode.rect
        cv2.putText(img, HiddenData, (points2[0], points2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(1)
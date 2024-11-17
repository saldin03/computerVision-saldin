import cv2
import numpy as np

image = cv2.imread('C:\cvision\edit\saldin1.jpeg')

if image is None:
    print("Gambar tidak ditemukan!")
else:
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 50, 50])   
    upper_green = np.array([85, 255, 255]) 

    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    image[green_mask != 0] = [0, 0, 255]

    cv2.imwrite('hsl-gmbr.jpeg', image)

    cv2.imshow('Hasil Gambar', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

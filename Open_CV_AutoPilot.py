
import numpy as np
from PIL import ImageGrab, Image
import cv2
import time

def process_img(image):
    original_image = image
    #convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #edge detection
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2 = 300)
    return processed_img

#def main():
while(True):
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('loop took {} deconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


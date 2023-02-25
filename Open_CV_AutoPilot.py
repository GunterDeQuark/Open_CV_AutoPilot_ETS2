import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, W, A, S, D 
import lanes


def process_img(original_image):
    try:
        processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        copy_img = np.copy(processed_img)
        processed_img = cv2.GaussianBlur(processed_img,(5,5),0)
        processed_img = cv2.Canny(processed_img, threshold1=50, threshold2=150) #1 to 2 or 1 to 3
        #mask 
        vertices = np.array([[100,500],[100,300],[300,300],[500,300],[800,300],[800,500],
                             ], np.int32)

        #processed_img = lanes.roi(processed_img, [vertices])
        processed_img = lanes.region_of_interest(processed_img)
        lines = cv2.HoughLinesP(processed_img, 2, np.pi/180, 100, np.array([]), 20, 5)
        averaged_lines = lanes.average_slope_intercept(processed_img, lines)
        line_image = lanes.display_lines(copy_img, averaged_lines)

        combo = cv2.addWeighted(copy_img, 0.8, line_image, 0.5, 1)
        return combo#processed_img
    except:
        return original_image





def main():
    last_time = time.time()
    while(True):
        screen =  np.array(ImageGrab.grab(bbox=(0,40, 800, 640)))
        new_screen = process_img(screen)
        print('Loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()

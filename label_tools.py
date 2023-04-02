import cv2
import os
from pathlib import Path
from twinkle 
def main():
    # Load image on window.
    
    global frame_id, image_files 
    
    data_root = "YOLOX_outputs/yolox_x_mix_det/track_vis/2023_04_02_04_08_25"
    images_path = Path(os.path.join(data_root, 'images'))
    image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]
    
    #For test, load one image to cv2 window
    
    frame_id = 0
    cv2.namedWindow('show image')
    cv2.setMouseCallback('show image', mouse_click)  
    
    def back(*args):
        pass  
    cv2.createButton("Back",back,None,cv2.QT_PUSH_BUTTON,1)
    
    while True:
        
        img = cv2.imread(os.path.join(images_path, image_files[frame_id]))
        cv2.imshow("show image", img)
        key = cv2.waitKey(100)
        
        # close window command using esc key
        if key == 27:
            print("ESC")
            cv2.destroyAllWindows()
            break
        # close window command 
        elif cv2.getWindowProperty('show image',cv2.WND_PROP_VISIBLE) < 1:
            break 
        
    cv2.destroyAllWindows()
    
def mouse_click(event, x, y, flags, param):
    global frame_id
    
    if event == cv2.EVENT_LBUTTONDOWN :
        countup()
        frame_id += 1

def countup():
    global frame_id, image_files
    frame_id += 1
    if frame_id > len(image_files):
        frame_id = len(image_files) - 1
    
if __name__ == "__main__":
    main()
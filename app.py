


#Screen Recording App using opencv


import cv2 as cv
import pyautogui as p
import numpy as np

#screensize
rs=p.size()

#filename in which you are storing video
                         
fn=input("Please enter the file name where  to save  ")

#fix the frame rate

fourcc=cv.VideoWriter_fourcc(*'XVID')
output=cv.VideoWriter(fn,fourcc,20.0,rs)


#recording module banauna lako
cv.namedWindow("Live Recording",cv.WINDOW_NORMAL)
cv.resizeWindow("Live Recording", (600,400))


while True:
    img=p.screenshot()
    arr=np.array(img)    
    arr=cv.cvtColor(arr, cv.COLOR_BGR2RGB)
    output.write(arr)
    if  cv.waitKey(1)==ord('s'):
        break

output.release()
cv.destroyAllWindows() 

import cv2
import numpy as np

from os.path import join
from os import listdir     
saving_directory="/home/iwizards/Pictures/task_7june/"
browsing_directory="/home/iwizards/Downloads/p2"

images = listdir(browsing_directory)
image_arrays=[]
count=0
for image in images:
    im=cv2.imread(join(browsing_directory,image))
    try:
        re=cv2.resize(im,(1280,720))
    except:
        print("error")
    exten="."+image.split(".")[-1]
    image_arrays.append(re)
    print(f"Image {image} has dimensions as {np.shape(re)[0]} X {np.shape(re)[1]}.")
    x,y,w,h=cv2.selectROI(re)
    cropped_image=re[y:y+h,x:x+w]
    cv2.imshow("Res",cropped_image)
    a = cv2.imwrite('/home/iwizards/Pictures/classes_not_fire'+str(count)+'.jpg',cropped_image)
    count=count+1
    print("Process complete...")
cv2.destroyAllWindows()

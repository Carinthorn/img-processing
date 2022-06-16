import os
import cv2

file_list = os.listdir("img")
# list file in img folder

for file in file_list:
    img = cv2.imread(f"img/{file}")
    # add text to file
    cv2.putText(img, "OpenCV", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 4)
    cv2.imwrite(f"img/result-{file}", img)
    
print("End program")

    
    


import cv2

# use webcam = 0
def detect(img, model, scaleFactor, minNeighbor, text, color):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = model.detectMultiScale(gray_img, scaleFactor, minNeighbor)
    print(features)
    
    coords = []

faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("img/car1.jpeg")
print(faceCascade)
img, coords = detect(img, faceCascade, 1.1, 5, "Face", (0,0,255))
        
    

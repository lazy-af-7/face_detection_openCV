import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap= cv2.VideoCapture(0)


while True:
    _,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.5,3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()














# The code below is for images 
# test_img = cv2.imread("test.jpg")

# gray_test_img=cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

# faces=face_cascade.detectMultiScale(gray_test_img,1.1,4)



# for (x,y,w,h) in faces:
#     cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),2)


# cv2.imshow('test_img',test_img)
# cv2.waitKey()
import time
from datetime import datetime

now = datetime.now()
now_c = now.strftime("%Y %m %d %H %M %S ")
new_time = str(now_c)

print(now_c)
times = ["Year " , "Month " ,  "Day "  , "Hour " , "Minute " , "Second " ]
x = []
x.append(now_c)
for f in x :
    print (f)
    
print("gffghgf")
print(now_c)


def camera():
    
    import cv2

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()




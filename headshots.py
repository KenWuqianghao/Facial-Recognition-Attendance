import cv2
import os
import sys

# initialize naems, camera, and image counter
# names = ['Nicolas', 'Matteo', 'Lorenzo', 'Erica', 'Rodrigo', 'Minje', 'Kim', 'Georgios', 'Niccolo', 'Paolo', 'Lucia', 'Matilde', 'Rafaela', 'Qianghao', 'Sara']
names = ['IDK']
cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

for name in names:
    # create a directory for every student  
    dirname = sys.path[0] + "/dataset/{}".format(name)
    os.mkdir(dirname)
    print(dirname)

    # keep on taking picture until image counter reaches 50
    while img_counter != 50:
        ret, frame = cam.read()

        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("press space to take a photo", frame)

        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

        elif k%256 == 32:
            # SPACE pressed
            img_name = sys.path[0] + "/dataset/{}/image_{}.jpg".format(name,img_counter)
            print(img_name)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

cam.release()

cv2.destroyAllWindows()
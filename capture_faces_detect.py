import cv2
import os

name = input("Enter your name:")

folder = f"dataset/{name}"

if not os.path.exists(folder):
    os.makedirs(folder)

camera = cv2.VideoCapture(0)

face_detector= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

count=0

print("Press 's' to save image, \nPress 'q' to quit   \n")

while True:
    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=4
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Capture", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):

        if len(faces) > 0:

            x, y, w, h = faces[0]

            face = frame[y:y+h, x:x+w]

            cv2.imwrite(
                f"{folder}/{count}.jpg",
                face
            )

            count += 1

            print(f"Saved face {count}")

        else:
            print("No face detected!")

    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows() 
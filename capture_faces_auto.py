import cv2
import os

name = input("Enter your name: ")

folder = os.path.join("dataset", name)  

if not os.path.exists(folder):
    os.makedirs(folder)     

camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

count = 0
frame_count = 0
max_images = 30

print("Collecting face images....")

while True:

    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)


    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        frame_count += 1

        # Save every 5th frame
        if frame_count % 5 == 0:

            face = frame[y:y+h, x:x+w]

            cv2.imwrite(
                f"{folder}/{count}.jpg",
                face
            )

            count += 1

            print(f"Saved {count}")

    cv2.putText(frame, f"Images Captured: {count}/{max_images}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Face Dataset Collection ", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if count >= max_images:
        break

camera.release()
cv2.destroyAllWindows()

print(f"Collected {count} face images for {name}.") 
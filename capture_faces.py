import cv2
import os

name = input("Enter your name: ")

folder = os.path.join("dataset", name)

if not os.path.exists(folder):
    os.makedirs(folder)

camera = cv2.VideoCapture(0)
count = 0

print("\nPress s to save image, \nPress q to quit   \n")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera error")
        break
    cv2.imshow("Capture Faces", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):

        filename = os.path.join(folder, f"{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Image saved: {filename}")
        count += 1

    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows() 
print(f"Captured {count} images for {name}.")
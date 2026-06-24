import cv2
import face_recognition
import pickle
from attendance import mark_attendance

with open("encodings/faces.pkl", "rb") as file:
    data = pickle.load(file)


known_encodings = data["encodings"]
known_names = data["names"]

camera = cv2.VideoCapture(0)

print("Starting face recognition. Press 'q' to quit.")

while True:
    ret, frame = camera.read()

    if not ret:
        break

    # Convert BGR (OpenCV) to RGB
    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Detect faces
    face_locations = face_recognition.face_locations(
        rgb_frame
    )

    # Generate encodings
    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )

    # Process each detected face
    for (top, right, bottom, left), face_encoding in zip(
        face_locations,
        face_encodings
    ):

        matches = face_recognition.compare_faces(
            known_encodings,
            face_encoding
        )

        name = "Unknown"

        if True in matches:

            first_match_index = matches.index(True)

            name = known_names[first_match_index]
            mark_attendance(name)

        # Draw rectangle
        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

        # Draw name
        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow(
        "Face Recognition Attendance",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
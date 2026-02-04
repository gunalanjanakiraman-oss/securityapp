import cv2

def face_auth():
    cam = cv2.VideoCapture(0)
    face = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.3, 5)

        cv2.imshow("Face Authentication - JARVIS-X", frame)

        if len(faces) > 0:
            cam.release()
            cv2.destroyAllWindows()
            return True

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    return False

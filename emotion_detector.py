from deepface import DeepFace
import cv2

def detectar_emocion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return None

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emocion = result[0]['dominant_emotion']
        return emocion
    except Exception as e:
        print(f"Error analizando emoción: {e}")
        return None
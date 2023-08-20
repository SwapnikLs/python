import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import serial
import time
import pyttsx3

data_path = r'C:\Users\swapn\OneDrive\Pictures\Screenshots\\'
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

## ... (other imports remain the same)

def train_face_recognizer(data_path):
    onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    Training_data, Labels = [], []
    
    for i, file in enumerate(onlyfiles):
        image_path = join(data_path, file)
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if images is not None:
            Training_data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)
    
    if len(Labels) == 0:
        raise ValueError("No valid images found for training.")
    
    Labels = np.asarray(Labels, dtype=np.int32)
    model = cv2.face_LBPHFaceRecognizer.create()  # Corrected creation of the LBPH face recognizer
    model.train(np.asarray(Training_data), np.asarray(Labels))
    return model

# ... (rest of the code remains unchanged)



def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 140)
    engine.setProperty("volume", 1.0)
    
    engine.say(audio)
    engine.runAndWait()

def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    face_regions = []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = gray[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
        face_regions.append(roi)
    
    return img, face_regions

def main():
    try:
        model = train_face_recognizer(data_path)
    except ValueError as e:
        print(e)
        return
    
    cap = cv2.VideoCapture(0)
    
    x, c, d = 0, 0, 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        image, face_regions = face_detector(frame)
        
        for face in face_regions:
            result = model.predict(face)
            
            if result[1] < 500:
                confidence = int((1 - (result[1]) / 300) * 100)
                display_string = str(confidence)
                cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
                
            if confidence >= 83:
                cv2.putText(image, "unlocked", (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                x += 1
            else:
                cv2.putText(image, "locked", (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                c += 1
        
        cv2.imshow('face', image)
        
        if cv2.waitKey(1) == 13 or x == 10 or c == 30 or d == 20:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    if x >= 5:
        ard = serial.Serial('com5', 9600)
        time.sleep(2)
        var = 'a'
        c = var.encode()
        speak("Face recognition complete. Matching with database. Welcome, sir. Door is opening in 5 seconds.")
        ard.write(c)
        time.sleep(4)
        speak("Door is closing.")
    
    elif c == 30:
        speak("Face is not matching. Please try again.")
    
    elif d == 20:
        speak("Face is not found. Please try again.")

if __name__ == "__main__":
    main()



            
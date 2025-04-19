import os
import cv2
import numpy as np
import face_recognition as fr
import pickle

# Path to the main images directory
path = "images"
encoded_faces = []
classnames = []

# Traverse subfolders (each subfolder = one person)
for person_name in os.listdir(path):
    person_folder = os.path.join(path, person_name)
    if os.path.isdir(person_folder):
        person_encodings = []

        for img_name in os.listdir(person_folder):
            img_path = os.path.join(person_folder, img_name)
            img = cv2.imread(img_path)

            if img is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encodes = fr.face_encodings(img)
                if encodes:
                    person_encodings.append(encodes[0])

        # Average the encodings if at least one was found
        if person_encodings:
            avg_encoding = np.mean(person_encodings, axis=0)
            encoded_faces.append(avg_encoding)
            classnames.append(person_name)

# Save encodings and class names
with open("face_encodings.pkl", "wb") as f:
    pickle.dump((encoded_faces, classnames), f)

print("Face encodings saved successfully.")

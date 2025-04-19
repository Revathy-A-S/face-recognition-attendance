import streamlit as st
import cv2
import numpy as np
import face_recognition as fr
import pickle
from datetime import datetime
from PIL import Image

# Load known encodings
with open("face_encodings.pkl", "rb") as f:
    encoded_faces, classnames = pickle.load(f)

# Attendance storage
attendance = set()
attendance_list = []

st.title("📸 Face Recognition Attendance System (Image Upload)")

uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# Utility: Mark attendance
def mark_attendance(name):
    if name not in attendance:
        attendance.add(name)
        attendance_list.append({
            "Name": name,
            "Time": datetime.now().strftime("%H:%M:%S")
        })

if uploaded_image:
    # Load and convert image
    image = Image.open(uploaded_image)
    frame = np.array(image)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    st.image(frame, caption="Uploaded Image", use_column_width=True)

    # Face detection and recognition
    faces = fr.face_locations(rgb_frame)
    encodings = fr.face_encodings(rgb_frame, faces)

    for encode_face, face_loc in zip(encodings, faces):
        matches = fr.compare_faces(encoded_faces, encode_face)
        face_dist = fr.face_distance(encoded_faces, encode_face)

        if any(matches):
            match_index = np.argmin(face_dist)
            name = classnames[match_index]
        else:
            name = "Unknown"

        mark_attendance(name)

        # Draw box and label
        top, right, bottom, left = face_loc
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Show results
    st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), caption="Processed Image", use_column_width=True)
    st.subheader("📋 Attendance Marked")
    st.table(attendance_list)

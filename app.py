import streamlit as st
import cv2
import numpy as np
import face_recognition as fr
import pickle
from datetime import datetime

# Load known encodings
with open("face_encodings.pkl", "rb") as f:
    encoded_faces, classnames = pickle.load(f)

# Initialize session state variables
if "stop_cam" not in st.session_state:
    st.session_state.stop_cam = False
if "attendance" not in st.session_state:
    st.session_state.attendance = set()
if "attendance_list" not in st.session_state:
    st.session_state.attendance_list = []

st.title("📸 Face Recognition Attendance System")

# Start/Stop buttons
start = st.button("Start Camera")
stop = st.button("Stop Camera")

# Streamlit placeholders
frame_placeholder = st.empty()
table_placeholder = st.empty()

# Utility: Mark attendance
def mark_attendance(name):
    if name not in st.session_state.attendance:
        st.session_state.attendance.add(name)
        st.session_state.attendance_list.append({
            "Name": name,
            "Time": datetime.now().strftime("%H:%M:%S")
        })

# Handle camera start
if start:
    st.session_state.stop_cam = False
    cap = cv2.VideoCapture(0)
    st.info("Camera started. Look into the camera to mark attendance.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        faces = fr.face_locations(rgb_small_frame)
        encodings = fr.face_encodings(rgb_small_frame, faces)

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
            top, right, bottom, left = [v * 4 for v in face_loc]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Show frame
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB")

        # Show attendance table
        table_placeholder.table(st.session_state.attendance_list)

        # Break if stop is pressed
        if st.session_state.stop_cam:
            break

    cap.release()
    cv2.destroyAllWindows()
    st.success("Camera stopped.")

# Handle stop
if stop:
    st.session_state.stop_cam = True

# Always show the attendance table
if st.session_state.attendance_list:
    table_placeholder.table(st.session_state.attendance_list)

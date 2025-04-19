# 🧠 Face Recognition Attendance System

A real-time face recognition attendance app built using **Python**, **OpenCV**, **face_recognition**, and **Streamlit**. This system uses your webcam to recognize faces and mark attendance automatically. Ideal for demo projects, internships, and smart attendance applications.

---

## 🚀 Features

- 📷 Live webcam-based attendance system
- 👥 Supports multiple known individuals
- 📅 Automatically marks timestamped attendance
- 🧑❓ Unknown faces are handled and labeled
- 📊 Displays attendance table in real-time
- 💾 Easy training using image folders

---

## 🛠 Requirements

Before installing the dependencies, make sure you have:

- **Python 3.11.0**  
  👉 [Download Python 3.11.0](https://www.python.org/downloads/release/python-3110/)

- **CMake 4.0.0 RC4 for Windows (x86_64)**  
  👉 [Download cmake-4.0.0-rc4-windows-x86_64.msi](https://github.com/Kitware/CMake/releases/tag/v4.0.0-rc4)

> ✅ Make sure to add both Python and CMake to your system PATH and restart your terminal or IDE after installation.

---

## 📦 Installation

1. Clone the repository:
   git clone https://github.com/Revathy-A-S/face-recognition-attendance.git
   
   cd face-recognition-attendance
   
2.Install dependencies:
  pip install -r requirements.txt

3.If dlib fails to build, install it manually from the provided wheel:

  pip install dlib-19.24.1-cp311-cp311-win_amd64.whl

## 🧠 How It Works
### Training:

Place face images in subfolders inside the images/ directory.

Each subfolder should be named after the person it represents.
Example: images/JohnDoe/image1.jpg, images/JaneDoe/image2.jpg.

### Encoding:

Run face_recognition_model.py to generate face_encodings.pkl.

### Attendance:

Launch the app with streamlit run app.py.

People come one by one and look into the webcam.

App matches the face and logs attendance with a timestamp.

Unknown faces are labeled as "Unknown Person".

### ▶️ Run the App
Make sure face_encodings.pkl is already generated using your training images.

  streamlit run app.py

### 📂 Project Structure
face-recognition-attendance/
├── app.py                     # Streamlit application
├── face_recognition_model.py  # Face encoding/training script
├── face_encodings.pkl         # Pickled encodings
├── requirements.txt           # Required Python packages
├── dlib-19.24.1-*.whl         # Precompiled dlib for Windows 
├── README.md                  # Project documentation
└── images/                    # Training images directory
    └── Person1/
        └── image1.jpg

### 📊 Sample Attendance Flow

Run the app
A webcam window opens
Individuals approach the camera
Faces are recognized and marked as present
Attendance table updates live
Press Stop in the app to end the session


### 🧰 Technologies Used

Python 3.11
OpenCV
face_recognition (based on dlib)
Streamlit
CMake (required for dlib)

### 🧪 Future Improvements

Store attendance logs in a CSV or database
Support for re-training within the app
Export attendance table
Face masking/detection alerts

### ✉️ Contact
Created by Revathy A S
📫 Email: revathyas0606@gmail.com
🔗 GitHub: github.com/Revathy-A-S
⭐ If you like this project, feel free to star the repo and share your feedback!

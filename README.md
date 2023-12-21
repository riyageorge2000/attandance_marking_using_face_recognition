# attandance_marking_using_face_recognition


### Objective:
The goal of this project is to create an automated attendance system using face recognition technology. The system utilizes a webcam to detect faces in real-time, matches them with known student faces, and maintains an attendance record based on the recognized individuals.



### Libraries Used:

face_recognition: for face detection and recognition.

os: for file path operations.

cv2 (OpenCV): for accessing and manipulating webcam video feed.

datetime: for timestamping attendance records.

csv and pandas: for handling Excel data.



### Functionality:

Face Detection and Recognition:

Utilizes face_recognition library to locate and recognize faces in real-time video frames.
Compares detected faces with pre-encoded face data of known students to identify them.

Attendance Recording:

Captures date, time, and recognized name to maintain attendance records.
Updates the Excel file with attendance status (present/absent) for each student on each date.

User Interface:

Displays live video feed from the webcam.
Draws rectangles around detected faces and labels them with recognized student names.


### Operation:

The system operates in a continuous loop until the user presses 'q' to quit.
Detected faces are marked as present in the Excel file if they match known student faces.


### Conclusion:
The system effectively tracks attendance using face recognition technology. However, it assumes a clear and direct view of the faces for accurate recognition. Enhancements could involve handling multiple faces in a frame, improving recognition accuracy in varying lighting conditions, and optimizing performance.

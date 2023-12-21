import face_recognition
import os
import cv2
import datetime
import csv
import pandas as pd

# Load the Excel file into a DataFrame
excel_file = 'students.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# Reset the index of the DataFrame to get a continuous range of numbers for the row indices
df = df.reset_index(drop=True)

# Create an empty list to store the attendance records
attendance_records = []

# Load the face encodings and names of the students into lists
known_face_encodings = []
known_face_names = []

for index, row in df.iterrows():
    image_path = os.path.join('images', row['Name'] + '.jpg')
    image = face_recognition.load_image_file(image_path)
    image_encoding = face_recognition.face_encodings(image)[0]
    known_face_names.append(row['Name'])
    known_face_encodings.append(image_encoding)

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Append the date, time, and name of the detected person to the attendance_records list
        attendance_records.append([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name])

        # Mark the person as present in the Excel sheet
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        if current_date not in df.columns:
            df[current_date] = 'Absent'

        try:
            row_index = df.loc[df['Name'] == name].index[0]
            df.at[row_index, current_date] = 'Present'
        except IndexError:
            print("Name not found in dataframe")

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Exit the loop when the user presses 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

# Save the updated DataFrame to an Excel file
df.to_excel('students.xlsx', index=False)
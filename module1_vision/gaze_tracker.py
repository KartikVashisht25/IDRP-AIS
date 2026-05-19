def get_gaze_direction(face_landmarks):

    try:

        eye_left = face_landmarks.landmark[33].x
        eye_right = face_landmarks.landmark[133].x

        iris_x = face_landmarks.landmark[468].x

        eye_center = (eye_left + eye_right) / 2

        # Mirror corrected
        if iris_x < eye_center - 0.01:
            return "RIGHT"

        elif iris_x > eye_center + 0.01:
            return "LEFT"

        else:
            return "CENTER"

    except:

        return "CENTER"
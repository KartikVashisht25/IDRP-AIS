import math


def calculate_distance(p1, p2):

    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2
    )


def calculate_mar(face_landmarks):

    try:

        upper_lip = face_landmarks.landmark[13]
        lower_lip = face_landmarks.landmark[14]

        left_mouth = face_landmarks.landmark[78]
        right_mouth = face_landmarks.landmark[308]

        mouth_height = calculate_distance(
            upper_lip,
            lower_lip
        )

        mouth_width = calculate_distance(
            left_mouth,
            right_mouth
        )

        mar = mouth_height / mouth_width

        return mar

    except:

        return 0
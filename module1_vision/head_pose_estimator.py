import math


def estimate_head_pose(face_landmarks, frame_shape):

    try:

        nose = face_landmarks.landmark[1]

        left_face = face_landmarks.landmark[234]
        right_face = face_landmarks.landmark[454]

        forehead = face_landmarks.landmark[10]
        chin = face_landmarks.landmark[152]

        # LEFT / RIGHT
        yaw = (0.5 - nose.x) * 100

        # UP / DOWN
        pitch = (0.5 - nose.y) * 100

        # ROLL
        dx = right_face.x - left_face.x
        dy = right_face.y - left_face.y

        roll = math.degrees(math.atan2(dy, dx))

        return (
            round(pitch, 2),
            round(yaw, 2),
            round(roll, 2)
        )

    except:

        return 0, 0, 0
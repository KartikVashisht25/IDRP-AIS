# import cv2

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("❌ Camera not working")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     cv2.imshow("Camera Test", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2

for i in range(5):

    cam = cv2.VideoCapture(i)

    success, frame = cam.read()

    if success:
        print(f"Camera found at index {i}")

    cam.release()
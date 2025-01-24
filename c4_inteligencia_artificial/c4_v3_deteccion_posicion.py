import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

img = cv2.imread("src/Meditating_LIL_191305.jpeg")

resized = cv2.resize(img, (1024, 768))

pose_results = pose.process(resized)
mp_drawing.draw_landmarks(
    resized,
    pose_results.pose_landmarks,
    mp_pose.POSE_CONNECTIONS
)

cv2.imshow("Pose Estimation", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# cap = cv2.VideoCapture(1)   # 1번 카메라
cap = cv2.VideoCapture('http://172.30.1.11:4747/video')

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)

while True:
    retval, frame = cap.read()  # 프레임 캡처
    if not retval: break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)   # 25ms 대기, 초당 frame (FPS)
    if key == 27: break # ESC키를 누른 경우 루프 탈출
if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()
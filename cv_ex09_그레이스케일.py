import cv2
# import numpy as np

img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
img[120, 200] = 0   # 화소값(밝기, 그레이스케일) 변경, (120,200)에 해당하는 점 하나
print(img[100:110, 200:210])    # ROI 접근

# numpy 없으면 다음과 같은 코드
# for y in range(100, 400):
# x in range(200, 300):
# img[y, x] = 0
# img[y, x] = [255, 0, 0] # 파란색으로 변경

# img[100:400, 200:300] = 0   # ROI 접근, 가로 100-400 세로 200-300을 검정색으로
img[0:200, 0:200] = img[200:400, 200:400]

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2

img = cv2.imread('dataset.png')
height, width = img.shape[:2]
print(f"{height}, {width}")
start_row, start_col = int(height * .1), int (width * .40)
end_row, end_col = int(height * 1), int (width * 1)
cropped = img[start_row:end_row, start_col:end_col]
cv2.imshow("tes", cropped)
cv2.waitKey(0)
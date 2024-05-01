import os
import cv2

def app():
    jmh_crop = 2
    img_path = 'II_2_1_HFD.tiff'

    img = cv2.imread(img_path)
    height, width = img.shape[:2]

    row_start, row_end = count_crop(jmh_crop, height)
    col_start, col_end = count_crop(jmh_crop, width)

    if (os.path.exists("saved_img")):
        if (os.path.isdir("saved_img")):
            os.system("rm -R saved_img")
            os.mkdir("saved_img")
    else:
        os.mkdir("saved_img")

    for i in range(0, jmh_crop):
        for j in range(0, jmh_crop):
            cropped = img[row_start[i]:row_end[i], col_start[j]:col_end[j]]

            cv2.imshow("test", cropped)
            cv2.waitKey(0)

            cv2.imwrite(f"saved_img/img_crop_{i + 1}_{j + 1}.png", cropped)



def count_crop(jmh_crop, size_img):
    start_crop = []
    end_crop = []

    size_crop = int(size_img / jmh_crop)
    for i in range(0, jmh_crop + 1):
        end_crop.append(i * size_crop)
        start_crop.append(end_crop[i] - size_crop)

    start_crop.pop(0)
    end_crop.pop(0)
    return  start_crop, end_crop

app()

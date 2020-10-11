# From MiCode's video of course

from cv2 import cv2

def main():
    CHAR_LIST = '@%#*+=-:. '
    num_chars = len(CHAR_LIST)

    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
    
    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()

        key = cv2.waitKey(20)
        if key == 27:
            break
    cv2.destroyWindow("preview")


def toASCII(frame, cols=50, rows=25):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = frame.shape
    cell_width = width / cols
    cell_height = height / rows
    if cols > width or rows > height:
        raise ValueError("Too much FDP")
    result = ""
    for i in range(rows):
        for j in range(cols):
            result += CHAR_LISTCHAR_LIST[min(int(np.mean(image[int(i * cell_height):min(int((i + 1) * cell_height), height),
                                                  int(j * cell_width):min(int((j + 1) * cell_width),
                                                                          width)]) * num_chars / 255), num_chars - 1)]
    print(result)

if __name__ == "__main__":
    main()
import cv2


def detect_face(path):
    global cutimg
    image = cv2.imread(path)
    image_temp = cv2.imread(path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    classifier = cv2.CascadeClassifier("D:\Python3.10\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
    faceRect = classifier.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=3, minSize=(50, 50))
    if len(faceRect):
        for face in faceRect:
            x, y, w, h = face
            x_exp = x - 30
            y_exp = y - 30
            w_exp = w + 30
            h_exp = h + 30
            cutimg = image_temp[y_exp:y + h_exp, x_exp:x + h_exp]
            cv2.rectangle(image, (x_exp, y_exp), (x + w_exp, y + h_exp), (0, 255, 0), 1)

    return cutimg


if __name__ == '__main__':
    filepath = "./img/2.jpg"
    face = detect_face(filepath)
    cv2.imshow('face', face)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
